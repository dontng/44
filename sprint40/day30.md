# Day 30｜组成原理＋计算机网络

[← Day 29](day29.md) · [总入口](README.md) · [Day 31 →](day31.md)

**选择题：10道，来自两份完整src题单；大题：2道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：65—95分钟。** 选择题及核对约20—30分钟，大题约40—55分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0814 · 组成原理

[存储器拼装：容量、长宽与片选](../src/0814.md) · 4道 · 复做第1次。

### 选择题1｜2021-15

<img src="../bank/2021/q15.png" alt="2021-15" style="display: block; width: 52.24em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

原题按字编址，每个地址对应32位。000000H—3FFFFFH 共4M个字地址。先用4片512K×8位芯片并联，组成512K×32位；再用8组扩为4M×32位，共32片。也可用总容量复核：4M个字×4B=16MiB，除以每片512KiB，仍为32片。

</details>

### 选择题2｜2022-17

<img src="../bank/2022/q17.png" alt="2022-17" style="display: block; width: 45.85em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

一片容量8192×8192×8位=64MiB，8片共512MiB；8片各给8位，合成64位突发传输。DRAM行列地址复用，8192=2¹³，地址引脚只需13根，不是把行、列相加成26根。行缓冲保存一整行，确为8192×8位。

</details>

### 选择题3｜2023-15

<img src="../bank/2023/q15.png" alt="2023-15" style="display: block; width: 46.85em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

30 位字节地址共有 2^30 B，合法地址为 00000000H—3FFFFFFFH。ROM 占四分之一，即 2^28 B，位于最高的四分之一区域，所以范围为 30000000H—3FFFFFFFH。上端点是总容量减1，不是40000000H。

</details>

### 选择题4｜2026-15

<img src="../bank/2026/q15.png" alt="2026-15" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

8片芯片、每片8位、总线64位，每次读取连续8字节组成一个64位字；按本题低位交叉编址，字节地址最低3位标识芯片。0018001DH 的低3位是101（芯片5）。A的000001D5H也以101结尾；B、C、D分别对应0、7、4，故选A。

</details>

## 选择题组2｜0901 · 计算机网络

[分层路径：数据穿过网络时每层做什么](../src/0901.md) · 6道 · 复做第1次。

### 选择题5｜2020-33

<img src="../bank/2020/q33.png" alt="2020-33" style="display: block; width: 42.42em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

图只展示消息发送、接收的先后顺序，描述协议的时序，因此只选III。

语法说明消息格式，语义说明字段含义和应做的动作，图中都没给出。看到消息箭头不能把语法、语义一起选上。

</details>

### 选择题6｜2021-33

<img src="../bank/2021/q33.png" alt="2021-33" style="display: block; width: 33.72em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

TCP/IP中传输层的下一层是网络层，路由选择是网络层功能。

A对话管理对应OSI会话层；C端到端报文段传输属于传输层自身；D结点到结点流控属于链路层。题目问“下一层”，不要直接选传输层的功能。

</details>

### 选择题7｜2023-33

<img src="../bank/2023/q33.png" alt="2023-33" style="display: block; width: 42.15em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

1000B分组在100Mb/s链路发送一次需80μs；每段传播时延=1000bit÷100Mb/s=10μs。1MB文件分1000组，经过两段等速、存储转发链路，总时间=(1000+1)×80μs+2×10μs=80.10ms。

A的80.02ms只算了文件在首链路的发送和两段传播，漏掉最后一组在第二段链路的发送。不能把整份文件的发送时间乘2，因为两段可流水传输。

</details>

### 选择题8｜2024-33

<img src="../bank/2024/q33.png" alt="2024-33" style="display: block; width: 42.47em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

无论选上方还是下方路径，H1、H2各自接入链路都只有10Mb/s，端到端吞吐量不可能超过10Mb/s；存在中间带宽足够的路径，所以最大值就是10Mb/s。

A的1Mb/s只是一条可绕开的直连链路；C、D只看了中间链路，忽略两端瓶颈。

</details>

### 选择题9｜2025-33

<img src="../bank/2025/q33.png" alt="2025-33" style="display: block; width: 42.55em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

文件发送量为16Mbit。电路交换用1.6s+32μs；报文交换逐链路整份存转，用1.6+0.16+0.016=1.776s；分组交换可流水，最后一组额外经过后两段需400×8/100Mb/s+400×8/1000Mb/s=35.2μs，即1.6s+35.2μs。因此Tms>Tps>Tcs。

分组虽比整份报文存转快，但本题电路建立只需32μs，小于分组尾部的35.2μs，不能凭“分组效率高”认定分组一定最快。共同传播时延不影响三者比较。

</details>

### 选择题10｜2026-33

<img src="../bank/2026/q33.png" alt="2026-33" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

分层方便接口标准化、各层独立演化，并降低设计实现复杂度；层数更多会引入额外接口和处理开销，不保证效率更高，所以B错误。

A、C、D都是分层的设计收益。设计更容易与运行更高效，是两个不同判断。

</details>

## 解答题

### 大题1｜2026-45

[原题单 0925｜并发同步：PV 操作大题](../src/0925.md)

<img src="../bank/2026/q45.png" alt="2026-45" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

（1）CPU占用时间线（ms）：10–20 P2，20–70 P4，70–80 P2，80–90 P4，90–140 P1，140–180 P3，180–225 P1。

P4在14ms到达但到20ms才能抢占。70ms时P4用完50ms时间片，优先级从5降至4，先前已入队的同优先级P2先执行。140ms时P1用完时间片，优先级从3降为2，较早入队的P3先执行。P1、P3、P4首次运行分别为90、140、20ms。从10到220ms共22次时钟中断，实际选进程的调度为7次（从首次选择算至全部完成，不计结束后选空闲进程）。

（2）时间片100ms时，P4和P1均无需因用完时间片重新入队，调度次数减少。时钟间隔改为1ms，单位时间内处理的时钟中断增多，系统开销增加。

</details>

### 大题2｜2020-46

[原题单 0926｜页面驻留：分配、置换与缺页过程](../src/0926.md)

<img src="../bank/2020/q46.png" alt="2020-46" style="display: block; width: 50.16em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

（1）虚址1080 0000H+(1024+2)×4=1080 1008H。页目录号42H，二级页号001H，偏移008H。目录项物理地址0020 1000H+42H×4=0020 1108H。二级页表的页框号00301H左移12位得0030 1000H，再加001H×4，表项物理地址为0030 1004H。

（2）数组的虚址区间连续。相邻虚页可映到任意不相邻的物理页框，请求分页下也可暂不驻留。

（3）按行遍历局部性更好，相邻元素差4B，整行4096B恰好一页。按列访问步长是4096B，每次跨到另一页。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
