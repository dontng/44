# Day 04｜组成原理＋计算机网络

[← Day 03](day03.md) · [总入口](README.md) · [Day 05 →](day05.md)

**选择题：16道，来自两份完整src题单；大题：1道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：100—150分钟。** 选择题及核对约70—105分钟，大题约25—35分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0813 · 组成原理

[有限位运算：溢出、标志与乘除](../src/0813.md) · 5道 · 首次。

### 选择题1｜2021-13

<img src="../bank/2021/q13.png" alt="2021-13" style="display: block; width: 52.2em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

16位有符号：x=FFFDH=−3，y=FFDFH=−33，z=7FFCH=32764，所以y<x<z。若按无符号解释则z<y<x。

</details>

### 选择题2｜2023-16

<img src="../bank/2023/q16.png" alt="2023-16" style="display: block; width: 46.81em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题3｜2024-15

<img src="../bank/2024/q15.png" alt="2024-15" style="display: block; width: 35.43em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

两个变量相乘也能用循环移位加法实现，D说无法转换是错的。阵列乘法器可在一个足够长的时钟周期完成；串行移位加法通常需多个周期。

</details>

### 选择题4｜2025-14

<img src="../bank/2025/q14.png" alt="2025-14" style="display: block; width: 52.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题5｜2026-13

<img src="../bank/2026/q13.png" alt="2026-13" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案与解析待补。**

</details>

## 选择题组2｜0907 · 计算机网络

[端到端状态：TCP序号、窗口与拥塞](../src/0907.md) · 11道 · 首次。

### 选择题6｜2020-38

<img src="../bank/2020/q38.png" alt="2020-38" style="display: block; width: 46.68em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题7｜2020-39

<img src="../bank/2020/q39.png" alt="2020-39" style="display: block; width: 46.72em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题8｜2021-38

<img src="../bank/2021/q38.png" alt="2021-38" style="display: block; width: 58.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题9｜2021-39

<img src="../bank/2021/q39.png" alt="2021-39" style="display: block; width: 46.72em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题10｜2021-40

<img src="../bank/2021/q40.png" alt="2021-40" style="display: block; width: 46.84em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题11｜2022-38

<img src="../bank/2022/q38.png" alt="2022-38" style="display: block; width: 45.88em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题12｜2022-39

<img src="../bank/2022/q39.png" alt="2022-39" style="display: block; width: 45.92em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题13｜2024-38

<img src="../bank/2024/q38.png" alt="2024-38" style="display: block; width: 46.0em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

建连至可发数据耗时1RTT。按本题参考解采用的慢开始起始窗口1MSS，3个段分1+2两轮，耗时2RTT。主动关闭最短再花1RTT，随后等2MSL。合计60.04s。原题未明说初始拥塞窗口，若给定初始窗口至少3MSS，数据可一轮发完，结果会变为60.03s。

</details>

### 选择题14｜2024-39

<img src="../bank/2024/q39.png" alt="2024-39" style="display: block; width: 46.0em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题15｜2025-38

<img src="../bank/2025/q38.png" alt="2025-38" style="display: block; width: 42.29em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：A（待逐题复核）。** 解析待补。

</details>

### 选择题16｜2025-39

<img src="../bank/2025/q39.png" alt="2025-39" style="display: block; width: 42.42em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

UDP请求和应答只花1RTT即8ms。TCP建连1RTT，第三次握手附请求，收到回应再花1RTT，共16ms。

</details>

## 解答题

### 大题1｜2025-41

[原题单 0914｜线性结构：数组与链表大题](../src/0914.md)

<img src="../bank/2025/q41.png" alt="2025-41" style="display: block; width: 42.55em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

（1）从右向左扫描，先把 A[i] 纳入后缀。A[i] 非负就乘后缀最大值，为负就乘后缀最小值。

（2）沿用题设 int 输出，假定应存入 res 的乘积在 int 范围内。

```c
void calMulMax(int A[], int res[], int n) {
    if (n <= 0) return;
    int lo = A[n - 1], hi = A[n - 1];
    for (int i = n - 1; i >= 0; --i) {
        int x = A[i];
        // 先纳入自身，保证后缀范围为 [i, n-1]
        if (x < lo) lo = x;
        if (x > hi) hi = x;
        res[i] = x * (x < 0 ? lo : hi);
    }
}
```

（3）每个位置处理一次，时间 O(n)，除输入输出外空间 O(1)。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
