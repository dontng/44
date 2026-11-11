# Day 24｜组成原理＋计算机网络

[← Day 23](day23.md) · [总入口](README.md) · [Day 25 →](day25.md)

**选择题：19道，来自两份完整src题单；大题：1道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：75—120分钟。** 选择题及核对约45—75分钟，大题约25—35分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0823 · 组成原理

[I/O路径：轮询、中断与DMA怎样交接控制权](../src/0823.md) · 14道 · 首次。

### 选择题1｜2020-20

<img src="../bank/2020/q20.png" alt="2020-20" style="display: block; width: 38.28em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

定时器到时和网络包到达由CPU外部设备提出请求，属于外部中断。访存缺页是在当前指令执行时由地址转换检测出的异常，属于内部同步异常，不因名字中常叫“缺页中断”就变成外中断。

</details>

### 选择题2｜2020-21

<img src="../bank/2020/q21.png" alt="2020-21" style="display: block; width: 52.36em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

可屏蔽请求有效后，还要满足开中断、未屏蔽及到达可响应时点，不能说立即响应，B错误。关中断通常只禁止可屏蔽中断，不禁止NMI；NMI优先级更高；屏蔽字能改变嵌套的处理优先关系，A、C、D成立。

</details>

### 选择题3｜2020-22

<img src="../bank/2020/q22.png" alt="2020-22" style="display: block; width: 46.68em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

周期挪用DMA每凑够32位就短暂占用总线传4B，传完释放，CPU仍可在其余时段访问主存；不是连续封锁整个512B传输期间，C错误。整块共128次这样的字传送，结束再产生完成中断；总线优先级让DMA及时接走设备数据。

</details>

### 选择题4｜2021-20

<img src="../bank/2021/q20.png" alt="2021-20" style="display: block; width: 46.72em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

磁盘驱动器是外部设备本身，不是连接主机与外设的I/O接口。打印机适配器、网络控制器和可编程中断控制器都属于接口／控制硬件。不要把“磁盘驱动器”误读为软件“磁盘驱动程序”，二者都不是本题所问的接口名称。

</details>

### 选择题5｜2021-21

<img src="../bank/2021/q21.png" alt="2021-21" style="display: block; width: 52.28em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

缺页时当前访存指令尚未完成，处理程序把所需页调入后，必须回到这条指令重做，才能完成原访问。系统调用返回通常继续下一条；DMA完成和打印机缺纸是外部事件，不要求把已执行完的当前指令重做。

</details>

### 选择题6｜2021-22

<img src="../bank/2021/q22.png" alt="2021-22" style="display: block; width: 39.16em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

多重中断允许内核中的中断服务程序在开中断后再被更高优先级请求打断，故“仅在用户态才能响应”错误。这里其余选项依教材可屏蔽中断模型讨论：有未屏蔽请求、允许中断并在可响应时点才进入响应周期。用户态／内核态是权限状态，开／关中断是响应许可，不能混为一个开关。

</details>

### 选择题7｜2022-21

<img src="../bank/2022/q21.png" alt="2022-21" style="display: block; width: 29.04em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

中断I/O适合相对较慢的字符设备：设备准备数据期间CPU可执行其他工作，准备好后由服务程序搬数据。为了不使CPU一直处理中断或来不及取走数据，设备相邻数据的准备间隔应足够长，而不是小于中断处理时间，C错误。高吞吐设备通常改用DMA。

</details>

### 选择题8｜2023-22

<img src="../bank/2023/q22.png" alt="2023-22" style="display: block; width: 34.88em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

DMA的数据搬运由控制器硬件在设备接口与主存之间完成，不是CPU反复执行所谓DMA传送程序，C错误。CPU仍负责设置地址、计数与方向，结束后处理中断；查询和中断方式则由CPU执行相应程序实际搬数据。

</details>

### 选择题9｜2024-21

<img src="../bank/2024/q21.png" alt="2024-21" style="display: block; width: 28.0em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

响应优先级由中断判优逻辑决定。屏蔽字可决定当前处理期间允许哪些中断嵌套，从而改变处理优先关系。断点和状态字由响应阶段保存，通用寄存器与新屏蔽字可由软件处理。

</details>

### 选择题10｜2024-22

<img src="../bank/2024/q22.png" alt="2024-22" style="display: block; width: 46.03em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

DMA建立的是设备接口到主存的直接数据通路，绕过CPU的数据寄存器，选C。DMA控制器负责地址、计数和总线控制，不意味着所有数据都必须先进入CPU，或把DMA控制器本身当作传输终点。

</details>

### 选择题11｜2025-21

<img src="../bank/2025/q21.png" alt="2025-21" style="display: block; width: 40.84em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

网卡和SSD数据量大、传输快，使用DMA成块搬到主存可减少CPU逐字搬运开销。键盘和针式打印机属于慢速字符设备，用中断方式即可，故选Ⅱ、Ⅲ。判断依据是数据流量与搬运开销，不是设备有没有控制器。

</details>

### 选择题12｜2025-22

<img src="../bank/2025/q22.png" alt="2025-22" style="display: block; width: 31.69em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

DMA整块传输结束，由控制器发完成中断通知CPU，属于外部中断。单次总线事务结束只完成一次总线交互，不必产生中断；缺页处理结束不再产生新的外部请求；断点指令由当前指令主动触发陷阱，是内部同步事件。

</details>

### 选择题13｜2026-21

<img src="../bank/2026/q21.png" alt="2026-21" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

系统调用指令允许用户程序主动陷入。直接控制设备、关中断和恢复中断前机器状态涉及特权，不能由普通用户程序任意执行。

</details>

### 选择题14｜2026-22

<img src="../bank/2026/q22.png" alt="2026-22" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

转入中断入口前必须保留被打断程序的PC，否则软件开始执行后已丢失返回位置，因此断点由硬件保存。开中断和保存通用寄存器可以由服务程序执行。中断判优虽常用硬件排队器，也能按规定优先次序用软件查询完成，B不满足“必须由硬件”。断点保存与通用寄存器现场保护不是同一件事。

</details>

## 选择题组2｜0906 · 计算机网络

[控制转发路径：ARP、路由协议与下一跳](../src/0906.md) · 5道 · 复做第1次。

### 选择题15｜2021-36

<img src="../bank/2021/q36.png" alt="2021-36" style="display: block; width: 46.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

每片扣20B首部后最多780B，但非末片数据必须是8B整数倍，所以实际最多776B。原数据1560B，分成776、776、8，共3片。第二片总长776+20=796B，后面还有第三片，MF=1。不是把第二片当作最后一片，也不能直接填满800B。

</details>

### 选择题16｜2021-37

<img src="../bank/2021/q37.png" alt="2021-37" style="display: block; width: 49.24em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

每个目的网络都计算“E到邻居距离＋邻居通告距离”再取最小。Net1最小8+1=9；Net2最小8+12=20；Net3最小为10+18或12+16，均28；Net4最小12+8=20。因此为9、20、28、20，不能只比较邻居通告值而漏掉到邻居这一段。

</details>

### 选择题17｜2025-37

<img src="../bank/2025/q37.png" alt="2025-37" style="display: block; width: 42.29em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

NAPT可能改源端口，源IP也变，UDP校验和涉及这些字段故需更新；目的端口与总长度不随普通地址端口转换改变。选I、IV。

</details>

### 选择题18｜2026-37

<img src="../bank/2026/q37.png" alt="2026-37" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

断链后到R2须经R3，走S2费用6+5=11，优于经R4、R3的3+4+5=12；到R3也仍走S2。于是199.10.20.0/27与.32/27可合成.0/26走S2；.64/26和.128/25合成.0/24走S3，并由更长前缀.0/26覆盖前64个地址。再保留服务器/32走S4及默认路由走S0，共4项。聚合时允许更具体路由纠正，不必只合并同出口且等长的相邻项。

</details>

### 选择题19｜2026-38

<img src="../bank/2026/q38.png" alt="2026-38" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

OSPF支持一个AS分成多个Area；RIP没有这种区域分层机制，BGP是外部网关协议，不符合题目“内部网关”。

</details>

## 解答题

### 大题1｜2022-46

[原题单 0925｜并发同步：PV 操作大题](../src/0925.md)

<img src="../bank/2022/q46.png" alt="2022-46" style="display: block; width: 47.8em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

设 aDone、cDone 初值均为0，分别表示 A 完成与 C 完成。

```text
T1: A; signal(aDone); wait(cDone); E; F
T2: B; wait(aDone); C; signal(cDone); D
```

T2 的 C 由程序顺序保证在 B 后，再由 wait(aDone) 保证在 A 后。T1 通过 wait(cDone) 在 C 后执行 E，其后才是 F。T2 内 D 写在 C 后。D 与 E 之间没有额外顺序要求。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
