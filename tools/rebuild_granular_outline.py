#!/usr/bin/env python3
"""Build and synchronize fine-grained 2027 Syllabus Knowledge Base indices under outline/.

Manages:
- outline/README.md (Master index of all 88 syllabus topics across 4 subjects)
- outline/<subj>/README.md (Subject-level index files)
- Safe initialization of missing topic files without overwriting existing content.
"""

import os
import argparse

OUTLINE_DIR = "outline"

TOPIC_STRUCTURE = {
    "01-ds": {
        "title": "数据结构",
        "sections": {
            "01-concepts": {
                "title": "基本概念与复杂度",
                "files": [
                    ("01-data-structures-basics.md", "数据结构基本概念", "逻辑结构、物理结构与运算关系"),
                    ("02-algorithm-complexity.md", "算法复杂度分析", "大O渐进分析、递归栈分析与循环累加模型")
                ]
            },
            "02-linear-list": {
                "title": "线性表",
                "files": [
                    ("01-sequential-list.md", "顺序表", "物理连续分配、随机存取与增删搬迁代价"),
                    ("02-linked-list.md", "链表", "单链表、双链表、循环链表与头结点作用")
                ]
            },
            "03-stack-queue-array": {
                "title": "栈、队列和数组",
                "files": [
                    ("01-stack.md", "栈", "LIFO特性、表达式求值与括号匹配"),
                    ("02-queue.md", "队列", "FIFO特性、循环队列判空判满与双端队列"),
                    ("03-matrix-compression.md", "特殊矩阵压缩存储", "对称矩阵、三角矩阵与三对角矩阵下标映射")
                ]
            },
            "04-tree": {
                "title": "树与二叉树",
                "files": [
                    ("01-binary-tree-properties.md", "二叉树性质与存储", "满二叉树、完全二叉树与节点计算公式"),
                    ("02-tree-traversal.md", "二叉树遍历", "先序、中序、后序与层次遍历递归与非递归"),
                    ("03-threaded-binary-tree.md", "线索二叉树", "线索化定义、空指针利用与前驱后继寻找"),
                    ("04-forest-conversion.md", "树与森林", "孩子兄弟表示法与森林-二叉树互转"),
                    ("05-huffman-tree.md", "哈夫曼树与编码", "带权路径长度WPL与前缀编码构建"),
                    ("06-heap-and-union-find.md", "并查集与堆", "双亲表示法、路径压缩与大根堆维护")
                ]
            },
            "05-graph": {
                "title": "图",
                "files": [
                    ("01-graph-storage.md", "图的存储结构", "邻接矩阵、邻接表、十字链表与邻接多重表"),
                    ("02-graph-traversal.md", "图的遍历", "深度优先搜索DFS与广度优先搜索BFS"),
                    ("03-minimum-spanning-tree.md", "最小生成树", "Prim算法与Kruskal算法权衡"),
                    ("04-shortest-path.md", "最短路径", "Dijkstra单源算法与Floyd全源算法"),
                    ("05-topo-and-critical-path.md", "拓扑排序与关键路径", "AOV网环路检测与AOE网关键活动")
                ]
            },
            "06-search": {
                "title": "查找",
                "files": [
                    ("01-linear-and-binary-search.md", "线性查找与折半查找", "顺序查找、分块查找与二分查找判定树"),
                    ("02-binary-search-tree.md", "二叉搜索树BST", "查找、插入、删除与中序有序性"),
                    ("03-balanced-trees.md", "平衡二叉树与红黑树", "AVL旋转调整与红黑树五大特性"),
                    ("04-b-trees.md", "B树与B+树", "多路平衡查找树、节点分裂合并与索引应用"),
                    ("05-hash-tables.md", "散列表", "散列函数构造、冲突解决与装填因子分析"),
                    ("06-string-matching-kmp.md", "字符串模式匹配与KMP算法", "朴素匹配回溯缺陷、主串不回溯推导、next与nextval数组手算轨迹")
                ]
            },
            "07-sort": {
                "title": "排序",
                "files": [
                    ("01-simple-sorts.md", "简单插入、冒泡与选择", "稳定排序与就地排序基础"),
                    ("02-efficient-sorts.md", "快速排序与归并排序", "分治思想、轴点划分与二路归并"),
                    ("03-heap-sort.md", "堆排序", "堆调整建堆、筛选下沉与原地堆排"),
                    ("04-external-sort.md", "外部排序", "多路平衡归并、败者树与置换-选择排序"),
                    ("05-shell-and-radix-sort.md", "希尔排序与基数排序", "增量序列分组插入、稳定性反例与多关键字LSD分配收集轨迹")
                ]
            }
        }
    },
    "02-co": {
        "title": "计算机组成原理",
        "sections": {
            "01-system-overview": {
                "title": "计算机系统概述",
                "files": [
                    ("01-computer-architecture.md", "计算机硬件层次", "冯诺依曼结构、总线架构与部件连接"),
                    ("02-performance-metrics.md", "性能指标", "CPI、MIPS、时钟周期与响应时间计算")
                ]
            },
            "02-data-representation": {
                "title": "数据的表示和运算",
                "files": [
                    ("01-fixed-point-numbers.md", "定点数表示与补码加减", "原码反码补码移码、溢出判断与标志位"),
                    ("02-floating-point-ieee754.md", "浮点数与IEEE 754", "符号位阶码尾数、规格化与特殊值"),
                    ("03-alu-and-circuits.md", "运算器电路", "加法器进位链与算术逻辑单元ALU"),
                    ("04-alignment-and-c-machine-code.md", "大小端对齐与C语言机器级表示", "大小端字节序、结构体边界对齐、选择循环分支与过程调用栈帧")
                ]
            },
            "03-memory-hierarchy": {
                "title": "存储器层次结构",
                "files": [
                    ("01-memory-types.md", "存储器分类与技术", "SRAM/DRAM刷新、ROM分类与多模块交替存储"),
                    ("02-cache-mapping.md", "Cache映射与替换", "直接映射、组相联映射、全相联与写策略"),
                    ("03-virtual-memory-hardware.md", "硬件级虚拟存储", "页式虚存、TLB快表与段页式MMU转换")
                ]
            },
            "04-instruction-system": {
                "title": "指令系统",
                "files": [
                    ("01-instruction-formats.md", "指令格式设计", "定长与变长操作码、扩展操作码技术"),
                    ("02-addressing-modes.md", "寻址方式", "立即、直接、间接、寄存器、基址变址相对寻址"),
                    ("03-cisc-and-risc.md", "CISC与RISC", "复杂指令集与精简指令集权衡与流水线亲和性")
                ]
            },
            "05-cpu": {
                "title": "中央处理器（CPU）",
                "files": [
                    ("01-cpu-datapath.md", "CPU数据通路", "总线连接、专用数据通路与控制信号时序"),
                    ("02-control-unit-design.md", "控制器设计", "硬布线控制器与微程序控制器比较"),
                    ("03-pipeline-hazards.md", "指令流水线与冲突", "结构冲突、数据冲突转发与控制冲突预测"),
                    ("04-multiprocessor-and-multithreading.md", "多处理器架构与硬件多线程", "Flynn分类SISD/SIMD/MIMD、SMP/UMA/NUMA与细粒度/粗粒度/SMT多线程")
                ]
            },
            "06-bus-and-io": {
                "title": "总线和输入/输出系统",
                "files": [
                    ("01-bus-mechanisms.md", "系统总线与仲裁", "同步异步定时、集中式仲裁与突发传输"),
                    ("02-io-interfaces.md", "I/O接口与寻址", "统一编址与独立编址、接口控制寄存器"),
                    ("03-interrupt-and-dma.md", "中断处理与DMA方式", "硬件隐指令、多重中断屏蔽字与DMA数据通路")
                ]
            }
        }
    },
    "03-os": {
        "title": "操作系统",
        "sections": {
            "01-fundamentals": {
                "title": "操作系统基础与边界",
                "files": [
                    ("01-cpu-modes.md", "CPU运行模式", "内核态与用户态、特权指令与PSW状态标志"),
                    ("02-interrupt-and-exception.md", "中断与异常处理", "内部异常、外部中断分类与硬件隐指令执行流"),
                    ("03-system-call.md", "系统调用机制", "陷入指令Trap、参数传递、用户栈与内核栈切换"),
                    ("04-os-architecture.md", "内核体系结构", "宏内核、微内核、分层结构与消息通信代价"),
                    ("05-virtual-machine.md", "虚拟机与虚拟化", "Hypervisor/VMM层次、特权级压制与敏感指令模拟")
                ]
            },
            "02-process": {
                "title": "进程管理",
                "files": [
                    ("01-process-states.md", "进程状态模型", "7状态流转图、创建态/就绪态/阻塞态/挂起态物理本质"),
                    ("02-cpu-scheduling.md", "CPU调度机制", "高程/中程/低程调度、调度时机与抢占非抢占"),
                    ("03-scheduling-algorithms.md", "典型调度算法", "FCFS、SJF、优先级、时间片轮转与多级反馈队列"),
                    ("04-process-synchronization.md", "同步与互斥基础", "临界区准则、软件方法、硬件指令TSL与互斥锁"),
                    ("05-semaphores-pv.md", "信号量机制与经典问题", "整型与记录型信号量、生产者消费者、读者写者与哲学家"),
                    ("06-deadlock.md", "死锁处理策略", "死锁四大必要条件、预防避免(银行家算法)与检测解除"),
                    ("07-threads-and-ipc.md", "线程实现模型与进程间通信IPC", "用户级/内核级线程、1:1/N:1/M:N多线程模型与共享存储/消息传递/管道机制")
                ]
            },
            "03-memory": {
                "title": "内存管理",
                "files": [
                    ("01-memory-basics.md", "内存管理基础与连续分配", "逻辑地址与物理地址、重定位、单一分区/动态分区分配"),
                    ("02-paging-and-segmentation.md", "基本分页与分段", "页表结构、两级与多级页表、段表与段页式保护"),
                    ("03-virtual-memory-basics.md", "虚拟内存与请求分页", "局部性原理、请求分页页表项与缺页异常处理流"),
                    ("04-page-replacement.md", "页置换算法深度解析", "OPT、FIFO与Belady异常、LRU与CLOCK四轮扫描必然性"),
                    ("05-thrashing-and-workingset.md", "抖动与工作集模型", "系统颠簸原因、工作集窗口计算与缺页率控制PFF")
                ]
            },
            "04-file": {
                "title": "文件管理",
                "files": [
                    ("01-file-concepts-and-inode.md", "文件结构与索引节点", "逻辑结构(流式/记录式)、物理结构(连续/链接/索引)与inode"),
                    ("02-directory-and-links.md", "目录与文件共享", "树形目录结构、软链接(符号链接)与硬链接物理实现"),
                    ("03-file-system-layout.md", "文件系统全局结构与VFS", "超级块、空闲空间管理(位示图/成组链接)与虚拟文件系统")
                ]
            },
            "05-io": {
                "title": "输入/输出（I/O）管理",
                "files": [
                    ("01-io-control-and-layers.md", "I/O控制与软件层次", "轮询/中断/DMA/通道、设备驱动、设备独立性软件与缓冲管理"),
                    ("02-disk-scheduling.md", "磁盘管理与磁头调度", "磁盘物理结构、寻道延迟、FCFS/SSTF/SCAN/C-SCAN同构性")
                ]
            }
        }
    },
    "04-cn": {
        "title": "计算机网络",
        "sections": {
            "01-architecture": {
                "title": "计算机网络概述",
                "files": [
                    ("01-network-layers.md", "网络体系结构", "OSI七层参考模型与TCP/IP四层模型协议封装"),
                    ("02-performance-delays.md", "网络性能与时延", "发送时延、传播时延、处理时延与排队时延计算")
                ]
            },
            "02-physical": {
                "title": "物理层",
                "files": [
                    ("01-channel-limits.md", "信道极限容量", "奈氏准则(无噪)与香农定理(有噪)极限速率计算"),
                    ("02-encoding-and-multiplexing.md", "编码调制与信道复用", "基带编码(曼彻斯特/差分曼彻斯特)与FDM/TDM/WDM/CDM")
                ]
            },
            "03-datalink": {
                "title": "数据链路层",
                "files": [
                    ("01-framing-and-error-control.md", "组帧与差错控制", "字符填充/比特填充、奇偶校验与循环冗余校验CRC"),
                    ("02-sliding-window-protocols.md", "点对点可靠传输", "停等协议、后退N帧(GBN)与选择重传(SR)窗口限制"),
                    ("03-mac-and-ethernet.md", "介质访问与局域网", "CSMA/CD碰撞检测、争用期最小帧长、以太网MAC与交换机自学习"),
                    ("04-wlan-and-vlan.md", "无线局域网802.11与VLAN虚拟局域网", "CSMA/CA碰撞避免、IFS/RTS/CTS隐蔽站、802.11四地址帧、802.1Q标签与ALOHA/令牌")
                ]
            },
            "04-network": {
                "title": "网络层",
                "files": [
                    ("01-ip-addressing-and-cidr.md", "IP编址与子网划分", "分类IP、子网掩码、CIDR无分类编址与路由聚合"),
                    ("02-routing-protocols.md", "路由协议原理", "距离向量算法(RIP)、链路状态算法(OSPF)与BGP路径向量"),
                    ("03-routing-devices-and-icmp.md", "网络层辅助协议与设备", "ARP地址解析、ICMP差错与询问、路由器转发表结构"),
                    ("04-ipv6-multicast-sdn.md", "IPv6、IP组播、移动IP与SDN", "IPv6固定首部与过渡机制、IGMP与组播路由、移动IP代理转发与SDN控制数据平面分离")
                ]
            },
            "05-transport": {
                "title": "传输层",
                "files": [
                    ("01-transport-services-udp.md", "传输层服务与UDP协议", "端口复用分用、UDP报头格式与无连接特性"),
                    ("02-tcp-connection-and-flow.md", "TCP连接与滑动窗口", "三次握手四次挥手、序号确认号与滑动窗口流量控制"),
                    ("03-tcp-congestion-control.md", "TCP拥塞控制算法", "慢启动、拥塞避免、快重传与快恢复AIMD状态机")
                ]
            },
            "06-application": {
                "title": "应用层",
                "files": [
                    ("01-dns-system.md", "域名系统DNS", "根/顶级/权限域名服务器、递归查询与迭代查询解析"),
                    ("02-http-protocol.md", "超文本传输协议HTTP", "持久非持久连接、状态码、HTTP/1.1与HTTP/2对比"),
                    ("03-email-and-ftp.md", "文件传输与电子邮件", "FTP双连接(控制21/数据20)、SMTP与POP3/IMAP")
                ]
            }
        }
    }
}


def sync_indices():
    """Generate or update outline/README.md and the 4 outline/<subj>/README.md files."""
    os.makedirs(OUTLINE_DIR, exist_ok=True)

    counts = {
        subj_key: sum(len(sec["files"]) for sec in subj_val["sections"].values())
        for subj_key, subj_val in TOPIC_STRUCTURE.items()
    }
    total_topics = sum(counts.values())

    # 1. Master outline/README.md
    master_lines = [
        "# 408 核心考纲知识库（细粒度模块化架构）",
        "",
        f"> 本知识库严格依照 408 最新考纲与命题脉络进行细分拆解，全库共收录 **{total_topics} 个细粒度考纲专题**（数据结构 {counts['01-ds']}、计算机组成原理 {counts['02-co']}、操作系统 {counts['03-os']}、计算机网络 {counts['04-cn']}）。",
        ">",
        "> - **无真题题面污染**：不堆砌孤立真题题干或年份代号，只沉淀系统机制与物理必然性；",
        "> - **细粒度切分**：拒绝长篇大论，每个专题独立成篇，专注一个核心机理，查阅直达；",
        "> - **网状贯通体系**：严密覆盖学科内跨章节依赖与跨学科协同；",
        "> - **质量工程把控**：全库专题标准与审查进展详见 [质量审查与修复记录](audit/README.md)。",
        "",
        "## 学科分册导航",
        f"- [数据结构（{counts['01-ds']} 专题）](01-ds/README.md)",
        f"- [计算机组成原理（{counts['02-co']} 专题）](02-co/README.md)",
        f"- [操作系统（{counts['03-os']} 专题）](03-os/README.md)",
        f"- [计算机网络（{counts['04-cn']} 专题）](04-cn/README.md)",
        "",
        "---",
        ""
    ]

    for subj_key, subj_val in TOPIC_STRUCTURE.items():
        subj_dir = os.path.join(OUTLINE_DIR, subj_key)
        os.makedirs(subj_dir, exist_ok=True)
        master_lines.append(f"## {subj_val['title']} (`{subj_key}`) · [分册目录]({subj_key}/README.md)")
        master_lines.append("")

        # 2. Subject outline/<subj>/README.md
        subject_lines = [
            f"# {subj_val['title']}（408 考纲知识库分册）",
            "",
            "> 📍 **导航**：[返回知识库总目录](../README.md)",
            ">",
            f"> 本分册共收录 **{counts[subj_key]} 个细粒度专题**，覆盖" + "、".join(sec["title"] for sec in subj_val["sections"].values()) + "。",
            "",
            "---",
            "",
            "## 目录索引",
            ""
        ]

        for sec_key, sec_val in subj_val["sections"].items():
            sec_dir = os.path.join(subj_dir, sec_key)
            os.makedirs(sec_dir, exist_ok=True)

            master_lines.append(f"### {sec_val['title']}")
            subject_lines.append(f"### {sec_val['title']}")

            for fname, ftitle, fdesc in sec_val["files"]:
                master_rel = f"{subj_key}/{sec_key}/{fname}"
                subject_rel = f"{sec_key}/{fname}"
                master_lines.append(f"- [{ftitle}：{fdesc}]({master_rel})")
                subject_lines.append(f"- [{ftitle}：{fdesc}]({subject_rel})")

            master_lines.append("")
            subject_lines.append("")

        master_lines.append("---")
        master_lines.append("")

        subj_readme_path = os.path.join(subj_dir, "README.md")
        with open(subj_readme_path, "w", encoding="utf-8") as f:
            f.write("\n".join(subject_lines))
        print(f"Updated subject index: {subj_readme_path} ({counts[subj_key]} topics)")

    master_readme_path = os.path.join(OUTLINE_DIR, "README.md")
    with open(master_readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(master_lines))
    print(f"Updated master index: {master_readme_path} ({total_topics} topics)")


def init_missing_topics():
    """Safely initialize empty placeholder files ONLY for files that do not exist."""
    created_count = 0
    for subj_key, subj_val in TOPIC_STRUCTURE.items():
        for sec_key, sec_val in subj_val["sections"].items():
            sec_dir = os.path.join(OUTLINE_DIR, subj_key, sec_key)
            os.makedirs(sec_dir, exist_ok=True)
            for fname, ftitle, fdesc in sec_val["files"]:
                fpath = os.path.join(sec_dir, fname)
                if not os.path.exists(fpath):
                    doc_lines = [
                        f"# {ftitle}",
                        "",
                        f"> 所属模块：[408 考纲知识库](../../README.md) $\\to$ [{subj_val['title']}](../README.md) $\\to$ {sec_val['title']}",
                        "",
                        "---",
                        "",
                        "## 1. 2027 考纲官方定位",
                        f"- **考察要点**：{fdesc}",
                        "",
                        "---",
                        "",
                        "## 2. 核心机理与物理必然性（为什么这么设计？）",
                        "> 思考路径：底层面临什么硬件物理约束或性能瓶颈？系统设计者通过什么折中（Trade-off）来化解矛盾？",
                        "",
                        "*(待补齐深入机制)*",
                        "",
                        "---",
                        "",
                        "## 3. 本学科内跨章节关联（网状贯通）",
                        "> 拒绝知识孤岛，梳理该知识点与本科目其他章节的核心因果联动：",
                        "",
                        "- *(待添加跨章节依赖)*",
                        "",
                        "---",
                        "",
                        "## 4. 闭环判定模型与核心认知结论",
                        "> 考场定性时的不可动摇依据：",
                        "",
                        "- *(待归纳闭环判定)*",
                        ""
                    ]
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write("\n".join(doc_lines))
                    print(f"Created placeholder: {fpath}")
                    created_count += 1
    print(f"Initialized {created_count} missing topic files.")


def main():
    parser = argparse.ArgumentParser(description="Manage outline topic structure and README indices.")
    parser.add_argument("--sync-index", action="store_true", help="Sync master and subject index README files")
    parser.add_argument("--init-missing", action="store_true", help="Initialize placeholder templates for missing topic files only")
    args = parser.parse_args()

    # Always safely sync indices unless other flags specified
    sync_indices()

    if args.init_missing:
        init_missing_topics()


if __name__ == "__main__":
    main()
