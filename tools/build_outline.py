#!/usr/bin/env python3
"""Build and scaffold outline/ from 27outline.md.

Creates a structured, chapter-by-chapter knowledge repository alongside src/
to manage syllabus points, mechanistic explanations, and exam feedback.
"""

import os
import re

SUBJECT_MAP = [
    {
        "id": "01-data-structure",
        "title": "数据结构",
        "raw_title": "一、数据结构",
        "chapters": [
            ("01-concepts.md", "一、基本概念", "基本概念与算法复杂度"),
            ("02-linear-list.md", "二、线性表", "顺序表与链表实现及应用"),
            ("03-stack-queue-array.md", "三、栈、队列和数组", "栈队列特性、循环队列与特殊矩阵压缩"),
            ("04-tree.md", "四、树与二叉树", "遍历、线索化、哈夫曼树、并查集与堆"),
            ("05-graph.md", "五、图", "遍历、最小生成树、最短路径与拓扑排序"),
            ("06-search.md", "六、查找", "二叉搜索树、平衡树、红黑树、B/B+树与哈希表"),
            ("07-sort.md", "七、排序", "内部排序算法对比与外部排序多路平衡归并"),
        ]
    },
    {
        "id": "02-computer-organization",
        "title": "计算机组成原理",
        "raw_title": "二、计算机组成原理",
        "chapters": [
            ("01-system-overview.md", "一、计算机系统概述", "计算机层次结构、性能指标与整机概念"),
            ("02-data-representation.md", "二、数据的表示和运算", "定点数补码运算、溢出判断与IEEE 754浮点数"),
            ("03-memory-hierarchy.md", "三、存储器层次结构", "SRAM/DRAM、主存扩展、Cache映射与虚拟存储器"),
            ("04-instruction-system.md", "四、指令系统", "寻址方式、CISC/RISC与指令格式设计"),
            ("05-cpu.md", "五、中央处理器（CPU）", "数据通路、控制器硬布线与微程序、流水线冲突与冒险"),
            ("06-bus-and-io.md", "六、总线和输入/输出系统", "总线仲裁、程序中断机制与DMA传送"),
        ]
    },
    {
        "id": "03-operating-system",
        "title": "操作系统",
        "raw_title": "三、操作系统",
        "chapters": [
            ("01-os-fundamentals.md", "一、操作系统基础", "双模机制、中断与异常、系统调用与内核架构"),
            ("02-process-management.md", "二、进程管理", "进程状态模型、CPU调度算法、同步互斥与死锁"),
            ("03-memory-management.md", "三、内存管理", "分页与分段、请求分页虚存、页置换算法与抖动"),
            ("04-file-management.md", "四、文件管理", "文件逻辑/物理结构、目录与FCB、虚拟文件系统"),
            ("05-io-management.md", "五、输入/输出（I/O）管理", "I/O软件层次、设备独立性、缓冲管理与磁盘调度"),
        ]
    },
    {
        "id": "04-computer-network",
        "title": "计算机网络",
        "raw_title": "四、计算机网络",
        "chapters": [
            ("01-network-architecture.md", "一、计算机网络概述", "OSI/TCP-IP分层体系、时延计算与端到端传输"),
            ("02-physical-layer.md", "二、物理层", "奈奎斯特与香农定理、编码调制与信道复用"),
            ("03-data-link-layer.md", "三、数据链路层", "滑动窗口、差错控制、以太网MAC与交换机自学习"),
            ("04-network-layer.md", "四、网络层", "IP编址与CIDR汇聚、路由协议RIP/OSPF/BGP与ARP"),
            ("05-transport-layer.md", "五、传输层", "UDP/TCP段格式、可靠传输、流量控制与拥塞控制"),
            ("06-application-layer.md", "六、应用层", "DNS解析递归与迭代、HTTP协议、FTP与邮件协议"),
        ]
    }
]

def parse_raw_outline():
    with open('27outline.md', 'r', encoding='utf-8') as f:
        content = f.read()

    subject_blocks = re.split(r'\n##\s+', content)
    raw_data = {}
    for block in subject_blocks[1:]:
        lines = block.split('\n')
        subj_name = lines[0].strip()
        raw_data[subj_name] = {}
        ch_blocks = re.split(r'\n###\s+', block)
        for cb in ch_blocks[1:]:
            clines = cb.split('\n')
            ch_name = clines[0].strip()
            ch_text = '\n'.join(clines[1:]).strip()
            raw_data[subj_name][ch_name] = ch_text
    return raw_data

def build():
    raw_data = parse_raw_outline()
    base_dir = "outline"
    os.makedirs(base_dir, exist_ok=True)

    # Generate Master README
    readme_lines = [
        "# 408 核心考纲知识库与真题反哺演进系统",
        "",
        "> 基于 `27outline.md` 官方考试大纲扩写。作为与 `src/` 平行的知识大本营，",
        "> 每个章节预置深层物理机制、工程权衡与横向跨学科对比；",
        "> 通过做题将真题踩坑经验与极窄判据反向投喂回本库，打造真正闭环的考研知识体系。",
        "",
        "---",
        ""
    ]

    for subj in SUBJECT_MAP:
        s_id = subj["id"]
        s_title = subj["title"]
        s_dir = os.path.join(base_dir, s_id)
        os.makedirs(s_dir, exist_ok=True)

        readme_lines.append(f"## {s_title} (`{s_id}`)")
        readme_lines.append("")

        raw_subj = raw_data.get(subj["raw_title"], {})

        for fname, ch_raw_name, ch_desc in subj["chapters"]:
            fpath = os.path.join(s_dir, fname)
            rel_path = f"{s_id}/{fname}"
            readme_lines.append(f"- [{ch_raw_name}：{ch_desc}]({rel_path})")

            raw_body = raw_subj.get(ch_raw_name, "")

            doc_lines = [
                f"# {subj['title']} · {ch_raw_name}：{ch_desc}",
                "",
                f"[← 返回考纲知识库总目录](../README.md)",
                "",
                "---",
                "",
                "## 1. 考纲官方条目",
                "",
                raw_body if raw_body else "*(待补充官方考纲条目)*",
                "",
                "---",
                "",
                "## 2. 底层机理与物理必然性（为什么这么设计？）",
                "",
                "> **核心矛盾**：计算机系统在此处面临什么现实物理绝境或硬件成本约束？",
                "> 操作系统与硬件是如何通过折中（Trade-off）来化解矛盾的？",
                "",
                "*(在此展开系统级深层机制剖析，避免教条定义)*",
                "",
                "---",
                "",
                "## 3. 横向跨学科与相近机制谱系",
                "",
                "> 观察该机制在计算机组成原理、操作系统、体系结构与网络中的**同构映射**：",
                "",
                "| 学科层次 | 对应机制 | 应对的物理瓶颈 | 核心算法与策略 |",
                "| :--- | :--- | :--- | :--- |",
                "| **CPU / 计组** | *(如 Cache 行替换、TLB 缺失)* | 纳秒级速度落差 | 硬件 LRU / 伪 LRU / 随机 |",
                "| **操作系统** | *(如 虚存页置换、磁盘调度)* | 微秒/毫秒级 I/O 鸿沟 | CLOCK / 改进型 CLOCK / SCAN |",
                "| **网络系统** | *(如 流量控制、滑动窗口)* | 不可靠网络与带宽瓶颈 | 滑动窗口 / 拥塞避免 |",
                "",
                "---",
                "",
                "## 4. 408 核心命题陷阱与双胞胎真题对撞",
                "",
                "*(记录真题中的极窄对比，抓出决定胜负的唯一变量)*",
                "",
                "---",
                "",
                "## 5. 真题反哺与经验投喂区（持续演进）",
                "",
                "<!-- 在做题与复盘过程中，将真题提炼的深层洞察持续追加到本节 -->",
                "",
                "- *暂无投喂记录，等待真题实战反哺。*",
                ""
            ]

            # Write file
            with open(fpath, 'w', encoding='utf-8') as ch_f:
                ch_f.write('\n'.join(doc_lines))

        readme_lines.append("")
        readme_lines.append("---")
        readme_lines.append("")

    with open(os.path.join(base_dir, "README.md"), 'w', encoding='utf-8') as rm_f:
        rm_f.write('\n'.join(readme_lines))

    print(f"Successfully generated outline structure under {base_dir}/ with {sum(len(s['chapters']) for s in SUBJECT_MAP)} chapters.")

if __name__ == "__main__":
    build()
