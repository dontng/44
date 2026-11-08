# 计算机组成原理（408 考纲知识库分册）

> 📍 **导航**：[返回知识库总目录](../README.md)
>
> 本分册共收录 **19 个细粒度专题**，覆盖计算机系统概述、数据的表示和运算、存储器层次结构、指令系统、中央处理器（CPU）、总线和输入/输出系统。

---

## 目录索引

### 计算机系统概述
- [计算机硬件层次：冯诺依曼结构、总线架构与部件连接](01-system-overview/01-computer-architecture.md)
- [性能指标：CPI、MIPS、时钟周期与响应时间计算](01-system-overview/02-performance-metrics.md)

### 数据的表示和运算
- [定点数表示与补码加减：原码反码补码移码、溢出判断与标志位](02-data-representation/01-fixed-point-numbers.md)
- [浮点数与IEEE 754：符号位阶码尾数、规格化与特殊值](02-data-representation/02-floating-point-ieee754.md)
- [运算器电路：加法器进位链与算术逻辑单元ALU](02-data-representation/03-alu-and-circuits.md)
- [大小端对齐与C语言机器级表示：大小端字节序、结构体边界对齐、选择循环分支与过程调用栈帧](02-data-representation/04-alignment-and-c-machine-code.md)

### 存储器层次结构
- [存储器分类与技术：SRAM/DRAM刷新、ROM分类与多模块交替存储](03-memory-hierarchy/01-memory-types.md)
- [Cache映射与替换：直接映射、组相联映射、全相联与写策略](03-memory-hierarchy/02-cache-mapping.md)
- [硬件级虚拟存储：页式虚存、TLB快表与段页式MMU转换](03-memory-hierarchy/03-virtual-memory-hardware.md)

### 指令系统
- [指令格式设计：定长与变长操作码、扩展操作码技术](04-instruction-system/01-instruction-formats.md)
- [寻址方式：立即、直接、间接、寄存器、基址变址相对寻址](04-instruction-system/02-addressing-modes.md)
- [CISC与RISC：复杂指令集与精简指令集权衡与流水线亲和性](04-instruction-system/03-cisc-and-risc.md)

### 中央处理器（CPU）
- [CPU数据通路：总线连接、专用数据通路与控制信号时序](05-cpu/01-cpu-datapath.md)
- [控制器设计：硬布线控制器与微程序控制器比较](05-cpu/02-control-unit-design.md)
- [指令流水线与冲突：结构冲突、数据冲突转发与控制冲突预测](05-cpu/03-pipeline-hazards.md)
- [多处理器架构与硬件多线程：Flynn分类SISD/SIMD/MIMD、SMP/UMA/NUMA与细粒度/粗粒度/SMT多线程](05-cpu/04-multiprocessor-and-multithreading.md)

### 总线和输入/输出系统
- [系统总线与仲裁：同步异步定时、集中式仲裁与突发传输](06-bus-and-io/01-bus-mechanisms.md)
- [I/O接口与寻址：统一编址与独立编址、接口控制寄存器](06-bus-and-io/02-io-interfaces.md)
- [中断处理与DMA方式：硬件隐指令、多重中断屏蔽字与DMA数据通路](06-bus-and-io/03-interrupt-and-dma.md)
