# Day 07｜数据结构＋操作系统

[← Day 06](day06.md) · [总入口](README.md) · [Day 08 →](day08.md)

**选择题：17道，来自两份完整src题单；大题：1道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：75—120分钟。** 选择题及核对约45—75分钟，大题约25—35分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0803 · 数据结构

[树的形状：遍历序列如何约束结构](../src/0803.md) · 11道 · 首次。

### 选择题1｜2020-03

<img src="../bank/2020/q03.png" alt="2020-03" style="display: block; width: 46.68em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

顺序存储使用完全二叉树的位置编号。高5层的树可能沿右孩子一直向下，最深结点编号为31，因此要能保存任意符合题意的树，至少预留31个位置。10是实际结点数，不是最坏位置跨度；16只够覆盖最左侧的第5层起点。

</details>

### 选择题2｜2020-04

<img src="../bank/2020/q04.png" alt="2020-04" style="display: block; width: 46.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

森林先根序列等于对应二叉树的先序，中根序列等于对应二叉树的中序。由先序a,b,c,d,e,f及中序b,a,d,f,e,c还原：a左为b、右为c；c左为d，d右为e，e左为f。按左右根输出b,f,e,d,c,a，选C。不要把森林的中根序列误当成二叉树后序。

</details>

### 选择题3｜2021-04

<img src="../bank/2021/q04.png" alt="2021-04" style="display: block; width: 46.8em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

森林各棵树的根在对应二叉树中沿根的右孩子链排列。先序首项a是根，中序中a右侧为e,g,c,f；右子树先序为c,e,g,f，所以右孩子是c。c的右子树仅f，得到根链a→c→f，共3棵；左子树里的b、d、e、g都是树内孩子，不增加森林棵数。

</details>

### 选择题4｜2022-03

<img src="../bank/2022/q03.png" alt="2022-03" style="display: block; width: 46.96em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

若p是左孩子且无右子树，紧接着就是双亲q，Ⅰ可能；若p的右孩子q没有左子树，Ⅱ可能；若p是祖父q的左子树最右结点，Ⅳ也可能。若q是p的右兄弟，二者共同双亲必在中序中排在p与q之间，因此不可能相邻，只有Ⅲ不成立。

</details>

### 选择题5｜2022-04

<img src="../bank/2022/q04.png" alt="2022-04" style="display: block; width: 40.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

三叉树h=5最多(3⁵−1)/2=121个，不够244；h=6最多364个，故最小高度6。

</details>

### 选择题6｜2023-05

<img src="../bank/2023/q05.png" alt="2023-05" style="display: block; width: 46.81em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

后序末项a是根；右子树仅一个结点c，左子树后序f,d,b,e，其根e、右孩子b、左孩子d（d右孩子f）。先序根左右得a,e,d,f,b,c，选A。按树形分配后序片段，不能仅靠末两项猜结构。

</details>

### 选择题7｜2024-03

<img src="../bank/2024/q03.png" alt="2024-03" style="display: block; width: 47.45em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

p是v的中序前驱，v有左子树时p为左子树最右结点，因此p无右孩子；q为右子树最左结点，因此q无左孩子。

</details>

### 选择题8｜2025-03

<img src="../bank/2025/q03.png" alt="2025-03" style="display: block; width: 41.71em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

顺序存储要求每个存在结点的双亲也存在。按下标从1看，D第4个位置为−1，但第9个位置为19；9的双亲位置4不存在，无法构成树。其他选项的−1下方没有正值结点。数组中有空位本身不是错，空位下面还接孩子才是错。

</details>

### 选择题9｜2025-04

<img src="../bank/2025/q04.png" alt="2025-04" style="display: block; width: 24.1em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

任意森林可用左孩子右兄弟转换成二叉树。完全二叉树可有一个度1结点；一般二叉树分支数未必少于叶子；表达式树根通常是最后执行的运算。

</details>

### 选择题10｜2026-03

<img src="../bank/2026/q03.png" alt="2026-03" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

层序首项a为根，中序把树分成左侧b,e,d,f,c和右侧g。左子树层序先遇b，且b在该中序最左，故b没有左子树；随后c为b的右子树根，d为c的左子树根，e、f为d的左右孩子。后序为e,f,d,c,b,g,a，选C。

</details>

### 选择题11｜2026-04

<img src="../bank/2026/q04.png" alt="2026-04" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

五棵树的根在转换后二叉树里串成右链，第5棵树的根已在第5层，而每棵至少2结点，还需下一层，所以高度至少6。把结点数按7、5、4、3、2排列，各树选择较紧凑形态，其转换子树高度可分别为4、4、3、3、2；加上根链偏移后最大为6，所以下界可达到。

</details>

## 选择题组2｜0826 · 操作系统

[并发约束：把交错执行压成可证明的顺序](../src/0826.md) · 6道 · 首次。

### 选择题12｜2020-32

<img src="../bank/2020/q32.png" alt="2020-32" style="display: block; width: 44.88em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

Ⅰ保证互斥，Ⅱ对应空闲让进，Ⅲ对应有限等待，均应满足。Ⅳ“等待时立即让出CPU”是让权等待，忙等锁不会这样做，但仍可实现临界区互斥，因此不是所有互斥机制必须满足的条件。

</details>

### 选择题13｜2024-28

<img src="../bank/2024/q28.png" alt="2024-28" style="display: block; width: 45.97em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

同一进程内线程共享进程地址空间和打开文件资源，所以Ⅰ、Ⅲ成立。每个线程有自己的执行栈及寄存器现场，Ta、Tb不能把T的栈当作共同运行栈，Ⅱ不选。共享地址空间使线程可能通过指针访问另一线程栈中的对象，但不等于共享其线程栈资源。

</details>

### 选择题14｜2024-30

<img src="../bank/2024/q30.png" alt="2024-30" style="display: block; width: 46.03em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

P需要25/5=5个时间片，且初始排队尾。其他9个进程所需时间均不短于P，因此在P完成前，每一轮都还有10个进程参与。五轮各50ms，P在第5轮最后完成，周转时间5×50=250ms；不能只计算P自己的25ms。

</details>

### 选择题15｜2025-27

<img src="../bank/2025/q27.png" alt="2025-27" style="display: block; width: 37.09em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

最少页框要保证一条指令能完成：指令本身和各次间接寻址、操作数访问可能落在不同页，因而取决于指令系统支持的寻址方式。虚拟空间或物理空间总大小决定总体规模，代码段长度决定全部代码多少页，都不直接决定这条指令需要同时驻留的最少页数。

</details>

### 选择题16｜2026-26

<img src="../bank/2026/q26.png" alt="2026-26" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

S=−2表示2个在wait处阻塞；临界代码Q最多5个并发，当前已有5个获得许可，故m=5、n=2。这里的m指已进入Q尚未归还许可的在执行者，不是历史累计次数。

</details>

### 选择题17｜2026-27

<img src="../bank/2026/q27.png" alt="2026-27" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

要排除写冲突，既不能两边写同一数据，也不能一边读另一边正在写的数据，对应Ⅰ、Ⅱ、Ⅲ。两进程只读同一数据不会相互改变结果，Ⅳ无须成立。题目按读写集合独立性的Bernstein条件判断，不把“读集合必须互斥”额外加进去。

</details>

## 解答题

### 大题1｜2020-42

[原题单 0915｜树的递归含义：路径、编码、表达式与存储形态](../src/0915.md)

<img src="../bank/2020/q42.png" alt="2020-42" style="display: block; width: 46.16em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

（1）使用二叉前缀树。左、右边分别代表0、1，结点保留两个孩子指针和终止标记，叶结点保存对应字符。根到叶的边序列就是该字符的编码。

（2）从根依次读位并沿对应边走。抵达字符结点就输出字符、回到根，再读余下位。遇到空边或全部位读完时停在非根的内部结点，说明输入无效或末尾不完整。

（3）逐个插入码字。走的途中若遇到已标记终止的结点，已有短码是当前码的前缀。走完若当前结点已有孩子，当前码是先前长码的前缀；若该结点已标记，还要判重复。其余情况标记为终点并保存字符。两种插入顺序均检查到，遍历位数与码长之和同阶。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
