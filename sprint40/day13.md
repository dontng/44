# Day 13｜数据结构＋操作系统

[← Day 12](day12.md) · [总入口](README.md) · [Day 14 →](day14.md)

**选择题：19道，来自两份完整src题单；大题：1道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：100—160分钟。** 选择题及核对约70—115分钟，大题约25—35分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0806 · 数据结构

[图的骨架：表示、遍历与连通](../src/0806.md) · 6道 · 首次。

### 选择题1｜2020-06

<img src="../bank/2020/q06.png" alt="2020-06" style="display: block; width: 46.44em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题2｜2022-06

<img src="../bank/2022/q06.png" alt="2022-06" style="display: block; width: 29.68em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

连通图有生成树，至少有 |V|−1 条边。边数达到下界仍可能不连通，例如三角形加一个孤点。

</details>

### 选择题3｜2023-06

<img src="../bank/2023/q06.png" alt="2023-06" style="display: block; width: 46.88em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题4｜2024-04

<img src="../bank/2024/q04.png" alt="2024-04" style="display: block; width: 43.57em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

b 关联 (0,1)、(1,3) 两条边；d 关联 (0,3)、(1,3)、(3,2)、(4,3) 四条边。追踪每条边时按所求端点位于 i 还是 j，选对应的链接。

</details>

### 选择题5｜2025-06

<img src="../bank/2025/q06.png" alt="2025-06" style="display: block; width: 29.87em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题6｜2026-06

<img src="../bank/2026/q06.png" alt="2026-06" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案与解析待补。**

</details>

## 选择题组2｜0829 · 操作系统

[页面驻留：置换、工作集与缺页代价](../src/0829.md) · 13道 · 首次。

### 选择题7｜2020-28

<img src="../bank/2020/q28.png" alt="2020-28" style="display: block; width: 44.71em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

缺页率决定走慢路径概率；磁盘读写、内存访存、CPU处理异常均贡献耗时，I—IV都影响。

</details>

### 选择题8｜2021-28

<img src="../bank/2021/q28.png" alt="2021-28" style="display: block; width: 46.12em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题9｜2021-29

<img src="../bank/2021/q29.png" alt="2021-29" style="display: block; width: 38.4em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题10｜2022-29

<img src="../bank/2022/q29.png" alt="2022-29" style="display: block; width: 47.72em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：A（待逐题复核）。** 解析待补。

</details>

### 选择题11｜2022-30

<img src="../bank/2022/q30.png" alt="2022-30" style="display: block; width: 33.73em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题12｜2023-25

<img src="../bank/2023/q25.png" alt="2023-25" style="display: block; width: 46.85em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

16GiB÷4KiB=2²²个页框，每框用1bit表示状态；位图占2²²bit÷8=2¹⁹B=512KiB。

D的4MB漏了bit转Byte的除8。位图不是每页框存一个字节。

</details>

### 选择题13｜2023-28

<img src="../bank/2023/q28.png" alt="2023-28" style="display: block; width: 44.62em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题14｜2024-25

<img src="../bank/2024/q25.png" alt="2024-25" style="display: block; width: 39.93em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题15｜2025-26

<img src="../bank/2025/q26.png" alt="2025-26" style="display: block; width: 42.61em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题16｜2025-27

<img src="../bank/2025/q27.png" alt="2025-27" style="display: block; width: 37.09em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

最少页框要保证一条指令能完成：指令本身和各次间接寻址、操作数访问可能落在不同页，因而取决于指令系统支持的寻址方式。虚拟空间或物理空间总大小决定总体规模，代码段长度决定全部代码多少页，都不直接决定这条指令需要同时驻留的最少页数。

</details>

### 选择题17｜2025-30

<img src="../bank/2025/q30.png" alt="2025-30" style="display: block; width: 40.35em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题18｜2026-29

<img src="../bank/2026/q29.png" alt="2026-29" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案与解析待补。**

</details>

### 选择题19｜2026-30

<img src="../bank/2026/q30.png" alt="2026-30" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

共享同一页意味着两个进程所见数据映射到同一物理页；虚拟起址可不同，页表项权限等内容可不同，页表项自身的存放地址也不必相同。

</details>

## 解答题

### 大题1｜2021-42

[原题单 0918｜查找与排序：让分布、权重和内存边界决定代价](../src/0918.md)

<img src="../bank/2021/q42.png" alt="2021-42" style="display: block; width: 46.56em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

（1）b最终为`[-10, 10, 11, 19, 25, 25]`。为检查稳定性，把原先两个25记为25a、25b，实际顺序为`[-10,10,11,19,25b,25a]`。

（2）内层分别执行n−1、n−2、…、1次，元素比较总数n(n−1)/2；本题n=6时为15次。时间O(n²)，辅助数组count占O(n)。

（3）原算法不稳定。当i<j且a[i]==a[j]，会进入else令count[i]++，使较早出现的相等元素排在后面。只需把比较改为：

```c
if (a[i] <= a[j]) ++count[j];
else ++count[i];
```

使相等时较晚元素的排名加1，即可保留原先次序；不同元素的大小关系不变。不能因为最后两个整数都显示25，就认为稳定性无从讨论。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
