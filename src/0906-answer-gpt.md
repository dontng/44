[« 0905-answer](0905-answer.md)　　[0907-answer »](0907-answer.md)

# 0906 Answer｜控制转发路径：从路由知识到下一跳动作

> [原题 18 题](0906.md) · [0905 网络地址](0905-answer.md) · [能力账本](answer-quality/learning-ledger.md)
>
> IP前缀确定“匹配谁”，路由协议生成“表怎么来”，转发时再用ARP找到下一跳MAC。18/18题逐项讲解；交叉题只补这一层判断，限时独立表现待验。

<details><summary><strong>考场入口</strong></summary>

| 题 | 第一笔 | 答案 |
| --- | --- | --- |
| [01](#q01) | RIP中16即无穷，不再经R2走 | D |
| [02](#q02) | 拥塞丢弃可报ICMP源点抑制 | C |
| [03](#q03) | 两/25汇成/24，下一跳R2的1.2 | D |
| [04](#q04) | 路由器可丢拥塞包、按目的转发 | C |
| [05](#q05) | ARP由下一跳IP找MAC | A |
| [06](#q06) | OSI表示层相邻应用做格式转换 | B |
| [07](#q07) | 整报文两段串行，分组流水 | D |
| [08](#q08) | 未知MAC泛洪，ACK按已学表发 | B |
| [09](#q09) | 三前缀皆匹配，选最具体/27 | C |
| [10](#q10) | 一次更新后仍有经R1的旧路由，距离3 | B |
| [11](#q11) | RIP→UDP，OSPF→IP，BGP→TCP | D |
| [12](#q12) | 32—63四个/21合/19 | C |
| [13](#q13) | 800B MTU非末片载荷776，总796 | B |
| [14](#q14) | 到邻居链路代价+向量，逐网取最小 | D |
| [15](#q15) | NAT后源是R2公网.33 | A |
| [16](#q16) | VLAN1的ARP不到VLAN3 | D |
| [17](#q17) | 未获址REQUEST仍用0源、全1目的 | C |
| [18](#q18) | NAT端口与伪首部变，源端口/校验和 | B |

</details>

<a id="q01"></a>
## 01｜2010-35：RIP里16不是很远，是不可达

<img src="../bank/2010/q35.png" alt="2010-35 原题" width="493" style="display:block; width:30.81em; max-width:100%; height:auto;">

R1从邻居R2收到 `<net1,16>`；RIP约定距离**16为无穷/不可达**，加一跳不是可用的17跳路由，因此只能断言 **R1不能经R2到net1，选 D**。第一笔先检查度量有没有碰到协议上限，再决定是否加邻居距离。

<details open><summary>为什么不能推断R2永远到不了</summary>

路由更新反映R2向R1通告的距离，可能有水平分割、毒性逆转等策略，也可能有其它路径；题能可靠得出的只是“R1不能使用这条经R2的路由”。A/B从通告反向推R2经R1的路径，方向错。
</details>

<a id="q02"></a>
## 02｜2010-36：拥塞丢包反馈源端属于ICMP控制消息

<img src="../bank/2010/q36.png" alt="2010-36 原题" width="494" style="display:block; width:30.88em; max-width:100%; height:auto;">

按该卷所考ICMP报文类型，路由器因拥塞丢分组可向原发送主机发**源点抑制（Source Quench），选 C**。第一笔把原因“拥塞”与目的不可达、TTL超时、重定向分别对应，不从“丢包”泛选目的不可达。

<details open><summary>历史语境</summary>

这是2010真题采用的历史ICMP分类；现代互联网已不建议依赖源点抑制进行拥塞控制。考试按当年题设识别该报文，不把它当今天应部署的机制。RIP、ICMP、ARP是不同控制信息，发生的位置不同。
</details>

<a id="q03"></a>
## 03｜2011-37：路由聚合来自目标前缀，下一跳来自拓扑

<img src="../bank/2011/q37.png" alt="2011-37 原题" width="535" style="display:block; width:33.44em; max-width:100%; height:auto;">

已在[0905-02](0905-answer.md#q02)推过：R2后方两个/25并成`192.168.2.0/24`，R1的下一跳为R2相邻接口`192.168.1.2`，**选 D**。新增控制视角：路由表只存目的前缀和下一跳，数据平面使用它，不必在R1列两条更细路由。

<details open><summary>一条汇总路由何时安全</summary>

只有该/24全都通向同一R2，汇总才不引入错误转发；图给的两个/25恰好完整覆盖/24。若只有其中一个/25可达，粗汇总会吞进不可达地址。
</details>

<a id="q04"></a>
## 04｜2012-37：路由表形成、拥塞丢包与逐包转发分开

<img src="../bank/2012/q37.png" alt="2012-37 原题" width="395" style="display:block; width:24.69em; max-width:100%; height:auto;">

已在[0903-04](0903-answer.md#q04)判 **I、II、IV，选 C**。本次只加时间层次：路由协议先维护路由知识 I，来包时按目的地址查表 IV，队列拥塞可丢包 II；IP首部校验不能保证整份分组送达，III错。

<details open><summary>做题保底</summary>

即使忘记路由协议名，也可先排“校验确保不丢”的III，因为物理错误之外还有拥塞、TTL、链路故障等丢包原因；再看其余选项是否包含III。
</details>

<a id="q05"></a>
## 05｜2012-38：有路由还要解析下一跳MAC

<img src="../bank/2012/q38.png" alt="2012-38 原题" width="431" style="display:block; width:26.94em; max-width:100%; height:auto;">

[0905-04](0905-answer.md#q04)的ARP题，**IP→MAC，选 A**。新动作是排序：先查路由表确定下一跳IP，再在本链路ARP取得下一跳MAC，最后封装帧；不能在查路由前直接ARP远端网站的MAC。

<details open><summary>控制与数据的接口</summary>

ARP应答产生短期映射缓存；转发平面用缓存填写帧目的MAC。DNS的域名解析不是这一步。
</details>

<a id="q06"></a>
## 06｜2013-33：OSI上层相邻职责仍须保留边界

<img src="../bank/2013/q33.png" alt="2013-33 原题" width="393" style="display:block; width:24.56em; max-width:100%; height:auto;">

此交叉题在[0901-08](0901-answer.md#q08)已解：应用层的相邻层是表示层，格式转换 **选 B**。此处用它防止把所有“格式转换”误放到路由器；路由器主要看网络层地址，不需要理解应用数据格式。

<details open><summary>相邻两题怎样分层判断</summary>

本题的关键词是“应用层的相邻层”和“格式转换”，落在表示层；[0902-03](0902-answer.md#q03)的信号波形题则落在物理层。先看当前题问的是数据表示还是线路信号，再调用相应机制，不能因题号相邻而把两题条件混用。
</details>

<a id="q07"></a>
## 07｜2013-35：转发方式先决定是否等整报文

<img src="../bank/2013/q35.png" alt="2013-35 原题" width="537" style="display:block; width:33.56em; max-width:100%; height:auto;">

[0901-09](0901-answer.md#q09)已算：整报文两段各800ms共1600ms；10kb分组共800包，两段存储转发流水801ms，**选 D**。路由器若要等整个报文才转，无法与前段传输流水；分组级缓存让不同链路同时工作。

<details open><summary>别把“控制转发路径”当最短路题</summary>

本题只有一台中间路由器与两段同速链路，关键是转发粒度；不需要跑任何路由算法。路线知识已给定，问的是时间。
</details>

<a id="q08"></a>
## 08｜2014-34：二层交换表也通过入帧学习

<img src="../bank/2014/q34.png" alt="2014-34 原题" width="524" style="display:block; width:32.75em; max-width:100%; height:auto;">

[0904-08](0904-answer.md#q08)已算：a→c时c未知，泛洪端口{2,3}，学习a→1；c→a确认只走{1}，**选 B**。它与三层路由表不是同一张表：二层由帧源MAC学习，三层由路由配置/协议形成。

<details open><summary>新来一个帧就更新状态</summary>

别把初始表静止地套两次；第二帧的转发已经能使用第一帧刚学到的a→1。无需知道a/c的IP前缀。
</details>

<a id="q09"></a>
## 09｜2015-38：多条路由同时匹配，先比前缀长度

<img src="../bank/2015/q38.png" alt="2015-38 原题" width="492" style="display:block; width:30.75em; max-width:100%; height:auto;">

目的 `169.96.40.5` 同时在 `169.96.40.0/23`、`/25`、`/27` 内，也匹配默认/0；最具体 **/27** 优先，应走表中第三行接口。题图表内写 **E3**，选项 C 却写 **S3**，接口名存在不一致；按选项指代第三行的命题口径取 **C**，不能把图中的 E3 默默改读成 S3。第一笔先在四行上标23、25、27、0，圈最大者，不以表格先后或接口名称决定。

<details open><summary>为什么这几条都覆盖.5</summary>

/27的最后字节0—31，.5在其中；/25的0—127也含.5；/23覆盖更广。最长前缀优先保证更精细的路由覆盖粗路由，默认只在没有更具体匹配时使用。
</details>

<a id="q10"></a>
## 10｜2016-37：一次更新不等于全网已经重新收敛

<img src="../bank/2016/q37.png" alt="2016-37 原题" width="548" style="display:block; width:34.25em; max-width:100%; height:auto;">

故障前已收敛：R3 到目标网距离 1，R1、R2 经 R3 距离均为 2。R3 发现不可达后仅向 R2 通告一次距离 16；此时 R1 尚未更新，仍向 R2 提供旧距离 2。R2 因此选经 R1 的 `1+2=3`，**选 B**，不能把 R3 的 16 直接当作 R2 更新后的最短距离。

<details open><summary>旧路由造成的慢收敛</summary>

R1 的旧路线实际上经过 R3，已经失效，但距离向量报文不携带完整路径，R2 暂时看不出来。题目只问一次更新后的状态，不是最终收敛后不可达的 16；也未给水平分割或毒性逆转等额外机制，不能擅自加入来改变更新结果。
</details>

<a id="q11"></a>
## 11｜2017-37：三种路由协议的承载层不同

<img src="../bank/2017/q37.png" alt="2017-37 原题" width="484" style="display:block; width:30.25em; max-width:100%; height:auto;">

RIP报文由 **UDP**承载；OSPF直接在 **IP** 上运行；BGP建立可靠会话经 **TCP**。依次 `UDP、IP、TCP`，**选 D**。第一笔按邻居交换的需求分类：距离向量简易报文、链路状态协议直接IP、自治系统间长会话。

<details open><summary>目的不是背“都在网络层”</summary>

这三者都服务于路由控制，但封装位置不同。BGP用TCP不意味着它是应用用户的Web流量；OSPF不用UDP/TCP是题的关键差异。
</details>

<a id="q12"></a>
## 12｜2018-38：四个相邻/21完整合成一个/19

<img src="../bank/2018/q38.png" alt="2018-38 原题" width="524" style="display:block; width:32.75em; max-width:100%; height:auto;">

四个网第三字节从32、40、48、56起，每块宽8，共连续覆盖 **32—63**，可由 `35.230.32.0/19` 一条路由覆盖，**选 C**。第一笔看起点是否在32边界且四块连续，合并两位前缀。

<details open><summary>聚合不可吞进不相干网络</summary>

/19第三字节块宽32，32—63正好；若用`35.230.0.0/19`将错收0—31，/20只覆盖其中两块。题还说四条路由的转发接口相同，故合并后的下一跳不会产生歧义。
</details>

<a id="q13"></a>
## 13｜2021-36：IP非末分片的载荷须按8字节对齐

<img src="../bank/2021/q36.png" alt="2021-36 原题" width="526" style="display:block; width:32.88em; max-width:100%; height:auto;">

原数据报总1580B，首部20B，数据1560B；MTU800B每片最多数据780B，但非末片数据长度须8B整倍数，取 `⌊780/8⌋×8=776B`。前两片各总 `776+20=796B`，还剩8B第三片，故第二片 **总长796、MF=1，选 B**。第一笔先扣首部，再向下取8的倍数。

<details open><summary>MF与偏移量不同</summary>

第二片后面还有第三片，因此“后面还有分片”标志MF=1。第二片偏移量以8B单位是776/8=97；题没有问偏移，不能把97填进总长。
</details>

<a id="q14"></a>
## 14｜2021-37：每个目的独立求“去邻居代价+邻居报告”

<img src="../bank/2021/q37.png" alt="2021-37 原题" width="554" style="display:block; width:34.63em; max-width:100%; height:auto;">

E到A/B/C/D直连代价为8/10/12/6。逐列相加后取最小：Net1 `min(9,33,32,28)=9`；Net2 `min(20,45,42,34)=20`；Net3 `min(32,28,28,42)=28`；Net4 `min(44,40,20,30)=20`。向量 **9、20、28、20，选 D**。第一笔在表每一列上方写四个直连成本，不把一个邻居当全网唯一最优。

<details open><summary>Net3并列也只问距离</summary>

经B为10+18=28，经C为12+16=28，两条同长；题问最短距离向量，不要求唯一下一跳。逐目标独立最小化，不能用Net1最优的A去包办所有网络。
</details>

<a id="q15"></a>
## 15｜2023-38：NAT在R2外侧改写源IP

<img src="../bank/2023/q38.png" alt="2023-38 原题" width="549" style="display:block; width:34.31em; max-width:100%; height:auto;">

[0905-13](0905-answer.md#q13)已讲：私网H的源`192.168.0.3`出R2后变公网接口 `195.123.0.33`，**选 A**。补一个边界：这是NAT主动改写IP源，普通路由转发通常只换当前链路帧的MAC，不换源IP。

<details open><summary>公网/30上的.35不能作源</summary>

该/30可用.33与.34，.35是广播。NAT后的分组还会经过R1继续转发，但不会把源改成R1的IP。
</details>

<a id="q16"></a>
## 16｜2024-35：ARP控制广播无法穿越VLAN

<img src="../bank/2024/q35.png" alt="2024-35 原题" width="540" style="display:block; width:33.75em; max-width:100%; height:auto;">

[0904-19](0904-answer.md#q19)、[0905-16](0905-answer.md#q16)已解，H4在VLAN1不会直接学VLAN3 H6的ARP条目，**选 D**。新视角：即使IP地址形式相近，控制报文被二层广播域边界截住，路由知识本身也不能凭空产生邻居MAC。

<details open><summary>若要跨VLAN</summary>

需要三层接口和合适的网关/地址规划；此时H4解析的是本VLAN网关的MAC，远端H6的MAC由目标VLAN一侧的路由接口处理。
</details>

<a id="q17"></a>
## 17｜2025-36：DHCP控制过程在获址前仍用广播

<img src="../bank/2025/q36.png" alt="2025-36 原题" width="492" style="display:block; width:30.75em; max-width:100%; height:auto;">

[0905-17](0905-answer.md#q17)已讲，REQUEST的IP首部是目的 `255.255.255.255`、源 `0.0.0.0`，**选 C**。这道交叉题与ARP并排：DHCP先获得本机可用IP，之后有了网关和路由信息才进行下一跳ARP。

<details open><summary>yiaddr不是IP首部源</summary>

图中`yiaddr=192.168.5.9`是服务器建议租给H的地址；REQUEST尚在请求与确认流程中，不应把建议值提前当作已配置的源IP。
</details>

<a id="q18"></a>
## 18｜2025-37：NAT改源端口后要重算UDP校验和

<img src="../bank/2025/q37.png" alt="2025-37 原题" width="491" style="display:block; width:30.69em; max-width:100%; height:auto;">

内网H `192.168.1.5/24` 向外发UDP。NAPT可改**源端口号 I**以区分共享公网IP的流；UDP校验和覆盖含源/目的IP的伪首部，NAT改IP源且可能改源端口后需**重算校验和 IV**。目的端口II仍指远端服务，UDP长度III未因地址翻译改变。仅I、IV，**选 B**。第一笔写出UDP校验覆盖“伪首部+UDP首部+数据”。

<details open><summary>为何IP头部校验和之外还要动UDP</summary>

IP层有自己的首部校验更新；UDP校验虽不在IP首部，其伪首部纳入IP源/目的地址，源IP一换原校验就不对应。若原IPv4 UDP校验和被置0代表不使用校验，具体实现细节另论，题按通常有效校验场景。
</details>

## 18题收束

控制平面形成路由，数据平面按最长前缀选下一跳，再由ARP补当前链路MAC；RIP的16表示不可达，NAT还会改变IP源及传输层校验依据。18题已讲，遮住解释后能否独立限时判定仍待测。

[« 0905-answer](0905-answer.md)　　[0907-answer »](0907-answer.md)
