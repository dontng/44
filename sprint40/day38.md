# Day 38｜组成原理＋计算机网络

[← Day 37](day37.md) · [总入口](README.md) · [Day 39 →](day39.md)

**选择题：16道，来自两份完整src题单；大题：1道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：60—95分钟。** 选择题及核对约30—50分钟，大题约25—35分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0818 · 组成原理

[程序层级：从源程序到CPU真正执行的对象](../src/0818.md) · 9道 · 复做第1次。

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

## 选择题组2｜0902 · 计算机网络

[信号与速率：带宽怎样限制可传数据](../src/0902.md) · 7道 · 复做第2次。

### 选择题10｜2020-34

<img src="../bank/2020/q34.png" alt="2020-34" style="display: block; width: 27.16em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

- **核心判据**：
  **虚电路网络（Virtual Circuit Network）在体系归属上属于分组交换（Packet Switching），绝非电路交换（Circuit Switching）**。
  - 电路交换才强制要求在通信前预先分配并端到端独占固定物理带宽；
  - 虚电路网络仅在逻辑上建立一条由虚电路号（VCID）串联的虚连接，沿途物理链路依然由所有经过的连接**采用统计时分复用（STDM）动态共享**，不强制预分配固定带宽（虽然支持可选的 QoS 带宽预留，但绝非每条虚电路都“需要预分配”）。

- **正选推导**：
  B 项断言“需要为每条虚电路预分配带宽”，混淆了虚电路技术与传统电路交换的物理本质。分组交换的灵活性恰恰在于动态统计复用，故 B 项叙述错误，正选。

- **干扰项击穿**：
  - **A 项正确**：虚电路在连接建立阶段锁定了唯一的转发路径，同一虚电路的所有数据分组严格沿相同路径按序流动，通常能可靠保证数据分组的到达顺序。
  - **C 项正确**：建立虚电路时发送呼叫请求分组，各中间节点必须根据路由表进行路由选择，以选定后续整条虚电路的物理转发拓扑。
  - **D 项正确**：数据传输阶段，分组首部无需携带全网全局 IP 地址，仅携带本地有效的虚电路号（VCID），交换机根据 VCID 查表进行标签交换并转发。

</details>

### 选择题11｜2021-34

<img src="../bank/2021/q34.png" alt="2021-34" style="display: block; width: 41.0em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

- **核心判据**：
  **差分曼彻斯特编码（Differential Manchester Encoding）判定物理法则**：
  1. **码元中心必有电平跳变**：该跳变仅充当接收端的自同步时钟信号，不代表数据比特本身；
  2. **码元起始边界决定数据值**：
     - **码元起始边界有电平跳变 $\iff$ 编码为 `0`**；
     - **码元起始边界无电平跳变（电平连续平滑） $\iff$ 编码为 `1`**。

- **正选推导**：
  按虚线划分的 8 个码元周期逐位检验边界状态（初始前导电平为高）：
  - **第 1 位**：起始边界无跳变（直接保持前导高电平进入） $\implies \mathbf{1}$。
  - **第 2 位**：起始边界发生低电平突变跳变 $\implies \mathbf{0}$。
  - **第 3 位**：起始边界无跳变（电平平滑延续） $\implies \mathbf{1}$。
  - **第 4 位**：起始边界无跳变（电平平滑延续） $\implies \mathbf{1}$。
  - 前 4 位确定为 `1011`（直接排除 B、C 选项）。
  - **第 5 位**：起始边界无跳变 $\implies \mathbf{1}$。
  - **第 6 位**：起始边界有跳变 $\implies \mathbf{0}$。
  - **第 7 位**：起始边界有跳变 $\implies \mathbf{0}$。
  - **第 8 位**：起始边界无跳变 $\implies \mathbf{1}$。
  后 4 位确定为 `1001`。完整二进制串为 `1011 1001`，选 A。

- **干扰项击穿**：
  - **C 选项（0010 1110）**：将“有跳变”与“无跳变”的定义完全颠倒。
  - **D 选项（1011 0110）**：在第 6、7 位判定跳变时发生眼花误判。

</details>

### 选择题12｜2022-34

<img src="../bank/2022/q34.png" alt="2022-34" style="display: block; width: 59.7em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

- **核心判据**：
  无噪声理想信道传输极限遵循**奈奎斯特准则（Nyquist Formula）**：
  $$\text{最大码元传输速率 } B = 2W \quad (\text{Baud})$$
  $$\text{最大数据传输速率 } C = 2W \log_2 M \quad (\text{b/s})$$
  其中 $W$ 为信道带宽，$M$ 为调制电平数（每个码元可表示的不同状态数）。

- **正选推导**：
  1. 信道带宽 $W = 200\text{ kHz}$。
  2. 采用 4 个幅值的 ASK 调制，则离散电平数 $M = 4$。
  3. 每个码元所承载的二进制信息量为：
     $$\log_2 M = \log_2 4 = 2\text{ bit/码元}$$
  4. 计算信道最大数据传输速率：
     $$C = 2 \times 200\text{ kHz} \times \log_2 4 = 400\text{ kBaud} \times 2\text{ bit/Baud} = \mathbf{800\text{ kbps}}$$
     选 C。

- **干扰项击穿**：
  - **A（200 kbps）**：遗漏了奈氏准则中乘以 2 的物理倍率，且漏乘了每码元 2 bit。
  - **B（400 kbps）**：误将“最大波特率/码元速率（400 kBaud）”当成了数据比特率（漏乘 $\log_2 4$）。
  - **D（1600 kbps）**：粗暴地直接将波特率 400 乘以幅值数 4（误将 $\log_2 M$ 当成 $M$）。

</details>

### 选择题13｜2023-34

<img src="../bank/2023/q34.png" alt="2023-34" style="display: block; width: 46.88em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

- **核心判据**：
  无噪声信道奈奎斯特极限逆推状态数：
  $$C = 2W \log_2 M \implies \log_2 M = \frac{C}{2W}$$
  QAM-$M$ 中的数值 $M = 2^k$ 代表调制星座图中的离散相位-幅度合成状态总数。

- **正选推导**：
  1. 信道带宽 $W = 4\text{ MHz}$，最大数据传输速率 $C = 48\text{ Mbps}$。
  2. 奈奎斯特极限码元速率：
     $$B = 2W = 2 \times 4\text{ MHz} = 8\text{ MBaud}$$
  3. 计算每个码元所携带的信息量（比特数）：
     $$\log_2 M = \frac{C}{B} = \frac{48\text{ Mbps}}{8\text{ MBaud}} = 6\text{ bit/码元}$$
  4. 计算调制状态总数 $M$：
     $$M = 2^6 = \mathbf{64}$$
     故采用的 QAM 调制方案为 **QAM-64**。选 C。

- **干扰项击穿**：
  - **A（QAM-16）**：若为 QAM-16，每个码元仅承载 4 bit，最大数据率仅为 $8 \times 4 = 32\text{ Mbps}$。
  - **B（QAM-32）**：每个码元承载 5 bit，数据率为 40 Mbps。
  - **D（QAM-128）**：每个码元承载 7 bit，数据率高达 56 Mbps，超出题设限制。

</details>

### 选择题14｜2024-34

<img src="../bank/2024/q34.png" alt="2024-34" style="display: block; width: 38.17em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

- **核心判据**：
  数字正弦载波调制三要素的物理机制：
  - **ASK（振幅键控）**：使用单一频率载波，通过改变载波的**振幅大小**表示 0 和 1（需要 1 个频率载波）；
  - **FSK（频移键控，Frequency Shift Keying）**：通过改变载波的**频率**表示二进制数据，以频率 $f_1$ 表示 0，频率 $f_2$ 表示 1（**需要 2 个不同频率载波**）；
  - **PSK（相移键控）**：使用单一频率载波，通过改变载波的**绝对初始相位**（如 0 与 $\pi$）表示 0 和 1；
  - **DPSK（差分相移键控）**：使用单一频率载波，通过前后相邻码元的**相对相位差**表示 0 和 1。

- **正选推导**：
  定义中明确需要 2 个不同频率载波的调制方法正是 FSK，选 C。

</details>

### 选择题15｜2025-34

<img src="../bank/2025/q34.png" alt="2025-34" style="display: block; width: 42.35em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

- **核心判据**：
  编码集的检错与纠错能力完全由**最小汉明距离 $d_{\min}$** 决定：
  1. **100% 检错能力**：若要检出不超过 $e$ 位的错误，要求合法码字之间的最小距离满足 $d_{\min} \ge e + 1 \implies \mathbf{e = d_{\min} - 1}$；
  2. **100% 纠错能力**：若要纠正不超过 $t$ 位的错误，要求以各合法码字为中心、半径为 $t$ 的汉明球互不相交，满足 $d_{\min} \ge 2t + 1 \implies \mathbf{t = \lfloor (d_{\min} - 1) / 2 \rfloor}$。

- **正选推导**：
  1. 计算码集 $\{C_1, C_2, C_3, C_4\}$ 中两两之间的汉明距离（异或结果中 1 的个数）：
     - $C_1 = 1001\ 1010, \quad C_2 = 0101\ 1100, \quad C_3 = 1111\ 0000, \quad C_4 = 0000\ 1111$
     - $d(C_1, C_2) = \text{weight}(1100\ 0110) = 4$
     - $d(C_1, C_3) = \text{weight}(0110\ 1010) = 4$
     - $d(C_1, C_4) = \text{weight}(1001\ 0101) = 4$
     - $d(C_2, C_3) = \text{weight}(1010\ 1100) = 4$
     - $d(C_2, C_4) = \text{weight}(0101\ 0011) = 4$
     - $d(C_3, C_4) = \text{weight}(1111\ 1111) = 8$
  2. 提取最小汉明距离：
     $$d_{\min} = 4$$
  3. 计算能力指标：
     - 检错能力：$e = d_{\min} - 1 = 4 - 1 = \mathbf{3}$ 位；
     - 纠错能力：$t = \lfloor (4 - 1) / 2 \rfloor = \mathbf{1}$ 位。
     - 选 C。

- **干扰项击穿**：
  - **A、B（检错不超过 2 位）**：低估了码集的检错能力（误以为 $d_{\min}=3$）。
  - **D（纠错不超过 2 位）**：若发生 2 位错误，接收码字到两个不同合法码字的距离可能同为 2（因为 $2+2=4$），处于重叠决策分界线上，译码器无法唯一判定原码字，故无法保证纠正 2 位错误。

</details>

### 选择题16｜2026-34

<img src="../bank/2026/q34.png" alt="2026-34" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

- **核心判据**：
  1. **有噪声信道极限数据率（香农定理 Shannon Formula）**：
     $$C = W \log_2 (1 + S/N)$$
     （注意：题干给出的 $S/N = 1023$ 是无量纲的真实比值，绝不能当作分贝数 dB 计算）。
  2. **传输时延（发送时延）**：
     $$t_{\text{trans}} = \frac{\text{分组大小（bit）}}{\text{信道传输速率（bps）}}$$

- **正选推导**：
  1. **计算极限传输速率 $C$**：
     - 带宽 $W = 200\text{ kHz}$。
     - $1 + S/N = 1 + 1023 = 1024 = 2^{10}$。
     - 香农极限容量：
       $$C = 200\text{ kHz} \times \log_2 (1024) = 200\text{ kHz} \times 10 = 2000\text{ kbps} = 2 \times 10^6\text{ bps}$$
  2. **计算分组传输时延**：
     - 分组大小为 $1500\text{ B} = 1500 \times 8\text{ bit} = 12000\text{ bit}$。
     - 传输时延：
       $$t = \frac{12000\text{ bit}}{2 \times 10^6\text{ bps}} = 0.006\text{ s} = \mathbf{6\text{ ms}}$$
     - 选 D。

- **干扰项击穿**：
  - **B（0.75 ms）**：粗心算漏，直接拿 1500 除以 $2 \times 10^6$，忘记将字节乘以 8 转换为比特（$0.00075\text{ s} = 0.75\text{ ms}$）。
  - **A（0.375 ms）**：未乘 8 且误用了奈氏准则乘 2。
  - **C（3 ms）**：计算香农公式时将对数值 $\log_2(1024)=10$ 误算为 20。

</details>

## 解答题

### 大题1｜2020-47

[原题单 1002｜网络服务：配置、地址转换与应用会话](../src/1002.md)

<img src="../bank/2020/q47.png" alt="2020-47" style="display: block; width: 48.75em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

（1）在R2配置静态端口映射：公网`203.10.2.2:80`对应内网Web服务器`192.168.1.2:80`，让H2、H3访问`http://203.10.2.2/`。还须有正确的默认网关与出网路由：右侧主机通过R3，R3默认下一跳203.10.2.5；R2默认下一跳203.10.2.1。图中已标出R2、R3提供NAT，右侧主动连接还须有出站转换项。

（2）只跟踪题目要求的IP字段：

| 位置 | 源IP | 目的IP |
|---|---|---|
| H2发出 | 192.168.1.2 | 203.10.2.2 |
| 经R3转发 | 203.10.2.6 | 203.10.2.2 |
| 经R2转发 | 203.10.2.6 | 192.168.1.2 |

R3做源地址转换，R2按静态映射做目的地址转换。R3的外侧临时端口只需与其NAT表一致，原题未给定，不能编造固定数值。若H2直接把目的IP写成192.168.1.2，它指向右侧本地地址，无法表示左侧服务器。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
