"""Validate the active full-coverage Sprint40 against source questions and Git paths.

No page regeneration. Sparse checkouts validate omitted tracked images against
Git's tree; existing local files must still have correct links and question IDs.
"""
from collections import Counter
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SPRINT = ROOT / 'sprint40'
QID = r'202[0-6]-\d{2}'
errors = []
tracked = set(subprocess.check_output(
    ['git', 'ls-tree', '-r', '--name-only', 'HEAD'], cwd=ROOT, text=True).splitlines())


def require(condition, label, message):
    if not condition:
        errors.append(f'{label}: {message}')


def visible(text):
    return re.sub(r'<!--.*?-->', '', text, flags=re.S)


def exists(path):
    if path.exists():
        return True
    try:
        rel = path.relative_to(ROOT).as_posix()
        return rel.startswith('bank/') and rel in tracked
    except ValueError:
        return False


def subject(q):
    n = int(q[-2:])
    if n <= 40:
        return 0 if n <= 11 else 1 if n <= 22 else 2 if n <= 32 else 3
    return 0 if n <= 42 else 1 if n <= 44 else 2 if n <= 46 else 3


def check_markdown(path):
    raw = path.read_text()
    label = path.relative_to(ROOT)
    require(raw.count('<!--') == raw.count('-->'), label, 'unbalanced HTML comments')
    text = visible(raw)
    fences = re.findall(r'^```', text, re.M)
    require(len(fences) % 2 == 0, label, 'unbalanced code fences')
    body = re.sub(r'^```[^\n]*\n.*?^```', '', text, flags=re.M | re.S)
    body = re.sub(r'`[^`\n]+`', '', body)
    require(body.count('<details>') == body.count('</details>'), label, 'unbalanced folds')
    targets = re.findall(r'\]\(([^)]+)\)', body)
    targets += re.findall(r'<img\b[^>]*\bsrc="([^"]+)"', body)
    for target in targets:
        if target.startswith(('https://', 'http://', '#')):
            continue
        dest = (path.parent / target.split('#', 1)[0]).resolve()
        require(dest.is_relative_to(ROOT) and exists(dest), label, f'invalid link {target}')
    return text


source = {}
groups = {}
family = {}
for path in sorted((ROOT / 'src').glob('*.md')):
    if not re.fullmatch(r'\d{4}', path.stem):
        continue
    ids = re.findall(rf'^### \d+\s*·\s*({QID})\b', visible(path.read_text()), re.M)
    for q in ids:
        source.setdefault(q, []).append(path.stem)
    if path.stem <= '0908':
        choices = [q for q in ids if int(q[-2:]) <= 40]
        if choices:
            groups[path.stem] = choices
            family[path.stem] = ('DS' if path.stem < '0812' else 'CO' if path.stem < '0824'
                                 else 'OS' if path.stem < '0901' else 'NW')
expected = {f'{y}-{n:02}' for y in range(2020, 2027) for n in range(1, 48)}
require(set(source) == expected, 'src', 'expected all 329 source IDs')
schedule = json.loads((SPRINT / 'content/schedule.json').read_text())
require(schedule['sources'] == source, 'schedule.json', 'stale source mappings')
require(set(schedule['choice_groups']) == set(groups), 'schedule.json', 'choice group list changed')
require([x['day'] for x in schedule['days']] == list(range(1, 41)), 'schedule.json', 'expected 40 days')
require(not (SPRINT / 'modules').exists() and not (SPRINT / 'lessons').exists(), 'sprint40', 'retired teaching directories must not remain')
for retired in ['modules.json', 'days.json']:
    require(not (SPRINT / 'content' / retired).exists(), 'content', f'old renderer data remains: {retired}')
readme = check_markdown(SPRINT / 'README.md')
coverage = check_markdown(SPRINT / 'coverage.md')
all_choices, all_written = [], []
visits = Counter()
assigned = {}
written_days = {}
seen_groups = set()
inline_choices = set(schedule['choice_explanations'])
inline_written = set(schedule['written_explanations'])
for item in schedule['days']:
    d = item['day']
    path = SPRINT / f'day{d:02}.md'
    label = path.relative_to(ROOT)
    text = check_markdown(path)
    require(text.startswith(f'# Day {d:02}｜'), label, 'wrong day heading')
    nav = text.split('\n\n', 2)[1]
    targets = set(re.findall(r'\]\(([^)]+)\)', nav))
    wanted_nav = {'README.md'} | {f'day{n:02}.md' for n in (d-1, d+1) if 1 <= n <= 40}
    require(targets == wanted_nav, label, 'wrong day navigation')
    require(f'](day{d:02}.md)' in readme, label, 'missing index entry')
    require(len(item['groups']) == 2, label, 'expected two whole source groups')
    wanted_subjects = ['DS', 'OS'] if d % 2 else ['CO', 'NW']
    require([g['subject'] for g in item['groups']] == wanted_subjects, label, 'wrong two-subject rotation')
    page_group_sections = re.split(r'(?=^## 选择题组\d+｜)', text, flags=re.M)[1:]
    require(len(page_group_sections) == 2, label, 'missing group headings')
    flattened = []
    for i, g in enumerate(item['groups']):
        node = g['source']
        wanted = groups.get(node, [])
        require(g['questions'] == wanted and g['subject'] == family.get(node), label, f'{node} was split, reordered or misclassified')
        visits[node] += 1
        require(g['round'] == visits[node], label, f'{node} wrong repeat count')
        section = page_group_sections[i].split('\n## 解答题', 1)[0]
        actual = re.findall(rf'^### 选择题\d+｜({QID})\b', section, re.M)
        require(actual == wanted, label, f'{node} rendered group differs from src')
        require(f'](../src/{node}.md)' in section, label, f'{node} missing source link')
        flattened += wanted
        if d <= 24:
            seen_groups.add(node)
    choices = re.findall(rf'^### 选择题\d+｜({QID})\b', text, re.M)
    written = re.findall(rf'^### 大题\d+｜({QID})\b', text, re.M)
    require(choices == flattened == item['choices'], label, 'wrong rendered choice list')
    require(written == item['written'] and 1 <= len(written) <= 2, label, 'wrong written list')
    require(all(int(q[-2:]) > 40 for q in written), label, 'choice in written block')
    require(not re.search(r'\]\((?:modules|lessons)/', text), label, 'teaching link still leaves day page')
    require(not any(s in text for s in ['已有讲解', '补救', '认知罗盘', '到点停止', '到120分钟', '离开前的一个检查']), label, 'retired workflow text remains')
    for section in re.split(r'(?=^### (?:选择题|大题)\d+｜)', text, flags=re.M)[1:]:
        q = re.match(rf'### (?:选择题|大题)\d+｜({QID})\b', section)[1]
        y, n = q.split('-')
        require(f'src="../bank/{y}/q{n}.png"' in section, label, f'{q} image mismatch')
        folded = re.search(r'<details>\s*<summary>答案与解析</summary>\s*(.*?)\s*</details>', section, re.S)
        require(folded, label, f'{q} needs a local folded answer')
        if folded and q in inline_choices:
            require('**答案：' in folded[1] and '**直接法：**' in folded[1] and '解析待补' not in folded[1], label, f'{q} inline choice explanation lost')
        if folded and q in inline_written:
            require(len(folded[1]) > 60 and '解析待补' not in folded[1], label, f'{q} inline written solution lost')
        assigned.setdefault(q, d)
        if int(n) > 40:
            require(any(f'](../src/{s}.md)' in section for s in source.get(q, [])), label, f'{q} wrong written source')
    e = item['estimate']
    require(e['total'] == [e['choices'][0] + e['written'][0] + 5,
                           e['choices'][1] + e['written'][1] + 10], label, 'estimate total mismatch')
    require(e['total'][0] <= e['total'][1], label, 'invalid time estimate range')
    require(f'预计用时：{e["total"][0]}—{e["total"][1]}分钟' in text, label, 'rendered estimate mismatch')
    all_choices += choices
    all_written += written
    written_days.update({q: d for q in written})
require(seen_groups == set(groups), 'coverage', 'not all 40 source groups visited by day24')
require(set(all_choices) == {q for q in source if int(q[-2:]) <= 40}, 'coverage', 'not all 280 choices assigned')
require(Counter(all_written) == Counter(q for q in source if int(q[-2:]) > 40), 'coverage', '49 written questions must each appear once')
require(set(assigned) == set(source), 'coverage', 'not all 329 questions assigned')
require(sum(len(d['written']) == 2 for d in schedule['days']) == 9, 'schedule.json', 'expected nine double-written days')
for y in (2023, 2024, 2025, 2026):
    require(written_days.get(f'{y}-43') == written_days.get(f'{y}-44'), 'schedule.json', f'{y}-43/44 shared stem split')
for q, d in assigned.items():
    require(f'| {q} | [Day {d:02}](day{d:02}.md) |' in coverage, 'coverage.md', f'{q} first day wrong')
require(inline_choices <= set(all_choices) and inline_written <= set(all_written), 'schedule.json', 'unassigned explanation IDs')
check_markdown(SPRINT / 'audit.md')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: 329/329 source IDs; 280 unique choices, 49 written; two whole src groups per day; '
      f'four subjects every two days; all 40 groups by day24; '
      f'{len(inline_choices)} choice and {len(inline_written)} written explanations inline; '
      f'estimates, shared stems, links and folds checked.')
