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

<details>
<summary>答案与解析</summary>

**解析待补。**

</details>

### 大题2｜2023-44

[原题单 0919｜表示到汇编：同一位模式在类型、指令与调用中怎样解释](../src/0919.md)

<img src="../bank/2023/q44.png" alt="2023-44" style="display: block; width: 47.0em; max-width: 100%; height: auto; margin: 12px 0;">

本题沿用本日43题的题干。

<details>
<summary>答案与解析</summary>

**解析待补。**

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
