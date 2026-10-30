from pathlib import Path
import fitz,io,re,json
from fontTools.ttLib import TTFont
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.cu2quPen import Cu2QuPen
from lxml import html
import argparse
parser=argparse.ArgumentParser(description='Rebuild the paper font subsets from repository PDFs and Fandol fonts')
parser.add_argument('--fandol-dir',type=Path,required=True,help='Directory containing the Fandol OTF files from https://mirrors.ctan.org/fonts/fandol.zip')
args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
target=''.join(''.join(html.parse(str(root/f'408-{y}.html')).xpath('//body//text()[not(ancestor::script)]')) for y in [2023,2026])
target+=''.join(p.read_text() for p in (root/'tools').glob('*') if p.is_file())
chars=set(map(ord,target));char_maps={};sources=[]
for year in [2019,2024]:
 path=root.parent/'past_papers'/f'{year}年计算机408统考真题.pdf';doc=fitz.open(path);cache={}
 for pg in doc:
  available={}
  for f in pg.get_fonts():
   if f[1]!='ttf' or '+' not in f[3] or f[3].startswith('*'):continue
   family=f[3].split('+',1)[1]
   if family not in ['TimesNewRomanPSMT','TimesNewRomanPS-BoldMT','TimesNewRomanPS-ItalicMT','CourierNewPSMT']:continue
   if f[0] not in cache:
    blob=doc.extract_font(f[0])[3]
    if not blob:continue
    font=TTFont(io.BytesIO(blob));cache[f[0]]=font
   available.setdefault(family,[]).append((cache[f[0]],f[0]))
  for span in pg.get_texttrace():
   family=span['font']
   if family not in available:continue
   cmap=char_maps.setdefault(family,{})
   for uni,gid,*_ in span['chars']:
    if uni not in chars or uni in cmap:continue
    for ff,xref in available[family]:
     order=ff.getGlyphOrder()
     if gid>=len(order):continue
     name=order[gid]
     if ff['glyf'][name].numberOfContours==0 and chr(uni).strip():continue
     cmap[uni]=(ff,name,year,xref);break
print({k:len(v) for k,v in char_maps.items()})
fandol=args.fandol_dir
fb_song=TTFont(fandol/'FandolSong-Regular.otf');fb_hei=TTFont(fandol/'FandolHei-Bold.otf')
configs=[('song','SimSun',fb_song),('hei','SimHei',fb_hei),('roman','TimesNewRomanPSMT',TTFont('/usr/share/fonts/opentype/urw-base35/NimbusRoman-Regular.otf')),('roman-bold','TimesNewRomanPS-BoldMT',TTFont('/usr/share/fonts/opentype/urw-base35/NimbusRoman-Bold.otf')),('roman-italic','TimesNewRomanPS-ItalicMT',TTFont('/usr/share/fonts/opentype/urw-base35/NimbusRoman-Italic.otf')),('mono','CourierNewPSMT',TTFont('/usr/share/fonts/opentype/urw-base35/NimbusMonoPS-Regular.otf'))]
report={}
for dest,family,fallback in configs:
 native=char_maps.get(family,{})
 fallback_cmap=fallback.getBestCmap();available=chars.intersection(set(native)|set(fallback_cmap))
 if dest in ['song','hei']:available={c for c in available if c>255} # Latin and ASCII punctuation use actual Times New Roman.
 glyphs={};metrics={};cmap={};provenance={}
 empty=TTGlyphPen(None).glyph();glyphs['.notdef']=empty;metrics['.notdef']=(1024,0)
 for c in sorted(available):
  name='uni'+format(c,'04X');cmap[c]=name
  if c in native and dest not in ['song','hei']:font,gname,year,xref=native[c];provenance[chr(c)]=f'{year}:{xref}'
  else:font=fallback;gname=fallback_cmap[c];provenance[chr(c)]='fallback'
  glyphset=font.getGlyphSet();recording=DecomposingRecordingPen(glyphset);glyphset[gname].draw(recording)
  pen=TTGlyphPen(None);curve=Cu2QuPen(pen,1.0,reverse_direction=False);scale=2048/font['head'].unitsPerEm
  transform=TransformPen(curve,(scale,0,0,scale,0,0));recording.replay(transform)
  glyphs[name]=pen.glyph();advance,lsb=font['hmtx'][gname];metrics[name]=(round(advance*scale),round(lsb*scale))
 b=FontBuilder(2048,isTTF=True);b.setupGlyphOrder(list(glyphs));b.setupCharacterMap(cmap);b.setupGlyf(glyphs);b.setupHorizontalMetrics(metrics)
 # Match the original Windows text metrics, avoiding Noto CJK's much taller baseline.
 asc,desc=(1760,-288) if dest in ['song','hei'] else (1825,-443)
 if dest=='mono':asc,desc=1705,-615
 b.setupHorizontalHeader(ascent=asc,descent=desc,lineGap=0)
 b.setupNameTable({'familyName':'PaperMatched'+dest,'styleName':'Regular','uniqueFontIdentifier':'408-paper-subset-'+dest,'fullName':'408 Paper matched '+dest,'psName':'PaperMatched'+dest.replace('-',''),'version':'Version 1.0'})
 b.setupOS2(sTypoAscender=asc,sTypoDescender=desc,sTypoLineGap=0,usWinAscent=asc,usWinDescent=-desc,fsType=0)
 b.setupPost();b.setupMaxp();b.font.flavor='woff';b.save(root/'assets'/f'{dest}.woff')
 # Standalone HTML embeds only these document-specific WOFF subsets.
 cjk=[c for c in available if 0x4e00<=c<=0x9fff]
 report[dest]={'original_family':family,'glyphs':len(available),'from_embedded_source':sum(c in native and dest not in ['song','hei'] for c in available),'cjk_glyphs':len(cjk),'cjk_from_embedded_source':0,'fallback_family':fallback['name'].getDebugName(1),'fallback_characters':''.join(chr(c) for c in sorted(available) if (c not in native or dest in ['song','hei']) and 0x4e00<=c<=0x9fff)}
report['song']['selected_family']='FandolSong-Regular'
report['hei']['selected_family']='FandolHei-Bold'
previous=root/'data/font-match.json'
if previous.exists():
 previous_data=json.loads(previous.read_text())
 if 'calibration' in previous_data:report['calibration']=previous_data['calibration']
(root/'data/font-match.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
