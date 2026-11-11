# Day 05｜数据结构＋操作系统

[← Day 04](day04.md) · [总入口](README.md) · [Day 06 →](day06.md)

**选择题：16道，来自两份完整src题单；大题：1道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：70—115分钟。** 选择题及核对约40—70分钟，大题约25—35分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0802 · 数据结构

[受限容器：栈与队列的状态推进](../src/0802.md) · 5道 · 首次。

该src另收录的大题 2026-42 单独安排在解答题部分，不混入本组选择题。

### 选择题1｜2020-02

<img src="../bank/2020/q02.png" alt="2020-02" style="display: block; width: 58.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

**直接法：** 逐步跟踪：入a、入b、出b、入c、出c、入d、入e、出e，输出b,c,e。不要自动把剩下的栈也全部弹出。

</details>

### 选择题2｜2021-02

<img src="../bank/2021/q02.png" alt="2021-02" style="display: block; width: 46.68em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题3｜2022-02

<img src="../bank/2022/q02.png" alt="2022-02" style="display: block; width: 47.72em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题4｜2024-02

<img src="../bank/2024/q02.png" alt="2024-02" style="display: block; width: 26.37em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

**直接法：** 先(z−u)→zu−，再y乘→yzu−*，再除v→yzu−*v/，最后与x相加→xyzu−*v/+。乘除同优先级按原式左结合。

</details>

### 选择题5｜2025-02

<img src="../bank/2025/q02.png" alt="2025-02" style="display: block; width: 41.77em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

## 选择题组2｜0830 · 操作系统

[文件路径：名字、索引、数据块与共享](../src/0830.md) · 11道 · 首次。

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

### 大题1｜2026-41

[原题单 0914｜线性结构：数组与链表大题](../src/0914.md)

<img src="../bank/2026/q41.png" alt="2026-41" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

（1）按严格BST约定，关键字互异。若当前值小于 k，当前结点及其左子树都不大于当前值，保留当前值后可以舍弃左子树。大于 k 时对称。未命中时只比较小于 k 的最大值和大于 k 的最小值。可能只有一侧，也可能两侧等距。

（2）下面用 long long 先扩宽再相减，避免32位 int 边界处的差值溢出。时间 O(h)，辅助空间 O(1)。

```c
#include <stdio.h>

void searchX(BTree root, int k) {
    BTree lo = NULL, hi = NULL;
    for (BTree p = root; p != NULL; ) {
        if (p->data == k) {
            printf("0 %d\n", k);
            return;
        }
        if (p->data < k) {
            lo = p;
            p = p->right;
        } else {
            hi = p;
            p = p->left;
        }
    }
    if (lo == NULL && hi == NULL) return;
    long long dl = lo ? (long long)k - lo->data : -1;
    long long dh = hi ? (long long)hi->data - k : -1;
    long long best = (dl >= 0 && (dh < 0 || dl <= dh)) ? dl : dh;
    printf("%lld", best);
    if (dl == best) printf(" %d", lo->data);
    if (dh == best) printf(" %d", hi->data);
    putchar('\n');
}
```

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
