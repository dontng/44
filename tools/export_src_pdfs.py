#!/usr/bin/env python3
"""Export the dated src question chains to one PDF per Markdown file.

The source Markdown deliberately embeds the original question crops.  The PDF
keeps every question on its own A4 page, scales the crop without trimming it,
and adds bookmarks so a long ability line remains easy to navigate.
"""

from __future__ import annotations

import argparse
import html
import os
import re
import urllib.request
from pathlib import Path

from PIL import Image as PILImage
from fontTools.ttLib import TTFont as OpenTypeFont
from fontTools.varLib.instancer import instantiateVariableFont
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
DEFAULT_OUTPUT = SRC / "pdf"
PAGE_W, PAGE_H = A4
FONT = "NotoSansSC"
FONT_URL = (
    "https://raw.githubusercontent.com/google/fonts/main/"
    "ofl/notosanssc/NotoSansSC%5Bwght%5D.ttf"
)

DATE_RE = re.compile(r"^\d{4}$")
TITLE_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
QUESTION_RE = re.compile(
    r"^###\s+([^\n]+)\s*\n+"
    r"<div[^>]*>\s*\n?"
    r"<img\s+[^>]*src=\"([^\"]+)\"[^>]*alt=\"([^\"]*)\"[^>]*>\s*\n?"
    r"</div>",
    re.MULTILINE,
)
LINK_RE = re.compile(r"\[([^\]]+)\]\([^\)]+\)")


def clean_inline(text: str) -> str:
    text = LINK_RE.sub(r"\1", text)
    text = text.replace("`", "").replace("**", "").strip()
    return html.unescape(text)


def dated_sources(start: str, end: str) -> list[Path]:
    sources = [
        path
        for path in SRC.glob("*.md")
        if DATE_RE.fullmatch(path.stem) and start <= path.stem <= end
    ]
    return sorted(sources, key=lambda path: path.stem)


def resolve_font(explicit: Path | None) -> Path:
    candidates = [
        explicit,
        Path(os.environ["SRC_PDF_CJK_FONT"]) if os.environ.get("SRC_PDF_CJK_FONT") else None,
        ROOT / "tmp" / "pdfs" / "fonts" / "NotoSansSC.ttf",
        Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"),
    ]
    for candidate in candidates:
        if candidate and candidate.is_file():
            return materialize_regular_font(candidate.resolve())

    target = ROOT / "tmp" / "pdfs" / "fonts" / "NotoSansSC.ttf"
    target.parent.mkdir(parents=True, exist_ok=True)
    print(f"Downloading the PDF CJK font to {target.relative_to(ROOT)}")
    urllib.request.urlretrieve(FONT_URL, target)
    return materialize_regular_font(target)


def materialize_regular_font(source: Path) -> Path:
    """Freeze variable fonts at weight 400 so print output is not too light."""
    font = OpenTypeFont(source)
    if "fvar" not in font:
        font.close()
        return source
    target = source.with_name(f"{source.stem}-Regular.ttf")
    if target.is_file() and target.stat().st_mtime >= source.stat().st_mtime:
        font.close()
        return target
    instantiateVariableFont(font, {"wght": 400}, inplace=True)
    font.save(target)
    font.close()
    return target


def parse_document(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    title_match = TITLE_RE.search(text)
    if not title_match:
        raise ValueError(f"Missing document title: {path}")

    questions = []
    for heading, src, alt in QUESTION_RE.findall(text):
        image_path = (path.parent / src).resolve()
        if not image_path.is_file():
            raise FileNotFoundError(f"Missing image referenced by {path}: {src}")
        questions.append(
            {
                "heading": clean_inline(heading),
                "alt": clean_inline(alt),
                "image": image_path,
            }
        )
    if not questions:
        raise ValueError(f"No question images found: {path}")

    before_questions, _, after_marker = text.partition("## 题单")
    intro_lines = before_questions.splitlines()
    intro: list[tuple[str, str]] = []
    paragraph: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            value = clean_inline(" ".join(paragraph))
            if value:
                intro.append(("p", value))
            paragraph.clear()

    for raw in intro_lines:
        line = raw.strip()
        if not line:
            flush_paragraph()
            continue
        if line.startswith("# "):
            continue
        if line.startswith("## "):
            flush_paragraph()
            intro.append(("h2", clean_inline(line[3:])))
            continue
        if line.startswith(">"):
            flush_paragraph()
            value = clean_inline(line.lstrip("> "))
            if value and "127.0.0.1" not in raw:
                intro.append(("meta", value))
            continue
        # Top navigation is useful in Markdown but redundant in a standalone PDF.
        if line.startswith("[") and "](" in line:
            continue
        paragraph.append(line)
    flush_paragraph()

    after_questions = ""
    last_question = list(QUESTION_RE.finditer(text))[-1]
    tail = text[last_question.end() :]
    result_pos = tail.find("## 结果")
    if result_pos >= 0:
        after_questions = tail[result_pos:]

    return {
        "title": clean_inline(title_match.group(1)),
        "intro": intro,
        "questions": questions,
        "after": after_questions,
    }


def split_lines(value: str, font_size: float, max_width: float) -> list[str]:
    """Wrap mixed Chinese/Latin text without assuming whitespace boundaries."""
    lines: list[str] = []
    current = ""
    for char in value:
        candidate = current + char
        if current and pdfmetrics.stringWidth(candidate, FONT, font_size) > max_width:
            lines.append(current.rstrip())
            current = char.lstrip()
        else:
            current = candidate
    if current:
        lines.append(current.rstrip())
    return lines or [""]


def draw_footer(pdf: canvas.Canvas, source_name: str, page_no: int) -> None:
    pdf.saveState()
    pdf.setStrokeColor(colors.HexColor("#d9dee7"))
    pdf.setLineWidth(0.45)
    pdf.line(16 * mm, 12 * mm, PAGE_W - 16 * mm, 12 * mm)
    pdf.setFont(FONT, 8)
    pdf.setFillColor(colors.HexColor("#6b7280"))
    pdf.drawString(16 * mm, 7.8 * mm, f"src/{source_name}")
    pdf.drawRightString(PAGE_W - 16 * mm, 7.8 * mm, str(page_no))
    pdf.restoreState()


def draw_intro(pdf: canvas.Canvas, doc: dict, source_name: str, page_no: int) -> None:
    pdf.bookmarkPage("overview")
    pdf.addOutlineEntry("概览", "overview", level=0, closed=False)
    pdf.setFillColor(colors.HexColor("#172033"))
    pdf.setFont(FONT, 22)
    title_lines = split_lines(doc["title"], 22, PAGE_W - 32 * mm)
    y = PAGE_H - 26 * mm
    for line in title_lines:
        pdf.drawString(16 * mm, y, line)
        y -= 9 * mm

    pdf.setStrokeColor(colors.HexColor("#2f6feb"))
    pdf.setLineWidth(1.5)
    pdf.line(16 * mm, y + 2 * mm, PAGE_W - 16 * mm, y + 2 * mm)
    y -= 8 * mm

    for kind, value in doc["intro"]:
        if kind == "h2":
            y -= 2 * mm
            pdf.setFillColor(colors.HexColor("#243b67"))
            pdf.setFont(FONT, 14)
            for line in split_lines(value, 14, PAGE_W - 32 * mm):
                pdf.drawString(16 * mm, y, line)
                y -= 6.2 * mm
            y -= 1.8 * mm
            continue

        if kind == "meta":
            font_size = 10
            leading = 4.8 * mm
            lines = split_lines(value, font_size, PAGE_W - 42 * mm)
            box_h = leading * len(lines) + 4 * mm
            if y - box_h < 22 * mm:
                draw_footer(pdf, source_name, page_no)
                pdf.showPage()
                page_no += 1
                y = PAGE_H - 22 * mm
            pdf.setFillColor(colors.HexColor("#f1f5fb"))
            pdf.roundRect(16 * mm, y - box_h + 1.5 * mm, PAGE_W - 32 * mm, box_h, 2.5 * mm, fill=1, stroke=0)
            pdf.setFillColor(colors.HexColor("#41536f"))
            pdf.setFont(FONT, font_size)
            ty = y - 3.5 * mm
            for line in lines:
                pdf.drawString(21 * mm, ty, line)
                ty -= leading
            y -= box_h + 2.5 * mm
            continue

        font_size = 11
        leading = 5.7 * mm
        lines = split_lines(value, font_size, PAGE_W - 32 * mm)
        needed = leading * len(lines) + 2 * mm
        if y - needed < 22 * mm:
            draw_footer(pdf, source_name, page_no)
            pdf.showPage()
            page_no += 1
            y = PAGE_H - 22 * mm
        pdf.setFillColor(colors.HexColor("#24292f"))
        pdf.setFont(FONT, font_size)
        for line in lines:
            pdf.drawString(16 * mm, y, line)
            y -= leading
        y -= 2 * mm

    pdf.setFillColor(colors.HexColor("#6b7280"))
    pdf.setFont(FONT, 9)
    pdf.drawString(16 * mm, 20 * mm, f"共 {len(doc['questions'])} 道题 - 每题独立成页 - 原图完整缩放")
    draw_footer(pdf, source_name, page_no)


def draw_question(
    pdf: canvas.Canvas,
    question: dict,
    source_name: str,
    page_no: int,
    index: int,
) -> None:
    key = f"q{index:03d}"
    pdf.bookmarkPage(key)
    pdf.addOutlineEntry(question["heading"], key, level=0, closed=False)

    pdf.setFillColor(colors.HexColor("#243b67"))
    pdf.setFont(FONT, 13)
    pdf.drawString(16 * mm, PAGE_H - 18 * mm, question["heading"])
    if question["alt"] and question["alt"] not in question["heading"]:
        pdf.setFillColor(colors.HexColor("#6b7280"))
        pdf.setFont(FONT, 9)
        pdf.drawRightString(PAGE_W - 16 * mm, PAGE_H - 18 * mm, question["alt"])
    pdf.setStrokeColor(colors.HexColor("#d9dee7"))
    pdf.setLineWidth(0.6)
    pdf.line(16 * mm, PAGE_H - 22 * mm, PAGE_W - 16 * mm, PAGE_H - 22 * mm)

    with PILImage.open(question["image"]) as image:
        pixel_w, pixel_h = image.size
    max_w = PAGE_W - 30 * mm
    max_h = PAGE_H - 42 * mm
    scale = min(max_w / pixel_w, max_h / pixel_h)
    draw_w = pixel_w * scale
    draw_h = pixel_h * scale
    x = (PAGE_W - draw_w) / 2
    y = 15 * mm + (max_h - draw_h) / 2
    pdf.drawImage(
        str(question["image"]),
        x,
        y,
        width=draw_w,
        height=draw_h,
        preserveAspectRatio=True,
        anchor="c",
        mask="auto",
    )
    draw_footer(pdf, source_name, page_no)


def parse_result_tail(tail: str) -> tuple[list[str], list[list[str]]]:
    if not tail:
        return [], []
    lines = tail.splitlines()
    paragraphs: list[str] = []
    table: list[list[str]] = []
    in_table = False
    for raw in lines:
        line = raw.strip()
        if not line or line == "## 结果":
            continue
        if line.startswith("[") and "](" in line:
            continue
        if line.startswith("|") and line.endswith("|"):
            cells = [
                clean_inline(cell.strip()).replace("✓", "对").replace("✗", "错")
                for cell in line.strip("|").split("|")
            ]
            if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                continue
            table.append(cells)
            in_table = True
        elif not in_table:
            paragraphs.append(clean_inline(line))
    return paragraphs, table


def draw_results(pdf: canvas.Canvas, tail: str, source_name: str, page_no: int) -> None:
    paragraphs, rows = parse_result_tail(tail)
    if not paragraphs and not rows:
        return
    pdf.bookmarkPage("results")
    pdf.addOutlineEntry("结果", "results", level=0, closed=False)
    pdf.setFillColor(colors.HexColor("#172033"))
    pdf.setFont(FONT, 20)
    pdf.drawString(16 * mm, PAGE_H - 24 * mm, "结果")
    y = PAGE_H - 38 * mm
    pdf.setFillColor(colors.HexColor("#24292f"))
    pdf.setFont(FONT, 11)
    for value in paragraphs:
        for line in split_lines(value, 11, PAGE_W - 32 * mm):
            pdf.drawString(16 * mm, y, line)
            y -= 5.5 * mm
        y -= 2 * mm

    if rows:
        cell_style = ParagraphStyle(
            "result-cell",
            fontName=FONT,
            fontSize=9,
            leading=12,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#24292f"),
        )
        data = [[Paragraph(html.escape(cell), cell_style) for cell in row] for row in rows]
        count = len(rows[0])
        col_widths = [(PAGE_W - 32 * mm) / count] * count
        result_table = Table(data, colWidths=col_widths, repeatRows=1)
        result_table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8eef8")),
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#c7cfda")),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("TOPPADDING", (0, 0), (-1, -1), 5),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ]
            )
        )
        _, table_h = result_table.wrap(PAGE_W - 32 * mm, y - 20 * mm)
        result_table.drawOn(pdf, 16 * mm, y - table_h)
    draw_footer(pdf, source_name, page_no)


def export_one(source: Path, output: Path) -> tuple[int, int]:
    doc = parse_document(source)
    output.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(output), pagesize=A4, pageCompression=1)
    pdf.setTitle(doc["title"])
    pdf.setAuthor("dontng / Codex")
    pdf.setSubject(f"408 question chain exported from src/{source.name}")

    page_no = 1
    draw_intro(pdf, doc, source.name, page_no)
    for index, question in enumerate(doc["questions"], start=1):
        pdf.showPage()
        page_no += 1
        draw_question(pdf, question, source.name, page_no, index)
    if doc["after"]:
        pdf.showPage()
        page_no += 1
        draw_results(pdf, doc["after"], source.name, page_no)
    pdf.save()
    return len(doc["questions"]), page_no


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", default="0731")
    parser.add_argument("--end", default="1002")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--only", help="Export one MMDD file, useful for previewing")
    parser.add_argument("--font", type=Path, help="Path to a Chinese TrueType font")
    args = parser.parse_args()

    pdfmetrics.registerFont(TTFont(FONT, str(resolve_font(args.font))))
    sources = dated_sources(args.start, args.end)
    if args.only:
        sources = [path for path in sources if path.stem == args.only]
    if not sources:
        raise SystemExit("No dated src Markdown files matched the requested range")

    args.output.mkdir(parents=True, exist_ok=True)
    total_questions = 0
    total_pages = 0
    for source in sources:
        question_count, page_count = export_one(source, args.output / f"{source.stem}.pdf")
        total_questions += question_count
        total_pages += page_count
        print(f"{source.stem}.pdf: {question_count} questions, {page_count} pages")
    print(f"Exported {len(sources)} PDFs, {total_questions} questions, {total_pages} pages")


if __name__ == "__main__":
    main()
