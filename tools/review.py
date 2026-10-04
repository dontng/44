#!/usr/bin/env python3
"""Local review queue based only on real, append-only attempts."""
import argparse,json,uuid
from collections import defaultdict
from datetime import date,datetime,timedelta,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
INTERVALS=(1,3,7,14,30,60)
RESULTS=('independent','prompted','uncertain','failed')
MODES=('original','transfer','mixed')

def catalog(root=ROOT):
 items={}
 for name in ('question_chain.json','written_chain.json'):
  for n in json.loads((root/'data'/name).read_text())['nodes']:
   for pos,qid in enumerate(n['questions'],1):
    key='q:'+qid
    if key in items:
     items[key]['lines'].append(n['line_id']);continue
    items[key]={'id':key,'title':qid+' · '+n['title'],'group':n['line_id'],'lines':[n['line_id']],
     'path':n['file']+f'#{pos:02d}--{qid}','answer':f"src/{n['key']}-answer.md",'review':f"review/main.md#r{n['key']}",
     'minutes':20 if name=='written_chain.json' else 4}
 for key,v in json.loads((root/'data/network_lessons.json').read_text()).items():
  k='net:'+key;items[k]={'id':k,'title':v['title'],'group':'net:'+v['skill'],'lines':[],
   'path':v['path'],'answer':v['path']+'#先合上解析','review':v['path']+'#换一个条件','minutes':v['minutes']}
 return items

def read_events(directory):
 events=[]
 if not directory.exists():return events
 for p in sorted(directory.glob('*.json')):
  e=json.loads(p.read_text())
  if not all(k in e for k in ('id','item','date','result','mode','note','created_at')):raise ValueError(f'Invalid event: {p}')
  date.fromisoformat(e['date'])
  if e['result'] not in RESULTS or e['mode'] not in MODES:raise ValueError(f'Invalid result/mode: {p}')
  if e.get('reinforces') and (e['result']!='independent' or e['mode']=='original' or not e.get('transfer_note')):raise ValueError(f'Invalid transfer evidence: {p}')
  events.append(e)
 if len({e['id'] for e in events})!=len(events):raise ValueError('Duplicate event ID')
 return sorted(events,key=lambda e:(e['date'],e['created_at'],e['id']))

def append_event(directory,items,item,result,note,mode='original',when=None,seconds=None,reinforces=None,transfer_note=None):
 when=when or date.today()
 if when>date.today():raise ValueError('不能预写未来作答')
 if item not in items:raise ValueError('题号不存在：'+item)
 if result not in RESULTS or mode not in MODES:raise ValueError('未知作答类型')
 if not note.strip():raise ValueError('必须保存实际作答依据/卡点，不只写通过')
 if seconds is not None and seconds<=0:raise ValueError('实际耗时必须大于0')
 if reinforces:
  if reinforces not in items or reinforces==item:raise ValueError('被加固题须是另一个已知题号')
  if result!='independent' or mode=='original' or not (transfer_note or '').strip():raise ValueError('加固需独立迁移/混合作答，并写出复用了旧题哪一步')
  if not any(e['item']==reinforces and e['date']<when.isoformat() for e in read_events(directory)):
   raise ValueError('旧题须有此前日期的实际记录，不能批量预填未学题')
 uid=uuid.uuid4().hex
 event={'id':uid,'item':item,'date':when.isoformat(),'created_at':datetime.now(timezone.utc).isoformat(),'result':result,'mode':mode,'note':note.strip()}
 if seconds is not None:event['seconds']=seconds
 if reinforces:event.update(reinforces=reinforces,transfer_note=transfer_note.strip())
 directory.mkdir(parents=True,exist_ok=True)
 with (directory/(when.isoformat()+'-'+uid+'.json')).open('x',encoding='utf-8') as f:
  json.dump(event,f,ensure_ascii=False,indent=2);f.write('\n')
 return event

def states(events,as_of):
 by=defaultdict(list)
 for e in events:
  if date.fromisoformat(e['date'])>as_of:continue
  by[e['item']].append(e)
  if e.get('reinforces'):by[e['reinforces']].append(dict(e,item=e['reinforces'],note=e['transfer_note'],mode='transfer'))
 out={}
 for key,rows in by.items():
  days=defaultdict(list)
  for e in rows:days[e['date']].append(e)
  level=-1;success=0;transfer=0;next_due=None;result=None
  for day,es in sorted(days.items()):
   current=date.fromisoformat(day)
   bad=any(e['result']!='independent' for e in es)
   if bad:
    level=-1;result=next(e['result'] for e in reversed(es) if e['result']!='independent');next_due=current+timedelta(days=1)
   else:
    result='independent';success+=1
    if any(e['mode'] in ('transfer','mixed') for e in es):transfer+=1
    # Early/same-day repetitions cannot accelerate spacing.
    if next_due is None or current>=next_due:
     level=min(level+1,len(INTERVALS)-1);next_due=current+timedelta(days=INTERVALS[max(level,0)])
  last=max(days)
  out[key]={'last':last,'due':next_due.isoformat(),'interval':INTERVALS[max(level,0)],'independent_days':success,'transfer_days':transfer,'result':result,'note':days[last][-1]['note']}
 return out

def choose(items,state,today,limit=5,minutes=25):
 due=[k for k,s in state.items() if s['due']<=today.isoformat() and k in items]
 due.sort(key=lambda k:(state[k]['result']=='independent',state[k]['due'],k))
 chosen=[];used=set();cost=0
 for diverse in (True,False):
  for k in due:
   if k in chosen or len(chosen)>=limit:continue
   if diverse and items[k]['group'] in used:continue
   m=items[k]['minutes']
   if cost+m>minutes:continue
   chosen.append(k);cost+=m;used.add(items[k]['group'])
 return chosen,len(due)-len(chosen),cost

def main(argv=None):
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--events-dir',type=Path,default=ROOT/'data/review_events')
 sub=p.add_subparsers(dest='command',required=True)
 t=sub.add_parser('today');t.add_argument('--date',type=date.fromisoformat,default=date.today());t.add_argument('--limit',type=int,default=5);t.add_argument('--minutes',type=int,default=25)
 a=sub.add_parser('record');a.add_argument('item');a.add_argument('result',choices=RESULTS);a.add_argument('--note',required=True);a.add_argument('--mode',choices=MODES,default='original');a.add_argument('--date',type=date.fromisoformat);a.add_argument('--seconds',type=float);a.add_argument('--reinforces');a.add_argument('--transfer-note')
 l=sub.add_parser('list');l.add_argument('query',nargs='?',default='');sub.add_parser('status')
 a=p.parse_args(argv);items=catalog()
 if a.command=='list':
  for k,v in items.items():
   if a.query.lower() in (k+' '+v['title']).lower():print(k,'|',v['title'],'|',v['path'])
  return
 if a.command=='record':
  e=append_event(a.events_dir,items,a.item,a.result,a.note,a.mode,a.date,a.seconds,a.reinforces,a.transfer_note);print('已追加真实作答：',e['id']);return
 events=read_events(a.events_dir);today=a.date if a.command=='today' else date.today();s=states(events,today)
 unknown=set(s)-items.keys()
 if unknown:raise ValueError('记录包含未知题号：'+', '.join(sorted(unknown)))
 if a.command=='status':
  print(f'可检索 {len(items)} 道唯一题；已有实际记录 {len(s)} 道；原始事件 {len(events)} 条。');print('未记录=未验证；不导入历史box/due，不由内容完成率推算成绩。');return
 if a.limit<1 or a.minutes<1:raise ValueError('预算须为正数')
 if not s:
  print('尚无新作答记录，没有到期欠账。任选一个已学入口；未学过则先学一题：')
  for k in ('q:2011-01','net:2025-0912'):print(k,'|',items[k]['title'],'|',items[k]['path'])
  return
 selected,waiting,cost=choose(items,s,today,a.limit,a.minutes)
 print(f'本次 {len(selected)} 项，预计 {cost} 分钟；另有 {waiting} 项待选，保留原日期，不自动算失败。')
 for k in selected:
  v=items[k];st=s[k];print('\n'+k+' | '+v['title']);print('先做：',v['path'],'| 机制检查：',v['review']);print('上次：',st['result'],'| 到期：',st['due'],'| 卡点/依据：',st['note'])
 if not selected:print('预算内没有到期项；不强制塞新题。大题默认留20分钟，可提高--minutes后整题作答。')
if __name__=='__main__':
 try:main()
 except (ValueError,KeyError,json.JSONDecodeError) as e:raise SystemExit(str(e))
