# Day 26｜组成原理＋计算机网络

[← Day 25](day25.md) · [总入口](README.md) · [Day 27 →](day27.md)

**选择题：18道，来自两份完整src题单；大题：1道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：70—110分钟。** 选择题及核对约40—65分钟，大题约25—35分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0812 · 组成原理

[位模式的解释权：整数、浮点与类型转换](../src/0812.md) · 13道 · 复做第1次。

### 选择题1｜2020-13

<img src="../bank/2020/q13.png" alt="2020-13" style="display: block; width: 46.72em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

先按32位补码解释：C8000000H的符号位为1，真值=C8000000H−100000000H=−38000000H=−7×2²⁷，所以A成立。

同一位串若按float解释，符号为负、阶码144，值为−2¹⁷，并非B的−2¹⁶；C、D为正数，与符号位不符。题目问“可能”，找到合法解释即可，但不能把整数与浮点的解码规则混用。

</details>

### 选择题2｜2020-14

<img src="../bank/2020/q14.png" alt="2020-14" style="display: block; width: 50.12em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

short占偏移0、1，偏移2、3用于对齐，int成员x2从偏移4开始。小端存12340000H时，低地址依次为00、00、34、12，因此34H位于首址+6=2020FE06H。

C的偏移5落在x2的第二个字节，仍是00H；B的偏移4是正确对齐后的x2起址，也是漏算对齐填充时34H会被误放的位置。先确定成员起址，再按小端排列字节。

</details>

### 选择题3｜2021-14

<img src="../bank/2021/q14.png" alt="2021-14" style="display: block; width: 52.24em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

1.2=6/5，最简分母含因子5，二进制是无限循环小数，有限尾数不能精确保存。

B的1.25=1.01₂，C的2.0=10₂，D的2.5=10.1₂，均能用有限二进制位精确表示。判断的是精确性，不是能否存下一个近似值。

</details>

### 选择题4｜2022-13

<img src="../bank/2022/q13.png" alt="2022-13" style="display: block; width: 52.55em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

32位补码最高位的权是−2³¹，其余31位最大和为2³¹−1，因此范围为−2³¹到2³¹−1。

其余选项至少有一端用到了2³²量级，已经超过32位补码的范围。负端比正端的绝对值多1，不是关于0对称。

</details>

### 选择题5｜2022-14

<img src="../bank/2022/q14.png" alt="2022-14" style="display: block; width: 53.05em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

−0.4375=−0.0111₂=−1.11₂×2⁻²。符号位1，阶码−2+127=125，尾数去掉隐含的1后为110…，拼得BEE00000H。

小数点移动后指数是−2；规格化数的隐含1不写进尾数字段。两处任一弄反，编码都会错。

</details>

### 选择题6｜2023-13

<img src="../bank/2023/q13.png" alt="2023-13" style="display: block; width: 40.65em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

先按16位计算：−8190的补码=2¹⁶−8190=57346=E002H。

先确定位宽再取补；十六进制最高位为E不代表数值是正的，short仍按有符号补码解释。

</details>

### 选择题7｜2023-14

<img src="../bank/2023/q14.png" alt="2023-14" style="display: block; width: 46.85em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

80200000H的符号位为1、阶码全0、尾数字段为0.01₂=1/4，属于非规格化数。值为−(1/4)×2⁻¹²⁶=−2⁻¹²⁸。

阶码全0时有效数是0.f，不是1.f，指数也按−126取。套规格化数的隐含1规则会得到错误结果。

</details>

### 选择题8｜2024-12

<img src="../bank/2024/q12.png" alt="2024-12" style="display: block; width: 24.97em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

按题目的16位short、32位int模型，32777=8009H。截成short后按16位补码解释为32777−65536=−32759；再转int进行符号扩展，数值仍为−32759。

D忽略了窄化后的符号位；C把8009H当成了正数；A把符号改变误当成直接给32777加负号。

</details>

### 选择题9｜2024-14

<img src="../bank/2024/q14.png" alt="2024-14" style="display: block; width: 45.97em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

α在±2²⁰内，用32位整数可精确表示且运算直接；β在±2⁴⁰内，32位整数不够，双精度有53位有效二进制精度，可精确保存这个范围的全部整数。

单精度只有24位有效二进制精度，范围虽然够大，却不能精确保留±2⁴⁰内的所有整数，因此B、D不行；A的β会越界。

</details>

### 选择题10｜2025-12

<img src="../bank/2025/q12.png" alt="2025-12" style="display: block; width: 40.32em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

si=−32767=−2¹⁵+1，转为32位unsigned int后按模2³²取值，得到2³²−2¹⁵+1。

B相当于只把16位位串当成无符号数，没有完成题目要求的32位转换；C把末尾的+1写反。

</details>

### 选择题11｜2025-13

<img src="../bank/2025/q13.png" alt="2025-13" style="display: block; width: 42.52em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

47300000H拆得符号0、阶码142、真实指数15；有效数为1.011₂=1.375，因此值为1.375×2¹⁵。

阶码要减偏置127；尾数字段前要补规格化数的隐含1。

</details>

### 选择题12｜2025-15

<img src="../bank/2025/q15.png" alt="2025-15" style="display: block; width: 42.29em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

结构体中id占4B，name占10B，随后补2B使salary按4B对齐，总大小20B=14H。employee[1].id起址为A0B0H+14H=A0C4H；小端字节为78、56、34、12，56H在A0C5H。

A的A0C3H漏计结构体对齐填充；B的A0C4H是该int的起始地址；D的A0C6H对应34H，而不是56H。

</details>

### 选择题13｜2026-14

<img src="../bank/2026/q14.png" alt="2026-14" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

12.1=1100.000110011…₂=1.100000110011…₂×2³，符号0，阶码3+127=130。尾数截到23位后得到41419999H，后续位超过半个末位单位，向上舍入为4141999AH。

A只截断没有就近舍入；C、D的阶码字段不符。这里只在恰好处于中点时才用“取偶”，不是所有小数都直接取偶。

</details>

## 选择题组2｜0908 · 计算机网络

[应用会话：DNS、Web、邮件与文件传输](../src/0908.md) · 5道 · 复做第1次。

### 选择题14｜2020-40

<img src="../bank/2020/q40.png" alt="2020-40" style="display: block; width: 46.8em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题15｜2022-40

<img src="../bank/2022/q40.png" alt="2022-40" style="display: block; width: 47.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

握手1RTT，HTML请求与1MSS响应1RTT。按本题参考解采用的初始1MSS慢开始，图像请求时窗口2MSS，3MSS图像分两轮，共4RTT=40ms。若题目另给足够大的发送窗口，图像可一轮发完，合计3RTT。

</details>

### 选择题16｜2024-40

<img src="../bank/2024/q40.png" alt="2024-40" style="display: block; width: 46.0em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：D（待逐题复核）。** 解析待补。

</details>

### 选择题17｜2025-40

<img src="../bank/2025/q40.png" alt="2025-40" style="display: block; width: 40.42em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**参考答案：B（待逐题复核）。** 解析待补。

</details>

### 选择题18｜2026-40

<img src="../bank/2026/q40.png" alt="2026-40" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

Cookie可携带会话标识，用于跟踪、推荐和购物车。缩短对象响应依赖缓存与传输等机制。

</details>

## 解答题

### 大题1｜2024-46

[原题单 0925｜并发同步：PV 操作大题](../src/0925.md)

<img src="../bank/2024/q46.png" alt="2024-46" style="display: block; width: 46.07em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

（1）是临界区。两个进程均修改同一缓冲区，若同时执行C1会使写入交错或覆盖，因此必须互斥。

（2）B初始为空，P1写一次，P2读一次。一个初值0的同步信号量ready即可：

```text
P1: C1; V(ready);
P2: P(ready); C2;
```

两个动作已被强制串行，无须再加互斥量；题目要求尽可能少的信号量。

（3）B初始非空，两个进程各修改一次。设mutex=1，P1和P2均执行`P(mutex); C3; V(mutex);`。这里不需要empty/full，因为没有把缓冲区从空变满或从满读空的操作。ready表示事件完成，mutex表示进入资格，初值不能互换。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
