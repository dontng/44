# Day 16｜组成原理＋计算机网络

[← Day 15](day15.md) · [总入口](README.md) · [Day 17 →](day17.md)

**选择题：10道，来自两份完整src题单；大题：1道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：55—90分钟。** 选择题及核对约25—45分钟，大题约25—35分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0819 · 组成原理

[数据通路：状态元件、操作元件与控制信号](../src/0819.md) · 5道 · 首次。

### 选择题1｜2021-18

<img src="../bank/2021/q18.png" alt="2021-18" style="display: block; width: 52.28em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

数据通路除了ALU、寄存器等，还需有溢出等异常检测、现场保存与转向处理所需电路，不能说完全不含异常检测及响应电路。组合元件负责运算，时序元件保存状态，控制信号决定选择与写入，所以A、B、D正确。控制器产生控制不等于全部响应动作都与数据通路无关。

</details>

### 选择题2｜2022-22

<img src="../bank/2022/q22.png" alt="2022-22" style="display: block; width: 39.4em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

单核也可保留多份线程上下文并交替发射。多核可执行多条指令流，向量计算是单指令作用于多项数据，SMP共享物理地址空间。

</details>

### 选择题3｜2023-18

<img src="../bank/2023/q18.png" alt="2023-18" style="display: block; width: 46.88em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

ALU和MUX的输出由当前输入决定，不负责跨时刻保存状态，属于组合逻辑操作元件。PC和通用寄存器组需要保存数值，属于时序逻辑状态元件。MUX即使只做选择、不做加减，也仍是组合逻辑，选Ⅰ、Ⅳ。

</details>

### 选择题4｜2025-19

<img src="../bank/2025/q19.png" alt="2025-19" style="display: block; width: 30.87em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

PC 是专用寄存器，无须放入通用寄存器组。多周期控制要分执行步骤，流水还要解决冒险。

</details>

### 选择题5｜2026-20

<img src="../bank/2026/q20.png" alt="2026-20" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A（I、II）。**

单周期一条指令一拍，CPI=1；多周期一条指令分多拍执行，CPI>1，因此I、II成立。

III把流水线的理想稳态值当作任何情况下都成立。题目虽排除了异常、中断和额外访存开销，仍未排除启动、数据冒险和控制冒险。

</details>

## 选择题组2｜0908 · 计算机网络

[应用会话：DNS、Web、邮件与文件传输](../src/0908.md) · 5道 · 首次。

### 选择题6｜2020-40

<img src="../bank/2020/q40.png" alt="2020-40" style="display: block; width: 46.8em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

DNS已缓存时可忽略本地查询时间，但仍需1RTT建TCP、1RTT请求并接收纯文本页，共20ms。未缓存时，本地域名服务器依次向根、com顶级、abc.com权威服务器迭代查询，再用2RTT取页，共5RTT=50ms。www.abc.com是Web主机，不是还要额外查询一次的独立DNS层级。

</details>

### 选择题7｜2022-40

<img src="../bank/2022/q40.png" alt="2022-40" style="display: block; width: 47.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

握手1RTT，HTML请求与1MSS响应1RTT。按本题参考解采用的初始1MSS慢开始，图像请求时窗口2MSS，3MSS图像分两轮，共4RTT=40ms。若题目另给足够大的发送窗口，图像可一轮发完，合计3RTT。

</details>

### 选择题8｜2024-40

<img src="../bank/2024/q40.png" alt="2024-40" style="display: block; width: 46.0em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

网页本身加7张图片，共8个对象。非持续HTTP每个对象各建一条TCP，至少1RTT建连、1RTT请求响应，共2RTT；不支持并行，只能串行8×2=16RTT。不能只数7张图片，也不能给8个对象共用一次握手。

</details>

### 选择题9｜2025-40

<img src="../bank/2025/q40.png" alt="2025-40" style="display: block; width: 40.42em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

POP3用于用户代理从邮件服务器取邮件，单次TCP会话可连续发送多条取信命令，收取多封邮件，Ⅰ、Ⅳ成立。用户提交邮件和邮件服务器之间转发邮件使用SMTP，不是POP3，Ⅱ、Ⅲ错误。收邮件协议不承担发送功能。

</details>

### 选择题10｜2026-40

<img src="../bank/2026/q40.png" alt="2026-40" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

Cookie可携带会话标识，用于跟踪、推荐和购物车。缩短对象响应依赖缓存与传输等机制。

</details>

## 解答题

### 大题1｜2024-42

[原题单 0918｜查找与排序：让分布、权重和内存边界决定代价](../src/0918.md)

<img src="../bank/2024/q42.png" alt="2024-42" style="display: block; width: 47.62em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

（1）按顺序，20、3、11、18、9、14、7 分别落入5、9、0、10、6、2、3。按槽0～10写为 [11, 空, 14, 7, 空, 20, 9, 空, 空, 3, 18]，装填因子7/11。

（2）14的 H₀=9，探查地址9、10、2，比较关键字3、18、14。

（3）8的 H₀=2，探查地址2、3、6、0、7；到地址7遇空，确认失败。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
