# Day 23｜数据结构＋操作系统

[← Day 22](day22.md) · [总入口](README.md) · [Day 24 →](day24.md)

**选择题：15道，来自两份完整src题单；大题：1道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：60—90分钟。** 选择题及核对约30—45分钟，大题约25—35分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0811 · 数据结构

[外存归并：内存装不下以后怎样排序](../src/0811.md) · 2道 · 首次。

### 选择题1｜2024-11

<img src="../bank/2024/q11.png" alt="2024-11" style="display: block; width: 47.41em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

升序归并的冠军对应各段当前最小段首。冠军结点保存该关键字所在的归并段号，由段号读取元素和补入下一条。

</details>

### 选择题2｜2026-11

<img src="../bank/2026/q11.png" alt="2026-11" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案与解析待补。**

</details>

## 选择题组2｜0825 · 操作系统

[执行生命线：进程、线程、状态与调度](../src/0825.md) · 13道 · 复做第1次。

### 选择题3｜2020-26

<img src="../bank/2020/q26.png" alt="2020-26" style="display: block; width: 46.75em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题4｜2020-29

<img src="../bank/2020/q29.png" alt="2020-29" style="display: block; width: 30.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题5｜2021-24

<img src="../bank/2021/q24.png" alt="2021-24" style="display: block; width: 44.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题6｜2021-25

<img src="../bank/2021/q25.png" alt="2021-25" style="display: block; width: 44.96em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

时间片轮转需PCB记录上下文、时钟中断计时、就绪队列轮换；不因采用轮转就必须用阻塞队列，选I、II、III。

</details>

### 选择题7｜2021-27

<img src="../bank/2021/q27.png" alt="2021-27" style="display: block; width: 45.28em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题8｜2022-23

<img src="../bank/2022/q23.png" alt="2022-23" style="display: block; width: 40.0em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题9｜2022-25

<img src="../bank/2022/q25.png" alt="2022-25" style="display: block; width: 47.8em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题10｜2022-28

<img src="../bank/2022/q28.png" alt="2022-28" style="display: block; width: 42.96em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

读文件、申请外设和P操作都可能等待而阻塞；时间片用完转就绪，不转阻塞。选I、III、IV。

</details>

### 选择题11｜2023-27

<img src="../bank/2023/q27.png" alt="2023-27" style="display: block; width: 43.96em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题12｜2023-29

<img src="../bank/2023/q29.png" alt="2023-29" style="display: block; width: 48.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题13｜2024-24

<img src="../bank/2024/q24.png" alt="2024-24" style="display: block; width: 32.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：A（待逐题复核）。** 解析待补。

</details>

### 选择题14｜2025-25

<img src="../bank/2025/q25.png" alt="2025-25" style="display: block; width: 42.61em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题15｜2026-25

<img src="../bank/2026/q25.png" alt="2026-25" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案与解析待补。**

</details>

## 解答题

### 大题1｜2021-45

[原题单 0925｜并发同步：PV 操作大题](../src/0925.md)

<img src="../bank/2021/q45.png" alt="2021-45" style="display: block; width: 46.8em; max-width: 100%; height: auto; margin: 12px 0;">

**题图勘误：** 方法2的 `while(S<=0)` 后应为左花括号，不能按图中的分号执行。作答时使用下面这个循环体：

```text
while (S <= 0) {
    开中断;
    关中断;
}
```

<details>
<summary>答案与解析</summary>

（1）S是共享资源计数，检查与修改必须互斥。否则两个调用者可能同时看到S=1并都通过等待，导致同一份资源被重复分配。

（2）以本题的单处理器模型判断。方法1错误：S≤0时一直关中断忙等，能执行 signal 的进程得不到调度，S可能一直无法增大。方法2正确：只有检查得到 S≤0 才进入循环体临时开中断，给其他进程运行机会；重新关中断后再检查。最后一次检查得到 S>0 时直接跳过循环体，接着执行 S--，这两步始终关中断。signal 修改 S 时也关中断。

上方已明确修正题图的循环边界。若坚持按分号空循环逐字执行，方法2同样会在关中断状态下忙等，不能得出“方法2正确”；本解的正确结论只针对花括号版本。

（3）用户程序不能用开/关中断指令实现临界区互斥，因为它们是特权指令，只能在内核态执行；用户态应通过提供的同步机制或原子操作实现互斥。即使在内核使用，单纯屏蔽本CPU中断也不能自动解决多核之间的互斥。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
