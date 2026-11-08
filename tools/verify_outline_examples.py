#!/usr/bin/env python3
"""Check the corrected numerical examples against independent executable models."""
from pathlib import Path
from itertools import product
import re

ROOT = Path(__file__).resolve().parents[1]

def clock_trace(sequence, capacity):
    pages, used, hand, faults = [None] * capacity, [0] * capacity, 0, 0
    rows = []
    for page in sequence:
        hit = page in pages
        if hit:
            used[pages.index(page)] = 1
        else:
            faults += 1
            while pages[hand] is not None and used[hand]:
                used[hand] = 0
                hand = (hand + 1) % capacity
            pages[hand], used[hand] = page, 1
            hand = (hand + 1) % capacity
        rows.append((page, hit, pages[:], used[:], hand, faults))
    return rows

def check_clock_tables():
    page = (ROOT / 'outline/03-os/03-memory/04-page-replacement.md').read_text()
    sequence = [5,2,4,1,5,2,0,5,2,3,1,0]
    for capacity, expected_faults in [(3,9),(4,10)]:
        section = page.split(f'##### {capacity} 个页框下的单步执行追踪')[1].split('\n> [!WARNING]')[0].split('\n##### ')[0]
        rows = [line for line in section.splitlines() if re.match(r'\| \d+ \|', line)]
        model = clock_trace(sequence, capacity)
        assert len(rows) == len(model)
        for i, (line, (value, hit, pages, bits, hand, faults)) in enumerate(zip(rows, model), 1):
            cells = [c.strip() for c in line.split('|')[1:-1]]
            assert cells[:3] == [str(i),str(value),'命中' if hit else '缺页'], line
            expected = ['空' if p is None else f'({p}, {u})' for p,u in zip(pages,bits)]
            assert cells[3:3+capacity] == expected, line
            assert cells[-2:] == [str(hand),str(faults)], line
        assert model[-1][-1] == expected_faults
    counts = {}
    sequence = [1,2,3,4,1,2,5,1,2,3]
    for name in ['OPT','FIFO','LRU']:
        resident, recent, count = [], [], 0
        for i, value in enumerate(sequence):
            if value not in resident:
                count += 1
                if len(resident) == 3:
                    if name == 'FIFO': victim = resident[0]
                    elif name == 'LRU': victim = next(p for p in recent if p in resident)
                    else:
                        def distance(p):
                            return next((j for j in range(i+1,len(sequence)) if sequence[j] == p), float('inf'))
                        victim = max(resident,key=distance)
                    resident.remove(victim)
                resident.append(value)
            if value in recent: recent.remove(value)
            recent.append(value)
        counts[name] = count
    counts['CLOCK'] = clock_trace(sequence,3)[-1][-1]
    assert list(counts.values()) == [6,8,8,8]
    summary = page.split('| **汇总** |')[1].splitlines()[0]
    assert [int(v) for v in re.findall(r'缺页 (\d+) 次', summary)] == list(counts.values())
    print('PASS: CLOCK every frame/bit/hand; OPT/FIFO/LRU/CLOCK totals')

def prefix_table(pattern):
    pi = [0] * len(pattern)
    for i in range(1,len(pattern)):
        j = pi[i-1]
        while j and pattern[i] != pattern[j]: j = pi[j-1]
        if pattern[i] == pattern[j]: j += 1
        pi[i] = j
    return pi

def kmp_find(text, pattern):
    if not pattern: return 0
    pi, matched = prefix_table(pattern), 0
    for i,c in enumerate(text):
        while matched and c != pattern[matched]: matched = pi[matched-1]
        if c == pattern[matched]: matched += 1
        if matched == len(pattern): return i-len(pattern)+1
    return -1

def check_kmp():
    assert kmp_find('ababaababaa','ababaa') == 0
    assert kmp_find('ababababaa','ababaa') == 4
    for n in range(7):
        for t in product('ab',repeat=n):
            text = ''.join(t)
            for m in range(1,5):
                for p in product('ab',repeat=m):
                    pattern = ''.join(p)
                    assert kmp_find(text,pattern) == text.find(pattern)
    page = (ROOT / 'outline/01-ds/06-search/06-string-matching-kmp.md').read_text()
    block = page.split('**条件变体：')[1].split('\n---')[0]
    for line in block.splitlines():
        if not re.match(r'\| \d+ \|',line): continue
        cells = [c.strip() for c in line.split('|')[1:-1]]
        i,j = int(cells[1]),int(cells[3])
        assert cells[2] == f"`'{ 'ababababaa'[i-1] }'`"
        assert cells[4] == f"`'{ 'ababaa'[j-1] }'`"
    print('PASS: KMP given inputs, table characters, exhaustive binary short strings')

if __name__ == '__main__':
    check_clock_tables()
    check_kmp()
