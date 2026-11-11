# Day 12｜组成原理＋计算机网络

[← Day 11](day11.md) · [总入口](README.md) · [Day 13 →](day13.md)

**选择题：10道，来自两份完整src题单；大题：2道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：85—135分钟。** 选择题及核对约40—70分钟，大题约40—55分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0817 · 组成原理

[指令取数：格式、寻址与有效地址](../src/0817.md) · 4道 · 首次。

### 选择题1｜2020-16

<img src="../bank/2020/q16.png" alt="2020-16" style="display: block; width: 52.32em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：A（待逐题复核）。** 解析待补。

</details>

### 选择题2｜2022-19

<img src="../bank/2022/q19.png" alt="2022-19" style="display: block; width: 47.12em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题3｜2023-17

<img src="../bank/2023/q17.png" alt="2023-17" style="display: block; width: 46.81em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

由寻址方式决定寄存器保存的是数据还是地址；寄存器编号只定位哪个寄存器，内容本身不能说明应如何解释。

</details>

### 选择题4｜2026-17

<img src="../bank/2026/q17.png" alt="2026-17" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案与解析待补。**

</details>

## 选择题组2｜0903 · 计算机网络

[链路可靠性：帧、窗口与重传状态](../src/0903.md) · 6道 · 首次。

### 选择题5｜2020-36

<img src="../bank/2020/q36.png" alt="2020-36" style="display: block; width: 46.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题6｜2022-33

<img src="../bank/2022/q33.png" alt="2022-33" style="display: block; width: 38.46em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

相邻结点之间流量控制属数据链路层；传输层处理端到端流量控制。看清题目限定的通信对象。

</details>

### 选择题7｜2023-35

<img src="../bank/2023/q35.png" alt="2023-35" style="display: block; width: 46.92em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题8｜2023-37

<img src="../bank/2023/q37.png" alt="2023-37" style="display: block; width: 46.88em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

101111100对10011做模2除法余数为0000，其他候选余数非零，故按题意选D。严格说CRC通过只能说明未检出差错，不能逻辑保证传输绝无错误；可检出范围取决于生成多项式。

</details>

### 选择题9｜2024-37

<img src="../bank/2024/q37.png" alt="2024-37" style="display: block; width: 46.0em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题10｜2026-35

<img src="../bank/2026/q35.png" alt="2026-35" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案与解析待补。**

</details>

## 解答题

### 大题1｜2020-43

[原题单 0920｜指令落到数据通路：寄存器、部件与控制信号协同](../src/0920.md)

<img src="../bank/2020/q43.png" alt="2020-43" style="display: block; width: 48.0em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

（1）能。二进制乘法可分解为移位与累加；有符号数可先处理符号与绝对值，再恢复符号，所以没有乘法指令不代表不能计算乘法。

（2）控制逻辑根据乘数当前位决定本轮是否加被乘数，控制寄存器装入、移位、循环计数与结束时机，使ALU、移位器和寄存器按既定顺序协同。

（3）在本题通常比较条件下，软件用多条加法/移位指令实现最慢；由阵列乘法器实现乘法指令最快；复用ALU和移位器的硬件乘法在两者之间。这里比较的是给定实现的工作量，不宣称所有机器都具有相同绝对时延。

（4）n=32，x=2^31−1，y=2，数学积为2^32−2。有符号和无符号解释下，两操作数都为正，完整64位积同为`00000000 FFFFFFFEH`。umul的32位无符号结果为FFFFFFFEH，没有超出无符号范围；imul的32位保留码同为FFFFFFFEH，但将被解释成−2，不能表示数学积，发生有符号溢出。无符号乘法只保留低n位时，完整2n位积的高n位非零便溢出。

</details>

### 大题2｜2022-43

[原题单 0920｜指令落到数据通路：寄存器、部件与控制信号协同](../src/0920.md)

<img src="../bank/2022/q43.png" alt="2022-43" style="display: block; width: 45.96em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

（1）SF=F₁₅。设 a、b、f 分别为 A₁₅、B₁₅、F₁₅。加法的 OF=(¬a∧¬b∧f)∨(a∧b∧¬f)，同号相加变号。减法的 OF=(¬a∧b∧f)∨(a∧¬b∧¬f)，异号相减且结果与被减数异号。

（2）内部总线一个时刻只允许一个部件驱动。先把第一个操作数送到Y，再用总线送第二个操作数到B。ALU结果先存Z，之后由Z占用总线送回目的寄存器，避免与第二操作数争用总线。

（3）rs 和 rd 都是4位，可编号16个通用寄存器。两字段来自IR。rd用于把写使能送给选中的寄存器，接地址译码器；rs 用于从多个寄存器中选择一个读出，接多路选择器。

（4）PCout、MARin 同拍，接下来 Read，主存经系统总线把字送到MDR。最后 MDRout、IRin 同拍。依题给出的读命令至MDR共5拍，取指至少 1+5+1=7 拍。

（5）控制信号由控制器CU产生。IR给出指令信息，FR给出ALU标志，后者供条件执行或控制时序使用。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
