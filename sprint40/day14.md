# Day 14｜组成原理＋计算机网络

[← Day 13](day13.md) · [总入口](README.md) · [Day 15 →](day15.md)

**选择题：14道，来自两份完整src题单；大题：1道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：65—105分钟。** 选择题及核对约35—60分钟，大题约25—35分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0818 · 组成原理

[程序层级：从源程序到CPU真正执行的对象](../src/0818.md) · 9道 · 首次。

### 选择题1｜2020-12

<img src="../bank/2020/q12.png" alt="2020-12" style="display: block; width: 42.41em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

机器字长通常对应CPU一次处理的基本整数位数，ALU与通用寄存器宽度据此设计，选Ⅰ、Ⅲ。IR宽度取决于指令长度，指令可多字或变长；浮点寄存器宽度取决于浮点格式，也不必与整数机器字长一致。

</details>

### 选择题2｜2021-17

<img src="../bank/2021/q17.png" alt="2021-17" style="display: block; width: 52.28em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

汇编程序可用基址寄存器参加有效地址计算，也会通过条件跳转等指令使用标志／状态寄存器，因此Ⅲ、Ⅳ可见。IR由取指控制逻辑使用，微指令寄存器属于内部控制实现，程序不直接指定它们。可见不等于每个位都允许用户程序任意改写。

</details>

### 选择题3｜2022-18

<img src="../bank/2022/q18.png" alt="2022-18" style="display: block; width: 41.23em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

指令字格式和通用寄存器是软件可见的约定。时钟周期和加法器进位方式可以换实现。

</details>

### 选择题4｜2022-20

<img src="../bank/2022/q20.png" alt="2022-20" style="display: block; width: 39.44em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

预处理展开宏和头文件；编译把源代码转换为汇编；汇编生成可重定位目标文件；链接合并目标与库、解析符号并重定位，得到可执行文件。汇编必须在编译之后，链接必须取得目标文件后进行。

</details>

### 选择题5｜2024-13

<img src="../bank/2024/q13.png" alt="2024-13" style="display: block; width: 38.9em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

CPU 可译码机器指令，微程序控制器也可根据微指令产生内部控制信号。汇编文本和伪指令先由汇编器翻译。

</details>

### 选择题6｜2025-16

<img src="../bank/2025/q16.png" alt="2025-16" style="display: block; width: 38.0em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

指令长度和格式直接决定机器码怎样解码，属于ISA对软件的约定。阵列乘法器、微程序控制器、单总线数据通路是实现指令功能的内部方案；换这些方案可以保持原机器码语义不变，因此A、C、D不由ISA强制规定。

</details>

### 选择题7｜2025-17

<img src="../bank/2025/q17.png" alt="2025-17" style="display: block; width: 22.35em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

RISC通常采用较规整的指令、Load/Store访存和较多寄存器，适合流水实现，所以“难以采用流水线”错误。硬布线控制及用寄存器传参都是常见做法。这里说常见特征，不应扩张成所有RISC实现都必须采用相同流水级数。

</details>

### 选择题8｜2026-12

<img src="../bank/2026/q12.png" alt="2026-12" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

本题区分微架构的逻辑组织与更下层的物理实现。微架构规定流水线、运算部件、Cache及控制器怎样组织来实现ISA；电路、器件及布局布线才进一步完成物理实现，因此C把层次混在了一起。ISA是软硬件接口，操作系统利用其指令、特权和异常机制向上提供抽象服务，B、D成立；A给出上下层端点。

</details>

### 选择题9｜2026-16

<img src="../bank/2026/q16.png" alt="2026-16" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

超流水把执行过程细分为更多流水段，属于处理器内部实现，可改变而保持相同ISA。是否包含I/O指令、怎样进入中断处理入口、虚拟地址采用何种转换格式，都影响软件可见的机器接口，A、B、C属于ISA约定。

</details>

## 选择题组2｜0906 · 计算机网络

[控制转发路径：ARP、路由协议与下一跳](../src/0906.md) · 5道 · 首次。

### 选择题10｜2021-36

<img src="../bank/2021/q36.png" alt="2021-36" style="display: block; width: 46.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

每片扣20B首部后最多780B，但非末片数据必须是8B整数倍，所以实际最多776B。原数据1560B，分成776、776、8，共3片。第二片总长776+20=796B，后面还有第三片，MF=1。不是把第二片当作最后一片，也不能直接填满800B。

</details>

### 选择题11｜2021-37

<img src="../bank/2021/q37.png" alt="2021-37" style="display: block; width: 49.24em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

每个目的网络都计算“E到邻居距离＋邻居通告距离”再取最小。Net1最小8+1=9；Net2最小8+12=20；Net3最小为10+18或12+16，均28；Net4最小12+8=20。因此为9、20、28、20，不能只比较邻居通告值而漏掉到邻居这一段。

</details>

### 选择题12｜2025-37

<img src="../bank/2025/q37.png" alt="2025-37" style="display: block; width: 42.29em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

NAPT可能改源端口，源IP也变，UDP校验和涉及这些字段故需更新；目的端口与总长度不随普通地址端口转换改变。选I、IV。

</details>

### 选择题13｜2026-37

<img src="../bank/2026/q37.png" alt="2026-37" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

断链后到R2须经R3，走S2费用6+5=11，优于经R4、R3的3+4+5=12；到R3也仍走S2。于是199.10.20.0/27与.32/27可合成.0/26走S2；.64/26和.128/25合成.0/24走S3，并由更长前缀.0/26覆盖前64个地址。再保留服务器/32走S4及默认路由走S0，共4项。聚合时允许更具体路由纠正，不必只合并同出口且等长的相邻项。

</details>

### 选择题14｜2026-38

<img src="../bank/2026/q38.png" alt="2026-38" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

OSPF支持一个AS分成多个Area；RIP没有这种区域分层机制，BGP是外部网关协议，不符合题目“内部网关”。

</details>

## 解答题

### 大题1｜2023-42

[原题单 0918｜查找与排序：让分布、权重和内存边界决定代价](../src/0918.md)

<img src="../bank/2023/q42.png" alt="2023-42" style="display: block; width: 46.96em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

（1）工作区初值为51、94、37、92。输出37后补14，14被冻结；输出51后补63，63仍可用于本段。继续每次取本段最小值，得到三个升序段。

- 第一段：37、51、63、92、94、99
- 第二段：14、15、23、31、48、56、60、90、166
- 第三段：8、17、43、100

（2）第一段最长 n，输入本身升序即可。最短 m，降序时每次补入都小于刚输出的值，初始 m 条出完就封段。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
