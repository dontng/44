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
        return path.relative_to(ROOT).as_posix() in tracked
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
for path in sorted((ROOT / 'src').glob('*.md')):
    for q in re.findall(rf'^### \d+\s*·\s*({QID})\b', visible(path.read_text()), re.M):
        source.setdefault(q, []).append(path.stem)
expected = {f'{y}-{n:02}' for y in range(2020, 2027) for n in range(1, 48)}
require(set(source) == expected, 'src', 'expected every question in 2020–2026: 329 unique IDs')
schedule = json.loads((SPRINT / 'content/schedule.json').read_text())
require(schedule['sources'] == source, 'schedule.json', 'source mappings changed or stale')
require([x['day'] for x in schedule['days']] == list(range(1, 41)), 'schedule.json', 'expected Day01–40 once')
all_choices, all_written = [], []
written_days = {}
readme = check_markdown(SPRINT / 'README.md')
coverage = check_markdown(SPRINT / 'coverage.md')
for item in schedule['days']:
    d = item['day']
    path = SPRINT / f'day{d:02}.md'
    label = path.relative_to(ROOT)
    text = check_markdown(path)
    require(text.startswith(f'# Day {d:02}｜'), label, 'wrong day heading')
    nav = text.split('\n\n', 2)[1]
    expected_nav = {'README.md'} | {f'day{n:02}.md' for n in (d-1, d+1) if 1 <= n <= 40}
    require(set(re.findall(r'\]\(([^)]+)\)', nav)) == expected_nav, label, 'wrong adjacent-day navigation')
    require(f'](day{d:02}.md)' in readme, label, 'missing from README')
    choices = re.findall(rf'^### 选择题\d+｜({QID})\b', text, re.M)
    written = re.findall(rf'^### 大题\d+｜({QID})\b', text, re.M)
    require(choices == item['choices'] and len(choices) == 7, label, 'daily choice list differs from schedule or is not seven')
    require(written == item['written'] and 1 <= len(written) <= 2, label, 'daily written list differs from schedule or exceeds two')
    require(all(int(q[-2:]) <= 40 for q in choices), label, 'written question placed in choice block')
    require(all(int(q[-2:]) > 40 for q in written), label, 'choice question placed in written block')
    distribution = Counter(subject(q) for q in choices)
    require(set(distribution) == {0, 1, 2, 3} and all(n in (1, 2) for n in distribution.values()), label, 'each subject must have one or two choices')
    b = item['budget']
    wanted = {'choices': 70 if len(written) == 2 else 75, 'written': 40 if len(written) == 2 else 35, 'recall': 10}
    require(b == wanted and sum(b.values()) == 120 and b['choices'] > b['written'], label, 'wrong budget or written work dominates')
    periods = [(int(a), int(z)) for a, z in re.findall(r'^\d\. \*\*(\d+)[–—-](\d+)分钟', text, re.M)]
    require(periods == [(0, b['choices']), (b['choices'], 110), (110, 120)], label, 'rendered budget differs from schedule')
    sections = re.split(r'(?=^### (?:选择题|大题)\d+｜)', text, flags=re.M)[1:]
    for section in sections:
        q = re.match(rf'### (?:选择题|大题)\d+｜({QID})\b', section)[1]
        year, number = q.split('-')
        expected_image = f'../bank/{year}/q{number}.png'
        require(f'src="{expected_image}"' in section, label, f'{q} has wrong or missing original image')
        origins = re.findall(r'\]\(\.\./src/(\d{4})\.md\)', section)
        require(bool(origins) and all(s in source.get(q, []) for s in origins), label, f'{q} source mismatch')
        require(f'| {q} | [Day {d:02}](day{d:02}.md) |' in coverage, label, f'{q} coverage row missing or wrong')
    all_choices += choices
    all_written += written
    written_days.update({q: d for q in written})

counts = Counter(all_choices + all_written)
require(set(counts) == set(source), 'coverage', f'missing {sorted(set(source)-set(counts))}; extra {sorted(set(counts)-set(source))}')
require(all(n == 1 for n in counts.values()), 'coverage', f'duplicate first assignments {[q for q, n in counts.items() if n != 1]}')
require(len(all_choices) == 280 and len(all_written) == 49, 'coverage', 'expected 280 choices and 49 written questions')
require(sum(len(d['written']) == 2 for d in schedule['days']) == 9, 'schedule.json', 'expected nine double-written days')
for y in (2023, 2024, 2025, 2026):
    require(written_days.get(f'{y}-43') == written_days.get(f'{y}-44'), 'schedule.json', f'{y}-43/44 shared stem split across days')
for q, node in schedule['choice_lessons'].items():
    path = SPRINT / 'modules' / f'{node}.md'
    require(re.search(rf'^## \d+\s*·\s*{q}\b', visible(path.read_text()), re.M), path.relative_to(ROOT), f'{q} lesson heading missing')
for q, ref in schedule['written_lessons'].items():
    path = SPRINT / 'lessons' / ref['page']
    text = visible(path.read_text())
    require(ref['heading'] in text and '完整解法与必要补学' in text, path.relative_to(ROOT), f'{q} written lesson missing')
for q, page in schedule['choice_checks'].items():
    require(q[:4] in visible((SPRINT/'lessons'/page).read_text()), page, f'{q} check page missing year')
for path in sorted((SPRINT/'modules').glob('*.md')) + sorted((SPRINT/'lessons').glob('*.md')):
    check_markdown(path)
require(len(list((SPRINT/'lessons').glob('day*.md'))) == 40, 'lessons', 'old lessons must be preserved')
require(len(list((SPRINT/'modules').glob('*.md'))) == 40, 'modules', 'original modules must be preserved')
check_markdown(SPRINT / 'audit.md')
if errors:
    raise SystemExit('\n'.join(errors))
print('PASS: 329/329 unique source questions; 280 choices + 49 written; '
      '40 days with 7 choices and 1–2 written; choice-first 120-minute budgets; '
      'shared stems, source images, coverage table, lessons and links checked.')
