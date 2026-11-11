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

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题2｜2021-17

<img src="../bank/2021/q17.png" alt="2021-17" style="display: block; width: 52.28em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

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

**参考答案：A（待逐题复核）。** 解析待补。

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

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题7｜2025-17

<img src="../bank/2025/q17.png" alt="2025-17" style="display: block; width: 22.35em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题8｜2026-12

<img src="../bank/2026/q12.png" alt="2026-12" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案与解析待补。**

</details>

### 选择题9｜2026-16

<img src="../bank/2026/q16.png" alt="2026-16" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案与解析待补。**

</details>

## 选择题组2｜0906 · 计算机网络

[控制转发路径：ARP、路由协议与下一跳](../src/0906.md) · 5道 · 首次。

### 选择题10｜2021-36

<img src="../bank/2021/q36.png" alt="2021-36" style="display: block; width: 46.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题11｜2021-37

<img src="../bank/2021/q37.png" alt="2021-37" style="display: block; width: 49.24em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

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

**答案与解析待补。**

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
