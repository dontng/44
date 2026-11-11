# Day 37｜数据结构＋操作系统

[← Day 36](day36.md) · [总入口](README.md) · [Day 38 →](day38.md)

**选择题：19道，来自两份完整src题单；大题：1道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：60—95分钟。** 选择题及核对约30—50分钟，大题约25—35分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0806 · 数据结构

[图的骨架：表示、遍历与连通](../src/0806.md) · 6道 · 复做第1次。

### 选择题1｜2020-06

<img src="../bank/2020/q06.png" alt="2020-06" style="display: block; width: 46.44em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题2｜2022-06

<img src="../bank/2022/q06.png" alt="2022-06" style="display: block; width: 29.68em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

**直接法：** 连通图有生成树，至少有 |V|−1 条边。边数达到下界仍可能不连通，例如三角形加一个孤点。

</details>

### 选择题3｜2023-06

<img src="../bank/2023/q06.png" alt="2023-06" style="display: block; width: 46.88em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题4｜2024-04

<img src="../bank/2024/q04.png" alt="2024-04" style="display: block; width: 43.57em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

**直接法：** b 关联 (0,1)、(1,3) 两条边；d 关联 (0,3)、(1,3)、(3,2)、(4,3) 四条边。追踪每条边时按所求端点位于 i 还是 j，选对应的链接。

</details>

### 选择题5｜2025-06

<img src="../bank/2025/q06.png" alt="2025-06" style="display: block; width: 29.87em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题6｜2026-06

<img src="../bank/2026/q06.png" alt="2026-06" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案与解析待补。**

</details>

## 选择题组2｜0825 · 操作系统

[执行生命线：进程、线程、状态与调度](../src/0825.md) · 13道 · 复做第2次。

### 选择题7｜2020-26

<img src="../bank/2020/q26.png" alt="2020-26" style="display: block; width: 46.75em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题8｜2020-29

<img src="../bank/2020/q29.png" alt="2020-29" style="display: block; width: 30.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题9｜2021-24

<img src="../bank/2021/q24.png" alt="2021-24" style="display: block; width: 44.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题10｜2021-25

<img src="../bank/2021/q25.png" alt="2021-25" style="display: block; width: 44.96em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

**直接法：** 时间片轮转需PCB记录上下文、时钟中断计时、就绪队列轮换；不因采用轮转就必须用阻塞队列，选I、II、III。

</details>

### 选择题11｜2021-27

<img src="../bank/2021/q27.png" alt="2021-27" style="display: block; width: 45.28em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题12｜2022-23

<img src="../bank/2022/q23.png" alt="2022-23" style="display: block; width: 40.0em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题13｜2022-25

<img src="../bank/2022/q25.png" alt="2022-25" style="display: block; width: 47.8em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题14｜2022-28

<img src="../bank/2022/q28.png" alt="2022-28" style="display: block; width: 42.96em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

**直接法：** 读文件、申请外设和P操作都可能等待而阻塞；时间片用完转就绪，不转阻塞。选I、III、IV。

</details>

### 选择题15｜2023-27

<img src="../bank/2023/q27.png" alt="2023-27" style="display: block; width: 43.96em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题16｜2023-29

<img src="../bank/2023/q29.png" alt="2023-29" style="display: block; width: 48.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题17｜2024-24

<img src="../bank/2024/q24.png" alt="2024-24" style="display: block; width: 32.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：A（待逐题复核）。** 解析待补。

</details>

### 选择题18｜2025-25

<img src="../bank/2025/q25.png" alt="2025-25" style="display: block; width: 42.61em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：C（待逐题复核）。** 解析待补。

</details>

### 选择题19｜2026-25

<img src="../bank/2026/q25.png" alt="2026-25" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案与解析待补。**

</details>

## 解答题

### 大题1｜2026-47

[原题单 0930｜传输窗口：序号空间、确认与超时共同推进](../src/0930.md)

<img src="../bank/2026/q47.png" alt="2026-47" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

（1）三次握手。C发出的SYN占用序号1000，服务器的SYN+ACK确认号为1001。

（2）ack_seq=2001已累计确认1000B，即两个500B段。按本题参考解采用的初始窗口1MSS以及题干给出的每段ACK条件，cwnd增至3MSS=1500B。发送窗口取 min(1500,1000)=1000B。窗口大小与扣掉在途数据后当前还能新发的字节数是两回事。

（3）按题目采用的客户端主动关闭、双方分别发送FIN的常规流程，四次挥手。C发送完文件后，下一个序号为3001，FIN占用这个序号，所以服务端对它确认3002。服务端未发送数据，C 收到的最后一段为服务端 FIN+ACK，seq=2001、ack_seq=3002、FIN=1。

（4）建连到可发首段1RTT。数据受窗口限制，三轮发1、2、1段，收到最后确认累计再用3RTT。合计4×5ms=20ms。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
