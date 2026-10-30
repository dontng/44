#!/usr/bin/env python3
"""Build the two standalone exam HTMLs. No network is used during the build."""
from pathlib import Path
from lxml import html, etree
import base64,json,re,hashlib
ROOT=Path(__file__).resolve().parents[1]
W,H=514.56,742.08

def data_uri(path,mime):return 'data:'+mime+';base64,'+base64.b64encode(path.read_bytes()).decode()
def font_css():
 out=[]
 for file,family,weight,style in [('song','PaperSong',400,'normal'),('hei','PaperHei',700,'normal'),('roman','PaperRoman',400,'normal'),('roman-bold','PaperRoman',700,'normal'),('roman-italic','PaperRoman',400,'italic'),('mono','PaperMono',400,'normal'),('symbols','PaperSymbols',400,'normal')]:
  out.append(f'@font-face{{font-family:{family};src:url("{data_uri(ROOT/"assets"/(file+".woff"),"font/woff")}") format("woff");font-weight:{weight};font-style:{style};font-display:block}}')
 return '\n'.join(out)
CSS='''
*{box-sizing:border-box}html{background:#e6e6e6;color:#000}body{margin:0;font-family:PaperRoman,PaperSong,PaperSymbols,serif;font-size:10pt;font-synthesis:weight}button{font:inherit;cursor:pointer}.toolbar{width:686px;max-width:100%;margin:20px auto 16px;display:flex;justify-content:space-between;align-items:center;font:14px system-ui,sans-serif;color:#333;gap:16px;padding:0 10px}.toolbar a{color:#333}.toolbar button{background:white;border:1px solid #aaa;border-radius:3px;padding:6px 14px}.papers{width:max-content;margin:0 auto}.paper{position:relative;width:514.56pt;height:742.08pt;background:white;-webkit-text-stroke:0.025pt #000;margin:0 0 20px;box-shadow:0 1px 5px #0002;overflow:hidden}.paper:last-child{margin-bottom:0}.line{position:absolute;white-space:pre;line-height:13pt;height:13pt;transform-origin:left center;font-size:10pt}.line b{font-family:PaperRoman,PaperSong,PaperSymbols,serif;font-weight:700}.line i{font-family:PaperRoman,PaperSong,PaperSymbols,serif}.line sup{font-size:70%;line-height:0;position:relative;vertical-align:super}.line .node{border:0.5pt solid #333;padding:2pt 4pt}.qno{position:absolute;left:-20.6pt;font-weight:bold}.diagram{position:absolute;display:block}.footer{position:absolute;top:694pt;left:0;width:100%;text-align:center;font-size:10pt;line-height:14pt}.codeblock{position:absolute;background:#e5e5e5;font:10pt/12.3pt PaperMono,PaperSong,monospace;white-space:pre;margin:0;padding:0 18pt;overflow:visible}.codeblock .cn{font-family:PaperSong,serif}.cover-title{position:absolute;top:104pt;left:65pt;width:385pt;text-align:center;font-family:PaperRoman,PaperHei,sans-serif;font-size:20.2pt;line-height:29.5pt;font-weight:700}.cover-code{position:absolute;top:174pt;left:0;width:100%;text-align:center;font-size:14pt}.cover-notice{position:absolute;left:0;top:246pt;width:100%;font-family:PaperHei,sans-serif;font-size:12pt;font-weight:700;text-align:center}.candidate{position:absolute;left:42pt;top:566pt;width:430pt;border-collapse:collapse;font-size:10pt;table-layout:fixed}.candidate td{border:.5pt solid #222;height:24pt;text-align:center}.candidate col:first-child{width:60pt}.candidate td:first-child{width:60pt}.candidate-caption{position:absolute;top:546pt;left:0;width:100%;font-size:10pt;text-align:center}.native-table{border-collapse:collapse;font-size:10pt;line-height:15.7pt}.native-table th,.native-table td{font-weight:normal;padding:0 2pt;text-align:center;border-bottom:.6pt solid #111;border-right:.5pt solid #111}.native-table th:last-child,.native-table td:last-child{border-right:0}.native-table thead{border-top:1pt solid #111}.native-table tr:last-child{border-bottom:1pt solid #111}.assembly{position:absolute;left:64pt;top:216pt;width:411pt;font:9.8pt/15.4pt PaperRoman,PaperSong,PaperSymbols,serif;border-collapse:collapse}.assembly td{padding:0;white-space:pre;height:15.4pt}.assembly td:nth-child(1){width:18pt}.assembly td:nth-child(2){width:50pt}.assembly td:nth-child(3){width:159pt}.assembly .band td{background:#d7d7d7;height:12pt;line-height:12pt;padding-left:18pt}.assembly .bold{font-weight:bold}.pseudocode{position:absolute;top:44pt;height:120pt;border:.5pt solid #111;font-size:9pt;line-height:12.6pt}.pseudocode header{text-align:center;border-bottom:.5pt solid #111;height:13pt;line-height:12pt}.pseudocode .inner{padding:2pt 5pt;white-space:pre}.pseudocode .dashed{border:.5pt dashed #555;margin-right:30pt;position:relative}.pseudocode .zone{position:absolute;right:-32pt;top:50%;transform:translateY(-50%);font-size:9pt}.code-caption{position:absolute;top:166pt;font-size:10pt;text-align:center}.flow-content{position:absolute;left:43.5pt;right:38pt;top:45pt;bottom:67pt;font-size:10pt;line-height:15.3pt}.flow-content p{margin:0}.flow-content .section-heading{font-size:10pt;font-weight:700;margin:0 0 5pt;line-height:15.3pt}.question{margin:0 0 5pt 20.6pt;position:relative}.question .qnum{position:absolute;left:-20.6pt;font-weight:700}.question .score{font-weight:normal}.question p{margin:0}.question figure{margin:3pt auto;text-align:center;break-inside:avoid}.question figure svg{display:block;margin:auto;max-width:100%;height:auto}.question figure svg text{font-family:PaperRoman,PaperSong,PaperSymbols,serif!important}.question table{border-collapse:collapse;margin:3pt auto;font-size:9pt;line-height:13pt}.question th,.question td{padding:1pt 6pt!important;border-bottom:.5pt solid #111;text-align:center!important;font-weight:normal}.question thead{border-top:1pt solid #111}.question tr:last-child{border-bottom:1pt solid #111}.question pre{white-space:pre-wrap;font:9pt/12pt PaperMono,PaperSong,monospace;margin:3pt 0;background:#e7e7e7;padding:3pt 8pt;tab-size:4}.question p code{font-family:PaperRoman,PaperSong,PaperSymbols,serif}.question pre code{font:inherit}.question .options{display:grid;gap:0 5pt;margin:1pt 0 0;line-height:15.3pt}.question .option{display:flex;align-items:baseline;gap:3pt;min-width:0}.question .option-label{flex:none}.question .option-content{min-width:0}.question .options.code-options{font-size:8.8pt;line-height:13.5pt}.question .assertions{display:grid;grid-template-columns:1fr 1fr;column-gap:8pt;margin:1pt 0}.question .assertions p{break-inside:avoid}.question sup,.question sub{font-size:70%;line-height:0}.question .continuation{color:#444;font-size:8pt;margin-bottom:2pt}.question[data-number="26"] figure{float:right;margin:0 0 2pt 7pt}.question[data-number="26"]:after{content:"";display:table;clear:both}.question[data-number="37"] figure{float:none;width:100%;margin:3pt auto}.question[data-number="37"] table{font-size:9pt}.question[data-number="37"] .options{clear:both}
@media print{@page{size:514.56pt 742.08pt;margin:0}html,body{background:white;margin:0!important;padding:0!important}.toolbar{display:none!important}.papers{margin:0}.paper{margin:0;box-shadow:none;break-after:page;page-break-after:always}.paper:last-child{break-after:auto;page-break-after:auto}*{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
'''
NOTICE=[
(289.2,'1. 答题前，考生在试题册指定位置上填写考生编号和考生姓名；在答题卡指定位置上填写报考单位、'),
(312.2,'考生姓名和考生编号，并涂写考生编号信息点。'),
(335.3,'2. 考生须把试题册上的“试卷条形码”粘贴条取下，粘贴在答题卡的“试卷条形码粘贴位置”框中，'),
(358.5,'不按规定粘贴条形码而影响评卷结果的，责任由考生自负。'),
(381.8,'3. 选择题的答案必须涂写在答题卡和相应题号的选项上，非选择题的答案必须书写在答题卡指定位'),
(405.0,'置的边框区域内，超出答题区域书写的答案无效；在草稿纸、试题册上答题无效。'),
(428.2,'4. 填（书）写部分必须使用黑色字迹签字笔书写，字迹工整、笔迹清楚；涂写部分必须使用 2B 铅'),
(451.3,'笔涂写。'),
(474.5,'5. 考试结束，将答题卡和试题册按规定交回。')]

def cover(year):
 text=f'<section class="paper cover" aria-label="{year} 年试卷封面"><h1 class="cover-title" style="margin:0">{year} 年全国硕士研究生招生考试<br>计算机学科专业基础试题</h1><div class="cover-code">（科目代码：408）</div><h2 class="cover-notice" style="margin:0">考生注意事项</h2>'
 for y,s in NOTICE:
  x=42 if re.match(r'\d\.',s) else 55
  text+=f'<div class="line" style="left:{x}pt;top:{y-6.7}pt" data-fit="{472-x}">{s}</div>'
 text+='<div class="candidate-caption">（以下信息考生必须认真填写）</div><table class="candidate" aria-label="考生信息"><colgroup><col>'+''.join('<col>' for _ in range(15))+'</colgroup><tbody><tr><td>考生编号</td>'+15*'<td></td>'+'</tr><tr><td>考生姓名</td><td colspan="15"></td></tr></tbody></table></section>'
 return text

def line_html(y,s,page,geometry):
 x={2:64.3,3:65.3,4:63.0,5:63.7,6:65.0,7:64.3,8:66.0}[page]
 ishead=s.startswith('!');s=s.lstrip('!')
 if ishead and ('一、' in s or '二、' in s):x-=20.6
 if s.startswith('&gt;'):x+=16.5;s=s[4:]
 q=re.match(r'^(\d{2})\. (.*)',s)
 attrs=''
 if q:s=f'<b class="qno">{q[1]}.</b>{q[2]}';attrs=f' data-question="{int(q[1])}" id="q{int(q[1])}"'
 columns=s.split('||');out=[]
 g=min(geometry,key=lambda l:abs(l['y']-y))
 for i,col in enumerate(columns):
  if len(columns)>1:
   # The original uses two/four columns, with special compact rows beside figures.
   step=206 if len(columns)==2 else (103 if len(columns)==4 else (82.4 if len(columns)==5 else 137.3))
   if page==2 and abs(y-409.2)<1:step=77.5
   if page==2 and abs(y-454.3)<1:step=121
   xx=x+i*step
   if page==2 and abs(y-454.3)<1:xx=[63.7,184.0,339.0][i]
   limit=step-3 if i<len(columns)-1 else 478-xx
   if page==2 and abs(y-454.3)<1:limit=[117,151,139][i]
   right=max(( (int(w['left'])+int(w['width']))/3 for w in g['words'] if xx-3<=int(w['left'])/3<xx+limit),default=xx+limit)
   width=min(limit,right-xx)
  else:
   xx=x;width=g['right']-x
   if page==6 and y in (320.5,335.8,351.7,367.5):width=min(width,320)
  if width<15:width=478-xx
  out.append(f'<div class="line'+(' heading' if ishead else '')+f'" style="left:{xx:.2f}pt;top:{y-6.7:.2f}pt'+(';font-weight:700' if ishead else '')+f'" data-fit="{width:.2f}"'+attrs+'>'+col+'</div>')
 return ''.join(out)

def extras(page):
 if page==3:return '<pre class="codeblock" style="left:65pt;top:570pt;width:412pt;height:62pt">I1    add  S2, S1, S0        // R[S2] ← R[S1] + R[S0]\nI2    load S3, 0(S2)         // R[S3] ← M[R[S2] + 0]\nI3    beq  t2, S3, L1        // if R[t2] = R[S3] jump to L1\nI4    addi t2, t2, 20        // R[t2] ← R[t2] + 20\nI5 L1:  …</pre>'
 if page==4:return '<table class="native-table" style="position:absolute;left:133pt;top:575pt;width:247pt;table-layout:fixed;white-space:nowrap"><colgroup><col style="width:38pt"><col style="width:93pt"><col style="width:39pt"><col style="width:77pt"></colgroup><thead><tr><th>进程名</th><th>进入就绪队列的时刻</th><th>优先数</th><th>CPU 的执行时间</th></tr></thead><tbody><tr><td>P1</td><td>0ms</td><td>1</td><td>60ms</td></tr><tr><td>P2</td><td>20ms</td><td>10</td><td>42ms</td></tr><tr><td>P3</td><td>30ms</td><td>100</td><td>13ms</td></tr></tbody></table>'
 if page==6:return '<pre class="codeblock" style="left:65pt;top:244pt;width:411pt;height:61pt">typedef struct {            <span class="cn">// 图的类型定义</span>\n   int numVertices,numEdges;<span class="cn">// 图的顶点数和有向边数</span>\n   char VerticesList[MAXV]; <span class="cn">// 顶点表，MAXV为已定义常量</span>\n   int Edge[MAXV][MAXV];    <span class="cn">// 邻接矩阵</span>\n} MGraph;</pre><pre class="codeblock" style="left:65pt;top:536pt;width:411pt;height:61pt">int a[24][24];\n……\nfor(i=0; i&lt;24; i++)\n   for(j=0; j&lt;64; j++)\n      a[i][j] = 10;</pre>'
 if page==7:
  rows=[('band','for (i = 0; i &lt; 24; i++)'),('',('1','00401072','C7 45 F8 00 00 00 00','mov[ebp - 8], 0')),('bold',('2','00401079','EB 09','jmp 00401084h')),('',('3','0040107B','8B 55 F8','mov eax, [ebp - 8]')),('',('','……','……','……')),('bold',('7','00401088','7D 32','jge 004010bch')),('band','for (j = 0; j &lt; 64; j++)'),('',('8','0040108A','C7 45 FC 00 00 00 00','mov[ebp - 4], 0')),('',('','……','……','……')),('band','a[i][j] = 10;'),('',('','……','……','……')),('bold',('19','004010AE','C7 84 82 00 20 42 00 0A 00 00 00','mov[ecx + edx * 4 + 00422000h], 0Ah')),('',('20','……','……','……'))]
  table='<table class="assembly"><tbody>'
  for cl,r in rows:
   table+=f'<tr class="{cl}">'+(f'<td colspan="4">{r}</td>' if cl=='band' else ''.join('<td>'+c+'</td>' for c in r))+'</tr>'
  table+='</tbody></table>'
  return '<pre class="codeblock" style="left:81pt;top:139pt;width:394pt;height:35pt">for(j=0; j&lt;64; j++)\n   for(i=0; i&lt;24; i++)\n      a[i][j]=10;</pre>'+table
 if page==8:return '''<section class="pseudocode" style="left:87pt;width:214pt"><header>某同学编写的伪代码</header><div class="inner">bool lock = FALSE ;　 // 共享变量
 ……
<div class="dashed">bool key = TRUE ;
if (key == TRUE)
    swap key, lock ;  // 交换 key 和 lock 的值<span class="zone">进入区</span></div> 临界区 ;
<div class="dashed">lock = TRUE ;<span class="zone">退出区</span></div> ……</div></section><section class="pseudocode" style="left:319pt;width:132pt"><header>newSwap() 的代码</header><div class="inner">void newSwap(bool *a, bool *b) {
    bool temp = *a ;
    *a = *b ;
    *b = temp ;
}</div></section><div class="code-caption" style="left:87pt;width:214pt">(a)</div><div class="code-caption" style="left:319pt;width:132pt">(b)</div>'''
 return ''

FIT_JS='''
function fitLines(){document.querySelectorAll('[data-fit]').forEach(el=>{const w=parseFloat(el.dataset.fit)*4/3;const natural=el.getBoundingClientRect().width;const s=w/natural;if(s<1.15&&s>.6)el.style.transform=`scaleX(${s})`;});}
'''

def shell(year,pages,script):
 return '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+str(year)+' 年 408 真题</title><style>'+font_css()+CSS+'</style></head><body><nav class="toolbar" aria-label="试卷操作"><span>'+str(year)+' 年 · 计算机学科专业基础</span><span><a href="408-'+('2026' if year==2023 else '2023')+'.html">'+('2026' if year==2023 else '2023')+' 卷</a>　<button id="print" disabled>打印试卷</button></span></nav><main class="papers">'+pages+'</main><script>'+script+'</script></body></html>'

def build_2023():
 geo=json.loads((ROOT/'data/2023-geometry.json').read_text());figs=json.loads((ROOT/'data/2023-figures.json').read_text());pages={};p=None
 for ln in (ROOT/'data/2023-layout.txt').read_text().splitlines():
  if not ln or ln.startswith('#'):continue
  if ln.startswith('['):p=int(ln[1:-1]);pages[p]=[];continue
  y,s=ln.split('|',1);pages[p].append(line_html(float(y),s,p,geo[str(p)]))
 out=cover(2023)
 for p,lines in pages.items():
  out+=f'<section class="paper replica" aria-label="第 {p} 页">'+''.join(lines)+extras(p)
  for fig in figs:
   if fig['page']!=p:continue
   x,y,r,b=fig['box'];src=data_uri(ROOT/fig['src'],'image/png')
   out+=f'<img class="diagram" src="{src}" alt="原卷第 {p} 页配图" style="left:{x}pt;top:{y}pt;width:{r-x}pt;height:{b-y}pt">'
  out+=f'<div class="footer">第 {p} 页（共 8 页）</div></section>'
 script=FIT_JS+'''document.fonts.ready.then(()=>{fitLines();window.paperReady=true;document.getElementById('print').disabled=false;});document.getElementById('print').onclick=()=>window.print();'''
 (ROOT/'408-2023.html').write_text(shell(2023,out,script))

# Display widths in points, measured for the print column rather than from web-card dimensions.
FIG_WIDTH={2:110,26:90,28:280,36:395,37:350,43:335,44:395,46:100,47:300}

def clean_2026(q):
 wrap=html.fragment_fromstring('<div>'+q['html']+'</div>')
 for e in wrap.xpath('.//figure/img'):
  path=ROOT/e.get('src');svg=etree.fromstring(path.read_bytes());prefix='q'+str(q['number'])+'-'+path.stem[:12]+'-'
  ids={v:prefix+v for v in svg.xpath('//@id')}
  for el in svg.iter():
   for k,v in list(el.attrib.items()):
    if k=='id':el.set(k,ids[v])
    else:
     for old,new in ids.items():v=v.replace('url(#'+old+')','url(#'+new+')')
     el.set(k,v)
  width=FIG_WIDTH[q['number']]
  if q['number']==43 and 'fig2' in path.name:width=200
  minimum={36:19,37:22,44:16,47:16}.get(q['number'],0)
  if minimum:
   for item in svg.xpath('//*[local-name()="text"]'):
    if item.get('font-size'):item.set('font-size',str(max(float(item.get('font-size')),minimum)))
  svg.set('style',f'width:{width}pt;max-width:100%;height:auto')
  svg.set('role','img');svg.set('aria-label',e.get('alt'))
  e.getparent().replace(e,svg)
 # Roman-numeral statements may share a two-column row, exactly as in the model paper.
 ps=list(wrap);i=0
 while i<len(ps):
  if ps[i].tag=='p' and re.match(r'^(?:I{1,3}|IV|V)\.',ps[i].text_content()):
   group=[]
   while i<len(ps) and ps[i].tag=='p' and re.match(r'^(?:I{1,3}|IV|V)\.',ps[i].text_content()):group.append(ps[i]);i+=1
   grid=html.Element('div',{'class':'assertions'});firstidx=wrap.index(group[0])
   if max(len(e.text_content()) for e in group)>37:grid.set('style','grid-template-columns:1fr')
   for e in group:wrap.remove(e);grid.append(e)
   wrap.insert(firstidx,grid)
  else:i+=1
 return ''.join(etree.tostring(e,encoding='unicode',method='html') for e in wrap)

def build_2026():
 qs=json.loads((ROOT/'data/2026.json').read_text());cards=[]
 for q in qs:
  n=q['number'];body=clean_2026(q)
  if n>40:body=body.replace('<p>','<p><span class="score">（'+str(q['score'])+' 分）</span>',1)
  if n==1:cards.append('<h2 class="section-heading">一、单项选择题：01～40 小题，每小题 2 分，共 80 分。下列每题给出的四个选项中，只有一个选项是最符合题目要求的。</h2>')
  if n==41:cards.append('<h2 class="section-heading">二、综合应用题：41～47 小题，共 70 分。</h2>')
  opts=''
  if q['options']:
   lens=[len(html.fragment_fromstring('<div>'+o['html']+'</div>').text_content()) for o in q['options']]
   columns=4 if max(lens)<=16 else 2 if max(lens)<=35 else 1
   if n==2:columns=1
   opts=f'<div class="options'+(' code-options' if n==2 else '')+f'" style="grid-template-columns:repeat({columns},minmax(0,1fr))">'+''.join('<div class="option"><span class="option-label">'+o['letter']+'.</span><div class="option-content">'+o['html']+'</div></div>' for o in q['options'])+'</div>'
  cards.append(f'<article class="question" data-number="{n}" id="q{n}"><span class="qnum">{n:02}.</span><div class="qbody">'+body+'</div>'+opts+'</article>')
 # The source is hidden until all fonts and SVG glyphs are ready; pagination is based on actual browser sizes.
 pages=cover(2026)+'<div id="flow-source" style="display:none">'+''.join(cards)+'</div>'
 script=FIT_JS+(ROOT/'tools/paginate.js').read_text()
 (ROOT/'408-2026.html').write_text(shell(2026,pages,script))

if __name__=='__main__':
 build_2023();build_2026()
 for y in [2023,2026]:
  p=ROOT/f'408-{y}.html';print(p.name,p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest())
