# Day 39｜数据结构＋操作系统

[← Day 38](day38.md) · [总入口](README.md) · [Day 40 →](day40.md)

**选择题：13道，来自两份完整src题单；大题：1道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：50—80分钟。** 选择题及核对约20—35分钟，大题约25—35分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0807 · 数据结构

[图上的推进：拓扑、最短路与关键路径](../src/0807.md) · 7道 · 复做第1次。

### 选择题1｜2020-07

<img src="../bank/2020/q07.png" alt="2020-07" style="display: block; width: 46.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：A（待逐题复核）。** 解析待补。

</details>

### 选择题2｜2020-08

<img src="../bank/2020/q08.png" alt="2020-08" style="display: block; width: 33.96em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题3｜2021-07

<img src="../bank/2021/q07.png" alt="2021-07" style="display: block; width: 33.92em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：A（待逐题复核）。** 解析待补。

</details>

### 选择题4｜2021-08

<img src="../bank/2021/q08.png" alt="2021-08" style="display: block; width: 46.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

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

各边权均为1，路径权重就是边数。BFS按距离一层层扩展，第一次到达顶点就得到最少边数路径。Prim、Kruskal最小化生成树所有边的总权，不保证树根到每个顶点的路最短；所有边等权时，任意生成树都是MST，更不能保证路径。

</details>

### 选择题7｜2026-07

<img src="../bank/2026/q07.png" alt="2026-07" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

无环时至多经过 n−1 条边，串长不会达到 n。可达且通往标记点的环能反复绕行。另取到某标记点的最短路，必不重复顶点，长度小于2n。

</details>

## 选择题组2｜0826 · 操作系统

[并发约束：把交错执行压成可证明的顺序](../src/0826.md) · 6道 · 复做第2次。

### 选择题8｜2020-32

<img src="../bank/2020/q32.png" alt="2020-32" style="display: block; width: 44.88em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

Ⅰ保证互斥，Ⅱ对应空闲让进，Ⅲ对应有限等待，均应满足。Ⅳ“等待时立即让出CPU”是让权等待，忙等锁不会这样做，但仍可实现临界区互斥，因此不是所有互斥机制必须满足的条件。

</details>

### 选择题9｜2024-28

<img src="../bank/2024/q28.png" alt="2024-28" style="display: block; width: 45.97em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

同一进程内线程共享进程地址空间和打开文件资源，所以Ⅰ、Ⅲ成立。每个线程有自己的执行栈及寄存器现场，Ta、Tb不能把T的栈当作共同运行栈，Ⅱ不选。共享地址空间使线程可能通过指针访问另一线程栈中的对象，但不等于共享其线程栈资源。

</details>

### 选择题10｜2024-30

<img src="../bank/2024/q30.png" alt="2024-30" style="display: block; width: 46.03em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

P需要25/5=5个时间片，且初始排队尾。其他9个进程所需时间均不短于P，因此在P完成前，每一轮都还有10个进程参与。五轮各50ms，P在第5轮最后完成，周转时间5×50=250ms；不能只计算P自己的25ms。

</details>

### 选择题11｜2025-27

<img src="../bank/2025/q27.png" alt="2025-27" style="display: block; width: 37.09em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

最少页框要保证一条指令能完成：指令本身和各次间接寻址、操作数访问可能落在不同页，因而取决于指令系统支持的寻址方式。虚拟空间或物理空间总大小决定总体规模，代码段长度决定全部代码多少页，都不直接决定这条指令需要同时驻留的最少页数。

</details>

### 选择题12｜2026-26

<img src="../bank/2026/q26.png" alt="2026-26" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

S=−2表示2个在wait处阻塞；临界代码Q最多5个并发，当前已有5个获得许可，故m=5、n=2。这里的m指已进入Q尚未归还许可的在执行者，不是历史累计次数。

</details>

### 选择题13｜2026-27

<img src="../bank/2026/q27.png" alt="2026-27" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

要排除写冲突，既不能两边写同一数据，也不能一边读另一边正在写的数据，对应Ⅰ、Ⅱ、Ⅲ。两进程只读同一数据不会相互改变结果，Ⅳ无须成立。题目按读写集合独立性的Bernstein条件判断，不把“读集合必须互斥”额外加进去。

</details>

## 解答题

### 大题1｜2021-47

[原题单 1002｜网络服务：配置、地址转换与应用会话](../src/1002.md)

<img src="../bank/2021/q47.png" alt="2021-47" style="display: block; width: 46.72em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

（1）HTTP之外的应用层协议是DNS。本题常规DNS查询由DNS→UDP→IP→以太网逐层封装。ARP提供地址解析，不能混写成DNS的应用层承载协议。

（2）H1先ARP查询本地域名服务器MAC，完成DNS查询后，再ARP查询默认网关MAC，并通过网关建立TCP连接、发HTTP请求。到t1，S已学到：

| MAC地址 | 端口 |
|---|---:|
| 00-11-22-33-44-cc（H1） | 4 |
| 00-11-22-33-44-bb（DNS） | 1 |
| 00-11-22-33-44-aa（R） | 2 |

H2未发送帧，因此没有H2→端口3的表项。

（3）H2至少收到2个ARP请求广播帧：H1查DNS、H1查网关，目的MAC均为FF-FF-FF-FF-FF-FF。ARP应答已使DNS与网关的MAC被学习，DNS、TCP、HTTP后续单播不会再因为目的MAC未知而泛洪到H2。此处依题设没有无关通信，且H1的ARP表初始为空。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
