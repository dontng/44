# Day 20｜组成原理＋计算机网络

[← Day 19](day19.md) · [总入口](README.md) · [Day 21 →](day21.md)

**选择题：12道，来自两份完整src题单；大题：2道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：75—115分钟。** 选择题及核对约30—50分钟，大题约40—55分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0821 · 组成原理

[性能方程：时间由多少工作和每步多慢共同决定](../src/0821.md) · 4道 · 首次。

### 选择题1｜2021-12

<img src="../bank/2021/q12.png" alt="2021-12" style="display: block; width: 46.64em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

P是十进制10¹⁵，93.0146PFLOPS约为9.3×10¹⁶次浮点运算/秒，也就是9.3亿亿次。A、B少了数量级；C的“千万亿”为10¹⁵，也少10倍。FLOPS是浮点运算次数，不是指令条数或时钟周期数。

</details>

### 选择题2｜2022-12

<img src="../bank/2022/q12.png" alt="2022-12" style="display: block; width: 47.72em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

平均 CPI=0.8×1+0.2×10=2.8。10000条需28000周期，1GHz下每周期1ns，共28μs。

</details>

### 选择题3｜2023-12

<img src="../bank/2023/q12.png" alt="2023-12" style="display: block; width: 46.81em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

每条指令平均1.2周期，所以指令速度1.5GHz/1.2=1.25GIPS。总周期5×10⁵×1.2=6×10⁵，执行时间6×10⁵/(1.5×10⁹)=4×10⁻⁴s=0.4ms。CPI要除进指令速率、乘进总周期；0.4μs会少算1000倍。

</details>

### 选择题4｜2025-18

<img src="../bank/2025/q18.png" alt="2025-18" style="display: block; width: 30.55em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

Cache缺失可使流水或访存停顿，平均CPI因增加的周期而上升。单周期和流水线时钟分别受最慢指令、最慢段约束。

</details>

## 选择题组2｜0904 · 计算机网络

[局域网转发：介质竞争、MAC与交换机](../src/0904.md) · 8道 · 复做第1次。

### 选择题5｜2020-35

<img src="../bank/2020/q35.png" alt="2020-35" style="display: block; width: 40.92em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

四个集线器各连到交换机独立端口，形成4个共享冲突域；中间路由器把左右分成2个广播域。按题目的统计口径，交换机与路由器间的点到点全双工链路不计为共享冲突域。

</details>

### 选择题6｜2020-37

<img src="../bank/2020/q37.png" alt="2020-37" style="display: block; width: 48.67em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

发送RTS前需按竞争接入等待DIFS；收到RTS回CTS、收到CTS发DATA、收到DATA回ACK，均等待较短的SIFS。故IFS1最长。后续三个短间隔用于让已取得信道的交换连续完成，不重新与其他站争用。

</details>

### 选择题7｜2022-37

<img src="../bank/2022/q37.png" alt="2022-37" style="display: block; width: 45.92em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

控制平面向数据平面下发流表用南向接口；北向连接应用与控制器。

</details>

### 选择题8｜2023-36

<img src="../bank/2023/q36.png" alt="2023-36" style="display: block; width: 46.92em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

第4次冲突后，退避随机数从0～2⁴−1即0～15中选，最大等待15×51.2μs=768μs。不是等待4个时隙，也不能取16；上界2⁴不包含在可选范围内。

</details>

### 选择题9｜2024-35

<img src="../bank/2024/q35.png" alt="2024-35" style="display: block; width: 45.97em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

H4在VLAN1，能ARP解析同广播域的H1、H2、H3；H6在VLAN3，其MAC不会通过普通跨VLAN ARP出现在H4表。IP看似同网段也不能越过VLAN广播隔离。

</details>

### 选择题10｜2024-36

<img src="../bank/2024/q36.png" alt="2024-36" style="display: block; width: 46.07em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

B收到CTS后，尚需等待SIFS、DATA、SIFS、ACK。DATA发送时延1998×8/54=296μs，因此NAV=28+296+28+2=354μs。RTS、CTS此前已发完，不再计入；DIFS是最初争用信道前的等待，也不在这段预约剩余时间中。

</details>

### 选择题11｜2025-35

<img src="../bank/2025/q35.png" alt="2025-35" style="display: block; width: 42.32em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

本题按10BaseT的51.2μs争用时隙计算。第11次冲突时退避指数截断为10，最大随机数2¹⁰−1=1023，最大退避1023×51.2μs=52.3776ms。不能继续取2¹¹−1。题图BaseT前的速率数字缺失，以上口径由选项对应10Mb/s确定；若是100Mb/s，时隙与结果都会缩为十分之一。

</details>

### 选择题12｜2026-36

<img src="../bank/2026/q36.png" alt="2026-36" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

H3与H1、H2同属VLAN1，所以能收到H1发给自己的单播F1，以及H2发出的本VLAN广播F3。H5发出的F2虽目的MAC是H3，却来自VLAN2，交换机不会跨VLAN转发；H6的广播F4也只能留在VLAN2。广播域边界先于目的地址判断。

</details>

## 解答题

### 大题1｜2023-43

[原题单 0923｜Cache 局部性：地址映射、访问序列与缺失代价](../src/0923.md)

<img src="../bank/2023/q43.png" alt="2023-43" style="display: block; width: 47.0em; max-width: 100%; height: auto; margin: 12px 0;">

**题面勘误：** 本题图及仓内PDF把声明写成`int a[24][24]`，但内层循环为`j<64`，与第44题的行偏移计算也矛盾。本页按`int a[24][64]`讲解；若照24列执行会数组越界，不能据此使用下面的数值答案。

<details>
<summary>答案与解析</summary>

（1）按题图下的声明勘误，以24×64个int计算。数组大小24×64×4=6144B，从00422000H开始，覆盖00422000H～004237FFH，共2页。两页初始均未驻留，且不置换，所以缺页2次，故障虚拟地址分别为00422000H（a[0][0]）、00423000H（a[16][0]）。不要把Cache首次缺失192次与缺页2次混为一谈。

（2）不计i、j，原循环每个数组元素只写一次，同一数据没有短期重复使用，故不具有数据访问的时间局部性；连续访问相邻元素体现的是空间局部性。

（3）块大小32B，块内地址用A4～A0。Cache有8192/(32×4)=64组，组号用A10～A5；这些位都在12位页内偏移内，地址转换前后不变，可以从虚拟地址直接取。a[1][0]地址00422000H+64×4=00422100H，组号(00422100H÷32) mod 64=8。

（4）共6144/32=192个主存块，每块8个int。按题目采用的写分配模型，首次写块时调入，随后7次命中，按行访问命中率7/8=87.5%。

交换循环后，相邻两行相差256B，即8个Cache组；24行在同一列映射到8个组，每组仅3块，小于4路容量，不会互相挤出。列0把24个块调入后，列1～7访问的仍是这些块；每8列重复一次，仍只有192次首次缺失，命中率也是87.5%。本题不能只凭“按列”就判定每次不命中；若采用非写分配策略，这个写入命中率结论需另算。

</details>

### 大题2｜2023-44

[原题单 0919｜表示到汇编：同一位模式在类型、指令与调用中怎样解释](../src/0919.md)

<img src="../bank/2023/q44.png" alt="2023-44" style="display: block; width: 47.0em; max-width: 100%; height: auto; margin: 12px 0;">

本题沿用本日43题的题干。

<details>
<summary>答案与解析</summary>

（1）第19条机器码共11B：C7、84、82、00、20、42、00、0A、00、00、00。因此第20条地址为004010AEH+0BH=004010B9H，不按32位字长给每条指令固定加4。

（2）两条跳转都采用相对寻址，位移相对下一条指令地址。第2条长2B，下一地址0040107BH，加有符号位移09H，得到00401084H；第7条同理，0040108AH+32H=004010BCH。题面汇编虽写完整目标地址，机器码保存的仍是相对位移。

（3）源操作数0AH直接在指令内，属于立即寻址；方括号里的表达式是目的操作数地址。按a[i][j]地址=首址+i×64×4+j×4，edx既然保存j，ecx就保存i×256，即i这一行的字节偏移。

位移00422000H在机器码中依低地址排列为00、20、42、00，立即数0000000AH为0A、00、00、00，故采用小端方式。不能把指令的操作码字节与多字节操作数字段的端序混算。

（4）第一次取第19条不会缺页。第1条00401072H和第19条004010AEH都在虚页00401H内；执行到第19条前，程序页已因前面的取指而驻留，题设又说明不发生页面置换。执行该条的数组写入可能触发数据页缺页，与取指是否缺页是两件事。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
