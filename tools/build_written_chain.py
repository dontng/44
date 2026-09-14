#!/usr/bin/env python3
"""Build the large-question chain without changing the sealed choice lines."""
import argparse
import datetime as dt
import json
import re
from collections import Counter
from pathlib import Path

from build_question_chain import (
    compile_chain as compile_choice_chain,
    display_widths,
    relative_link,
    render_index as render_choice_index,
    validate_source as validate_choice_source,
)
from PIL import Image


REPO = Path(__file__).resolve().parent.parent
SOURCE = REPO / "data" / "written_lines.json"
CHAIN = REPO / "data" / "written_chain.json"
SRC_DIR = REPO / "src"
INDEX = SRC_DIR / "README.md"
CHOICE_END = SRC_DIR / "0908.md"
DISPLAY_BASE_FONT_PX = 16


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def question_parts(qid):
    match = re.fullmatch(r"(\d{4})-(4[1-7])", qid)
    if not match:
        raise ValueError(f"bad written-question id: {qid}")
    return match.group(1), int(match.group(2))


def validate_source(data):
    lines = data.get("lines", [])
    if not lines:
        raise ValueError("written lines are empty")

    markers = read_json(REPO / data["source"])
    catalog = {
        f"{year}-{question}"
        for year, item in markers["years"].items()
        for question in item
        if question != "end"
    }

    line_ids = [line["id"] for line in lines]
    if len(line_ids) != len(set(line_ids)):
        raise ValueError("duplicate written-line id")

    refs = []
    for line in lines:
        questions = line.get("questions", [])
        if not line.get("title") or not line.get("story") or not questions:
            raise ValueError(f"incomplete written line: {line.get('id')}")
        if questions != sorted(questions, key=question_parts):
            raise ValueError(f"questions are not chronological: {line['id']}")
        for qid in questions:
            if qid not in catalog:
                raise ValueError(f"uncatalogued written question: {qid}")
        refs.extend(questions)

    counts = Counter(refs)
    duplicates = sorted((qid for qid, count in counts.items() if count != 1), key=question_parts)
    if duplicates:
        raise ValueError(f"written questions must have one primary group: {', '.join(duplicates)}")
    unassigned = sorted(catalog - set(refs), key=question_parts)
    if unassigned:
        raise ValueError(f"unassigned written questions: {', '.join(unassigned)}")

    for qid in catalog:
        year, number = question_parts(qid)
        image = REPO / "bank" / year / f"q{number:02d}.png"
        if not image.exists():
            raise ValueError(f"missing complete image: {qid}")
        with Image.open(image) as question_image:
            question_image.verify()

    choice_ids = {line["id"] for line in read_json(REPO / "data" / "ability_lines.json")["lines"]}
    for line in lines:
        unknown = set(line.get("prerequisites", [])) - choice_ids
        if unknown:
            raise ValueError(f"unknown prerequisites in {line['id']}: {', '.join(sorted(unknown))}")
    return counts


def compile_chain(data):
    start = dt.date.fromisoformat(data["start_date"])
    nodes = []
    for index, line in enumerate(data["lines"], 1):
        date = start + dt.timedelta(days=index - 1)
        nodes.append(
            {
                "index": index,
                "date": date.isoformat(),
                "key": date.strftime("%m%d"),
                "file": f"src/{date.strftime('%m%d')}.md",
                "line_id": line["id"],
                "title": line["title"],
                "story": line["story"],
                "prerequisites": line.get("prerequisites", []),
                "questions": line["questions"],
            }
        )
    for index, node in enumerate(nodes):
        node["prev"] = nodes[index - 1]["file"] if index else "src/0908.md"
        node["next"] = nodes[index + 1]["file"] if index + 1 < len(nodes) else None
    return nodes


def nav(node, nodes, path):
    if node["index"] == 1:
        previous = "[← 0908 选择题终点](0908.md)"
    else:
        prev = nodes[node["index"] - 2]
        previous = f"[← {prev['key']}]({Path(prev['file']).name})"
    parts = [previous, "[总索引](README.md)"]
    if node["next"]:
        nxt = nodes[node["index"]]
        parts.append(f"[{nxt['key']} →]({Path(nxt['file']).name})")
    return " · ".join(parts)


def existing_record(path):
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    marker = "\n## 作答记录\n"
    if marker not in text:
        return ""
    record = text[text.index(marker):].rstrip()
    lines = record.splitlines()
    if lines and lines[-1].startswith("["):
        lines.pop()
    return "\n".join(lines).rstrip()


def render_node(node, nodes, data, widths, record=""):
    path = REPO / node["file"]
    links = nav(node, nodes, path)
    prereqs = "、".join(f"`{item}`" for item in node["prerequisites"])
    lines = [
        links,
        "",
        f"# {node['key']}｜{node['title']}",
        "",
        f"> 大题线 `{node['line_id']}` · 第 {node['index']:02d}/{len(nodes):02d} 个节点 · "
        f"{len(node['questions'])} 道完整真题引用",
        ">",
        f"> 选择题前置线：{prereqs}",
        "",
        "## 归类依据",
        "",
        node["story"],
        "",
        "这一节点以完整作答为单位。公共题干、全部小问、代码或计算过程必须在同一次作答中收口；再次出现的接口题只检查它与当前机制的连接，不重复抄题。",
        "",
        "## 题单",
        "",
    ]
    for index, qid in enumerate(node["questions"], 1):
        year, number = question_parts(qid)
        image = REPO / "bank" / year / f"q{number:02d}.png"
        width_em = widths[qid] / DISPLAY_BASE_FONT_PX
        lines.extend(
            [
                f"### {index:02d} · {qid}",
                "",
                '<div style="max-width:100%; max-height:min(90vh, 72em); overflow:auto;">',
                f'<img src="{relative_link(path, image)}" alt="{qid}" '
                f'style="display:block; width:{width_em:.4g}em; max-width:none; height:auto;">',
                "</div>",
                "",
            ]
        )
    if record:
        lines.extend([record, ""])
    lines.extend([links, ""])
    return "\n".join(lines)


def refresh_choice_links():
    """Join the two chains without regenerating the sealed choice question pages."""
    choice_data = read_json(REPO / "data" / "ability_lines.json")
    choice_counts = validate_choice_source(choice_data)
    choice_nodes = compile_choice_chain(choice_data)
    INDEX.write_text(render_choice_index(choice_data, choice_nodes, choice_counts), encoding="utf-8")

    text = CHOICE_END.read_text(encoding="utf-8")
    old = "[← 0907](0907.md) · [总索引](README.md)"
    new = old + " · [0914 大题 →](0914.md)"
    text = text.replace(new, old).replace(old, new)
    CHOICE_END.write_text(text, encoding="utf-8")


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
        "source": data["source"],
        "nodes": nodes,
    }
    rendered = {CHAIN: json.dumps(payload, ensure_ascii=False, indent=2) + "\n"}
    for node in nodes:
        path = REPO / node["file"]
        rendered[path] = render_node(node, nodes, data, widths, existing_record(path))

    if check_only:
        mismatches = [
            path.relative_to(REPO).as_posix()
            for path, text in rendered.items()
            if not path.exists() or path.read_text(encoding="utf-8") != text
        ]
        if mismatches:
            raise SystemExit("written chain is stale or missing:\n" + "\n".join(mismatches))
        print(
            f"ok: {len(nodes)} written nodes, {len(counts)} complete questions, "
            f"{sum(counts.values())} references"
        )
        return

    for path, text in rendered.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    refresh_choice_links()
    print(
        f"built {len(nodes)} written nodes: {nodes[0]['key']} -> {nodes[-1]['key']} · "
        f"{len(counts)} complete questions · {sum(counts.values())} references"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    build(check_only=args.check)


if __name__ == "__main__":
    main()
