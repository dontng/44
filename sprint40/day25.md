# Day 25｜数据结构＋操作系统

[← Day 24](day24.md) · [总入口](README.md) · [Day 26 →](day26.md)

**选择题：17道，来自两份完整src题单；大题：1道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：70—115分钟。** 选择题及核对约40—70分钟，大题约25—35分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0731 · 数据结构

[时间复杂度：循环执行次数](../src/0731.md) · 4道 · 复做第1次。

### 选择题1｜2022-01

<img src="../bank/2022/q01.png" alt="2022-01" style="display: block; width: 48.32em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

**直接法：** i依次取1、2、4、8……，每轮内层执行i次。设最后一轮i=L，总次数1+2+4+…+L=2L−1；L与n同量级，所以是O(n)。

**排除法／易混点：** A的O(log n)只数了外层轮数；C的O(n log n)把每轮内层都当成n次；D的O(n²)忽略了i每次翻倍。内层上限跟着i变，不能直接把两层的最大次数相乘。

</details>

### 选择题2｜2023-01

<img src="../bank/2023/q01.png" alt="2023-01" style="display: block; width: 46.96em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

**直接法：** 顺序表按下标取第i个元素，地址=首地址+(i−1)×元素大小，一次计算即可，O(1)。

**排除法／易混点：** A是按值查找：有序只能帮助二分，平均O(log n)，不是直接知道下标；B插入、C删除一般要移动后续元素，平均O(n)。分清“给值找位置”和“给位置取值”。

</details>

### 选择题3｜2025-01

<img src="../bank/2025/q01.png" alt="2025-01" style="display: block; width: 37.65em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

**直接法：** 外层i从1加到⌊√n⌋，内层每轮执行i次。令m=⌊√n⌋，总次数为1+2+…+m=m(m+1)/2，与n同量级，故O(n)。

**排除法／易混点：** A错在把i++看成翻倍；C、D错在没有先由i²≤n得到外层上限√n。√n轮，每轮最多√n次，已经给出O(n)上界。

</details>

### 选择题4｜2026-01

<img src="../bank/2026/q01.png" alt="2026-01" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

**直接法：** 表头插入要将原n个元素后移，表头删除要将后续n−1个元素前移；n≥3，I、II都必然移动多个元素。

**排除法／易混点：** III表尾插入已有空位，直接写入；IV表尾删除只需减小表长，不必搬动其余元素。保持原元素相对次序，排除了用末尾元素覆盖表头的做法。

</details>

## 选择题组2｜0829 · 操作系统

[页面驻留：置换、工作集与缺页代价](../src/0829.md) · 13道 · 复做第1次。

### 选择题5｜2020-28

<img src="../bank/2020/q28.png" alt="2020-28" style="display: block; width: 44.71em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

**直接法：** 缺页率决定走慢路径概率；磁盘读写、内存访存、CPU处理异常均贡献耗时，I—IV都影响。

</details>

### 选择题6｜2021-28

<img src="../bank/2021/q28.png" alt="2021-28" style="display: block; width: 46.12em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题7｜2021-29

<img src="../bank/2021/q29.png" alt="2021-29" style="display: block; width: 38.4em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题8｜2022-29

<img src="../bank/2022/q29.png" alt="2022-29" style="display: block; width: 47.72em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：A（待逐题复核）。** 解析待补。

</details>

### 选择题9｜2022-30

<img src="../bank/2022/q30.png" alt="2022-30" style="display: block; width: 33.73em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题10｜2023-25

<img src="../bank/2023/q25.png" alt="2023-25" style="display: block; width: 46.85em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

**直接法：** 16GiB÷4KiB=2²²个页框，每框用1bit表示状态；位图占2²²bit÷8=2¹⁹B=512KiB。

**排除法／易混点：** D的4MB漏了bit转Byte的除8。位图不是每页框存一个字节。

</details>

### 选择题11｜2023-28

<img src="../bank/2023/q28.png" alt="2023-28" style="display: block; width: 44.62em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题12｜2024-25

<img src="../bank/2024/q25.png" alt="2024-25" style="display: block; width: 39.93em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题13｜2025-26

<img src="../bank/2025/q26.png" alt="2025-26" style="display: block; width: 42.61em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题14｜2025-27

<img src="../bank/2025/q27.png" alt="2025-27" style="display: block; width: 37.09em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题15｜2025-30

<img src="../bank/2025/q30.png" alt="2025-30" style="display: block; width: 40.35em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题16｜2026-29

<img src="../bank/2026/q29.png" alt="2026-29" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案与解析待补。**

</details>

### 选择题17｜2026-30

<img src="../bank/2026/q30.png" alt="2026-30" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

**直接法：** 共享同一页意味着两个进程所见数据映射到同一物理页；虚拟起址可不同，页表项权限等内容可不同，页表项自身的存放地址也不必相同。

</details>

## 解答题

### 大题1｜2023-45

[原题单 0925｜并发同步：PV 操作大题](../src/0925.md)

<img src="../bank/2023/q45.png" alt="2023-45" style="display: block; width: 46.92em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

（1）进入区中的`if (key == TRUE)`须改为`while (key == TRUE)`；退出区中的`lock = TRUE`须改为`lock = FALSE`。正确逻辑为：

```text
bool key = TRUE;
while (key == TRUE) swap key, lock;
临界区;
lock = FALSE;
```

硬件swap原子交换key与共享lock。拿到FALSE的线程停止自旋，同时把lock置TRUE；没拿到锁的线程继续等待。

（2）不能直接用题示newSwap替代。函数里的读取、赋值是多条普通操作，可与另一线程交错；函数调用本身不会使整个函数原子化。两个线程可能都在lock为FALSE时读到它并误以为取得锁。判断依据是原子保证，不是变量交换后的单线程结果是否相同。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
