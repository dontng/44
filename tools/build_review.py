#!/usr/bin/env python3
"""Render review entry points from curated prompts; never touch question/answer sheets."""
import argparse,json
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
NAMES={'dhcp':'地址自动配置','ppp':'PPP','hamming':'海明码','delay':'时延与在途量','aloha':'介质竞争','framing':'帧定界','medium-access':'介质访问','tcp-timer':'TCP计时器','multicast':'组播地址','ipv6':'IPv6','wifi':'无线LAN','http-state':'HTTP状态','bgp':'BGP','checksum':'检验和','routing':'寻址与路由','ospf':'OSPF','ip-address':'IPv4地址','subnet':'子网划分','encapsulation':'分层封装','packetization':'分组流水线','physical-interface':'物理接口','line-code':'线路编码','modulation':'调制','capacity':'信道容量','capacity-bdp':'容量与在途量','cdma':'CDMA','csma-cd':'CSMA/CD','mac-address':'MAC地址','address-space':'地址空间','fragmentation':'IPv4分片','crc':'CRC','arq-window':'可靠链路窗口','application':'应用协议','tcp-sequence':'TCP序号','network-device':'互连设备','routing-delay':'路径与时延','routing-arp':'路径与ARP','integrated-lan':'LAN综合','error-control':'差错控制','tcp-congestion':'拥塞控制','csma':'CSMA','packet-decode':'报文字节解码','ip-header':'首部与填充','tcp-handshake':'TCP握手','tcp-timing':'TCP时间线','http-delay':'HTTP时序','dns':'DNS','ftp-tcp':'FTP与TCP','layering':'分层机制','capacity-csma':'容量与最短帧','sdn':'SDN','reliability':'可靠传输','collision-domain':'冲突域'}
NAMES.update({'icmp':'ICMP与TTL','ip-forward':'IP转发','ip-multicast':'组播映射','mac-access':'介质访问','ppp-stuffing':'PPP填充','tcp-window':'TCP窗口','transport-service':'传输服务','wifi-address':'无线地址','wifi-backoff':'无线退避','wifi-nav':'无线虚拟载波监听'})
def load(name):return json.loads((ROOT/'data'/name).read_text())
def outputs():
 prompts=load('review_prompts.json');network=load('network_lessons.json')
 nodes=load('question_chain.json')['nodes']+load('written_chain.json')['nodes']
 assert set(prompts)=={n['key'] for n in nodes}
 out={};s=['# 真题闭卷复盘：59条线\n','[复习入口](README.md) · [原题总索引](../src/README.md)\n','每次只进入当前学过的一条线。下面的检查卡用于暴露机制缺口，不代替全题验收；原题和解析仍各保留一份。先回答再展开，变式也先独立完成。选题时用该线第一道尚未做过或已到期的题；大题必须连同全部小问完整作答。\n','| 节点 | 复盘方向 |\n| --- | --- |']
 for n in nodes:s.append(f"| [{n['key']}](#r{n['key']}) | {n['title']} |")
 for n in nodes:
  k=n['key'];p=prompts[k];s+=['',f'<a id="r{k}"></a>',f"## {k} · {n['title']}",'',f"[原题](../{n['file']}) · [完整解析](../src/{k}-answer.md)",'',p['prompt'],'','<details>','<summary>回答后核对机制</summary>','',p['check'],'','</details>','','**改一个条件：** '+p['variation'],'','<details>','<summary>变式完成后核对</summary>','',p['answer'],'','</details>','','回到原题，指出哪条已知条件让这条机制能用；不会时只展开对应断点。卡片通过不代表本线所有题通过。']
 out['review/main.md']='\n'.join(s)+'\n'
 groups=defaultdict(list)
 for key,v in network.items():groups[v['skill']].append((key,v))
 s=['# 网络复盘：按机制找回，不按旧日期补债\n','[复习入口](README.md) · [真题计网线](main.md#r0901)\n','96道原题均已有解析、闭卷检查、变式核对和关联题。这里按机制集合，不另复制答案。每次只选当前需要的一题；能在新题独立用出同一机制时，记录具体加固证据，不把同组所有题自动判为通过。\n']
 for skill,entries in sorted(groups.items()):
  s += [f'## {NAMES.get(skill,skill)}','', '| 原题 | 复盘目标 |','| --- | --- |']
  for k,v in entries:s.append(f"| [{k}](../{v['path']}) | {v['title']}"+('（含题面边界说明）' if v['boundary'] else '')+' |')
  s.append('')
 out['review/network.md']='\n'.join(s).rstrip()+'\n'
 for year in ['2025','2026']:
  subset=[(k,v) for k,v in sorted(network.items()) if k.startswith(year)]
  s=[f'# {year}年发布：计算机网络每日一题\n','[总目录](../README.md) · [按机制复盘](../../review/network.md)\n',f'{len(subset)}道现有题图已补完整讲解。年份按发布日期，题图上的考研年份可能是下一年；不为缺失日期编造题。\n','| 日期 | 原题实际考点 |','| --- | --- |']
  for k,v in subset:s.append(f"| [{k[5:7]}-{k[7:]}]({k[5:]}.md) | {v['title']} |")
  out[f'daily-network/{year}/README.md']='\n'.join(s)+'\n'
 return out

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');a=parser.parse_args();bad=[]
 for rel,content in outputs().items():
  p=ROOT/rel
  if a.check:
   if not p.exists() or p.read_text()!=content:bad.append(rel)
  else:p.parent.mkdir(parents=True,exist_ok=True);p.write_text(content)
 if bad:raise SystemExit('Review output differs: '+', '.join(bad))
 print('review entries: 59 main lines, 96 network lessons; '+('checked' if a.check else 'rendered'))
if __name__=='__main__':main()
