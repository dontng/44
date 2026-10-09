#!/usr/bin/env python3
"""Export audited answer Markdown, including every fold and current image.

Requires pandoc, ReportLab, PyMuPDF and Pillow. Intro occupies its own page;
questions then flow continuously. No Markdown or image is modified.
"""
import argparse
import hashlib
import html
import json
import re
import subprocess
import unicodedata
from pathlib import Path

import fitz
from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Image, Spacer, PageBreak, Table, TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
WIDTH = A4[0] - 80
FONT_DIR = ROOT / 'tmp/pdfs/fonts'
FONT_MAP = {}
REQUIRED_CHARS = set()


def register_fonts():
    FONT_DIR.mkdir(parents=True, exist_ok=True)
    cjk = FONT_DIR / 'DroidSansFallback.ttf'
    if not cjk.exists():
        cjk.write_bytes(fitz.Font('cjk').buffer)
    for name, path in [('CJK', cjk), ('Latin', Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')),
                       ('LatinBold', Path('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')),
                       ('Mono', Path('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'))]:
        pdfmetrics.registerFont(TTFont(name, str(path)))
        FONT_MAP[name] = pdfmetrics.getFont(name).face.charToGlyph
    pdfmetrics.registerFontFamily('CJK', normal='CJK', bold='CJK', italic='CJK', boldItalic='CJK')
    pdfmetrics.registerFontFamily('Latin', normal='Latin', bold='LatinBold', italic='Latin', boldItalic='LatinBold')
    pdfmetrics.registerFontFamily('Mono', normal='Mono', bold='Mono', italic='Mono', boldItalic='Mono')


def escaped(value, preferred='Latin'):
    """Select a font with an actual glyph, including Chinese inside code."""
    runs = []
    previous = None
    for char in value:
        REQUIRED_CHARS.add(char)
        font = preferred if ord(char) in FONT_MAP[preferred] else 'CJK'
        if char not in '\n\t\r' and ord(char) not in FONT_MAP[font]:
            raise ValueError(f'Missing glyph U+{ord(char):04X}: {char!r}')
        if font != previous:
            if previous:
                runs.append('</font>')
            runs.append(f'<font name="{font}">')
            previous = font
        runs.append(html.escape(char))
    if previous:
        runs.append('</font>')
    return ''.join(runs)


def normalized(value):
    return re.sub(r'\s+', '', unicodedata.normalize('NFKC', value))


def inline(nodes):
    out = []
    for node in nodes:
        kind, value = node['t'], node.get('c')
        if kind == 'Str': out.append(escaped(value))
        elif kind in ('Space', 'SoftBreak'): out.append(' ')
        elif kind == 'LineBreak': out.append('<br/>')
        elif kind == 'Strong': out.append('<b>' + inline(value) + '</b>')
        elif kind in ('Emph', 'Strikeout', 'SmallCaps'): out.append(inline(value))
        elif kind in ('Superscript', 'Subscript'):
            tag = 'super' if kind == 'Superscript' else 'sub'
            out.append(f'<{tag}>' + inline(value) + f'</{tag}>')
        elif kind == 'Code': out.append(escaped(value[1], 'Mono'))
        elif kind == 'Math': out.append(escaped(value[1]))
        elif kind in ('Link', 'Span', 'Quoted'): out.append(inline(value[1]))
        elif kind == 'RawInline':
            out.append(escaped(html.unescape(re.sub(r'<[^>]*>', '', value[1]))))
        else: raise ValueError(f'Unsupported inline: {kind}')
    return ''.join(out)


STYLES = {
    'body': ParagraphStyle('body', fontName='CJK', fontSize=10, leading=15, spaceAfter=7, wordWrap='CJK'),
    'title': ParagraphStyle('title', fontName='CJK', fontSize=18, leading=25, spaceAfter=14, wordWrap='CJK'),
    'heading': ParagraphStyle('heading', fontName='CJK', fontSize=12, leading=18, spaceBefore=10, spaceAfter=7, keepWithNext=True, wordWrap='CJK', textColor=colors.HexColor('#243b67')),
    'quote': ParagraphStyle('quote', fontName='CJK', fontSize=9, leading=14, leftIndent=10, spaceAfter=8, wordWrap='CJK', textColor=colors.HexColor('#526078')),
    'code': ParagraphStyle('code', fontName='CJK', fontSize=9, leading=13, spaceAfter=9, wordWrap='CJK', backColor=colors.HexColor('#f3f5f7'), borderPadding=5),
    'cell': ParagraphStyle('cell', fontName='CJK', fontSize=8, leading=12, wordWrap='CJK'),
}


def prepared(source):
    text = source.read_text()
    # PDF has no clickable folds: retain the contents of ALL details.
    text = re.sub(r'</?(?:details|summary|div)[^>]*>', '\n\n', text)
    text = re.sub(r'<a[^>]*>\s*</a>', '', text)
    # Isolate images before parsing, preserving the calibrated em width.
    images = []
    def image_token(match):
        images.append(match.group())
        return f'\n\nPDFIMAGE{len(images)-1:04d}\n\n'
    text = re.sub(r'<img\b[^>]*>', image_token, text)
    # Standalone navigation is meaningful in Markdown, not in a printed PDF.
    text = '\n'.join(line for line in text.splitlines() if not re.match(r'^\[(?:«|\d{4}-answer)', line))
    ast = json.loads(subprocess.check_output(['pandoc', '-f', 'markdown+raw_html', '-t', 'json'], input=text.encode()))
    return ast['blocks'], images


def export(source, target):
    blocks, images = prepared(source)
    story, expected_images, expected_text = [], [], []
    first_question = True

    def add_blocks(blocks, style='body'):
        nonlocal first_question
        for block in blocks:
            kind, value = block['t'], block.get('c')
            if kind in ('Para', 'Plain'):
                if len(value) == 1 and value[0]['t'] == 'Str' and re.fullmatch(r'PDFIMAGE\d{4}', value[0]['c']):
                    tag = images[int(value[0]['c'][8:])]
                    src = re.search(r'src="([^"]+)"', tag).group(1)
                    path = (source.parent / src).resolve()
                    with PILImage.open(path) as im: pw, ph = im.size
                    em = re.search(r'(?<![-\w])width:([\d.]+)em', tag)
                    # Markdown em width uses its 16px body font; preserve its
                    # ratio to the PDF 10pt body font rather than enlarging crops.
                    w = float(em.group(1))*10 if em else min(pw*.75, WIDTH)
                    scale = min(w/pw, WIDTH/pw, 640/ph)
                    image = Image(str(path), width=pw*scale, height=ph*scale)
                    image.hAlign = 'LEFT'
                    image.spaceAfter = 8
                    image.keepWithNext = image.drawHeight < 560
                    story.append(image)
                    expected_images.append({'path': str(path.relative_to(ROOT)), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
                else:
                    rendered = inline(value)
                    if rendered.strip():
                        expected_text.append(html.unescape(re.sub(r'<[^>]*>', '', rendered)))
                        story.append(Paragraph(rendered, STYLES[style]))
            elif kind == 'Header':
                level, _, nodes = value
                if level == 2 and first_question:
                    story.append(PageBreak()); first_question = False
                story.append(Paragraph(inline(nodes), STYLES['title' if level == 1 else 'heading']))
                expected_text.append(html.unescape(re.sub(r'<[^>]*>', '', inline(nodes))))
            elif kind == 'CodeBlock':
                lines = value[1].expandtabs(4).splitlines()
                rendered = '<br/>'.join(escaped(line.replace(' ', '\u00a0'), 'Mono') for line in lines)
                story.append(Paragraph(rendered or ' ', STYLES['code']))
                expected_text.append(value[1])
            elif kind == 'BlockQuote': add_blocks(value, 'quote')
            elif kind in ('BulletList', 'OrderedList'):
                items = value if kind == 'BulletList' else value[1]
                for i, item in enumerate(items):
                    story.append(Paragraph(escaped('•' if kind == 'BulletList' else f'{i+1}.'), STYLES['body']))
                    add_blocks(item, style)
            elif kind == 'Table':
                rows = list(value[3][1])
                for body in value[4]: rows.extend(body[2] + body[3])
                rows.extend(value[5][1])
                data = []
                for row in rows:
                    cells = []
                    for cell in row[1]:
                        parts = []
                        for b in cell[4]:
                            if b['t'] in ('Plain','Para'): parts.append(inline(b['c']))
                            else: raise ValueError(f'Unsupported table cell: {b["t"]}')
                        cells.append(Paragraph('<br/>'.join(parts), STYLES['cell']))
                        expected_text.extend(html.unescape(re.sub(r'<[^>]*>', '', part)) for part in parts)
                    data.append(cells)
                table = Table(data, colWidths=[WIDTH/len(data[0])]*len(data[0]), repeatRows=1, hAlign='LEFT')
                table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'), ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#eef2f8')), ('GRID',(0,0),(-1,-1),.35,colors.HexColor('#ccd4df')), ('LEFTPADDING',(0,0),(-1,-1),5), ('RIGHTPADDING',(0,0),(-1,-1),5)]))
                table.spaceAfter=10;story.append(table)
            elif kind == 'HorizontalRule': story.append(Spacer(1,5))
            elif kind == 'RawBlock':
                text = html.unescape(re.sub(r'<[^>]*>', '', value[1])).strip()
                if text: story.append(Paragraph(escaped(text), STYLES[style]))
            elif kind == 'Div': add_blocks(value[1],style)
            else: raise ValueError(f'Unsupported block: {kind}')

    add_blocks(blocks)
    target.parent.mkdir(parents=True, exist_ok=True)
    temp = target.with_suffix('.pending.pdf')
    def footer(canvas, doc):
        canvas.saveState();canvas.setFont('Latin',8);canvas.setFillColor(colors.HexColor('#68758a'))
        canvas.drawString(40,22,f'44 / {source.stem}');canvas.drawRightString(A4[0]-40,22,str(doc.page));canvas.restoreState()
    doc = SimpleDocTemplate(str(temp), pagesize=A4, leftMargin=40, rightMargin=40, topMargin=38, bottomMargin=40,
                            title=source.stem, author='dontng / Codex')
    doc.build(story,onFirstPage=footer,onLaterPages=footer)
    pdf = fitz.open(temp)
    errors=[]
    for i,page in enumerate(pdf):
        if not page.get_text().strip(): errors.append(f'blank page {i+1}')
        for item in page.get_text('dict')['blocks']:
            x0,y0,x1,y1=item['bbox']
            if x0 < 35 or x1 > A4[0]-35 or y0 < 30 or (item['type']==0 and y1 > A4[1]-32 and y0 < A4[1]-40):
                # Ignore the deliberate footer; flag overflow in actual content.
                if y0 < A4[1]-40: errors.append(f'overflow page {i+1}: {item["bbox"]}')
        if '\ufffd' in page.get_text(): errors.append(f'replacement glyph page {i+1}')
    actual_images=sum(len(p.get_image_info()) for p in pdf)
    if actual_images != len(expected_images): errors.append(f'images {actual_images} != {len(expected_images)}')
    actual_text = normalized(''.join(p.get_text(clip=fitz.Rect(0, 0, p.rect.width, p.rect.height-40)) for p in pdf))
    for fragment in expected_text:
        if normalized(fragment) not in actual_text:
            errors.append(f'missing text: {fragment[:100]!r}')
    # Compare decoded pixels as well as counts: the PDF must embed the current
    # source crops, not an older copy with the same name.
    decoded = []
    for page in pdf:
        for image in page.get_image_info(xrefs=True):
            pix = fitz.Pixmap(pdf, image['xref'])
            if pix.n != 3 or pix.alpha: pix = fitz.Pixmap(fitz.csRGB, pix)
            decoded.append(hashlib.sha256(pix.samples).hexdigest())
    for index, dependency in enumerate(expected_images):
        with PILImage.open(ROOT/dependency['path']) as image:
            pixel_hash = hashlib.sha256(image.convert('RGB').tobytes()).hexdigest()
        if index >= len(decoded) or pixel_hash != decoded[index]:
            errors.append(f'outdated image pixels: {dependency["path"]}')
    result={'source':str(source.relative_to(ROOT)), 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
            'pdf':str(target.relative_to(ROOT)), 'pages':len(pdf), 'images':expected_images,
            'text_blocks_checked':len(expected_text), 'errors':errors}
    pdf.close()
    if errors: raise ValueError(f'{source.name}: {errors}')
    temp.replace(target)
    result['pdf_sha256']=hashlib.sha256(target.read_bytes()).hexdigest()
    return result


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--only',nargs='*')
    parser.add_argument('--audit',type=Path,default=ROOT/'tmp/pdfs/new-audit.json')
    args=parser.parse_args();register_fonts()
    sources=sorted(p for p in (ROOT/'src').glob('*-answer.md') if re.fullmatch(r'\d{4}-answer',p.stem))
    if args.only: sources=[p for p in sources if p.stem[:4] in args.only]
    results=[]
    for source in sources:
        result=export(source,ROOT/'src/pdf'/f'{source.stem}.pdf');results.append(result)
        print(f'{source.stem}: {result["pages"]} pages, {len(result["images"])} images, verified',flush=True)
    args.audit.parent.mkdir(parents=True,exist_ok=True)
    args.audit.write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')


if __name__=='__main__': main()
