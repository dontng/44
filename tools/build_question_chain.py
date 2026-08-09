#!/usr/bin/env python3
"""Compile the 2009-2025 choice bank into a continuous ability-line chain."""
import argparse
import datetime as dt
import json
import os
import re
import statistics
from collections import Counter
from collections import deque
from pathlib import Path

from PIL import Image


REPO = Path(__file__).resolve().parent.parent
SOURCE = REPO / "data" / "ability_lines.json"
CHAIN = REPO / "data" / "question_chain.json"
ROSTER_DIR = REPO / "data" / "rosters"
SRC_DIR = REPO / "src"
INDEX = SRC_DIR / "README.md"

# Normalize the displayed glyph size across scanned papers.  Their crops have
# different widths, so merely constraining every image to the page width makes
# text in narrow crops much larger than text in wide crops.
DISPLAY_TEXT_PX = 11
DISPLAY_MAX_WIDTH = 760
DISPLAY_MIN_WIDTH = 150
SAMPLES_PER_YEAR = 6


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def question_parts(qid):
    match = re.fullmatch(r"(\d{4})-(\d{2})", qid)
    if not match:
        raise ValueError(f"bad qid: {qid}")
    return match.group(1), int(match.group(2))


def question_path(date):
    return SRC_DIR / f"{date.strftime('%m%d')}.md"


def relative_link(origin, target):
    return Path(os.path.relpath(target, origin.parent)).as_posix()


def glyph_height(path):
    """Return a robust proxy for Chinese glyph height in a scanned question."""
    im = Image.open(path).convert("L")
    width, height = im.size
    pixels = im.load()
    dark = [[pixels[x, y] < 140 for x in range(width)] for y in range(height)]
    seen = [[False] * width for _ in range(height)]
    heights = []
    for y0 in range(height):
        for x0 in range(width):
            if not dark[y0][x0] or seen[y0][x0]:
                continue
            min_y = max_y = y0
            min_x = max_x = x0
            count = 0
            queue = deque([(y0, x0)])
            seen[y0][x0] = True
            while queue:
                y, x = queue.popleft()
                count += 1
                min_y, max_y = min(min_y, y), max(max_y, y)
                min_x, max_x = min(min_x, x), max(max_x, x)
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        ny, nx = y + dy, x + dx
                        if (
                            0 <= ny < height
                            and 0 <= nx < width
                            and dark[ny][nx]
                            and not seen[ny][nx]
                        ):
                            seen[ny][nx] = True
                            queue.append((ny, nx))
            component_height = max_y - min_y + 1
            component_width = max_x - min_x + 1
            if count >= 15 and 12 <= component_height <= 60 and 6 <= component_width <= 60:
                heights.append(component_height)
    return statistics.median(heights) if heights else None


def display_widths():
    """Compute a per-question width that gives each year the same text size."""
    widths = {}
    for year_dir in sorted((REPO / "bank").glob("*")):
        if not year_dir.is_dir() or not year_dir.name.isdigit():
            continue
        samples = []
        for image in sorted(year_dir.glob("q*.png"), key=lambda path: path.stat().st_size, reverse=True):
            height = glyph_height(image)
            if height:
                samples.append(height)
            if len(samples) == SAMPLES_PER_YEAR:
                break
        if not samples:
            raise ValueError(f"could not measure glyph height: {year_dir.name}")
        scale = DISPLAY_TEXT_PX / statistics.median(samples)
        for image in year_dir.glob("q*.png"):
            number = int(image.stem[1:])
            image_width = Image.open(image).size[0]
            widths[f"{year_dir.name}-{number:02d}"] = max(
                DISPLAY_MIN_WIDTH, min(DISPLAY_MAX_WIDTH, round(image_width * scale))
            )
    return widths


def validate_source(data):
    lines = data.get("lines", [])
    if not lines:
        raise ValueError("no ability lines")
    ids = [line["id"] for line in lines]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate ability-line id")

    all_refs = []
    for line in lines:
        questions = line.get("questions", [])
        if not line.get("title") or not line.get("story") or not questions:
            raise ValueError(f"incomplete ability line: {line.get('id')}")
        if questions != sorted(questions, key=question_parts):
            raise ValueError(f"questions are not chronological: {line['id']}")
        for qid in questions:
            year, number = question_parts(qid)
            if not (REPO / "bank" / year / f"q{number:02d}.png").exists():
                raise ValueError(f"missing image: {qid}")
        all_refs.extend(questions)

    bank = {
        f"{year.name}-{int(image.stem[1:]):02d}"
        for year in (REPO / "bank").iterdir()
        if year.is_dir() and year.name.isdigit()
        for image in year.glob("q*.png")
    }
    missing = sorted(bank - set(all_refs), key=question_parts)
    unknown = sorted(set(all_refs) - bank, key=question_parts)
    if missing:
        raise ValueError(f"unassigned bank questions: {', '.join(missing)}")
    if unknown:
        raise ValueError(f"unknown question refs: {', '.join(unknown)}")
    return Counter(all_refs)


def compile_chain(data):
    start = dt.date.fromisoformat(data["start_date"])
    nodes = []
    for index, line in enumerate(data["lines"], 1):
        date = start + dt.timedelta(days=index - 1)
        path = question_path(date)
        nodes.append(
            {
                "index": index,
                "date": date.isoformat(),
                "key": date.strftime("%m%d"),
                "file": path.relative_to(REPO).as_posix(),
                "line_id": line["id"],
                "title": line["title"],
                "story": line["story"],
                "questions": line["questions"],
            }
        )
    for index, node in enumerate(nodes):
        node["prev"] = nodes[index - 1]["file"] if index else None
        node["next"] = nodes[index + 1]["file"] if index + 1 < len(nodes) else None
    return nodes


def nav(node, nodes, path):
    parts = [f"[总索引]({relative_link(path, INDEX)})"]
    if node["prev"]:
        prev = nodes[node["index"] - 2]
        parts.insert(0, f"[← {prev['key']}]({relative_link(path, REPO / prev['file'])})")
    if node["next"]:
        nxt = nodes[node["index"]]
        parts.append(f"[{nxt['key']} →]({relative_link(path, REPO / nxt['file'])})")
    return " · ".join(parts)


def existing_result(path):
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    marker = "\n## 结果\n"
    if marker not in text:
        return ""
    result = text[text.index(marker):].rstrip()
    lines = result.splitlines()
    if lines and lines[-1].startswith("["):
        lines.pop()
    return "\n".join(lines).rstrip()


def render_node(node, nodes, widths, result=""):
    path = REPO / node["file"]
    links = nav(node, nodes, path)
    lines = [
        links,
        "",
        f"# {node['key']}｜{node['title']}",
        "",
        f"> 能力线 `{node['line_id']}` · 第 {node['index']:02d}/{len(nodes):02d} 个节点 · "
        f"{len(node['questions'])} 道真题引用",
        ">",
        f"> [打开答题卡](http://127.0.0.1:8409/?date={node['key']})",
        "",
        "## 故事梗概",
        "",
        node["story"],
        "",
        "这里的日期是链表节点，不是完成期限；是否前进，由这条能力线能否从题干恢复决定。",
        "",
        "## 题单",
        "",
    ]
    for index, qid in enumerate(node["questions"], 1):
        year, number = question_parts(qid)
        image = REPO / "bank" / year / f"q{number:02d}.png"
        width_percent = widths[qid] / DISPLAY_MAX_WIDTH * 100
        lines.extend(
            [
                f"### {index:02d} · {qid}",
                "",
                f'<div style="width:min(100%, {DISPLAY_MAX_WIDTH}px);">',
                f'<img src="{relative_link(path, image)}" alt="{qid}" '
                f'style="width:{width_percent:.4g}%; height:auto;">',
                "</div>",
                "",
            ]
        )
    if result:
        lines.extend([result, ""])
    lines.extend([links, ""])
    return "\n".join(lines)


def render_index(data, nodes, counts):
    duplicate_questions = sorted((qid for qid, count in counts.items() if count > 1), key=question_parts)
    lines = [
        "# 408 真题能力线",
        "",
        data["principle"],
        "",
        f"本轮共 **{len(nodes)} 条能力线、680 道不同真题、{sum(counts.values())} 次题目引用**。"
        f"其中 {len(duplicate_questions)} 道接口题出现在不止一条能力线中；它们不是重复配额，而是用来接通两套机制。",
        "",
        "| 节点 | 能力线 | 题数 | 年份跨度 |",
        "|---|---|---:|---|",
    ]
    for node in nodes:
        years = [question_parts(qid)[0] for qid in node["questions"]]
        lines.append(
            f"| [{node['key']}]({Path(node['file']).name}) | {node['title']} | "
            f"{len(node['questions'])} | {years[0]}–{years[-1]} |"
        )
    lines.extend(
        [
            "",
            "## 交叉引用",
            "",
            "这些题承担两个或三个能力线的接口。第一次遇到时解决原题；再次出现时只检查它能否接通当前能力线。",
            "",
            ", ".join(f"`{qid}`" for qid in duplicate_questions),
            "",
        ]
    )
    return "\n".join(lines)


def roster(node):
    items = []
    for index, qid in enumerate(node["questions"], 1):
        year, number = question_parts(qid)
        items.append(
            {
                "idx": index,
                "qid": qid,
                "year": year,
                "q": number,
                "image": f"bank/{year}/q{number:02d}.png",
                "answer_known": True,
                "source": "ability_line",
            }
        )
    return {
        "date": node["date"],
        "day": node["index"],
        "mode": "ability_line",
        "line_id": node["line_id"],
        "line_title": node["title"],
        "md_path": node["file"],
        "items": items,
    }


def build(check_only=False):
    data = read_json(SOURCE)
    counts = validate_source(data)
    nodes = compile_chain(data)
    widths = display_widths()
    payload = {
        "version": data["version"],
        "name": data["name"],
        "start_date": data["start_date"],
        "end_date": nodes[-1]["date"],
        "node_count": len(nodes),
        "unique_questions": len(counts),
        "question_refs": sum(counts.values()),
        "nodes": nodes,
    }
    rendered = {
        CHAIN: json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        INDEX: render_index(data, nodes, counts),
    }
    for node in nodes:
        path = REPO / node["file"]
        rendered[path] = render_node(node, nodes, widths, existing_result(path))
        rendered[ROSTER_DIR / f"{node['key']}.json"] = (
            json.dumps(roster(node), ensure_ascii=False, indent=2) + "\n"
        )

    if check_only:
        mismatches = [
            path.relative_to(REPO).as_posix()
            for path, text in rendered.items()
            if not path.exists() or path.read_text(encoding="utf-8") != text
        ]
        if mismatches:
            raise SystemExit("question chain is stale or missing:\n" + "\n".join(mismatches))
        print(
            f"ok: {len(nodes)} nodes, {len(counts)} unique questions, "
            f"{sum(counts.values())} references"
        )
        return

    for path, text in rendered.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    print(
        f"built {len(nodes)} nodes: {nodes[0]['key']} -> {nodes[-1]['key']} · "
        f"{len(counts)} unique questions · {sum(counts.values())} references"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    build(check_only=args.check)


if __name__ == "__main__":
    main()
