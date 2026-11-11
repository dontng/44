# Day 11｜数据结构＋操作系统

[← Day 10](day10.md) · [总入口](README.md) · [Day 12 →](day12.md)

**选择题：13道，来自两份完整src题单；大题：1道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：65—100分钟。** 选择题及核对约35—55分钟，大题约25—35分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0805 · 数据结构

[有序树：从局部旋转到多路分裂](../src/0805.md) · 9道 · 首次。

### 选择题1｜2020-05

<img src="../bank/2020/q05.png" alt="2020-05" style="display: block; width: 46.8em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

目标左子树根是2，故2必须在1、3之前插入。B先插1再插2，会把1变成4的左孩子，不能得到题图。

</details>

### 选择题2｜2020-10

<img src="../bank/2020/q10.png" alt="2020-10" style="display: block; width: 46.68em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题3｜2021-06

<img src="../bank/2021/q06.png" alt="2021-06" style="display: block; width: 38.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题4｜2021-09

<img src="../bank/2021/q09.png" alt="2021-09" style="display: block; width: 46.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：A（待逐题复核）。** 解析待补。

</details>

### 选择题5｜2022-08

<img src="../bank/2022/q08.png" alt="2022-08" style="display: block; width: 47.6em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题6｜2023-07

<img src="../bank/2023/q07.png" alt="2023-07" style="display: block; width: 43.23em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

I插入根分裂可增高；II删除最终在叶层移除或调整关键字，会改变叶；III错，B树可在内部命中；IV错，插入关键字可分裂提升。选I、II。

</details>

### 选择题7｜2024-07

<img src="../bank/2024/q07.png" alt="2024-07" style="display: block; width: 45.4em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

T在k3右侧且在k2左侧，所有x满足k3<x<k2，同时继承k1<x。D给出有效的更紧区间。

</details>

### 选择题8｜2025-08

<img src="../bank/2025/q08.png" alt="2025-08" style="display: block; width: 36.74em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题9｜2026-08

<img src="../bank/2026/q08.png" alt="2026-08" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案与解析待补。**

</details>

## 选择题组2｜0828 · 操作系统

[内存边界：分配、回收与保护](../src/0828.md) · 4道 · 首次。

### 选择题10｜2020-24

<img src="../bank/2020/q24.png" alt="2020-24" style="display: block; width: 41.52em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：A（待逐题复核）。** 解析待补。

</details>

### 选择题11｜2023-30

<img src="../bank/2023/q30.png" alt="2023-30" style="display: block; width: 46.85em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

R与S可用不同虚拟页号p1、p2映射共享数据，但共享同一物理页框，f1=f2。别把各自地址空间的编号当成全局编号。

</details>

### 选择题12｜2024-27

<img src="../bank/2024/q27.png" alt="2024-27" style="display: block; width: 36.72em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：A（待逐题复核）。** 解析待补。

</details>

### 选择题13｜2026-28

<img src="../bank/2026/q28.png" alt="2026-28" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案与解析待补。**

</details>

## 解答题

### 大题1｜2025-42

[原题单 0917｜图上的最优推进：最短路、生成树与关键路径](../src/0917.md)

<img src="../bank/2025/q42.png" alt="2025-42" style="display: block; width: 42.52em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**解析待补。**

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
