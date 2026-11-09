# Day 23｜数据通路攻坚｜从机器码走到控制线

[← Day 22](day22.md) · [总入口](README.md) · [Day 24 →](day24.md)

**今日判断。** 先判字段是哪种指令格式，再从寄存器和立即数的来源反查 MUX 输入端。

## 今天按这个顺序做

1. **0–10分钟｜回收。** 闭卷重写昨天的一处断点，写不出就标U。
2. **10–35分钟｜前置题。** 重做 [Day 10 的2022-43](day10.md) 取指小问，对照今天的图看 PC 与 ALU 是否可以同时向不同去处送值。
3. **35–100分钟｜整题。** 两道题各给约30分钟，先完整写出步骤，剩余时间修正关键一步。先尝试5分钟，再开提示。
4. **100–120分钟｜验收。** 回答下方条件变化，订正后闭卷再写一次。到120分钟停止。

## 大题1｜2026-43 · 三种指令格式与16位机器码

[原题单 0919](../src/0919.md)

<img src="../bank/2026/q43.png" alt="2026-43" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>没有入口时的第一步</summary>

高四位先判 R、I、M。按字节编址，连续的16位变量相差2字节。

</details>

<details>
<summary>完整解法与必要补学</summary>

（1）按字节编址，主存可编址单元8位。通用寄存器16位。

（2）op1 在R型低4位，高4位已用0000识别R型，所以可以与op2重码。op2与op3都在高4位，用来区分指令及格式，不能重码。

（3）该指令做 R2←R2+R9，保留低16位。ABCDH+F001H=19BCEH，R2为9BCEH，R9仍为F001H。

（4）①1110，从R15+0取x到R0。②0000 0100，rt=0、左移4位。③1111 1011，为−5的8位补码。④0000 0000 0010，写回R15+2的y。

</details>

<details>
<summary>重做后检查</summary>

逐条写 R0 的内容：x、16x的低16位、16x−5的低16位，最后写存储器。

</details>

## 大题2｜2026-44 · 多路选择、扩展模式与PC自增

[原题单 0920](../src/0920.md)

<img src="../bank/2026/q44.png" alt="2026-44" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>没有入口时的第一步</summary>

本题共享上一题指令格式。把需要的输入沿实线反向追到MUX，再按端口标号填控制值。

</details>

<details>
<summary>完整解法与必要补学</summary>

（1）①、②均为二选一多路选择器，分别选寄存器组读地址。

（2）至少2位。至少区分 imm8 零扩展、imm8 符号扩展、offset12 符号扩展三个模式。左移量 num 的提取也可用第四种模式编码。

（3）取指周期 MARsrc=0，使MAR接PC。ALUAsrc=0，ALUBsrc=1，用PC与常量2相加更新PC。RegWr=0，不写通用寄存器组。

（4）左移量来自扩展器，ALUBsrc=2。写回ALU，RegWsrc=1。目标是rt，RegDst=1，RegWr=1。ExtOp须与M型不同。左移仅取IR[7:4]的无符号 num，M型要对IR[11:0]整体符号扩展；若套用后者，rt和op1会一起混入移位操作数。

</details>

<details>
<summary>重做后检查</summary>

本题取指周期 ALUBsrc=1 对应常量2。不要套用另一张图中的 MUX 编号。

</details>

## 闭卷变式

若从按字节编址改成按16位字编址，且每条指令仍为一个16位字，顺序取指的PC应加几？

<details>
<summary>检查答案</summary>

应加1。PC增量用可编址单元计数。

</details>

记录：实际用时__；两次作答状态 I／H／U__；卡住的题号与第一处断点__。
