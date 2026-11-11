# Day 18｜组成原理＋计算机网络

[← Day 17](day17.md) · [总入口](README.md) · [Day 19 →](day19.md)

**选择题：14道，来自两份完整src题单；大题：1道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：70—110分钟。** 选择题及核对约40—65分钟，大题约25—35分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0820 · 组成原理

[流水线：结果何时产生，下一条何时需要](../src/0820.md) · 3道 · 首次。

### 选择题1｜2020-17

<img src="../bank/2020/q17.png" alt="2020-17" style="display: block; width: 65.4em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B（I、III）。**

**直接法：** 单周期CPU每条指令占一个周期；基本流水线理想稳态下每周期完成一条指令，二者理想CPI为1。

**排除法／易混点：** 多周期CPU一条指令通常需多个周期；超标量每周期可完成多条，理想CPI可小于1。别把“CPI为1”与“时钟周期短”混为一谈。

</details>

### 选择题2｜2023-19

<img src="../bank/2023/q19.png" alt="2023-19" style="display: block; width: 46.88em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

**直接法：** I1 的 add 结果在执行段结束就能转给 I2；I2 的 load 值到访存段后才出现，紧随其后的 I3 必须等。I3 的分支结果也决定后续取指，控制阻塞波及 I4。

</details>

### 选择题3｜2024-19

<img src="../bank/2024/q19.png" alt="2024-19" style="display: block; width: 45.97em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

**直接法：** 旁路无法消除紧邻的 load-use 等待。插入气泡或足够 nop 可以推迟消费者，重排则要保持原依赖关系。

</details>

## 选择题组2｜0907 · 计算机网络

[端到端状态：TCP序号、窗口与拥塞](../src/0907.md) · 11道 · 复做第1次。

### 选择题4｜2020-38

<img src="../bank/2020/q38.png" alt="2020-38" style="display: block; width: 46.68em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题5｜2020-39

<img src="../bank/2020/q39.png" alt="2020-39" style="display: block; width: 46.72em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题6｜2021-38

<img src="../bank/2021/q38.png" alt="2021-38" style="display: block; width: 58.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题7｜2021-39

<img src="../bank/2021/q39.png" alt="2021-39" style="display: block; width: 46.72em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题8｜2021-40

<img src="../bank/2021/q40.png" alt="2021-40" style="display: block; width: 46.84em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题9｜2022-38

<img src="../bank/2022/q38.png" alt="2022-38" style="display: block; width: 45.88em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题10｜2022-39

<img src="../bank/2022/q39.png" alt="2022-39" style="display: block; width: 45.92em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题11｜2024-38

<img src="../bank/2024/q38.png" alt="2024-38" style="display: block; width: 46.0em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

**直接法：** 建连至可发数据耗时1RTT。按本题参考解采用的慢开始起始窗口1MSS，3个段分1+2两轮，耗时2RTT。主动关闭最短再花1RTT，随后等2MSL。合计60.04s。原题未明说初始拥塞窗口，若给定初始窗口至少3MSS，数据可一轮发完，结果会变为60.03s。

</details>

### 选择题12｜2024-39

<img src="../bank/2024/q39.png" alt="2024-39" style="display: block; width: 46.0em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题13｜2025-38

<img src="../bank/2025/q38.png" alt="2025-38" style="display: block; width: 42.29em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：A（待逐题复核）。** 解析待补。

</details>

### 选择题14｜2025-39

<img src="../bank/2025/q39.png" alt="2025-39" style="display: block; width: 42.42em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

**直接法：** UDP请求和应答只花1RTT即8ms。TCP建连1RTT，第三次握手附请求，收到回应再花1RTT，共16ms。

</details>

## 解答题

### 大题1｜2020-44

[原题单 0923｜Cache 局部性：地址映射、访问序列与缺失代价](../src/0923.md)

<img src="../bank/2020/q44.png" alt="2020-44" style="display: block; width: 50.2em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

（1）每个Cache的数据区32KiB，每块64B，共512行；8路得到64组。32位地址切为Tag20位、组号6位、块内偏移6位。每行用3位LRU序号区分组内8个位置；直写策略没有脏位（修改位），但仍需要有效位。

（2）S有1024个int，占4096B；起始008000C0H是64B整块边界，每块装16个int，共64块。每块第一次读取缺失，以后读取及对同一元素的写入均命中；按顺序访问且容量足够，缺失64次。直写表示命中写同时更新主存，不意味着每次写都是Cache缺失。

（3）00010003H：块内偏移3，组号0，Tag=00010H。访问指令Cache第0组，并行比较8路有效标记。初始Cache空，首次必缺失；从主存读入00010000H起的64B块到该组空行（若无空行才依LRU替换），置有效位、标记并更新LRU，然后按偏移3取指令内容。指令Cache和数据Cache分别管理，不混为一张表。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
