# Day 27｜数据结构＋操作系统

[← Day 26](day26.md) · [总入口](README.md) · [Day 28 →](day28.md)

**选择题：15道，来自两份完整src题单；大题：1道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：55—85分钟。** 选择题及核对约25—40分钟，大题约25—35分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0801 · 数据结构

[位置关系：指针、下标与压缩存储](../src/0801.md) · 8道 · 复做第1次。

### 选择题1｜2020-01

<img src="../bank/2020/q01.png" alt="2020-01" style="display: block; width: 46.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题2｜2021-01

<img src="../bank/2021/q01.png" alt="2021-01" style="display: block; width: 46.72em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

先q=h→next，再h→next=q→next；若p==q说明删的是唯一数据结点，尾指针p必须改为h，最后释放q。

</details>

### 选择题3｜2021-03

<img src="../bank/2021/q03.png" alt="2021-03" style="display: block; width: 46.8em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题4｜2023-02

<img src="../bank/2023/q02.png" alt="2023-02" style="display: block; width: 46.96em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

两条next赋值后，s的后继仍是原p的后继，其prev仍指p。先s→prev=s→next→prev得到p，再s→next→prev=s，补齐反向链。

</details>

### 选择题5｜2023-03

<img src="../bank/2023/q03.png" alt="2023-03" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

需要保存矩阵总行数、总列数，即I、III；含非零元素的行列数不能告诉你末尾全零行列有多少。

</details>

### 选择题6｜2024-01

<img src="../bank/2024/q01.png" alt="2024-01" style="display: block; width: 45.97em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

先把q=p的后继摘下：p→next=q→next；再将q头插到h之后。被移动的是q，不是p。

</details>

### 选择题7｜2026-01

<img src="../bank/2026/q01.png" alt="2026-01" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

表头插入要将原n个元素后移，表头删除要将后续n−1个元素前移；n≥3，I、II都必然移动多个元素。

III表尾插入已有空位，直接写入；IV表尾删除只需减小表长，不必搬动其余元素。保持原元素相对次序，排除了用末尾元素覆盖表头的做法。

</details>

### 选择题8｜2026-02

<img src="../bank/2026/q02.png" alt="2026-02" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案与解析待补。**

</details>

## 选择题组2｜0831 · 操作系统

[设备服务：缓冲、磁盘与请求调度](../src/0831.md) · 7道 · 复做第1次。

### 选择题9｜2021-26

<img src="../bank/2021/q26.png" alt="2021-26" style="display: block; width: 46.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题10｜2022-32

<img src="../bank/2022/q32.png" alt="2022-32" style="display: block; width: 26.04em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：A（待逐题复核）。** 解析待补。

</details>

### 选择题11｜2023-32

<img src="../bank/2023/q32.png" alt="2023-32" style="display: block; width: 44.04em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题12｜2024-31

<img src="../bank/2024/q31.png" alt="2024-31" style="display: block; width: 33.23em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

中断例程把字符放入内核缓冲区。CPU寄存器只是临时载体，用户缓冲区属于后续交付。

</details>

### 选择题13｜2024-32

<img src="../bank/2024/q32.png" alt="2024-32" style="display: block; width: 47.59em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题14｜2026-31

<img src="../bank/2026/q31.png" alt="2026-31" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

块设备和字符设备的传输单位与设备特性不同，I/O控制方式可以不同。它们仍可在内核规定的接口下提供启动和读写操作。

</details>

### 选择题15｜2026-32

<img src="../bank/2026/q32.png" alt="2026-32" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案与解析待补。**

</details>

## 解答题

### 大题1｜2025-45

[原题单 0925｜并发同步：PV 操作大题](../src/0925.md)

<img src="../bank/2025/q45.png" alt="2025-45" style="display: block; width: 42.48em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

四个信号量：slots=3 表示还能挖的坑配额，dug=0 表示可供乙种植的空坑，planted=0 表示可浇的树，spade=1 表示铁锹可用。

```text
甲重复：
    wait(slots)
    wait(spade)
    挖坑
    signal(spade)
    signal(dug)

乙重复：
    wait(dug)
    放树苗
    wait(spade)
    填土
    signal(spade)
    signal(slots)
    signal(planted)

丙重复：
    wait(planted)
    浇水
```

甲在动工前预扣坑配额，乙在填土后归还，因此未填满的坑最多三个。乙须等甲挖完，丙须等乙填完。铁锹只覆盖挖坑、填土，不持有铁锹等待坑位或空坑。水桶只有丙一个使用者，丙顺序执行即可。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
