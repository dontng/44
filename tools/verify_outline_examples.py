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

# Additional arithmetic/state checks for the second correction batch.
def check_arithmetic_and_pipeline():
    for x in range(-16,16):
        for y in range(-16,16):
            acc, mq, bit = 0, y & 15, 0
            for t in range(5):
                digit = (mq & 1) if t < 4 else int(y < 0)
                acc = (acc + (x if (digit,bit)==(0,1) else -x if (digit,bit)==(1,0) else 0)) & 63
                if t < 4:
                    bit, mq = mq & 1, ((acc & 1) << 3) | (mq >> 1)
                    acc = (acc >> 1) | (acc & 32)
            encoded = (acc << 4) | mq
            signed = encoded - 1024 if encoded & 512 else encoded
            assert signed == x*y, (x,y,signed)
    for divisor in range(1,16):
        for dividend in range(divisor):
            rem, quotient = dividend-divisor, 0
            for _ in range(4):
                rem = 2*rem + (divisor if rem < 0 else -divisor)
                quotient = (quotient << 1) | int(rem >= 0)
            if rem < 0: rem += divisor
            assert (quotient,rem) == divmod(dividend*16,divisor)
    alu = (ROOT/'outline/02-co/02-data-representation/03-alu-and-circuits.md').read_text()
    assert '00.10001111' in alu and '0.01001001' not in alu
    eat = .95*8 + (.05-1e-5)*58 + 1e-5*5000054
    assert abs(eat-60.49996)<1e-8
    vm=(ROOT/'outline/02-co/03-memory-hierarchy/03-virtual-memory-hardware.md').read_text()
    assert '60.49996' in vm and '(1 - h_{\\text{tlb}}) p_{\\text{fault}}' not in vm
    ready, previous_id, schedule = {}, 1, []
    for dest,sources in [(1,[2]),(3,[1,4]),(5,[3,6]),(7,[1,8]),(9,[5,10])]:
        decode = max(previous_id+1,max(ready.get(r,0) for r in sources))
        schedule.append((decode,decode+3));ready[dest]=decode+3;previous_id=decode
    assert schedule==[(2,5),(5,8),(8,11),(9,12),(11,14)]
    page=(ROOT/'outline/02-co/05-cpu/03-pipeline-hazards.md').read_text()
    block=page.split('##### 模式 A 时空图网格')[1].split('\n---')[0]
    rows=[line for line in block.splitlines() if line.startswith('| $I_')]
    for line,(decode,writeback) in zip(rows,schedule):
        cells=[s.strip() for s in line.split('|')[2:-1]]
        assert len(cells)==14 and cells[decode-1]=='ID' and cells[writeback-1]=='WB'
    assert len(rows)==5
    import os
    r,w=os.pipe();os.write(w,b'AB');os.close(w)
    assert os.read(r,4)==b'AB' and os.read(r,4)==b'';os.close(r)
    print('PASS: 1024 Booth products, all 4-bit proper divisions, EAT, pipeline table, pipe EOF')

if __name__ == '__main__':
    check_arithmetic_and_pipeline()

def check_sort_and_floyd():
    records = [(49,'a'),(38,''),(65,''),(97,''),(76,''),(13,''),(27,''),(49,'b')]
    for gap in [4,2,1]:
        for i in range(gap,len(records)):
            key,j=records[i],i
            while j>=gap and records[j-gap][0]>key[0]: records[j]=records[j-gap];j-=gap
            records[j]=key
    assert [tag for value,tag in records if value==49]==['a','b']
    page=(ROOT/'outline/01-ds/07-sort/05-shell-and-radix-sort.md').read_text()
    assert '[13, 27, 38, 49, 49*, 65, 76, 97]' in page
    assert '[13, 27, 38, 49*, 49, 65, 76, 97]' not in page
    inf=float('inf');matrix=[[0,5,inf,7],[inf,0,4,2],[3,inf,0,1],[inf,inf,inf,0]]
    page=(ROOT/'outline/01-ds/05-graph/04-shortest-path.md').read_text()
    for k in range(4):
        before=[r[:] for r in matrix]
        matrix=[[min(before[i][j],before[i][k]+before[k][j]) for j in range(4)] for i in range(4)]
        line=next(l for l in page.splitlines() if l.startswith(f'| $k={k}$'))
        expected=['['+','.join('INF' if v==inf else str(v) for v in row)+']' for row in matrix]
        assert re.findall(r'`(\[[^`]+\])`',line)==expected
    assert (0x12345678<<8)&0xffffffff==0x34567800
    assert 60//64 != 64//64 and 0//64==4//64
    print('PASS: labeled Shell result, every Floyd stage, unsigned shift and cache-line boundaries')

if __name__ == '__main__':
    check_sort_and_floyd()

def check_battlefield_cleanup():
    # 1. CLA 超前进位展开式
    alu = (ROOT / 'outline/02-co/02-data-representation/03-alu-and-circuits.md').read_text()
    assert 'C_4 = G_4 + P_4 G_3 + P_4 P_3 G_2 + P_4 P_3 P_2 G_1 + P_4 P_3 P_2 P_1 C_0' in alu
    assert 'C_4 = G_4 + P_4 G_4' not in alu
    assert '进位传递项' in alu

    # 2. 30 位物理地址 0x002A5018 的 Cache Index 位切分
    pa = 0x002A5018
    offset = pa & 0x3F
    index = (pa >> 6) & 0x1FF
    tag = pa >> 15
    assert offset == 24 and index == 0x140 and index == 320 and tag == 0x54
    vm = (ROOT / 'outline/02-co/03-memory-hierarchy/03-virtual-memory-hardware.md').read_text()
    assert '0x140' in vm and '第 320 行' in vm
    assert '0x001（第 1 行）' not in vm

    # 3. 四级多重中断嵌套 0~45 μs 时序闭合
    intr = (ROOT / 'outline/02-co/06-bus-and-io/03-interrupt-and-dma.md').read_text()
    assert '| **15 ~ 18 μs** |' in intr
    assert (3 + 5 + 2) + 10 + 10 + (5 + 5) + 5 == 45

    # 4. 单总线 CPU 中断周期 T0/T1 无总线冲突
    cpu = (ROOT / 'outline/02-co/05-cpu/01-cpu-datapath.md').read_text()
    assert ('(SP) - 4 -> Z' in cpu or '(SP) - 4 \\to Z' in cpu)
    assert ('(Z) -> SP, MAR' in cpu or '(Z) \\to SP, MAR' in cpu)

    # 5. 系统调用 read() 内核拷贝方向
    sc = (ROOT / 'outline/03-os/01-fundamentals/03-system-call.md').read_text()
    assert 'copy_to_user' in sc
    assert '`copy_from_user` 将数据安全拷贝至用户态' not in sc

    # 6. 微内核 read() IPC 上下文切换次数
    micro = (ROOT / 'outline/03-os/01-fundamentals/04-os-architecture.md').read_text()
    assert '1 次进程切换' in micro and '4 次进程上下文切换' in micro
    assert '2~3 次完整的上下文切换' not in micro

    # 7. 差分曼彻斯特编码 101100 波形
    level = '-'
    wave = []
    for b in '101100':
        if b == '0':
            level = '+' if level == '-' else '-'
        next_level = '+' if level == '-' else '-'
        chunk = f'{level} {level} {next_level} {next_level}'
        wave.append(chunk)
        level = next_level
    assert wave == ['- - + +', '- - + +', '+ + - -', '- - + +', '- - + +', '- - + +']
    enc = (ROOT / 'outline/04-cn/02-physical/02-encoding-and-multiplexing.md').read_text()
    assert '- - + +  - - + +  + + - -  - - + +  - - + +' in enc

    # 8. TCP 经典首部 32 位对齐
    assert 4 + 6 + 6 + 16 == 32
    tcp = (ROOT / 'outline/04-cn/05-transport/02-tcp-connection-and-flow.md').read_text()
    assert '保留 (6 bits)' in tcp and '保留 (4 bits)' not in tcp

    # 9. DHCP 广播目的 MAC 与 ICMP 回送 Type/Code
    icmp = (ROOT / 'outline/04-cn/04-network/03-routing-devices-and-icmp.md').read_text()
    assert 'FF-FF-FF-FF-FF-FF' in icmp
    assert 'Type = 8, Code = 0' in icmp and 'Type = 0, Code = 0' in icmp

    # 10. 无重复三级标题序号
    for rel in [
        'outline/01-ds/05-graph/04-shortest-path.md',
        'outline/03-os/02-process/07-threads-and-ipc.md',
        'outline/04-cn/03-datalink/04-wlan-and-vlan.md',
    ]:
        txt = (ROOT / rel).read_text()
        headings = re.findall(r'^### \((\d+)\)', txt, re.M)
        assert len(headings) == len(set(headings)), f'Duplicate heading index in {rel}: {headings}'

    print('PASS: battlefield cleanup checks (CLA, PA cache index, interrupt timeline, bus conflict, syscall, microkernel IPC, Diff-Manchester, TCP header, DHCP/ICMP, heading uniqueness)')

if __name__ == '__main__':
    check_battlefield_cleanup()
