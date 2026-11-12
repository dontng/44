# Day 15｜数据结构＋操作系统

[← Day 14](day14.md) · [总入口](README.md) · [Day 16 →](day16.md)

**选择题：10道，来自两份完整src题单；大题：2道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：75—115分钟。** 选择题及核对约30—50分钟，大题约40—55分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0807 · 数据结构

[图上的推进：拓扑、最短路与关键路径](../src/0807.md) · 7道 · 首次。

### 选择题1｜2020-07

<img src="../bank/2020/q07.png" alt="2020-07" style="display: block; width: 46.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

Kruskal按全图边权从小到大选且不成环：先bf=5、bd=6；df=7会与前两边成环，跳过；再ae=9、ce=10、be=11，六顶点共取5边即结束。对应A；B先选11再选9、10，已违背算法选边次序。

</details>

### 选择题2｜2020-08

<img src="../bank/2020/q08.png" alt="2020-08" style="display: block; width: 33.96em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

关键路径是源到汇路径中持续时间总和最长的路径，决定工程最短工期。边数多不代表耗时最长，A错；延长关键活动会推迟工期，C错；若有多条关键路径，只缩短一条上的活动，另一条仍可能限制工期，D并非必然成立。

</details>

### 选择题3｜2021-07

<img src="../bank/2021/q07.png" alt="2021-07" style="display: block; width: 33.92em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

图中存在完整先后约束链A→B→C→D→E→F，已把六个顶点的次序全部固定。额外的A→F、B→D等边不会增加可选次序，因此只有ABCDEF一种。不要因图上有多条路径就认为拓扑序也有多种。

</details>

### 选择题4｜2021-08

<img src="../bank/2021/q08.png" alt="2021-08" style="display: block; width: 46.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

初始dist按2、3、4、5为[26,3,∞,6]。先确定顶点3，利用3→2权22把26改为25；再确定顶点5，利用5→2权15改为21，5→4权8得到14。第二次确定并松弛后为[21,3,14,6]。顶点4尚未确定，不能提前用4→2把21改到15。

</details>

### 选择题5｜2022-07

<img src="../bank/2022/q07.png" alt="2022-07" style="display: block; width: 47.72em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

事件1～6的最早时刻为0、2、5、8、9、12，最迟为0、4、5、8、11、12。用终点最迟减时长再减起点最早，c、g、h、j 的余量是2、6、2、2。

</details>

### 选择题6｜2023-06

<img src="../bank/2023/q06.png" alt="2023-06" style="display: block; width: 46.88em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

* **核心判据**：最小生成树（MST）与单源最短路径（SPT）的目标泛函根本差异：
  * **生成树目标**：最小化全图所有边的**总权值和**（$\min \sum_{e \in T} w(e)$），它对特定源点到各顶点的单条路径长度没有任何保证；
  * **等权图的特殊性质**：当全图所有边权值均为 1 时，任意一棵包含 $|V|-1$ 条边的生成树其总权值均为 $|V|-1$。这意味着**原图中的任意生成树都是最小生成树**！显然，随意挑选的一棵生成树根本无法保证源点到目标顶点的路径长度最短；
  * **BFS 的最短路径特性**：广度优先搜索依赖 FIFO 队列推进，每次按边数层次递增。当边权全为 1 时，路径权值和即为边数，顶点**首次被访问出队时的路径必然是边数最少的最短路径**。
* **正选推导**：
  * 在所有边权均为 1 的图中：
    * 路径权值等于路径所含边数；
    * BFS 算法从源点出发，距离为 1 的顶点最先入队并访问，接着是距离为 2 的顶点……满足单调性与无权最短路径充要条件，时间复杂度为最优的 $O(|V|+|E|)$，III 必然正确。选 B。
* **干扰项击穿**：
  * **反例击穿 Prim 与 Kruskal（I、II 错误）**：
    * 构造 4 个顶点构成的环形加弦图：顶点 $A, B, C, D$，边为 $(A, B), (B, C), (C, D), (D, A)$ 以及直连对角弦 $(A, C)$，所有边权均为 1；
    * 求从源点 $A$ 到 $C$ 的最短路径：原图中直连边 $(A, C)$ 长度为 1；
    * 运行 Prim 或 Kruskal 算法时，由于所有边权均为 1，选边完全由遍历顺序决定。若算法选择生成树边为 $(A, B), (B, C), (C, D)$（总权值为 3，是一棵合法的最小生成树）；
    * 此时在生成树上，从 $A$ 到 $C$ 的唯一路径是 $A \to B \to C$，路径权值为 2 $\ne$ 最短距离 1！
    * 证明 MST 树上路径不能保证为原图单源最短路径。

</details>

### 选择题7｜2026-07

<img src="../bank/2026/q07.png" alt="2026-07" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

无环时至多经过 n−1 条边，串长不会达到 n。可达且通往标记点的环能反复绕行。另取到某标记点的最短路，必不重复顶点，长度小于2n。

</details>

## 选择题组2｜0827 · 操作系统

[资源闭环：死锁、避免与检测](../src/0827.md) · 3道 · 首次。

### 选择题8｜2020-27

<img src="../bank/2020/q27.png" alt="2020-27" style="display: block; width: 39.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

剩余资源为(6−5,6−6)=(1,0)。P1还需(2,1)，P2还需(1,0)，P3还需(2,2)，只能先让P2完成；回收后可用(3,1)，此时P1可完成而P3仍缺B。再回收P1后P3才能完成，安全序列P2、P1、P3。

</details>

### 选择题9｜2021-31

<img src="../bank/2021/q31.png" alt="2021-31" style="display: block; width: 46.8em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

最坏每个进程各占1个资源，再各等第2个，n个资源就会全部被占住而无法推进。多给1个，必有进程能取得第2个、完成并释放，再让其他进程依次完成，因此最少n+1。2n是让全部进程同时满足需求的数量，保证无死锁不需要这么多。

</details>

### 选择题10｜2022-26

<img src="../bank/2022/q26.png" alt="2022-26" style="display: block; width: 45.92em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

Available=(1,3,2)，起初只有P0可完成；释放(2,0,1)后Work=(3,3,3)，P1、P2任意顺序皆可。因此P0P1P2、P0P2P1，共2种。

</details>

## 解答题

### 大题1｜2024-43

[原题单 0920｜指令落到数据通路：寄存器、部件与控制信号协同](../src/0920.md)

<img src="../bank/2024/q43.png" alt="2024-43" style="display: block; width: 46.07em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

（1）寄存器编号5位，最多32个。32位字合法左移量为0～31，故 shamt 为5位。

（2）add 取寄存器B，ALUBsrc=0。完整和为 1 1FDB 9753H，32位 F=1FDB 9753H。两个最高位均为1的补码相加得到正数，OF=1。最高位向外进位，CF=1。无符号加法用 CF 判断溢出。

（3）slli 的 IR[31:25] 全为0，扩展输入最高位为0。零扩展与符号扩展都补0，所以Ext任取。

（4）lw 的 imm 是补码位移，Ext=1。有效地址做加法，ALUctr=000，同时 ALUBsrc=1。

（5）A040 A103H 的低7位是0000011，且位14～12为010，与表内 lw 相符。rs1=01H，imm=A04H，符号扩展为 FFFF FA04H（−1532）。地址是 FFFF A2D0H−05FCH=FFFF 9CD4H。

</details>

### 大题2｜2024-44

[原题单 0919｜表示到汇编：同一位模式在类型、指令与调用中怎样解释](../src/0919.md)

<img src="../bank/2024/q44.png" alt="2024-44" style="display: block; width: 46.03em; max-width: 100%; height: auto; margin: 12px 0;">

本题沿用本日43题的题干。

<details>
<summary>答案与解析</summary>

（1）r2 保存 i，左移2得到4i。r3 保存 a 的首址。最后一条把 r5 加回 r1，所以 r1 保存 sum。所求依次为03H、02H、01H。

（2）a[5] 地址=0013 DFF0H+5×4=0013 E004H。四字节按低址到高址是 DC、EC、FF、FF，小端拼成 FFFF ECDCH。sum 机器数为 0000 1332H+FFFF ECDCH 的低32位，即 0000 000EH。4KiB页的页号为0013EH。数组起点在0013DH页，已访问的元素在0013EH页，所以至少占2页。

（3）slli 的高7位为0，shamt=2，rs1=2，位14～12为010，rd=4，低7位0010011，机器码0021 2213H。按题目的2B short，偏移改为2i，故写 slli r4, r2, 1。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
