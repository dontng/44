# 408 核心考纲知识库（细粒度模块化架构）

> 本知识库严格依照 408 最新考纲与命题脉络进行细分拆解，全库共收录 **88 个细粒度考纲专题**（数据结构 29、计算机组成原理 19、操作系统 22、计算机网络 18）。
>
> - **无真题题面污染**：不堆砌孤立真题题干或年份代号，只沉淀系统机制与物理必然性；
> - **细粒度切分**：拒绝长篇大论，每个专题独立成篇，专注一个核心机理，查阅直达；
> - **网状贯通体系**：严密覆盖学科内跨章节依赖与跨学科协同；
> - **质量工程把控**：全库专题标准与审查进展详见 [质量审查与修复记录](audit/README.md)。

## 学科分册导航
- [数据结构（29 专题）](01-ds/README.md)
- [计算机组成原理（19 专题）](02-co/README.md)
- [操作系统（22 专题）](03-os/README.md)
- [计算机网络（18 专题）](04-cn/README.md)

---

## 数据结构 (`01-ds`) · [分册目录](01-ds/README.md)

### 基本概念与复杂度
- [数据结构基本概念：逻辑结构、物理结构与运算关系](01-ds/01-concepts/01-data-structures-basics.md)
- [算法复杂度分析：大O渐进分析、递归栈分析与循环累加模型](01-ds/01-concepts/02-algorithm-complexity.md)

### 线性表
- [顺序表：物理连续分配、随机存取与增删搬迁代价](01-ds/02-linear-list/01-sequential-list.md)
- [链表：单链表、双链表、循环链表与头结点作用](01-ds/02-linear-list/02-linked-list.md)

### 栈、队列和数组
- [栈：LIFO特性、表达式求值与括号匹配](01-ds/03-stack-queue-array/01-stack.md)
- [队列：FIFO特性、循环队列判空判满与双端队列](01-ds/03-stack-queue-array/02-queue.md)
- [特殊矩阵压缩存储：对称矩阵、三角矩阵与三对角矩阵下标映射](01-ds/03-stack-queue-array/03-matrix-compression.md)

### 树与二叉树
- [二叉树性质与存储：满二叉树、完全二叉树与节点计算公式](01-ds/04-tree/01-binary-tree-properties.md)
- [二叉树遍历：先序、中序、后序与层次遍历递归与非递归](01-ds/04-tree/02-tree-traversal.md)
- [线索二叉树：线索化定义、空指针利用与前驱后继寻找](01-ds/04-tree/03-threaded-binary-tree.md)
- [树与森林：孩子兄弟表示法与森林-二叉树互转](01-ds/04-tree/04-forest-conversion.md)
- [哈夫曼树与编码：带权路径长度WPL与前缀编码构建](01-ds/04-tree/05-huffman-tree.md)
- [并查集与堆：双亲表示法、路径压缩与大根堆维护](01-ds/04-tree/06-heap-and-union-find.md)

### 图
- [图的存储结构：邻接矩阵、邻接表、十字链表与邻接多重表](01-ds/05-graph/01-graph-storage.md)
- [图的遍历：深度优先搜索DFS与广度优先搜索BFS](01-ds/05-graph/02-graph-traversal.md)
- [最小生成树：Prim算法与Kruskal算法权衡](01-ds/05-graph/03-minimum-spanning-tree.md)
- [最短路径：Dijkstra单源算法与Floyd全源算法](01-ds/05-graph/04-shortest-path.md)
- [拓扑排序与关键路径：AOV网环路检测与AOE网关键活动](01-ds/05-graph/05-topo-and-critical-path.md)

### 查找
- [线性查找与折半查找：顺序查找、分块查找与二分查找判定树](01-ds/06-search/01-linear-and-binary-search.md)
- [二叉搜索树BST：查找、插入、删除与中序有序性](01-ds/06-search/02-binary-search-tree.md)
- [平衡二叉树与红黑树：AVL旋转调整与红黑树五大特性](01-ds/06-search/03-balanced-trees.md)
- [B树与B+树：多路平衡查找树、节点分裂合并与索引应用](01-ds/06-search/04-b-trees.md)
- [散列表：散列函数构造、冲突解决与装填因子分析](01-ds/06-search/05-hash-tables.md)
- [字符串模式匹配与KMP算法：朴素匹配回溯缺陷、主串不回溯推导、next与nextval数组手算轨迹](01-ds/06-search/06-string-matching-kmp.md)

### 排序
- [简单插入、冒泡与选择：稳定排序与就地排序基础](01-ds/07-sort/01-simple-sorts.md)
- [快速排序与归并排序：分治思想、轴点划分与二路归并](01-ds/07-sort/02-efficient-sorts.md)
- [堆排序：堆调整建堆、筛选下沉与原地堆排](01-ds/07-sort/03-heap-sort.md)
- [外部排序：多路平衡归并、败者树与置换-选择排序](01-ds/07-sort/04-external-sort.md)
- [希尔排序与基数排序：增量序列分组插入、稳定性反例与多关键字LSD分配收集轨迹](01-ds/07-sort/05-shell-and-radix-sort.md)

---

## 计算机组成原理 (`02-co`) · [分册目录](02-co/README.md)

### 计算机系统概述
- [计算机硬件层次：冯诺依曼结构、总线架构与部件连接](02-co/01-system-overview/01-computer-architecture.md)
- [性能指标：CPI、MIPS、时钟周期与响应时间计算](02-co/01-system-overview/02-performance-metrics.md)

### 数据的表示和运算
- [定点数表示与补码加减：原码反码补码移码、溢出判断与标志位](02-co/02-data-representation/01-fixed-point-numbers.md)
- [浮点数与IEEE 754：符号位阶码尾数、规格化与特殊值](02-co/02-data-representation/02-floating-point-ieee754.md)
- [运算器电路：加法器进位链与算术逻辑单元ALU](02-co/02-data-representation/03-alu-and-circuits.md)
- [大小端对齐与C语言机器级表示：大小端字节序、结构体边界对齐、选择循环分支与过程调用栈帧](02-co/02-data-representation/04-alignment-and-c-machine-code.md)

### 存储器层次结构
- [存储器分类与技术：SRAM/DRAM刷新、ROM分类与多模块交替存储](02-co/03-memory-hierarchy/01-memory-types.md)
- [Cache映射与替换：直接映射、组相联映射、全相联与写策略](02-co/03-memory-hierarchy/02-cache-mapping.md)
- [硬件级虚拟存储：页式虚存、TLB快表与段页式MMU转换](02-co/03-memory-hierarchy/03-virtual-memory-hardware.md)

### 指令系统
- [指令格式设计：定长与变长操作码、扩展操作码技术](02-co/04-instruction-system/01-instruction-formats.md)
- [寻址方式：立即、直接、间接、寄存器、基址变址相对寻址](02-co/04-instruction-system/02-addressing-modes.md)
- [CISC与RISC：复杂指令集与精简指令集权衡与流水线亲和性](02-co/04-instruction-system/03-cisc-and-risc.md)

### 中央处理器（CPU）
- [CPU数据通路：总线连接、专用数据通路与控制信号时序](02-co/05-cpu/01-cpu-datapath.md)
- [控制器设计：硬布线控制器与微程序控制器比较](02-co/05-cpu/02-control-unit-design.md)
- [指令流水线与冲突：结构冲突、数据冲突转发与控制冲突预测](02-co/05-cpu/03-pipeline-hazards.md)
- [多处理器架构与硬件多线程：Flynn分类SISD/SIMD/MIMD、SMP/UMA/NUMA与细粒度/粗粒度/SMT多线程](02-co/05-cpu/04-multiprocessor-and-multithreading.md)

### 总线和输入/输出系统
- [系统总线与仲裁：同步异步定时、集中式仲裁与突发传输](02-co/06-bus-and-io/01-bus-mechanisms.md)
- [I/O接口与寻址：统一编址与独立编址、接口控制寄存器](02-co/06-bus-and-io/02-io-interfaces.md)
- [中断处理与DMA方式：硬件隐指令、多重中断屏蔽字与DMA数据通路](02-co/06-bus-and-io/03-interrupt-and-dma.md)

---

## 操作系统 (`03-os`) · [分册目录](03-os/README.md)

### 操作系统基础与边界
- [CPU运行模式：内核态与用户态、特权指令与PSW状态标志](03-os/01-fundamentals/01-cpu-modes.md)
- [中断与异常处理：内部异常、外部中断分类与硬件隐指令执行流](03-os/01-fundamentals/02-interrupt-and-exception.md)
- [系统调用机制：陷入指令Trap、参数传递、用户栈与内核栈切换](03-os/01-fundamentals/03-system-call.md)
- [内核体系结构：宏内核、微内核、分层结构与消息通信代价](03-os/01-fundamentals/04-os-architecture.md)
- [虚拟机与虚拟化：Hypervisor/VMM层次、特权级压制与敏感指令模拟](03-os/01-fundamentals/05-virtual-machine.md)

### 进程管理
- [进程状态模型：7状态流转图、创建态/就绪态/阻塞态/挂起态物理本质](03-os/02-process/01-process-states.md)
- [CPU调度机制：高程/中程/低程调度、调度时机与抢占非抢占](03-os/02-process/02-cpu-scheduling.md)
- [典型调度算法：FCFS、SJF、优先级、时间片轮转与多级反馈队列](03-os/02-process/03-scheduling-algorithms.md)
- [同步与互斥基础：临界区准则、软件方法、硬件指令TSL与互斥锁](03-os/02-process/04-process-synchronization.md)
- [信号量机制与经典问题：整型与记录型信号量、生产者消费者、读者写者与哲学家](03-os/02-process/05-semaphores-pv.md)
- [死锁处理策略：死锁四大必要条件、预防避免(银行家算法)与检测解除](03-os/02-process/06-deadlock.md)
- [线程实现模型与进程间通信IPC：用户级/内核级线程、1:1/N:1/M:N多线程模型与共享存储/消息传递/管道机制](03-os/02-process/07-threads-and-ipc.md)

### 内存管理
- [内存管理基础与连续分配：逻辑地址与物理地址、重定位、单一分区/动态分区分配](03-os/03-memory/01-memory-basics.md)
- [基本分页与分段：页表结构、两级与多级页表、段表与段页式保护](03-os/03-memory/02-paging-and-segmentation.md)
- [虚拟内存与请求分页：局部性原理、请求分页页表项与缺页异常处理流](03-os/03-memory/03-virtual-memory-basics.md)
- [页置换算法深度解析：OPT、FIFO与Belady异常、LRU与CLOCK四轮扫描必然性](03-os/03-memory/04-page-replacement.md)
- [抖动与工作集模型：系统颠簸原因、工作集窗口计算与缺页率控制PFF](03-os/03-memory/05-thrashing-and-workingset.md)

### 文件管理
- [文件结构与索引节点：逻辑结构(流式/记录式)、物理结构(连续/链接/索引)与inode](03-os/04-file/01-file-concepts-and-inode.md)
- [目录与文件共享：树形目录结构、软链接(符号链接)与硬链接物理实现](03-os/04-file/02-directory-and-links.md)
- [文件系统全局结构与VFS：超级块、空闲空间管理(位示图/成组链接)与虚拟文件系统](03-os/04-file/03-file-system-layout.md)

### 输入/输出（I/O）管理
- [I/O控制与软件层次：轮询/中断/DMA/通道、设备驱动、设备独立性软件与缓冲管理](03-os/05-io/01-io-control-and-layers.md)
- [磁盘管理与磁头调度：磁盘物理结构、寻道延迟、FCFS/SSTF/SCAN/C-SCAN同构性](03-os/05-io/02-disk-scheduling.md)

---

## 计算机网络 (`04-cn`) · [分册目录](04-cn/README.md)

### 计算机网络概述
- [网络体系结构：OSI七层参考模型与TCP/IP四层模型协议封装](04-cn/01-architecture/01-network-layers.md)
- [网络性能与时延：发送时延、传播时延、处理时延与排队时延计算](04-cn/01-architecture/02-performance-delays.md)

### 物理层
- [信道极限容量：奈氏准则(无噪)与香农定理(有噪)极限速率计算](04-cn/02-physical/01-channel-limits.md)
- [编码调制与信道复用：基带编码(曼彻斯特/差分曼彻斯特)与FDM/TDM/WDM/CDM](04-cn/02-physical/02-encoding-and-multiplexing.md)

### 数据链路层
- [组帧与差错控制：字符填充/比特填充、奇偶校验与循环冗余校验CRC](04-cn/03-datalink/01-framing-and-error-control.md)
- [点对点可靠传输：停等协议、后退N帧(GBN)与选择重传(SR)窗口限制](04-cn/03-datalink/02-sliding-window-protocols.md)
- [介质访问与局域网：CSMA/CD碰撞检测、争用期最小帧长、以太网MAC与交换机自学习](04-cn/03-datalink/03-mac-and-ethernet.md)
- [无线局域网802.11与VLAN虚拟局域网：CSMA/CA碰撞避免、IFS/RTS/CTS隐蔽站、802.11四地址帧、802.1Q标签与ALOHA/令牌](04-cn/03-datalink/04-wlan-and-vlan.md)

### 网络层
- [IP编址与子网划分：分类IP、子网掩码、CIDR无分类编址与路由聚合](04-cn/04-network/01-ip-addressing-and-cidr.md)
- [路由协议原理：距离向量算法(RIP)、链路状态算法(OSPF)与BGP路径向量](04-cn/04-network/02-routing-protocols.md)
- [网络层辅助协议与设备：ARP地址解析、ICMP差错与询问、路由器转发表结构](04-cn/04-network/03-routing-devices-and-icmp.md)
- [IPv6、IP组播、移动IP与SDN：IPv6固定首部与过渡机制、IGMP与组播路由、移动IP代理转发与SDN控制数据平面分离](04-cn/04-network/04-ipv6-multicast-sdn.md)

### 传输层
- [传输层服务与UDP协议：端口复用分用、UDP报头格式与无连接特性](04-cn/05-transport/01-transport-services-udp.md)
- [TCP连接与滑动窗口：三次握手四次挥手、序号确认号与滑动窗口流量控制](04-cn/05-transport/02-tcp-connection-and-flow.md)
- [TCP拥塞控制算法：慢启动、拥塞避免、快重传与快恢复AIMD状态机](04-cn/05-transport/03-tcp-congestion-control.md)

### 应用层
- [域名系统DNS：根/顶级/权限域名服务器、递归查询与迭代查询解析](04-cn/06-application/01-dns-system.md)
- [超文本传输协议HTTP：持久非持久连接、状态码、HTTP/1.1与HTTP/2对比](04-cn/06-application/02-http-protocol.md)
- [文件传输与电子邮件：FTP双连接(控制21/数据20)、SMTP与POP3/IMAP](04-cn/06-application/03-email-and-ftp.md)

---
