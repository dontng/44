#!/usr/bin/env python3
"""Populate all 2026 sliced questions into src/*.md topic sheets."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

GUIDES = {
    1: "顺序表相对次序保持不变，表头插入或删除需要把后面所有元素挨个后移或前移，必定移动多个元素；表尾操作若未满直接读写，无需移动。",
    2: "双向链表指针调整。注意题中 cu->p2 要修改为指向 cu->p1 的直接后继，必须确保当前结点的直接后继非空才能继续跨步，仔细比对 while 边界条件。",
    3: "根据层序遍历序列确定根结点，在中序遍历序列中切分左、右子树，递归恢复二叉树树形后再写出后序遍历序列。",
    4: "森林转二叉树采用“左孩子右兄弟”法则。根结点的兄弟在二叉树中形成右斜单链，要使总高度最小，应尽量将树高较小的树排在右侧，或者根据各树内部高度组合。",
    5: "带权路径长度最小即构建哈夫曼树。7个权值每次挑最小的两个合并，画出哈夫曼树后直接数结点 e 的深度及同层叶结点。",
    6: "普通邻接表只直接保存出边表，要计算某个顶点的入度，必须遍历全图所有顶点的边表，时间复杂度为 $O(n+e)$。",
    7: "有向图遍历生成序列。由于存在强连通分支和环路，分析从初始点出发所有可能产生的边权路径字符串集 S 的性质。",
    8: "高度为 4 的平衡二叉树，根结点的左、右子树高度差至多为 1。利用 AVL 树各高度最少结点数递推式 $N_h = N_{h-1} + N_{h-2} + 1$，求左右子树结点数最大差值。",
    9: "直接插入排序的比较次数直接取决于序列中的逆序对数量。序列越接近正序，逆序对越少，比较次数就越少。",
    10: "多关键字排序要求：先按单科成绩排序，再按总成绩排序，若要保持单科高者在前，第二次排序所用的算法必须具有稳定性。",
    11: "k-路平衡归并的归并趟数公式为 $d = \\lceil\\log_k r\\rceil$。增加归并路数 $k$ 可以减少归并趟数，但会增加内部归并的选择开销，通常配合败者树优化。",
    12: "微程序机器直接执行微指令，传统机器语言由微程序解释执行；高级语言和操作系统处于更高抽象层，各层之间通过定义明确的接口衔接。",
    13: "补码算术右移时高位补符号位，算术左移时低位补 0。注意算术左移可能导致符号位改变（溢出），仔细推演每一步二进制位。",
    14: "单精度浮点数有效位为 24 位（含隐含最高位 1）。就近舍入时考察被舍去的最高位及其后续位，注意阶码偏移量 127 与尾数规格化处理。",
    15: "8 个 DRAM 芯片低位交叉编址，主存地址的最低 3 位用于选片（芯片编号 0～7）。将两个十六进制地址转换后对比低 3 位，相同则位于同一芯片。",
    16: "ISA（指令集体系结构）规定软件开发者和编译器可见的机器特性（指令格式、寻址方式、通用寄存器个数等）；硬件部件实现方式（如流水线段数、ALU加法器结构）属于微架构。",
    17: "条件转移指令只有在转移条件满足时才修改 PC 发生跳转；若转移条件不满足，则自然流向 PC+指令长度的下一条指令。",
    18: "4路组相联映射：Cache 行数 1024，每组 4 行，共有 256 组（组号占 8 位）。主存地址切分为 Tag、组号、块内偏移，提取组号字段直接得出。",
    19: "TLB 采用 4 路组相联，16 个表项共 4 组（组号占 2 位）。虚拟页号 VPN 的低 2 位作为 TLB 组索引，高位作为 TLB Tag，比对组号为 2 的有效表项。",
    20: "单周期数据通路每条指令都在一个长时钟周期内完成（CPI=1，但时钟周期长）；多周期数据通路将指令拆为多步（CPI>1，但时钟频率高）。",
    21: "特权指令涉及关键硬件资源和安全控制（如关中断、设置时钟、修改基址寄存器）；访管指令（trap/syscall）用于从用户态切换到内核态，属于普通指令。",
    22: "中断响应由硬件中断隐指令自动完成：包括关中断、保存断点（PC 和 PSW）、引出中断服务程序。保护通用寄存器和执行具体处理由软件（中断服务程序）完成。",
    23: "操作系统内核代码、中断/异常处理程序、核心设备驱动程序运行在内核模式（管态）；普通用户应用程序、解释器进程运行在用户模式（目态）。",
    24: "缺页异常发生在取指或执行访存操作期间，属于故障（Fault）。缺页处理程序从外存调入页后，异常返回时重新执行导致缺页的那条指令。",
    25: "内核级线程（KLT）是 CPU 调度的独立实体，一个线程阻塞不会导致所属进程的其他线程阻塞；用户级线程（ULT）的调度由用户态线程库完成，内核无法感知。",
    26: "信号量 S 初值为 5，当 S > 0 时表示可用资源数；当 S < 0 时，|S| 表示等待队列中的进程数。根据并发执行进程数和进入临界区的数量推导 S 和 n。",
    27: "两并发进程 P、Q 可并发执行且结果确定的充要条件是 Bernstein 条件：$R(P) \\cap W(Q) = \\emptyset$ 且 $W(P) \\cap R(Q) = \\emptyset$ 且 $W(P) \\cap W(Q) = \\emptyset$。",
    28: "64位三级页表，虚拟地址各层划分明确。页表项占 8 字节，求一个进程满负荷使用时第三级页表所占用的最大页框数，自顶向下逐级推算。",
    29: "页式虚存的主要访存开销在于查页表。引入 TLB（快表）可使大部分虚地址翻译在 CPU 内部完成，大幅降低平均访存时间。",
    30: "两进程共享同一个物理页时，各自页表中对应的页表项指向同一个物理页框，但各自的虚拟地址（虚页号）可以完全不同。",
    31: "设备驱动程序将上层抽象的 I/O 请求转换为控制器特定的命令，通过读写设备控制器中的寄存器来启动设备操作。",
    32: "鼠标移动触发硬件中断，鼠标中断服务程序负责从控制器读出相对位移和按键状态，存入操作系统输入缓冲区并唤醒上层事件线程。",
    33: "网络分层保证了各层协议的独立性，某一层技术的改进不影响其他层。但分层并非越多越好，过多层次会增加头部开销和处理时延。",
    34: "首先通过香农公式 $C = B \\log_2(1 + S/N)$ 计算信道最大数据传输速率（信噪比 1023 即 $1+1023=1024=2^{10}$），再计算 1500 B 分组的发送时延。",
    35: "主机发送数据帧过程：发送前等待 DIFS，发送数据帧耗时 $L/R$，接收方收到后等待 SIFS 发送 ACK。确认接收完毕所需总时间为各阶段时延之和。",
    36: "交换机按端口划分 VLAN，不同 VLAN 之间在二层完全隔离；广播帧和未知单播帧仅在同一 VLAN 内部泛洪，只有同 VLAN 的端口才能收到。",
    37: "链路断开触发链路状态更新与 Dijkstra 重新计算。求聚合后路由项数：找出相同下一跳接口的目的网段，利用 CIDR 进行超网合并。",
    38: "OSPF 是基于链路状态的内部网关协议（IGP），通过将自治系统（AS）划分为骨干区域 Area 0 和非骨干区域来减小路由更新泛洪开销。",
    39: "/22 均分为 32（$2^5$）个子网，每个子网掩码增加 5 位变为 /27。根据给定 IP 地址计算第三、第四字节所在的子网边界。",
    40: "HTTP 是无状态协议，服务器通过 Set-Cookie 响应头向浏览器植入 Cookie，后续请求自动携带 Cookie，典型用于用户登录状态保持与购物车跟踪。",
    41: "二叉搜索树（BST）算法设计大题。树上查找与关键字修改：写出递归或非递归遍历查找算法，并在更新关键字后注意维持 BST 的有序性。",
    42: "有向图拓扑排序与关键路径综合大题。从邻接矩阵出发计算各顶点入度，推导拓扑序列并分析事件最早发生时间。",
    43: "16 位计算机定长指令字编码分析：R 型、I 型、M 型操作码扩展与字段切分，根据指令二进制机器码手工反汇编并跟踪寄存器内容变化。",
    44: "单周期数据通路控制信号深度分析。结合题 43 架构，推导移位指令在执行周期的各控制信号取值以及符号扩展控制信号 ExtOp 的位数。",
    45: "时间片轮转（RR）调度过程推演。结合时钟中断触发时机，沿时间轴列出就绪队列变迁，计算各进程首次响应时间与总调度次数。",
    46: "UNIX inode 多级寻址计算。结合 5 个直接项、一次/二次/三次间接项，计算偏移地址所需访问的磁盘块号，并推演目录删除操作的元数据变更。",
    47: "TCP 协议全流程计算大题：三次握手序号演化、滑动窗口与拥塞控制（慢开始、拥塞避免）窗口增长推算，以及结合 RTT 计算文件完整传输耗时。"
}

def img_block(qn):
    return f'<img src="../bank/2026/q{qn:02d}.png" alt="2026-{qn:02d}" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">'

def renumber_file(path):
    content = path.read_text()
    # Find all question headings
    # e.g. ### 01 · 2016-01 or ### 15 · 2026-42（大题联动）
    pattern = r"^###\s+\d+\s+·\s+([^\n]+)"
    counter = 1
    def repl(m):
        nonlocal counter
        res = f"### {counter:02d} · {m.group(1)}"
        counter += 1
        return res
    new_content = re.sub(pattern, repl, content, flags=re.M)
    path.write_text(new_content)

def populate():
    # 1. First, replace all existing 2026 placeholders across all src/*.md
    for p in sorted(SRC.glob("*.md")):
        content = p.read_text()
        def repl(m):
            heading = m.group(1)
            qn = int(m.group(2))
            guide = GUIDES.get(qn, "2026 年真题解析与考点考查。")
            img = img_block(qn)
            return f"{heading}\n> *{guide}*\n{img}"

        # Match ### XX · 2026-YY\n<!-- ... -->
        pattern = r"(###\s+\d+\s+·\s+2026-(\d+)[^\n]*)\n<!--[^\n]*-->"
        if re.search(pattern, content):
            new_content = re.sub(pattern, repl, content)
            p.write_text(new_content)
            print(f"Populated placeholders in {p.name}")

    # 2. Add Q12 into src/0818.md (Section 一 end)
    p_0818 = SRC / "0818.md"
    c_0818 = p_0818.read_text()
    if "2026-12" not in c_0818:
        block_12 = f"\n### 99 · 2026-12\n> *{GUIDES[12]}*\n{img_block(12)}\n"
        # Insert before Section 二
        idx = c_0818.find("## 二、")
        c_0818 = c_0818[:idx] + block_12 + "\n" + c_0818[idx:]
        p_0818.write_text(c_0818)
        print("Added 2026-12 into 0818.md")

    # 3. Add Q22 into src/0823.md (Section 二 end)
    p_0823 = SRC / "0823.md"
    c_0823 = p_0823.read_text()
    if "2026-22" not in c_0823:
        block_22 = f"\n### 99 · 2026-22\n> *{GUIDES[22]}*\n{img_block(22)}\n"
        c_0823 = c_0823.rstrip() + "\n" + block_22
        p_0823.write_text(c_0823)
        print("Added 2026-22 into 0823.md")

    # 4. Add Q42 into src/0916.md (Section 二 end)
    p_0916 = SRC / "0916.md"
    c_0916 = p_0916.read_text()
    if "2026-42" not in c_0916:
        block_42 = f"\n### 99 · 2026-42\n> *{GUIDES[42]}*\n{img_block(42)}\n"
        c_0916 = c_0916.rstrip() + "\n" + block_42
        p_0916.write_text(c_0916)
        print("Added 2026-42 into 0916.md")

    # 5. Renumber all files in src/*.md
    for p in sorted(SRC.glob("*.md")):
        if p.name in ("README.md", "408_深度研题与AI思维建模协议.md"):
            continue
        renumber_file(p)

    # 6. Update README.md
    readme = (SRC / "README.md").read_text()
    # Update year range in choice table if needed
    readme = re.sub(r"2013–2024", "2013–2026", readme)
    readme = re.sub(r"2009–2025", "2009–2026", readme)
    readme = re.sub(r"2010–2025", "2010–2026", readme)
    readme = re.sub(r"2011–2025", "2011–2026", readme)
    readme = re.sub(r"2016–2024", "2016–2026", readme)
    readme = re.sub(r"2009–2024", "2009–2026", readme)
    (SRC / "README.md").write_text(readme)
    print("Renumbered all files and updated README.md.")

if __name__ == "__main__":
    populate()
