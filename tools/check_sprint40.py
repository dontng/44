"""Check the active Sprint40 Markdown without regenerating pages."""
from collections import Counter
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SPRINT = ROOT / "sprint40"
QID = r"20(?:20|21|22|23|24|25|26)-\d{2}"
MOCK_YEARS = {33: 2022, 35: 2023, 37: 2024, 38: 2025, 39: 2026}
errors = []


def require(condition, path, message):
    if not condition:
        errors.append(f"{path.relative_to(ROOT)}: {message}")


def visible(text):
    return re.sub(r"<!--.*?-->", "", text, flags=re.S)


def question_image(qid):
    year, number = qid.split("-")
    return ROOT / "bank" / year / f"q{number}.png"


def link_targets(text):
    return re.findall(r"\]\(([^)]+)\)", text)


def check_markdown(path):
    raw = path.read_text()
    require(raw.count("<!--") == raw.count("-->"), path, "unbalanced HTML comments")
    text = visible(raw)
    require(len(re.findall(r"^```", text, re.M)) % 2 == 0, path, "unbalanced code fences")
    body = re.sub(r"^```[^\n]*\n.*?^```", "", text, flags=re.M | re.S)
    body = re.sub(r"`[^`\n]+`", "", body)
    require(body.count("<details>") == body.count("</details>"), path, "unbalanced folds")
    for target in link_targets(body) + re.findall(r'<img\b[^>]*\bsrc="([^"]+)"', body):
        if target.startswith(("https://", "http://")) or target.startswith("#"):
            continue
        dest = (path.parent / target.split("#", 1)[0]).resolve()
        require(dest.is_relative_to(ROOT) and dest.exists(), path, f"invalid link: {target}")
        match = re.search(r"/bank/(\d{4})/q\d{2}\.png$", dest.as_posix())
        require(not match or 2020 <= int(match[1]) <= 2026, path, f"inactive question: {target}")
    return text


def check_question_source(path, qid, section, source):
    expected = question_image(qid)
    images = re.findall(r'<img\b[^>]*\bsrc="([^"]+)"', section)
    require(any((path.parent / image).resolve() == expected for image in images),
            path, f"{qid} image does not match its heading")
    require(source.is_file() and re.search(rf"^### \d+ · {qid}\b", visible(source.read_text()), re.M),
            path, f"{qid} missing from active {source.name}")


def check_time(path, text):
    budgets = re.findall(r"^\d\. \*\*([^*\n]+)", text, re.M)[:4]
    require(len(budgets) == 4, path, "expected four time blocks")
    clock = 0
    for block in budgets:
        period = re.search(r"(\d+)[–—-](\d+)分钟", block)
        if period:
            start, end = map(int, period.groups())
            require(start == clock and end > start, path, f"invalid time interval: {block}")
            clock = end
        else:
            duration = re.search(r"(\d+)分钟", block)
            require(duration, path, f"missing duration: {block}")
            if duration:
                clock += int(duration[1])
    require(clock == 120, path, f"budget ends at {clock}, expected 120")


index = SPRINT / "README.md"
index_text = check_markdown(index)
check_markdown(SPRINT / "audit.md")
modules = {}
for path in sorted((SPRINT / "modules").glob("*.md")):
    text = check_markdown(path)
    entries = {}
    for section in re.split(r"^## ", text, flags=re.M)[1:]:
        heading = re.match(rf"\d+ · ({QID})\b", section)
        if not heading:
            continue
        qid = heading[1]
        answer = re.search(r"<details>.*?\*\*答案[：:]\s*([ABCD]).*?</details>", section, re.S)
        require(answer and qid not in entries, path, f"{qid} has missing or duplicate folded answer")
        entries[qid] = answer[1] if answer else None
        check_question_source(path, qid, section, ROOT / "src" / path.name)
    require(entries, path, "no active choices")
    modules[path.stem] = entries

days = {}
written = {}
assigned = Counter()
for day in range(1, 41):
    path = SPRINT / f"day{day:02d}.md"
    if not path.exists():
        require(False, path, "missing daily page")
        continue
    text = check_markdown(path)
    days[day] = text
    require(text.startswith(f"# Day {day:02d}｜"), path, "day heading mismatch")
    require(path.name in link_targets(index_text), path, "missing from main index")
    nav = link_targets(text.split("\n\n", 2)[1]) if "\n\n" in text else []
    neighbors = {f"day{n:02d}.md" for n in (day - 1, day + 1) if 1 <= n <= 40}
    require(set(nav) == neighbors | {"README.md"}, path, "day navigation mismatch")
    check_time(path, text)

    if day <= 20:
        matches = {}
        for line in text.splitlines():
            node = re.search(r"\]\(modules/(\d{4})\.md\)", line)
            if node:
                qids = re.findall(QID, line)
                if qids:
                    matches[node[1]] = qids
        require(len(matches) == 2, path, "expected two modules with explicit question IDs")
        for node, qids in matches.items():
            require(qids == list(modules.get(node, {})), path, f"question IDs mismatch in {node}")
        assigned.update(matches.keys())
        require(len(re.findall(r"^## 大题\d+｜", text, re.M)) == 2, path, "expected two written tasks")

    written[day] = set()
    for part in re.split(r"^## 大题\d+｜", text, flags=re.M)[1:]:
        heading = re.match(QID, part)
        require(heading, path, "missing written question ID")
        if not heading:
            continue
        qid = heading[0]
        section = part.split("\n## ", 1)[0]
        source = re.search(r"\]\(\.\./src/(\d{4}\.md)\)", section)
        if source:
            check_question_source(path, qid, section, ROOT / "src" / source[1])
            require("完整解法与必要补学" in section, path, f"missing written solution for {qid}")
            written[day].add(qid)
        else:
            target = re.search(r"\]\(day(\d\d)\.md\)", section)
            require(target and qid in written.get(int(target[1]), set()),
                    path, f"revisit {qid} has no matching original lesson")

for day in range(1, 9):
    row = re.search(rf"^\| \*\*Day {day:02d}\*\*[^\n]+", index_text, re.M)
    require(row, index, f"missing Day {day:02d} quick-reference row")
    if row and day in days:
        first = days[day].split("## 今天", 1)[0]
        require(set(re.findall(QID, row[0])) == set(re.findall(QID, first)),
                index, f"Day {day:02d} quick-reference question IDs mismatch")

require(len(modules) == 40 and assigned == Counter(modules.keys()), index,
        "first 20 days must assign each of the 40 modules once")

for day, year in MOCK_YEARS.items():
    if day not in days:
        continue
    path = SPRINT / f"day{day:02d}.md"
    text = days[day]
    original, _, folded = text.partition("<details>")
    picks = re.findall(rf"\]\(\.\./bank/{year}/q(\d\d)\.png\)", original)
    choices = [n for n in picks if int(n) <= 40]
    answers = re.findall(r"^\| (\d\d) \| ([ABCD]) \| ([^\n]+)", folded.split("</details>", 1)[0], re.M)
    require(len(choices) == len(set(choices)) == 12 and choices == [n for n, _, _ in answers],
            path, "mock choice questions and folded key differ")
    for n, answer, row in answers:
        target = re.search(r"\]\(modules/(\d{4})\.md\)", row)
        require(not target or modules.get(target[1], {}).get(f"{year}-{n}") == answer,
                path, f"{year}-{n} answer differs from linked module")
    keys = re.findall(rf"^- ({year}-\d\d)｜.*\]\(day(\d\d)\.md\)", folded, re.M)
    originals = [f"{year}-{n}" for n in picks if int(n) > 40]
    require(originals == [qid for qid, _ in keys] and len(originals) == (3 if day == 39 else 2),
            path, "mock written questions and folded review links differ")
    for qid, target in keys:
        require(qid in written.get(int(target), set()), path, f"wrong review target for {qid}")

if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS: {len(days)} days, {len(modules)} choice modules, "
      f"{sum(map(len, modules.values()))} module entries, {sum(map(len, written.values()))} written lessons, "
      f"{len(MOCK_YEARS)} timed sets; budgets, links and folds checked")
