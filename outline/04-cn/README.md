# 计算机网络（408 考纲知识库分册）

> 📍 **导航**：[返回知识库总目录](../README.md)
>
> 本分册共收录 **18 个细粒度专题**，覆盖计算机网络概述、物理层、数据链路层、网络层、传输层、应用层。

---

## 目录索引

### 计算机网络概述
- [网络体系结构：OSI七层参考模型与TCP/IP四层模型协议封装](01-architecture/01-network-layers.md)
- [网络性能与时延：发送时延、传播时延、处理时延与排队时延计算](01-architecture/02-performance-delays.md)

### 物理层
- [信道极限容量：奈氏准则(无噪)与香农定理(有噪)极限速率计算](02-physical/01-channel-limits.md)
- [编码调制与信道复用：基带编码(曼彻斯特/差分曼彻斯特)与FDM/TDM/WDM/CDM](02-physical/02-encoding-and-multiplexing.md)

### 数据链路层
- [组帧与差错控制：字符填充/比特填充、奇偶校验与循环冗余校验CRC](03-datalink/01-framing-and-error-control.md)
- [点对点可靠传输：停等协议、后退N帧(GBN)与选择重传(SR)窗口限制](03-datalink/02-sliding-window-protocols.md)
- [介质访问与局域网：CSMA/CD碰撞检测、争用期最小帧长、以太网MAC与交换机自学习](03-datalink/03-mac-and-ethernet.md)
- [无线局域网802.11与VLAN虚拟局域网：CSMA/CA碰撞避免、IFS/RTS/CTS隐蔽站、802.11四地址帧、802.1Q标签与ALOHA/令牌](03-datalink/04-wlan-and-vlan.md)

### 网络层
- [IP编址与子网划分：分类IP、子网掩码、CIDR无分类编址与路由聚合](04-network/01-ip-addressing-and-cidr.md)
- [路由协议原理：距离向量算法(RIP)、链路状态算法(OSPF)与BGP路径向量](04-network/02-routing-protocols.md)
- [网络层辅助协议与设备：ARP地址解析、ICMP差错与询问、路由器转发表结构](04-network/03-routing-devices-and-icmp.md)
- [IPv6、IP组播、移动IP与SDN：IPv6固定首部与过渡机制、IGMP与组播路由、移动IP代理转发与SDN控制数据平面分离](04-network/04-ipv6-multicast-sdn.md)

### 传输层
- [传输层服务与UDP协议：端口复用分用、UDP报头格式与无连接特性](05-transport/01-transport-services-udp.md)
- [TCP连接与滑动窗口：三次握手四次挥手、序号确认号与滑动窗口流量控制](05-transport/02-tcp-connection-and-flow.md)
- [TCP拥塞控制算法：慢启动、拥塞避免、快重传与快恢复AIMD状态机](05-transport/03-tcp-congestion-control.md)

### 应用层
- [域名系统DNS：根/顶级/权限域名服务器、递归查询与迭代查询解析](06-application/01-dns-system.md)
- [超文本传输协议HTTP：持久非持久连接、状态码、HTTP/1.1与HTTP/2对比](06-application/02-http-protocol.md)
- [文件传输与电子邮件：FTP双连接(控制21/数据20)、SMTP与POP3/IMAP](06-application/03-email-and-ftp.md)
