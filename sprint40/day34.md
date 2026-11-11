# Day 34｜组成原理＋计算机网络

[← Day 33](day33.md) · [总入口](README.md) · [Day 35 →](day35.md)

**选择题：16道，来自两份完整src题单；大题：1道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：70—110分钟。** 选择题及核对约40—65分钟，大题约25—35分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0816 · 组成原理

[地址翻译链：虚拟地址怎样到达数据](../src/0816.md) · 5道 · 复做第1次。

### 选择题1｜2020-15

<img src="../bank/2020/q15.png" alt="2020-15" style="display: block; width: 37.58em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

- **核心判据**：
  TLB（Translation Lookaside Buffer，快表）与 Cache 均是为弥合 CPU 极高主频与主存慢速访问之间的延迟代差而设立的**高速硬件缓冲部件**。DRAM（动态随机存取存储器）依靠电容存储电荷，必须周期性动态刷新，读写延迟高达数十纳秒，根本无法满足 CPU 核心流水线内单周期或数周期的访问需求。因此，TLB 与 Cache 在物理介质上均由**静态存储器（SRAM）**或相联存储电路（CAM）组成，绝不可能由 DRAM 构成。

- **正选推导**：
  D 项断言两者“都由 DRAM 存储器组成”彻底颠倒了存储层次的硬件物理介质：
  - TLB 位于 CPU 内部 MMU 中，采用按内容寻址的高速相联检索电路/SRAM；
  - Cache 位于 CPU 片内或紧密总线上，采用高速 SRAM；
  - 只有下层的主存才主要采用高密度的 DRAM 芯片。
  故 D 项叙述错误，正选。

- **干扰项击穿**：
  - **A 项正确**：TLB 缓存虚拟页号到物理页框号的映射，利用了空间局部性（连续访问同一页面内的指令或数据）和时间局部性（循环执行相同代码段）；Cache 缓存主存物理块，同样依赖程序局部性原理以提升命中率。
  - **B 项正确**：TLB 缺失意味着快表中无该页映射项，必须访问存放在主存中的页表（慢表）；Cache 缺失意味着数据不在缓存中，必须向主存发起总线事务调入数据块。
  - **C 项正确**：Cache 缺失处理全程由专用的硬件 Cache 控制器完成，对软件透明；TLB 缺失在绝大多数现代主流处理器架构（如 x86 的硬件 Page Miss Handler / MMU Page Walk）也是由纯硬件自动遍历多级页表，在少数精简架构（如早期 MIPS）则支持由操作系统内核的中断/异常处理程序软遍历，因此“都可以由硬件实现”表述严谨正确。

</details>

### 选择题2｜2022-15

<img src="../bank/2022/q15.png" alt="2022-15" style="display: block; width: 45.85em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

4KiB页使页内偏移为低12位。00082840H分成虚页号82H=130和偏移840H；虚页130存在位为1、页框018H，拼接得018840H。表中的82是十进制虚页号，不是本次的82H，不能误查其存在位0。

</details>

### 选择题3｜2024-17

<img src="../bank/2024/q17.png" alt="2024-17" style="display: block; width: 46.0em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

页大小1KiB，偏移10位，虚页号32−10=22位。TLB为32项、4路，共8组，组号占3位，Tag至少22−3=19位。TLB按虚页号查找，不能拿30位物理地址减字段；页内偏移也不存进Tag。

</details>

### 选择题4｜2024-18

<img src="../bank/2024/q18.png" alt="2024-18" style="display: block; width: 39.77em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

MMU检测翻译和保护相关的TLB缺失、页面缺失、越权；Cache缺失由Cache访问与标记比较检测，不是MMU翻译的职责。

</details>

### 选择题5｜2026-19

<img src="../bank/2026/q19.png" alt="2026-19" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

16项、4路即4组，虚页22=16H的组号为2，Tag=22÷4的整数商=05H。主存页表P=0意味着该页不在内存，同步后不能有Tag05H且V=1的有效TLB映射，故A不可能。B的Tag06H对应另一虚页；C、D的V=0，失效项中的旧Tag与PPN无需代表当前映射。

</details>

## 选择题组2｜0907 · 计算机网络

[端到端状态：TCP序号、窗口与拥塞](../src/0907.md) · 11道 · 复做第2次。

### 选择题6｜2020-38

<img src="../bank/2020/q38.png" alt="2020-38" style="display: block; width: 46.68em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>



**答案：D。**

* **核心判据**：TCP 拥塞控制状态机转换规则：
  * **慢开始阶段**：`cwnd` 呈指数级翻倍增长（每个 RTT 翻倍）；
  * **拥塞避免阶段**：`cwnd` 呈加法线性增长（每个 RTT 仅增加 1 MSS）；
  * **“最长时间”的边界判定**：若要求增长耗时最长，则意味着连接从 `8KB` 起始点就**直接处于加法增大的拥塞避免阶段**（例如此前发生拥塞，门限刚好被降至 8KB）。
* **正选推导**：
  * 处于拥塞避免阶段时，每个 RTT（2ms）窗口仅增加 1 MSS（1KB）；
  * 从 8KB 线性增加至 32KB，需要的窗口增量为 $\Delta = 32 - 8 = 24\text{ KB}$；
  * 所需的 RTT 轮数 $= \frac{24\text{ KB}}{1\text{ KB}} = 24\text{ 轮}$；
  * 总耗时最长为 $24 \times 2\text{ms} = \mathbf{48\text{ms}}$，选 D。
* **干扰项击穿**：
  * 若处于慢开始指数增长：$8 \to 16 \to 32$，只需 2 个 RTT（4ms），这是可能的最短时间，题干明确设问“最长时间”。



</details>

### 选择题7｜2020-39

<img src="../bank/2020/q39.png" alt="2020-39" style="display: block; width: 46.72em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>



**答案：C。**

* **核心判据**：TCP 序号消耗与应用层载荷映射机制：
  * **SYN 报文段不携带任何应用层数据，但物理上消耗 1 个序号**（`seq = 1000`），因此首个应用层数据字节的序号严格从 `1001` 开始；
  * **FIN 报文段不携带应用层数据，但同样消耗 1 个序号**（本报文段使用 `seq = 5001`），说明在发出 FIN 之前，已发送的最后一个应用层数据字节序号恰好为 $5001 - 1 = 5000$。
* **正选推导**：
  * 本连接发送的应用层数据字节序号闭区间为 $[1001, 5000]$；
  * 传送的应用层数据总字节数 $= 5000 - 1001 + 1 = 5001 - 1001 = \mathbf{4000\text{ 字节}}$，选 C。
* **干扰项击穿**：
  * 若直接用 $5001 - 1000 = 4001$，漏掉了 SYN 自身占用的 1 个序号；
  * 若算成 $5001 - 1000 - 2 = 3999$，混淆了端点闭开区间的数学定义。



</details>

### 选择题8｜2021-38

<img src="../bank/2021/q38.png" alt="2021-38" style="display: block; width: 58.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>



**答案：B。**

* **核心判据**：TCP 四次挥手有限状态机（FSM）路径：
  * **主动关闭方**：`ESTABLISHED` $\to$ 发送 FIN 进入 `FIN_WAIT_1` $\to$ 收到对端 ACK 进入 `FIN_WAIT_2` $\to$ 收到对端 FIN 并回复最后 ACK 后进入 **`TIME_WAIT`**，强制等待 $2\text{MSL}$ 后进入 `CLOSED`。
* **正选推导**：
  * 题设“客户端主动关闭连接，在收到服务器发送的 FIN 报文段并发出最终的 ACK 报文段后”，根据状态机转移，客户端立即进入 **`TIME_WAIT`** 状态，选 B。
* **干扰项击穿**：
  * **CLOSE_WAIT**：是**被动关闭方**在收到对方 FIN 报文段后进入的状态；
  * **LAST_ACK**：是被动关闭方发送自己的 FIN 报文段后等待对方最后确认的状态。



</details>

### 选择题9｜2021-39

<img src="../bank/2021/q39.png" alt="2021-39" style="display: block; width: 46.72em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>



**答案：D。**

* **核心判据**：传输层传输效率定义公式为 $\text{Efficiency} = \frac{\text{应用层载荷大小}}{\text{传输层总报文长度}}$。
  * **UDP 首部固定为最小 8 字节**；
  * **TCP 首部在无任何可选字段时最小为 20 字节**。
* **正选推导**：
  * 应用层数据载荷 $= 12\text{ 字节}$；
  * UDP 最大传输效率：
    $$\text{Eff}_{\text{UDP}} = \frac{12}{12 + 8} = \frac{12}{20} = \mathbf{60\%}$$
  * TCP 最大传输效率：
    $$\text{Eff}_{\text{TCP}} = \frac{12}{12 + 20} = \frac{12}{32} = \mathbf{37.5\%}$$
  * 故选 D。
* **干扰项击穿**：
  * 题目明确要求只计算 UDP 和 TCP 本身的传输效率，切勿把下层的 IP 首部（20B）或以太网帧头帧尾（18B）算入。



</details>

### 选择题10｜2021-40

<img src="../bank/2021/q40.png" alt="2021-40" style="display: block; width: 46.84em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>



**答案：C。**

* **核心判据**：TCP 滑动窗口边界不变量：接收方通过 `ack` 和 `rwnd` 划定允许发送的合法序号闭区间为 $[\text{ack}, \text{ack} + \text{rwnd} - 1]$。已发送的字节不能重复发送，只能从未发送的起始序号开始新发。
* **正选推导**：
  1. 乙回复甲的报文中：$\text{ack} = 501, \text{rwnd} = 500$；
  2. 此时乙允许甲发送的有效字节序号区间为 $[501, 501 + 500 - 1] = [501, 1000]$；
  3. 题干指出甲已连续发送了 $[501, 700]$ 共 200 字节数据；
  4. 扣除已发送的数据后，甲在窗口内**还能新发送的数据序号范围**严格为 **`701 ~ 1000`**，选 C。
* **干扰项击穿**：
  * 乙报文自身携带的 `seq = 601` 属于乙向甲反向传输数据流的序列号，与甲的发送窗口没有任何关系，切勿被该字段误导。



</details>

### 选择题11｜2022-38

<img src="../bank/2022/q38.png" alt="2022-38" style="display: block; width: 45.88em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>



**答案：C。**

* **核心判据**：TCP 超时重传（Timeout）惩罚机制：
  1. 发生超时时，门限值更新为当前拥塞窗口的一半：$\text{ssthresh} = \max(\text{cwnd} / 2, 2\text{MSS}) = 16\text{KB} / 2 = 8\text{KB}$；
  2. 拥塞窗口被**硬性重置归零为 1 MSS（1KB）**；
  3. 从 1KB 重启慢开始阶段（指数增长）；达到门限 8KB 后立即切换为拥塞避免阶段（线性加法增长）。
* **正选推导**：
  * **慢开始阶段（1KB $\to$ 8KB）**：
    * 经过第 1 个 RTT：$1\text{KB} \to 2\text{KB}$；
    * 经过第 2 个 RTT：$2\text{KB} \to 4\text{KB}$；
    * 经过第 3 个 RTT：$4\text{KB} \to 8\text{KB}$（达到门限 $\text{ssthresh} = 8\text{KB}$，耗时 3 RTT）；
  * **拥塞避免阶段（8KB $\to$ 16KB）**：
    * 此后每个 RTT 窗口仅线性增加 1KB；
    * 从 8KB 增至 16KB 还需要增加 $16 - 8 = 8\text{KB}$，耗时 8 RTT；
  * **总耗时累加**：$3\text{ RTT} + 8\text{ RTT} = \mathbf{11\text{ RTT}}$，选 C。
* **干扰项击穿**：
  * 切勿误以为超时后 `cwnd` 从 8KB 起步；也切勿在越过 8KB 门限后继续翻倍（若继续翻倍会算成 4 RTT 错解）。



</details>

### 选择题12｜2022-39

<img src="../bank/2022/q39.png" alt="2022-39" style="display: block; width: 45.92em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>



**答案：D。**

* **核心判据**：主动关闭方彻底关闭的时延流转模型：**发起 FIN $\to$ 单程传播 $\to$ 服务端合并回送 FIN/ACK $\to$ 单程传播 $\to$ 客户端发送最后 ACK 并进入 TIME_WAIT $\to$ 等待完整的 $2\text{MSL}$ 物理计时 $\to$ CLOSED 彻底关闭**。
* **正选推导**：
  1. $t = 0\text{ms}$：客户端甲发出第 1 次挥手 FIN 报文段；
  2. $t = 25\text{ms}$：服务端乙收到 FIN，因无数据发送，立即合并发送第 2 次 ACK 与第 3 次 FIN；
  3. $t = 50\text{ms}$：客户端甲收到乙的 FIN，立即回复第 4 次挥手 ACK，并在此时**正式进入 TIME_WAIT 状态**；
  4. 客户端必须强制等待 $2\text{MSL} = 2 \times 800\text{ms} = 1600\text{ms}$；
  5. 客户端甲彻底关闭的时间点 $= 50\text{ms} + 1600\text{ms} = \mathbf{1650\text{ms}}$，选 D。
* **干扰项击穿**：
  * 服务端（被动关闭方）在 $t = 50 + 25 = 75\text{ms}$ 收到甲最后的 ACK 后即可立即彻底关闭；但题干明确设问的是**客户端甲**的彻底关闭时间。



</details>

### 选择题13｜2024-38

<img src="../bank/2024/q38.png" alt="2024-38" style="display: block; width: 46.0em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>



**答案：D。**

* **核心判据**：完整 TCP 交互会话生命周期模型：**建连时延（三次握手 1 RTT） + 数据传输时延（慢开始阶段） + 挥手时延（1 RTT） + TIME_WAIT 强制等待时间（$2\text{MSL}$）**。
* **正选推导**：
  1. **连接建立**：三次握手完成，客户端收到 SYN+ACK 并可发数据，耗时 **1 RTT**；
  2. **数据传输（共 3 个段）**：
     * 慢开始初始 `cwnd = 1 MSS`，第 1 轮发 1 个段，耗时 1 RTT；
     * 收到确认后 `cwnd` 增至 2 MSS，第 2 轮并发发送剩余 2 个段，耗时 1 RTT；
     * 数据传输总计耗时 **2 RTT**；
  3. **连接释放**：客户端发 FIN，收到服务端的 ACK+FIN，客户端回复最后 ACK，耗时 **1 RTT**；
  4. **TIME_WAIT 状态**：强制等待 $2\text{MSL} = 2 \times 30\text{s} = 60\text{s}$；
  5. **总时间求和**：
     $$\text{总时间} = (1 + 2 + 1) \times \text{RTT} + 2\text{MSL} = 4 \times 0.01\text{s} + 60\text{s} = \mathbf{60.04\text{s}}$$
  * 故选 D。



</details>

### 选择题14｜2024-39

<img src="../bank/2024/q39.png" alt="2024-39" style="display: block; width: 46.0em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>



**答案：C。**

* **核心判据**：网络校验和（Internet Checksum）二进制反码求和（1's Complement Sum）三步法则：
  1. 将所有 16 位整型数据按普通二进制加法累加；
  2. **循环进位（End-around Carry）**：若相加产生最高位进位（溢出到第 17 位），必须将该进位回卷加到最低位；
  3. **逐位取反**：对回卷后的结果按位取反得到最终校验和。
* **正选推导**：
  1. 两个 16 位数二进制累加：
     $$\text{B9B6H} + \text{65C5H} = \text{11F7BH}$$
  2. 最高位产生进位 1，将其回卷加至最低位：
     $$\text{1F7BH} + 1 = \text{1F7CH}$$
  3. 对 `1F7CH`（`0001 1111 0111 1100`）按位取反：
     $$\sim(\text{0001 1111 0111 1100}_2) = \text{1110 0000 1000 0011}_2 = \mathbf{\text{E083H}}$$
  * 故选 C。
* **干扰项击穿**：
  * **A 项**：未做进位回卷且未取反；
  * **B 项**：仅算出累加值未做反码取反；
  * **D 项**：取反前漏掉了进位回卷。



</details>

### 选择题15｜2025-38

<img src="../bank/2025/q38.png" alt="2025-38" style="display: block; width: 42.29em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>



**答案：A。**

* **核心判据**：TCP 发送方可用窗口物理不变量：
  $$\text{还可新发数据量} = \min(\text{cwnd}, \text{rwnd}) - \text{已发送但未被确认的在途字节数}$$
* **正选推导**：
  1. 甲收到乙发来的 `ack = 3001`：确认了此前发送的第一个 1000B 数据段（序号 2001~3000）；
  2. 第二个 1000B 数据段（序号 3001~4000）仍未确认，当前**在途未确认数据量为 1000 字节**；
  3. 拥塞窗口更新：当前 $\text{cwnd} = 2000\text{B} < \text{ssthresh} = 8000\text{B}$，处于慢开始阶段。收到一个有效 ACK 增加 1 个 MSS（1000B），故更新后 $\text{cwnd} = 2000 + 1000 = 3000\text{B}$；
  4. 当前有效发送窗口为：$W = \min(\text{cwnd}, \text{rwnd}) = \min(3000, 4000) = 3000\text{B}$；
  5. 扣除在途数据后，甲当前还可发送的字节数：
     $$\text{剩余可用容量} = 3000\text{B} - 1000\text{B} = \mathbf{2000\text{ 字节}}$$
  * 即还可以新发 2 个 1000B 的报文段，选 A。
* **干扰项击穿**：
  * 易混点：看到当前窗口扩大为 3000B 就盲目认为还能新发 3000B，完全漏掉了已经在网络中飞行（在途）的 1000B 未确认数据。



</details>

### 选择题16｜2025-39

<img src="../bank/2025/q39.png" alt="2025-39" style="display: block; width: 42.42em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>



**答案：B。**

* **核心判据**：传输层连接开销对应用层请求时延的直接影响：
  * **UDP（无连接）**：客户端直接发查询报文，服务端直接回送应答报文，全程耗时仅为 **1 个 RTT**；
  * **TCP（面向连接）**：必须先执行三次握手建立连接（耗时 1 RTT），在第三次握手的 ACK 报文中捎带 DNS 查询请求，服务端回复响应耗时再加 1 RTT，总共耗时 **2 个 RTT**。
* **正选推导**：
  * 题设单向传播及传输时延总计 $1\text{ RTT} = 8\text{ms}$；
  * UDP 总耗时 $= 1 \times 8\text{ms} = 8\text{ms}$；
  * TCP 总耗时 $= 2 \times 8\text{ms} = 16\text{ms}$；
  * 故选 B。



</details>

## 解答题

### 大题1｜2025-46

[原题单 0928｜进程生命线：调度、输入与用户—内核边界](../src/0928.md)

<img src="../bank/2025/q46.png" alt="2025-46" style="display: block; width: 43.8em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

（1）PCB在内核区，由操作系统管理。scanf 等待键盘输入期间进程阻塞。

（2）main代码在只读代码区。题设以终端为I/O设备，scanf 读取键盘、printf 向终端输出，其底层需要系统调用和相应驱动。strlen 在用户态读字符串；malloc/free 管理进程堆，扩展堆等可能请求内核，无须依赖键盘或终端驱动。

（3）全局指针 ptr 在可读写数据区。length 未放寄存器时通常在用户栈。ptr 指向 malloc 分配的对象，位于运行时堆。题图中的分配大小只够一个 char，真实程序读普通非空字符串时还要预留结尾的空字符；这一点不改变各对象所在区。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
