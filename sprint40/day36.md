# Day 36｜组成原理＋计算机网络

[← Day 35](day35.md) · [总入口](README.md) · [Day 37 →](day37.md)

**选择题：12道，来自两份完整src题单；大题：2道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：65—105分钟。** 选择题及核对约20—40分钟，大题约40—55分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0817 · 组成原理

[指令取数：格式、寻址与有效地址](../src/0817.md) · 4道 · 复做第1次。

### 选择题1｜2020-16

<img src="../bank/2020/q16.png" alt="2020-16" style="display: block; width: 52.32em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：A（待逐题复核）。** 解析待补。

</details>

### 选择题2｜2022-19

<img src="../bank/2022/q19.png" alt="2022-19" style="display: block; width: 47.12em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题3｜2023-17

<img src="../bank/2023/q17.png" alt="2023-17" style="display: block; width: 46.81em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

**直接法：** 由寻址方式决定寄存器保存的是数据还是地址；寄存器编号只定位哪个寄存器，内容本身不能说明应如何解释。

</details>

### 选择题4｜2026-17

<img src="../bank/2026/q17.png" alt="2026-17" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案与解析待补。**

</details>

## 选择题组2｜0904 · 计算机网络

[局域网转发：介质竞争、MAC与交换机](../src/0904.md) · 8道 · 复做第2次。

### 选择题5｜2020-35

<img src="../bank/2020/q35.png" alt="2020-35" style="display: block; width: 40.92em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

**直接法：** 四个集线器各连到交换机独立端口，形成4个共享冲突域；中间路由器把左右分成2个广播域。按题目的统计口径，交换机与路由器间的点到点全双工链路不计为共享冲突域。

</details>

### 选择题6｜2020-37

<img src="../bank/2020/q37.png" alt="2020-37" style="display: block; width: 48.67em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：A（待逐题复核）。** 解析待补。

</details>

### 选择题7｜2022-37

<img src="../bank/2022/q37.png" alt="2022-37" style="display: block; width: 45.92em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

**直接法：** 控制平面向数据平面下发流表用南向接口；北向连接应用与控制器。

</details>

### 选择题8｜2023-36

<img src="../bank/2023/q36.png" alt="2023-36" style="display: block; width: 46.92em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题9｜2024-35

<img src="../bank/2024/q35.png" alt="2024-35" style="display: block; width: 45.97em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

**直接法：** H4在VLAN1，能ARP解析同广播域的H1、H2、H3；H6在VLAN3，其MAC不会通过普通跨VLAN ARP出现在H4表。IP看似同网段也不能越过VLAN广播隔离。

</details>

### 选择题10｜2024-36

<img src="../bank/2024/q36.png" alt="2024-36" style="display: block; width: 46.07em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题11｜2025-35

<img src="../bank/2025/q35.png" alt="2025-35" style="display: block; width: 42.32em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题12｜2026-36

<img src="../bank/2026/q36.png" alt="2026-36" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案与解析待补。**

</details>

## 解答题

### 大题1｜2024-47

[原题单 0929｜寻址与路由：从前缀匹配到路由协议收敛](../src/0929.md)

<img src="../bank/2024/q47.png" alt="2024-47" style="display: block; width: 48.0em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

（1）AS4选OSPF。RIP以16为不可达，不能支持题设可能超过20台路由器的路径。

（2）AS3最多经过15台路由器，每次转发TTL减1，要到目的主机时仍可交付，初始TTL至少16。

（3）初始向量在起始时刻立即交换，此后每30s一轮。210.2.3.0/24直连R14，t=0时R11、R15得知，t=30s时R12、R13、R16得知，全网至少30s。210.2.4.0/24直连R16，t=0时R13、R15得知，t=30s时R12、R14得知，t=60s时最远的R11得知，全网至少60s。不能把“初次立即交换”再额外记为30s。

（4）R44→R13为外部BGP（eBGP）会话，用UPDATE报文通告；R13向同一AS中的R14、R15通过内部BGP（iBGP）会话传播可达性。

（5）先比AS_PATH长度，R11与R13通告的路径均为3个AS，R12通告为4个AS，先排除R12。在题设无其他策略差异时，比较到出口的内部开销。R14到R11一跳，到R13两跳，选R11；R15到R13一跳，到R11两跳，选R13。先选外部路径属性，再用内部距离打破平局，不能一开始只看出口离自己多近。

</details>

### 大题2｜2023-47

[原题单 0930｜传输窗口：序号空间、确认与超时共同推进](../src/0930.md)

<img src="../bank/2023/q47.png" alt="2023-47" style="display: block; width: 46.92em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

（1）FTP控制连接在整个会话期间保持，属于持续连接；数据连接用于本次文件传输，传完关闭，属于非持续连接。登录时建立的是控制连接。

（2）数据连接初始序号100，SYN占一个序号，文件首字节序号为101。18000B传完后下一字节序号18101，H的FIN又占一个序号；服务器对H的FIN发出的第二次挥手ACK，确认号为18102。

（3）原题只给慢开始门限。按这道题参考解采用的初始 cwnd=1MSS 推算。ACK1101确认第1段，窗口增为2MSS；随后ACK2101确认第2段，仍处慢开始，增为3MSS，即3000B。第一轮1段、第二轮2段后窗口达到门限4MSS。第三轮确认完第4—7段（ACK7101）后，按题目常用拥塞避免模型增为5MSS，即5000B。

（4）忽略发送时延，RTT=10ms，收到SYN+ACK后即可携带第三次握手ACK开始发数据：

| 从请求建连起 | 本轮发送段数 | 累计发送段数 |
|---|---:|---:|
| 10ms | 1 | 1 |
| 20ms | 2 | 3 |
| 30ms | 4 | 7 |
| 40ms | 5 | 12 |
| 50ms | 6 | 18 |
| 60ms | 收到最后一批确认 | 18 |

因此从请求建连到确认文件全部收到至少60ms，平均应用数据速率18000B/0.06s=300000B/s=2.4Mb/s。题目截止到文件确认，不再加断开连接耗时，也不能把FTP早已完成的登录再算一遍。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
