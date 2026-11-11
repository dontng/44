# Day 35｜数据结构＋操作系统

[← Day 34](day34.md) · [总入口](README.md) · [Day 36 →](day36.md)

**选择题：16道，来自两份完整src题单；大题：1道。** 先做选择题，再展开题下解析。组内题目沿用src顺序；标为复做的组，已会的快速通过，重点处理上次错题。

**预计用时：55—85分钟。** 选择题及核对约25—40分钟，大题约25—35分钟，最后用5—10分钟重做今天最值得记住的一道错题。约两小时是配题目标，不是必须耗满或到点强停；计算卡住时先保留题号，先完成其余选择题。

## 选择题组1｜0805 · 数据结构

[有序树：从局部旋转到多路分裂](../src/0805.md) · 9道 · 复做第1次。

### 选择题1｜2020-05

<img src="../bank/2020/q05.png" alt="2020-05" style="display: block; width: 46.8em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

目标左子树根是2，故2必须在1、3之前插入。B先插1再插2，会把1变成4的左孩子，不能得到题图。

</details>

### 选择题2｜2020-10

<img src="../bank/2020/q10.png" alt="2020-10" style="display: block; width: 46.68em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

4阶B树每结点至多3个关键字，插入第4个时分裂。插到13时根分裂并提升6；再插8、2后，插12使右叶[8,9,12,13]分裂，提升9到根；最后15进入右叶。根最终为[6,9]。分裂时提升中间关键字，不能把新插入值直接当提升值。

</details>

### 选择题3｜2021-06

<img src="../bank/2021/q06.png" alt="2021-06" style="display: block; width: 38.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

23按查找路径20→30→25插入25左侧。最低失衡结点是20，新增结点落在其右孩子30的左子树，属RL型：先右旋30，再左旋20，新根为25。23只是新叶结点；旋转提升的是中间结点25。

</details>

### 选择题4｜2021-09

<img src="../bank/2021/q09.png" alt="2021-09" style="display: block; width: 46.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

3阶B树每结点最多2个关键字。第二层总共4个关键字，要使结点数最多就分成3个结点，各含1、1、2个关键字，根相应含2个关键字。第二层孩子总数为(1+1)+(1+1)+(2+1)=7，第三层最多7个结点。总数1+3+7=11，别把第二层的关键字数4当成结点数4。

</details>

### 选择题5｜2022-08

<img src="../bank/2022/q08.png" alt="2022-08" style="display: block; width: 47.6em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

5阶B树非根结点至少2个关键字。若以左子树前驱110替换260，原叶[100,110]删后仅[100]，必须调整；左兄弟[70,80,85]可借，85上移、90下移，根变为[60,85,110,350]，对应C。D虽把260替换成110，却保留其余根关键字，漏了下溢调整。A、B可由后继替换后合并或直接合并得到。

</details>

### 选择题6｜2023-07

<img src="../bank/2023/q07.png" alt="2023-07" style="display: block; width: 43.23em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：B。**

I插入根分裂可增高；II删除最终在叶层移除或调整关键字，会改变叶；III错，B树可在内部命中；IV错，插入关键字可分裂提升。选I、II。

</details>

### 选择题7｜2024-07

<img src="../bank/2024/q07.png" alt="2024-07" style="display: block; width: 45.4em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

T在k3右侧且在k2左侧，所有x满足k3<x<k2，同时继承k1<x。D给出有效的更紧区间。

</details>

### 选择题8｜2025-08

<img src="../bank/2025/q08.png" alt="2025-08" style="display: block; width: 36.74em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

4阶B树每结点1～3个关键字，非根至少1个。高2层时：根含1个关键字，两叶共6个，只能3+3，1种；根含2个，三叶共5个，分配为3+1+1或2+2+1的排列，共6种；根含3个，四叶各1个，1种。高3层最少正好7个关键字，根、两子结点、四叶均各1个，另1种。总计1+6+1+1=9；关键字有序后，各结点内容由这些数量唯一确定。

</details>

### 选择题9｜2026-08

<img src="../bank/2026/q08.png" alt="2026-08" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

根的子树最大高度为3，AVL要求另一子树高度至少2。让高3的子树满，共7个结点；让高2的子树最稀疏，仅2个结点，差7−2=5。AVL限制的是高度差，不是结点数量差；高3的稀疏子树反而不能让数量差最大。

</details>

## 选择题组2｜0831 · 操作系统

[设备服务：缓冲、磁盘与请求调度](../src/0831.md) · 7道 · 复做第2次。

### 选择题10｜2021-26

<img src="../bank/2021/q26.png" alt="2021-26" style="display: block; width: 46.76em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

SSTF每次从当前位置挑最近请求。184号请求先原地完成，随后依次到182、187、176、199，移动量为0+2+5+11+23=41。选的是离当前磁头最近的请求，不是按输入次序，也不是把全部请求从小到大排序。

</details>

### 选择题11｜2022-32

<img src="../bank/2022/q32.png" alt="2022-32" style="display: block; width: 26.04em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：A。**

驱动必须配合具体I/O控制方式：查询方式要反复读状态，中断方式要处理中断，DMA方式要设置传输参数，因此“与I/O控制方式无关”错误。设备初始化、启动读写都由驱动控制；同步I/O等待设备完成时，请求进程可能阻塞，B、C、D成立。

</details>

### 选择题12｜2023-32

<img src="../bank/2023/q32.png" alt="2023-32" style="display: block; width: 44.04em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

分配设备既要看设备类型是否满足请求，也要查进程有无访问权限、设备是否被占用，并建立逻辑设备到实际物理设备的对应关系。四项分别对应适用性、保护、可用性和设备独立性，均需考虑。

</details>

### 选择题13｜2024-31

<img src="../bank/2024/q31.png" alt="2024-31" style="display: block; width: 33.23em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

中断例程把字符放入内核缓冲区。CPU寄存器只是临时载体，用户缓冲区属于后续交付。

</details>

### 选择题14｜2024-32

<img src="../bank/2024/q32.png" alt="2024-32" style="display: block; width: 47.59em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：C。**

磁头向小号方向服务：200→160→120→110→0；随后循环跳到399，再向下服务300、210。总距离为200+399+(399−210)=788。循环扫描的回跳也有真实寻道距离；只扫到最小请求再跳最高请求的C-LOOK不能替代本题C-SCAN。

</details>

### 选择题15｜2026-31

<img src="../bank/2026/q31.png" alt="2026-31" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

块设备和字符设备的传输单位与设备特性不同，I/O控制方式可以不同。它们仍可在内核规定的接口下提供启动和读写操作。

</details>

### 选择题16｜2026-32

<img src="../bank/2026/q32.png" alt="2026-32" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

**答案：D。**

鼠标中断处理程序读取设备接口的数据寄存器，将输入数据交给内核缓冲区，选D。模式切换在开始执行处理程序前由硬件完成，B不属于该程序执行的动作；把数据放进接口寄存器是设备完成的，C也不对。中断输入通常唤醒等待者，不是把当前进程改为阻塞。

</details>

## 解答题

### 大题1｜2025-47

[原题单 0930｜传输窗口：序号空间、确认与超时共同推进](../src/0930.md)

<img src="../bank/2025/q47.png" alt="2025-47" style="display: block; width: 42.55em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>答案与解析</summary>

（1）单程传播时延为2×36000/300000=0.24s，单方向吞吐量由卫星链路限制为200kb/s。4000B序列化耗时0.16s，在题设忽略开销且按瓶颈链路下界计时的口径下，共0.40s。

（2）每帧1500×8/200000=0.06s，首帧发出到ACK返回需0.06+2×0.24=0.54s。利用率至少80%要求 W×0.06≥0.8×0.54，向上取整得8帧。GBN要求 W≤2ᵏ−1，最少4位序号。

（3）生活区需/25，另两区需/26。H1=10.10.10.33/26锁定管理区为10.10.10.0/26。作业区为10.10.10.64/26，生活区为10.10.10.128/25。

</details>

## 一行记录

```text
实际用时__；未完成或未核对的题号__；今天最容易混淆的是__
```
