#!/usr/bin/env python3
"""Validate review coverage, local destinations and folds; not a proof of answers."""
import json,re
from pathlib import Path
from urllib.parse import unquote
from build_review import outputs
ROOT=Path(__file__).resolve().parent.parent

def slug(text):
 text=re.sub(r'<[^>]+>','',text).lower()
 return re.sub(r'[^\w\-\s]','',text).replace(' ','-')

def check():
 metadata=json.loads((ROOT/'data/network_lessons.json').read_text())
 pages=set(ROOT.glob('daily-network/[0-9][0-9][0-9][0-9]/[0-9][0-9][0-9][0-9].md'))
 assert len(pages)==len(metadata)==96
 assert {ROOT/v['path'] for v in metadata.values()}==pages
 for key,v in metadata.items():
  s=(ROOT/v['path']).read_text()
  assert all(x in s for x in ('## 先合上解析','## 换一个条件','原视频','题图')),key
  assert s.count('<details>')==s.count('</details>')==3,key
  assert v['status']=='explained',key
 for rel,content in outputs().items():assert (ROOT/rel).read_text()==content,rel
 pages|=set(ROOT.glob('review/*.md'))|{ROOT/'README.md',ROOT/'ARCHITECTURE.md',ROOT/'src/README.md',ROOT/'daily-network/README.md',ROOT/'daily-network/2025/README.md',ROOT/'daily-network/2026/README.md'}
 for name in ('question_chain.json','written_chain.json'):
  pages|={ROOT/n['file'] for n in json.loads((ROOT/'data'/name).read_text())['nodes']}
 count=0
 for p in pages:
  s=p.read_text();assert s.count('<details>')==s.count('</details>'),p
  for link in re.findall(r'\]\(([^)]+)\)',s):
   if re.match(r'[a-z]+://',link):continue
   dest,_,anchor=link.partition('#');target=(p.parent/unquote(dest)).resolve() if dest else p
   assert target.exists(),(str(p),link)
   if anchor and target.suffix=='.md':
    t=target.read_text();anchors=set(re.findall(r'<a id="([^"]+)"',t))|{slug(h) for h in re.findall(r'^#+\s+(.+)',t,re.M)}
    assert unquote(anchor) in anchors,(str(p),link)
   count+=1
 print(f'96 complete lesson structures; 59 curated line cards; {count} local links/anchors checked. Subject reasoning requires human review.')
if __name__=='__main__':check()
