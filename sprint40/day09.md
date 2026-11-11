# Day 09｜数据结构＋操作系统

[← Day 08](day08.md) · [总入口](README.md) · [Day 10 →](day10.md)

**选择题：18道，来自两份完整src题单；大题：1道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：85—135分钟。** 选择题及核对约55—90分钟，大题约25—35分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0804 · 数据结构

[编码代价：哈夫曼树与前缀码](../src/0804.md) · 5道 · 首次。

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

定长编码的所有字符都是同一深度，频次不同也不改变码长。哈夫曼树中频次不同的字符也可同层。两种树的高度可以相同；例如4个等频字符都用2位。结点数也未必相同，例如3个字符的定长码取00、01、10，按这三条路径建树有6个结点，而二叉哈夫曼树有5个。

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

## 选择题组2｜0825 · 操作系统

[执行生命线：进程、线程、状态与调度](../src/0825.md) · 13道 · 首次。

### 选择题6｜2020-26

<img src="../bank/2020/q26.png" alt="2020-26" style="display: block; width: 46.75em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题7｜2020-29

<img src="../bank/2020/q29.png" alt="2020-29" style="display: block; width: 30.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题8｜2021-24

<img src="../bank/2021/q24.png" alt="2021-24" style="display: block; width: 44.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题9｜2021-25

<img src="../bank/2021/q25.png" alt="2021-25" style="display: block; width: 44.96em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

时间片轮转需PCB记录上下文、时钟中断计时、就绪队列轮换；不因采用轮转就必须用阻塞队列，选I、II、III。

</details>

### 选择题10｜2021-27

<img src="../bank/2021/q27.png" alt="2021-27" style="display: block; width: 45.28em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题11｜2022-23

<img src="../bank/2022/q23.png" alt="2022-23" style="display: block; width: 40.0em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题12｜2022-25

<img src="../bank/2022/q25.png" alt="2022-25" style="display: block; width: 47.8em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题13｜2022-28

<img src="../bank/2022/q28.png" alt="2022-28" style="display: block; width: 42.96em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

读文件、申请外设和P操作都可能等待而阻塞；时间片用完转就绪，不转阻塞。选I、III、IV。

</details>

### 选择题14｜2023-27

<img src="../bank/2023/q27.png" alt="2023-27" style="display: block; width: 43.96em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题15｜2023-29

<img src="../bank/2023/q29.png" alt="2023-29" style="display: block; width: 48.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题16｜2024-24

<img src="../bank/2024/q24.png" alt="2024-24" style="display: block; width: 32.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：A（待逐题复核）。** 解析待补。

</details>

### 选择题17｜2025-25

<img src="../bank/2025/q25.png" alt="2025-25" style="display: block; width: 42.61em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题18｜2026-25

<img src="../bank/2026/q25.png" alt="2026-25" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案与解析待补。**

</details>

## 解答题

### 大题1｜2021-41

[原题单 0916｜图的结构判定：从邻接信息恢复全局性质](../src/0916.md)

<img src="../bank/2021/q41.png" alt="2021-41" style="display: block; width: 46.8em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**思想。** 对邻接矩阵逐行求和得到各顶点度数；奇数度顶点数为0或2时返回1，否则返回0。连通性是题设，不能多添一次不必要的图遍历；若换成一般输入，才须额外核验所有有边顶点连通。

```c
int IsExistEL(MGraph G) {
    int odd = 0;
    for (int i = 0; i < G.numVertices; ++i) {
        int degree = 0;
        for (int j = 0; j < G.numVertices; ++j)
            degree += G.Edge[i][j];
        if (degree % 2 != 0) ++odd;
    }
    return odd == 0 || odd == 2;
}
```

共检查V²个矩阵元素，时间O(V²)，辅助空间O(1)。这是判定题，无须写输出路径的算法。代码沿用原题无向图邻接矩阵的0/1表示。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
