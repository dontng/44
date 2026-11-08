# 操作系统（408 考纲知识库分册）

> 📍 **导航**：[返回知识库总目录](../README.md)
>
> 本分册共收录 **22 个细粒度专题**，覆盖操作系统基础与边界、进程管理、内存管理、文件管理、输入/输出（I/O）管理。

---

## 目录索引

### 操作系统基础与边界
- [CPU运行模式：内核态与用户态、特权指令与PSW状态标志](01-fundamentals/01-cpu-modes.md)
- [中断与异常处理：内部异常、外部中断分类与硬件隐指令执行流](01-fundamentals/02-interrupt-and-exception.md)
- [系统调用机制：陷入指令Trap、参数传递、用户栈与内核栈切换](01-fundamentals/03-system-call.md)
- [内核体系结构：宏内核、微内核、分层结构与消息通信代价](01-fundamentals/04-os-architecture.md)
- [虚拟机与虚拟化：Hypervisor/VMM层次、特权级压制与敏感指令模拟](01-fundamentals/05-virtual-machine.md)

### 进程管理
- [进程状态模型：7状态流转图、创建态/就绪态/阻塞态/挂起态物理本质](02-process/01-process-states.md)
- [CPU调度机制：高程/中程/低程调度、调度时机与抢占非抢占](02-process/02-cpu-scheduling.md)
- [典型调度算法：FCFS、SJF、优先级、时间片轮转与多级反馈队列](02-process/03-scheduling-algorithms.md)
- [同步与互斥基础：临界区准则、软件方法、硬件指令TSL与互斥锁](02-process/04-process-synchronization.md)
- [信号量机制与经典问题：整型与记录型信号量、生产者消费者、读者写者与哲学家](02-process/05-semaphores-pv.md)
- [死锁处理策略：死锁四大必要条件、预防避免(银行家算法)与检测解除](02-process/06-deadlock.md)
- [线程实现模型与进程间通信IPC：用户级/内核级线程、1:1/N:1/M:N多线程模型与共享存储/消息传递/管道机制](02-process/07-threads-and-ipc.md)

### 内存管理
- [内存管理基础与连续分配：逻辑地址与物理地址、重定位、单一分区/动态分区分配](03-memory/01-memory-basics.md)
- [基本分页与分段：页表结构、两级与多级页表、段表与段页式保护](03-memory/02-paging-and-segmentation.md)
- [虚拟内存与请求分页：局部性原理、请求分页页表项与缺页异常处理流](03-memory/03-virtual-memory-basics.md)
- [页置换算法深度解析：OPT、FIFO与Belady异常、LRU与CLOCK四轮扫描必然性](03-memory/04-page-replacement.md)
- [抖动与工作集模型：系统颠簸原因、工作集窗口计算与缺页率控制PFF](03-memory/05-thrashing-and-workingset.md)

### 文件管理
- [文件结构与索引节点：逻辑结构(流式/记录式)、物理结构(连续/链接/索引)与inode](04-file/01-file-concepts-and-inode.md)
- [目录与文件共享：树形目录结构、软链接(符号链接)与硬链接物理实现](04-file/02-directory-and-links.md)
- [文件系统全局结构与VFS：超级块、空闲空间管理(位示图/成组链接)与虚拟文件系统](04-file/03-file-system-layout.md)

### 输入/输出（I/O）管理
- [I/O控制与软件层次：轮询/中断/DMA/通道、设备驱动、设备独立性软件与缓冲管理](05-io/01-io-control-and-layers.md)
- [磁盘管理与磁头调度：磁盘物理结构、寻道延迟、FCFS/SSTF/SCAN/C-SCAN同构性](05-io/02-disk-scheduling.md)
