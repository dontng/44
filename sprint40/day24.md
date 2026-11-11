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

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题2｜2020-21

<img src="../bank/2020/q21.png" alt="2020-21" style="display: block; width: 52.36em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题3｜2020-22

<img src="../bank/2020/q22.png" alt="2020-22" style="display: block; width: 46.68em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题4｜2021-20

<img src="../bank/2021/q20.png" alt="2021-20" style="display: block; width: 46.72em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：A（待逐题复核）。** 解析待补。

</details>

### 选择题5｜2021-21

<img src="../bank/2021/q21.png" alt="2021-21" style="display: block; width: 52.28em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题6｜2021-22

<img src="../bank/2021/q22.png" alt="2021-22" style="display: block; width: 39.16em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：A（待逐题复核）。** 解析待补。

</details>

### 选择题7｜2022-21

<img src="../bank/2022/q21.png" alt="2022-21" style="display: block; width: 29.04em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题8｜2023-22

<img src="../bank/2023/q22.png" alt="2023-22" style="display: block; width: 34.88em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题9｜2024-21

<img src="../bank/2024/q21.png" alt="2024-21" style="display: block; width: 28.0em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

**直接法：** 响应优先级由中断判优逻辑决定。屏蔽字可决定当前处理期间允许哪些中断嵌套，从而改变处理优先关系。断点和状态字由响应阶段保存，通用寄存器与新屏蔽字可由软件处理。

</details>

### 选择题10｜2024-22

<img src="../bank/2024/q22.png" alt="2024-22" style="display: block; width: 46.03em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题11｜2025-21

<img src="../bank/2025/q21.png" alt="2025-21" style="display: block; width: 40.84em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题12｜2025-22

<img src="../bank/2025/q22.png" alt="2025-22" style="display: block; width: 31.69em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：A（待逐题复核）。** 解析待补。

</details>

### 选择题13｜2026-21

<img src="../bank/2026/q21.png" alt="2026-21" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

**直接法：** 系统调用指令允许用户程序主动陷入。直接控制设备、关中断和恢复中断前机器状态涉及特权，不能由普通用户程序任意执行。

</details>

### 选择题14｜2026-22

<img src="../bank/2026/q22.png" alt="2026-22" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案与解析待补。**

</details>

## 选择题组2｜0906 · 计算机网络

[控制转发路径：ARP、路由协议与下一跳](../src/0906.md) · 5道 · 复做第1次。

### 选择题15｜2021-36

<img src="../bank/2021/q36.png" alt="2021-36" style="display: block; width: 46.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题16｜2021-37

<img src="../bank/2021/q37.png" alt="2021-37" style="display: block; width: 49.24em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题17｜2025-37

<img src="../bank/2025/q37.png" alt="2025-37" style="display: block; width: 42.29em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

**直接法：** NAPT可能改源端口，源IP也变，UDP校验和涉及这些字段故需更新；目的端口与总长度不随普通地址端口转换改变。选I、IV。

</details>

### 选择题18｜2026-37

<img src="../bank/2026/q37.png" alt="2026-37" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案与解析待补。**

</details>

### 选择题19｜2026-38

<img src="../bank/2026/q38.png" alt="2026-38" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

**直接法：** OSPF支持一个AS分成多个Area；RIP没有这种区域分层机制，BGP是外部网关协议，不符合题目“内部网关”。

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
