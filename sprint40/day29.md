# Day 29｜数据结构＋操作系统

[← Day 28](day28.md) · [总入口](README.md) · [Day 30 →](day30.md)

**选择题：11道，来自两份完整src题单；大题：1道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：45—75分钟。** 选择题及核对约15—30分钟，大题约25—35分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0802 · 数据结构

[受限容器：栈与队列的状态推进](../src/0802.md) · 5道 · 复做第1次。

该src另收录的大题 2026-42 单独安排在解答题部分，不混入本组选择题。

### 选择题1｜2020-02

<img src="../bank/2020/q02.png" alt="2020-02" style="display: block; width: 58.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

逐步跟踪：入a、入b、出b、入c、出c、入d、入e、出e，输出b,c,e。不要自动把剩下的栈也全部弹出。

</details>

### 选择题2｜2021-02

<img src="../bank/2021/q02.png" alt="2021-02" style="display: block; width: 46.68em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

以可出队的一端为右端。要先出4，再出1，1、2、3必须按从右到左1、2、3排列；4从右端插入后立即弹出。此时1出队后，右端露出2，不能越过2先出3，所以D不可能。A、B、C都能通过把后续元素插到左端或右端实现，双端入队不等于双端都能出队。

</details>

### 选择题3｜2022-02

<img src="../bank/2022/q02.png" alt="2022-02" style="display: block; width: 47.72em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

把in中的元素全部压栈，再逐个弹出，out正好是in的倒序，所以D成立。若每压入一个立即弹出，in与out也可以相同，C错误。给定两个序列可以模拟压栈、弹栈判定其合法性，不存在A、B所说的无法判断。

</details>

### 选择题4｜2024-02

<img src="../bank/2024/q02.png" alt="2024-02" style="display: block; width: 26.37em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

先(z−u)→zu−，再y乘→yzu−*，再除v→yzu−*v/，最后与x相加→xyzu−*v/+。乘除同优先级按原式左结合。

</details>

### 选择题5｜2025-02

<img src="../bank/2025/q02.png" alt="2025-02" style="display: block; width: 41.77em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

栈保存尚未匹配的左括号，容量取决于最大嵌套深度。D读到(d+e)的左圆括号时，栈中已有外层[、(、[，再压入(需第4个位置，容量3不够。A、B、C的最大深度均为3；表达式长短和括号总数不是判据。

</details>

## 选择题组2｜0826 · 操作系统

[并发约束：把交错执行压成可证明的顺序](../src/0826.md) · 6道 · 复做第1次。

### 选择题6｜2020-32

<img src="../bank/2020/q32.png" alt="2020-32" style="display: block; width: 44.88em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

Ⅰ保证互斥，Ⅱ对应空闲让进，Ⅲ对应有限等待，均应满足。Ⅳ“等待时立即让出CPU”是让权等待，忙等锁不会这样做，但仍可实现临界区互斥，因此不是所有互斥机制必须满足的条件。

</details>

### 选择题7｜2024-28

<img src="../bank/2024/q28.png" alt="2024-28" style="display: block; width: 45.97em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

同一进程内线程共享进程地址空间和打开文件资源，所以Ⅰ、Ⅲ成立。每个线程有自己的执行栈及寄存器现场，Ta、Tb不能把T的栈当作共同运行栈，Ⅱ不选。共享地址空间使线程可能通过指针访问另一线程栈中的对象，但不等于共享其线程栈资源。

</details>

### 选择题8｜2024-30

<img src="../bank/2024/q30.png" alt="2024-30" style="display: block; width: 46.03em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

P需要25/5=5个时间片，且初始排队尾。其他9个进程所需时间均不短于P，因此在P完成前，每一轮都还有10个进程参与。五轮各50ms，P在第5轮最后完成，周转时间5×50=250ms；不能只计算P自己的25ms。

</details>

### 选择题9｜2025-27

<img src="../bank/2025/q27.png" alt="2025-27" style="display: block; width: 37.09em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

最少页框要保证一条指令能完成：指令本身和各次间接寻址、操作数访问可能落在不同页，因而取决于指令系统支持的寻址方式。虚拟空间或物理空间总大小决定总体规模，代码段长度决定全部代码多少页，都不直接决定这条指令需要同时驻留的最少页数。

</details>

### 选择题10｜2026-26

<img src="../bank/2026/q26.png" alt="2026-26" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

S=−2表示2个在wait处阻塞；临界代码Q最多5个并发，当前已有5个获得许可，故m=5、n=2。这里的m指已进入Q尚未归还许可的在执行者，不是历史累计次数。

</details>

### 选择题11｜2026-27

<img src="../bank/2026/q27.png" alt="2026-27" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

要排除写冲突，既不能两边写同一数据，也不能一边读另一边正在写的数据，对应Ⅰ、Ⅱ、Ⅲ。两进程只读同一数据不会相互改变结果，Ⅳ无须成立。题目按读写集合独立性的Bernstein条件判断，不把“读集合必须互斥”额外加进去。

</details>

## 解答题

### 大题1｜2021-46

[原题单 0927｜文件与磁盘：名字、索引和物理块怎样连接](../src/0927.md)

<img src="../bank/2021/q46.png" alt="2021-46" style="display: block; width: 46.72em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

（1）ROM引导程序 → 磁盘主引导记录中的磁盘引导程序 → 所选分区首扇区的分区引导程序 → 操作系统初始化程序。磁盘引导程序读取分区表定位要启动的分区。

（2）物理格式化 → 磁盘分区 → 逻辑格式化 → 安装操作系统。先建立可读写的扇区，再决定哪些扇区组成分区，最后在目标分区建立文件系统并安装系统。

（3）划分扇区属于物理格式化。建立文件系统根目录属于逻辑格式化。分区表描述分区范围，根目录是分区中文件系统的一部分。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
