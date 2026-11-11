# Day 27｜数据结构＋操作系统

[← Day 26](day26.md) · [总入口](README.md) · [Day 28 →](day28.md)

**选择题：15道，来自两份完整src题单；大题：1道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：55—85分钟。** 选择题及核对约25—40分钟，大题约25—35分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0801 · 数据结构

[位置关系：指针、下标与压缩存储](../src/0801.md) · 8道 · 复做第1次。

### 选择题1｜2020-01

<img src="../bank/2020/q01.png" alt="2020-01" style="display: block; width: 46.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

矩阵对称，m₇,₂与m₂,₇共用存储位置。上三角按列存储，第7列之前有1+2+3+4+5+6=21个元素；m₂,₇在本列排第2，C数组从0编号，下标为21+1=22。不能直接拿下三角的行号7、列号2套入上三角存储。

</details>

### 选择题2｜2021-01

<img src="../bank/2021/q01.png" alt="2021-01" style="display: block; width: 46.72em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

先q=h→next，再h→next=q→next；若p==q说明删的是唯一数据结点，尾指针p必须改为h，最后释放q。

</details>

### 选择题3｜2021-03

<img src="../bank/2021/q03.png" alt="2021-03" style="display: block; width: 46.8em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

设每行有c个元素，则A[3][3]相对A[0][0]偏移3c+3=220−100=120，得c=39。A[5][5]的地址为100+5×39+5=300。每元素只占一个存储单元，不再乘额外的字节数。

</details>

### 选择题4｜2023-02

<img src="../bank/2023/q02.png" alt="2023-02" style="display: block; width: 46.96em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

两条next赋值后，s的后继仍是原p的后继，其prev仍指p。先s→prev=s→next→prev得到p，再s→next→prev=s，补齐反向链。

</details>

### 选择题5｜2023-03

<img src="../bank/2023/q03.png" alt="2023-03" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

需要保存矩阵总行数、总列数，即I、III；含非零元素的行列数不能告诉你末尾全零行列有多少。

</details>

### 选择题6｜2024-01

<img src="../bank/2024/q01.png" alt="2024-01" style="display: block; width: 45.97em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

先把q=p的后继摘下：p→next=q→next；再将q头插到h之后。被移动的是q，不是p。

</details>

### 选择题7｜2026-01

<img src="../bank/2026/q01.png" alt="2026-01" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

表头插入要将原n个元素后移，表头删除要将后续n−1个元素前移；n≥3，I、II都必然移动多个元素。

III表尾插入已有空位，直接写入；IV表尾删除只需减小表长，不必搬动其余元素。保持原元素相对次序，排除了用末尾元素覆盖表头的做法。

</details>

### 选择题8｜2026-02

<img src="../bank/2026/q02.png" alt="2026-02" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

逐个结点沿p1向后走：若有后继，令p2指向后继的后继；若已到尾结点，令p2=NULL。D对两种情况都处理并始终推进cu。A在尾结点解引用NULL；B一开始head的p2就是NULL，循环不执行；C到尾结点后不再推进cu，会死循环。

</details>

## 选择题组2｜0831 · 操作系统

[设备服务：缓冲、磁盘与请求调度](../src/0831.md) · 7道 · 复做第1次。

### 选择题9｜2021-26

<img src="../bank/2021/q26.png" alt="2021-26" style="display: block; width: 46.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

SSTF每次从当前位置挑最近请求。184号请求先原地完成，随后依次到182、187、176、199，移动量为0+2+5+11+23=41。选的是离当前磁头最近的请求，不是按输入次序，也不是把全部请求从小到大排序。

</details>

### 选择题10｜2022-32

<img src="../bank/2022/q32.png" alt="2022-32" style="display: block; width: 26.04em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

驱动必须配合具体I/O控制方式：查询方式要反复读状态，中断方式要处理中断，DMA方式要设置传输参数，因此“与I/O控制方式无关”错误。设备初始化、启动读写都由驱动控制；同步I/O等待设备完成时，请求进程可能阻塞，B、C、D成立。

</details>

### 选择题11｜2023-32

<img src="../bank/2023/q32.png" alt="2023-32" style="display: block; width: 44.04em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

分配设备既要看设备类型是否满足请求，也要查进程有无访问权限、设备是否被占用，并建立逻辑设备到实际物理设备的对应关系。四项分别对应适用性、保护、可用性和设备独立性，均需考虑。

</details>

### 选择题12｜2024-31

<img src="../bank/2024/q31.png" alt="2024-31" style="display: block; width: 33.23em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

中断例程把字符放入内核缓冲区。CPU寄存器只是临时载体，用户缓冲区属于后续交付。

</details>

### 选择题13｜2024-32

<img src="../bank/2024/q32.png" alt="2024-32" style="display: block; width: 47.59em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

磁头向小号方向服务：200→160→120→110→0；随后循环跳到399，再向下服务300、210。总距离为200+399+(399−210)=788。循环扫描的回跳也有真实寻道距离；只扫到最小请求再跳最高请求的C-LOOK不能替代本题C-SCAN。

</details>

### 选择题14｜2026-31

<img src="../bank/2026/q31.png" alt="2026-31" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

块设备和字符设备的传输单位与设备特性不同，I/O控制方式可以不同。它们仍可在内核规定的接口下提供启动和读写操作。

</details>

### 选择题15｜2026-32

<img src="../bank/2026/q32.png" alt="2026-32" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

鼠标中断处理程序读取设备接口的数据寄存器，将输入数据交给内核缓冲区，选D。模式切换在开始执行处理程序前由硬件完成，B不属于该程序执行的动作；把数据放进接口寄存器是设备完成的，C也不对。中断输入通常唤醒等待者，不是把当前进程改为阻塞。

</details>

## 解答题

### 大题1｜2025-45

[原题单 0925｜并发同步：PV 操作大题](../src/0925.md)

<img src="../bank/2025/q45.png" alt="2025-45" style="display: block; width: 42.48em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

四个信号量：slots=3 表示还能挖的坑配额，dug=0 表示可供乙种植的空坑，planted=0 表示可浇的树，spade=1 表示铁锹可用。

```text
甲重复：
    wait(slots)
    wait(spade)
    挖坑
    signal(spade)
    signal(dug)

乙重复：
    wait(dug)
    放树苗
    wait(spade)
    填土
    signal(spade)
    signal(slots)
    signal(planted)

丙重复：
    wait(planted)
    浇水
```

甲在动工前预扣坑配额，乙在填土后归还，因此未填满的坑最多三个。乙须等甲挖完，丙须等乙填完。铁锹只覆盖挖坑、填土，不持有铁锹等待坑位或空坑。水桶只有丙一个使用者，丙顺序执行即可。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
