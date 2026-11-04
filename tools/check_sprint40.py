"""Integrity checks, not a claim that text correctness or learning is proved."""
import json
import re
from pathlib import Path
from build_sprint40 import ROOT, OUT, load_questions

modules = json.loads((OUT / 'content/modules.json').read_text())
days = json.loads((OUT / 'content/days.json').read_text())
errors = []
for node, item in modules.items():
    expected = [q for _, q in load_questions(node)]
    if list(item['answers']) != expected:
        errors.append(f'{node}: fast-question coverage/order mismatch')
    if str(item['day']) not in days and item.get('delivery') != 'standalone':
        errors.append(f'{node}: missing daily route')
    if not (OUT / 'modules' / f'{node}.md').exists():
        errors.append(f'{node}: missing rendered module')
    for qid, (answer, explanation) in item['answers'].items():
        if answer not in 'ABCD' or not explanation.strip():
            errors.append(f'{qid}: missing answer/explanation')
for number, day in days.items():
    if len(day['modules']) != 2 or len(day['written']) != 2:
        errors.append(f'day{number}: needs two choice modules and two written problems')
    for q in day['written']:
        if (q['number'], q['id']) not in load_questions(q['source'], False):
            errors.append(f'day{number}: written question/number mismatch {q["id"]}')
        if not all(q.get(k, '').strip() for k in ('prompt', 'solution', 'check')):
            errors.append(f'day{number}: incomplete written teaching {q["id"]}')
for path in OUT.rglob('*.md'):
    text = path.read_text()
    if text.count('<details>') != text.count('</details>'):
        errors.append(f'{path}: unbalanced folds')
    if len(re.findall(r'^```', text, re.M)) % 2:
        errors.append(f'{path}: unbalanced code fence')
    for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', text):
        if re.match(r'https?://', target):
            continue
        if not (path.parent / target.split('#')[0]).resolve().exists():
            errors.append(f'{path.relative_to(ROOT)}: broken link {target}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(days)} days, {len(modules)} choice modules, '
      f'{sum(len(v["answers"]) for v in modules.values())} fast-question explanations, '
      f'{sum(len(v["written"]) for v in days.values())} complete written teaching entries; links/folds/fences valid')
