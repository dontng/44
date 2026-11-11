# Day 33｜数据结构＋操作系统

[← Day 32](day32.md) · [总入口](README.md) · [Day 34 →](day34.md)

**选择题：16道，来自两份完整src题单；大题：1道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：60—95分钟。** 选择题及核对约30—50分钟，大题约25—35分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0804 · 数据结构

[编码代价：哈夫曼树与前缀码](../src/0804.md) · 5道 · 复做第1次。

### 选择题1｜2021-05

<img src="../bank/2021/q05.png" alt="2021-05" style="display: block; width: 46.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题2｜2022-05

<img src="../bank/2022/q05.png" alt="2022-05" style="display: block; width: 47.72em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

**直接法：** 定长编码的所有字符都是同一深度，频次不同也不改变码长。哈夫曼树中频次不同的字符也可同层。两种树的高度可以相同；例如4个等频字符都用2位。结点数也未必相同，例如3个字符的定长码取00、01、10，按这三条路径建树有6个结点，而二叉哈夫曼树有5个。

</details>

### 选择题3｜2023-04

<img src="../bank/2023/q04.png" alt="2023-04" style="display: block; width: 46.92em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题4｜2025-05

<img src="../bank/2025/q05.png" alt="2025-05" style="display: block; width: 41.65em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题5｜2026-05

<img src="../bank/2026/q05.png" alt="2026-05" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案与解析待补。**

</details>

## 选择题组2｜0830 · 操作系统

[文件路径：名字、索引、数据块与共享](../src/0830.md) · 11道 · 复做第2次。

### 选择题6｜2020-23

<img src="../bank/2020/q23.png" alt="2020-23" style="display: block; width: 34.68em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题7｜2020-30

<img src="../bank/2020/q30.png" alt="2020-30" style="display: block; width: 34.08em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题8｜2020-31

<img src="../bank/2020/q31.png" alt="2020-31" style="display: block; width: 46.84em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题9｜2021-30

<img src="../bank/2021/q30.png" alt="2021-30" style="display: block; width: 43.46em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：A（待逐题复核）。** 解析待补。

</details>

### 选择题10｜2023-31

<img src="../bank/2023/q31.png" alt="2023-31" style="display: block; width: 46.88em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题11｜2024-26

<img src="../bank/2024/q26.png" alt="2024-26" style="display: block; width: 46.0em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：A（待逐题复核）。** 解析待补。

</details>

### 选择题12｜2024-29

<img src="../bank/2024/q29.png" alt="2024-29" style="display: block; width: 31.07em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

**直接法：** open 接收路径名，必须查找文件。后三者接收已分配的文件描述符。

</details>

### 选择题13｜2025-28

<img src="../bank/2025/q28.png" alt="2025-28" style="display: block; width: 30.42em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

**直接法：** VFS 为不同底层文件系统提供统一接口，可分派到本地或网络文件系统。“虚拟”描述接口抽象，访问速度取决于实现和缓存。

</details>

### 选择题14｜2025-29

<img src="../bank/2025/q29.png" alt="2025-29" style="display: block; width: 42.39em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题15｜2025-31

<img src="../bank/2025/q31.png" alt="2025-31" style="display: block; width: 35.19em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

**直接法：** FAT覆盖卷内各簇，表项可用特定值区分空闲簇、后继簇等状态，因此能反映外存空间使用情况。

**排除法／易混点：** 目录、FCB描述文件及其属性；系统打开文件表记录已打开的文件，三者都不能独立说明全盘哪些簇空闲。

</details>

### 选择题16｜2025-32

<img src="../bank/2025/q32.png" alt="2025-32" style="display: block; width: 34.9em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

## 解答题

### 大题1｜2023-46

[原题单 0928｜进程生命线：调度、输入与用户—内核边界](../src/0928.md)

<img src="../bank/2023/q46.png" alt="2023-46" style="display: block; width: 48.84em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

（1）顺序②⑥④③①⑤。①的前一个是③、后一个是⑤；⑥的下一个是④。

（2）②后进程因等待输入阻塞，CPU切换到其他可运行进程，必要时运行空闲进程。①后P进入就绪队列，才可能被调度。

（3）③读控制器并把字符放入内核缓冲区，由键盘驱动负责。

（4）进入键盘中断处理时，P因等字符而阻塞，CPU在内核态。处理到①才将P置为就绪，仍须调度才能执行。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
