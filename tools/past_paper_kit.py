#!/usr/bin/env python3
"""Unified 2025-style 408 past-paper HTML template, A4 PDF exporter, and quality auditor."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAST_PAPERS_DIR = ROOT / "past_papers"
HTML_DIR = PAST_PAPERS_DIR / "html"
PDF_DIR = PAST_PAPERS_DIR / "pdf"

TEMPLATE_CSS = """\
@page {
  size: A4;
  margin: 18mm 20mm 21mm 20mm;
  @bottom-center {
    content: "计算机学科专业基础试题　第 " counter(page) " 页（共 " counter(pages) " 页）";
    font-family: "Songti SC", "SimSun", "STSong", "Noto Serif CJK SC", serif;
    font-size: 9.5pt;
    color: #000;
  }
}
@page cover {
  size: A4;
  margin: 16mm 20mm 18mm 20mm;
  @bottom-center {
    content: none;
  }
}

* {
  box-sizing: border-box;
}

html, body {
  margin: 0;
  padding: 0;
  background: #eef0f3;
  color: #000;
  font-family: "Times New Roman", "Songti SC", "SimSun", "STSong", "Noto Serif CJK SC", serif;
  font-size: 10.5pt;
  line-height: 1.65;
  -webkit-font-smoothing: antialiased;
}

.toolbar {
  position: sticky;
  top: 0;
  z-index: 100;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 20px;
  background: #1f2937;
  color: #f9fafb;
  font-family: "Heiti SC", "Noto Sans CJK SC", sans-serif;
  font-size: 13px;
}

.toolbar button {
  padding: 5px 14px;
  border: 1px solid #9ca3af;
  border-radius: 4px;
  background: #fff;
  color: #111827;
  font-size: 13px;
  cursor: pointer;
}

.toolbar button:hover {
  background: #f3f4f6;
}

.exam-wrapper {
  width: 210mm;
  margin: 16px auto 32px;
  background: #fff;
  box-shadow: 0 2px 14px rgba(0, 0, 0, 0.12);
}

/* ===== Cover Page (2025 Official Replica) ===== */
.cover-page {
  page: cover;
  break-after: page;
  min-height: 263mm;
  padding: 16mm 20mm 18mm 20mm;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.cover-secret {
  font-family: "Heiti SC", "SimHei", "STHeiti", "Noto Sans CJK SC", sans-serif;
  font-size: 10.5pt;
  font-weight: 700;
  letter-spacing: 0.05em;
  margin: 0 0 18mm 0;
}

.cover-header {
  text-align: center;
  margin-bottom: 14mm;
}

.cover-year {
  font-size: 16pt;
  font-weight: 700;
  letter-spacing: 0.06em;
  margin: 0 0 7mm 0;
}

.cover-subject {
  font-family: "Heiti SC", "SimHei", "STHeiti", "Noto Sans CJK SC", sans-serif;
  font-size: 24pt;
  font-weight: 700;
  letter-spacing: 0.08em;
  margin: 0 0 6mm 0;
}

.cover-code {
  font-size: 13.5pt;
  margin: 0;
}

.cover-notice-title {
  text-align: center;
  font-family: "Heiti SC", "SimHei", "STHeiti", "Noto Sans CJK SC", sans-serif;
  font-size: 13pt;
  font-weight: 700;
  letter-spacing: 0.08em;
  margin: 10mm 0 6mm 0;
}

.cover-notice {
  margin: 0;
  padding-left: 1.8em;
  font-size: 11pt;
  line-height: 1.95;
  text-align: justify;
}

.cover-notice li {
  margin-bottom: 4pt;
}

.cover-info-wrap {
  margin-top: auto;
  padding-top: 14mm;
}

.cover-info-hint {
  text-align: center;
  font-size: 10.5pt;
  margin: 0 0 5pt 0;
}

.cover-info-table {
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed;
  border: 1.4pt solid #000;
}

.cover-info-table td {
  border: 1pt solid #000;
  height: 11.5mm;
  text-align: center;
  vertical-align: middle;
  font-size: 10.5pt;
}

.cover-info-table td.label-cell {
  width: 24mm;
  letter-spacing: 0.08em;
}

/* ===== Exam Body ===== */
.exam-body {
  padding: 18mm 20mm 20mm 20mm;
}

.section-title {
  font-family: "Heiti SC", "SimHei", "STHeiti", "Noto Sans CJK SC", sans-serif;
  font-size: 11pt;
  font-weight: 700;
  line-height: 1.6;
  margin: 10pt 0 8pt 0;
  text-indent: 0;
  break-after: avoid;
}

.section-title:first-child {
  margin-top: 0;
}

.question {
  margin: 0 0 7.5pt 0;
}

.question.mcq {
  break-inside: avoid;
}

.q-stem {
  margin: 0 0 2.5pt 0;
  text-align: justify;
}

.q-num {
  font-weight: 400;
  margin-right: 0.25em;
}

.q-score {
  margin-right: 0.2em;
}

.q-items {
  margin: 2pt 0 3pt 1.8em;
  padding: 0;
  list-style: none;
}

.q-items.cols-2 {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  column-gap: 12pt;
}

.q-items.cols-4 {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  column-gap: 8pt;
}

.options {
  margin: 2pt 0 0 1.6em;
  display: grid;
  row-gap: 1.5pt;
  column-gap: 12pt;
}

.options.cols-4 {
  grid-template-columns: repeat(4, minmax(0, 1fr));
}

.options.cols-2 {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.options.cols-1 {
  grid-template-columns: 1fr;
}

.option {
  display: flex;
  align-items: baseline;
  gap: 0.25em;
  min-width: 0;
}

.opt-label {
  flex: 0 0 auto;
}

.opt-text {
  flex: 1 1 auto;
  min-width: 0;
}

.subquestions {
  margin: 4pt 0 0 0;
  padding: 0;
  list-style: none;
}

.subquestions li {
  margin: 2.5pt 0;
  text-indent: 2em;
  text-align: justify;
}

.q-para {
  margin: 3pt 0;
  text-indent: 2em;
  text-align: justify;
}

/* Code blocks */
.code-box {
  margin: 5pt auto;
  padding: 6pt 10pt;
  border: 0.9pt solid #000;
  background: #fff;
  font-family: "Times New Roman", "Noto Sans Mono CJK SC", "Courier New", monospace;
  font-size: 9.8pt;
  line-height: 1.48;
  white-space: pre-wrap;
  word-break: break-word;
  break-inside: avoid;
}

.code-plain {
  margin: 3.5pt 0 4pt 2em;
  padding: 4pt 8pt;
  background: #f5f5f5;
  font-family: "Times New Roman", "Noto Sans Mono CJK SC", "Courier New", monospace;
  font-size: 9.8pt;
  line-height: 1.48;
  white-space: pre-wrap;
  word-break: break-word;
  break-inside: avoid;
}

.code-pair {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 10pt;
  margin: 6pt 0;
  break-inside: avoid;
}

/* Tables */
table.exam-table {
  border-collapse: collapse;
  margin: 6pt auto;
  font-size: 9.5pt;
  line-height: 1.45;
  max-width: 100%;
  break-inside: avoid;
}

table.exam-table th,
table.exam-table td {
  border: 0.8pt solid #000;
  padding: 3pt 6pt;
  text-align: center;
  vertical-align: middle;
}

table.exam-table th {
  font-weight: 700;
}

table.exam-table td.left,
table.exam-table th.left {
  text-align: left;
}

.table-caption {
  text-align: center;
  font-size: 9.8pt;
  margin: 5pt 0 2pt 0;
  break-after: avoid;
}

/* Figures & SVGs */
.figure {
  margin: 6pt auto;
  text-align: center;
  break-inside: avoid;
}

.figure svg {
  display: block;
  margin: 0 auto;
  max-width: 100%;
  height: auto;
}

.fig-caption {
  text-align: center;
  font-size: 9.8pt;
  margin: 3pt 0 0 0;
}

.stem-with-fig {
  display: flex;
  align-items: flex-start;
  gap: 12pt;
}

.stem-with-fig .stem-col {
  flex: 1 1 auto;
  min-width: 0;
}

.stem-with-fig .fig-col {
  flex: 0 0 auto;
  text-align: center;
}

/* Math & inline helpers */
.math, var {
  font-family: "Times New Roman", "STIX Two Math", serif;
  font-style: italic;
}

.blank {
  display: inline-block;
  min-width: 2.6em;
  border-bottom: 0.75pt solid #000;
  vertical-align: baseline;
}

.paren {
  display: inline-block;
  min-width: 2.4em;
  text-align: center;
}

sub, sup {
  font-size: 74%;
  line-height: 0;
}

@media print {
  html, body {
    background: #fff;
  }
  .toolbar {
    display: none !important;
  }
  .exam-wrapper {
    width: auto;
    margin: 0;
    box-shadow: none;
  }
  .cover-page {
    min-height: 263mm;
    padding: 0;
  }
  .exam-body {
    padding: 0;
  }
}
"""


def build_cover_html(year: int) -> str:
    subject = "计算机学科专业基础综合" if year <= 2021 else "计算机学科专业基础"
    boxes = "".join("<td></td>" for _ in range(15))
    return f"""\
  <section class="cover-page" aria-label="{year} 年试卷封面">
    <div>
      <p class="cover-secret">绝密★启用前</p>
      <header class="cover-header">
        <p class="cover-year">{year} 年全国硕士研究生招生考试</p>
        <h1 class="cover-subject">{subject}</h1>
        <p class="cover-code">（科目代码：408）</p>
      </header>
      <p class="cover-notice-title">考生注意事项</p>
      <ol class="cover-notice">
        <li>答题前，考生须在答题卡指定位置上填写考生编号和考生姓名；在答题卡指定位置上填写报考单位、考生姓名和考生编号，并涂写考生编号信息点。</li>
        <li>选择题的答案必须涂写在答题卡相应题号的选项上，非选择题的答案必须书写在答题卡指定位置的边框区域内。超出答题区域书写的答案无效；在草稿纸、试题册上答题无效。</li>
        <li>填（书）写部分必须使用黑色字迹签字笔书写，字迹工整、笔迹清楚；涂写部分必须使用 2B 铅笔填涂。</li>
        <li>考试结束，将答题卡和试题册按规定交回。</li>
      </ol>
    </div>
    <div class="cover-info-wrap">
      <p class="cover-info-hint">（以下信息考生必须认真填写）</p>
      <table class="cover-info-table" aria-label="考生信息填写栏">
        <tr>
          <td class="label-cell">考生编号</td>
          {boxes}
        </tr>
        <tr>
          <td class="label-cell">考生姓名</td>
          <td colspan="15"></td>
        </tr>
      </table>
    </div>
  </section>"""


def wrap_exam_html(year: int, body_html: str) -> str:
    subject = "计算机学科专业基础综合" if year <= 2021 else "计算机学科专业基础"
    footer_subject = f"{subject}试题"
    css = TEMPLATE_CSS.replace("计算机学科专业基础试题", footer_subject)
    cover = build_cover_html(year)
    return f"""\
<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{year} 年{subject}（408）真题</title>
  <style>
{css}
  </style>
</head>
<body>
  <nav class="toolbar" aria-label="试卷操作">
    <span>{year} 年 · {subject}（408）</span>
    <button type="button" onclick="window.print()">打印 / 导出 A4 PDF</button>
  </nav>
  <div class="exam-wrapper">
{cover}
    <main class="exam-body" aria-label="{year} 年 408 真题正文">
{body_html}
    </main>
  </div>
</body>
</html>
"""


def export_pdf(year: int) -> Path:
    from playwright.sync_api import sync_playwright

    html_path = HTML_DIR / f"408-{year}.html"
    pdf_path = PDF_DIR / f"408-{year}.pdf"
    if not html_path.exists():
        raise FileNotFoundError(f"Missing HTML: {html_path}")
    PDF_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path="/usr/bin/google-chrome")
        page = browser.new_page()
        page.goto(html_path.resolve().as_uri(), wait_until="networkidle")
        page.pdf(
            path=str(pdf_path),
            prefer_css_page_size=True,
            print_background=True,
        )
        browser.close()
    return pdf_path


def audit_paper(year: int) -> tuple[bool, list[str]]:
    issues: list[str] = []
    html_path = HTML_DIR / f"408-{year}.html"
    pdf_path = PDF_DIR / f"408-{year}.pdf"

    if not html_path.exists():
        return False, [f"Missing {html_path}"]
    if not pdf_path.exists():
        return False, [f"Missing {pdf_path}"]

    h = html_path.read_text(encoding="utf-8")

    # 1. Unified 2025 template checks
    if 'class="cover-page"' not in h or "绝密★启用前" not in h or 'class="exam-body"' not in h:
        issues.append("HTML does not use the unified 2025 template (missing cover-page / 绝密★启用前 / exam-body)")
    if "xmlns:inkscape" in h or 'viewBox="0 0 541.5' in h or 'viewBox="0 0 595.32' in h:
        issues.append("HTML contains raw PDF-to-SVG page dump")

    # 2. Zero raster images
    if re.search(r"<img\b|<image\b|data:image/", h, re.I):
        issues.append("HTML contains raster <img>/<image>/data:image (diagrams must be hand-drawn SVG)")

    # 3. Zero PUA / FFFD / answer leaks in HTML
    pua_h = [c for c in h if 0xE000 <= ord(c) <= 0xF8FF]
    if pua_h:
        issues.append(f"HTML has {len(pua_h)} PUA chars")
    if "\ufffd" in h:
        issues.append("HTML has U+FFFD replacement chars")
    ans_h = re.findall(r"(?:参考答案|答案速查|标准答案|正确答案)", h)
    if ans_h:
        issues.append(f"HTML has answer leak keywords: {ans_h}")

    scores = [
        int(score)
        for score in re.findall(r'class="q-score">\s*[（(]\s*(\d+)\s*分\s*[）)]', h)
    ]
    if len(scores) != 7 or sum(scores) != 70:
        issues.append(f"Written section requires 7 scores totaling 70: {scores}")

    # 4. PDF checks
    info = subprocess.check_output(["pdfinfo", str(pdf_path)], text=True)
    m_pages = re.search(r"Pages:\s+(\d+)", info)
    m_size = re.search(r"Page size:\s+([0-9.]+)\s*x\s*([0-9.]+)", info)
    pages = int(m_pages.group(1)) if m_pages else 0
    if m_size:
        w, ht = float(m_size.group(1)), float(m_size.group(2))
        if not (593 <= w <= 597 and 840 <= ht <= 844):
            issues.append(f"PDF page size is not A4: {w}x{ht} pt")
    else:
        issues.append("Could not read PDF page size")

    txt = subprocess.check_output(["pdftotext", str(pdf_path), "-"], text=True)
    pua_p = [c for c in txt if 0xE000 <= ord(c) <= 0xF8FF]
    if pua_p:
        issues.append(f"PDF has {len(pua_p)} PUA chars")
    if "\ufffd" in txt:
        issues.append("PDF has U+FFFD replacement chars")
    ans_p = re.findall(r"(?:参考答案|答案速查|标准答案|正确答案)", txt)
    if ans_p:
        issues.append(f"PDF has answer leak keywords: {ans_p}")

    # Question numbers 1..47
    found_q = set()
    for line in txt.splitlines():
        m = re.match(r"^\s*0?(\d{1,2})\s*[．\.\、]", line)
        if m:
            n = int(m.group(1))
            if 1 <= n <= 47:
                found_q.add(n)
    missing_q = sorted(set(range(1, 48)) - found_q)
    if missing_q:
        issues.append(f"Missing question numbers in PDF text: {missing_q}")

    # Option counts A..D
    opts = Counter(re.findall(r"(?:^|[\s\u3000])([A-D])\s*[．\.]", txt, re.M))
    if any(opts.get(k, 0) < 40 for k in "ABCD"):
        issues.append(f"Option counts below 40: {dict(sorted(opts.items()))}")

    svgs = len(re.findall(r"<svg\b", h, re.I))
    status = "PASS" if not issues else "FAIL"
    print(f"[{status}] 408-{year}: {pages}p A4 | Q={len(found_q)}/47 | opts={dict(sorted(opts.items()))} | svgs={svgs}")
    for iss in issues:
        print(f"  - {iss}")
    return len(issues) == 0, issues


def main() -> int:
    parser = argparse.ArgumentParser(description="408 past-paper unified template kit")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_exp = sub.add_parser("export", help="Export HTML to A4 PDF via headless Chrome")
    p_exp.add_argument("years", nargs="+", type=int)

    p_aud = sub.add_parser("audit", help="Audit HTML and PDF against 2025 unified standards")
    p_aud.add_argument("years", nargs="+", type=int)

    args = parser.parse_args()
    ok = True
    if args.cmd == "export":
        for y in args.years:
            out = export_pdf(y)
            print(f"Exported {out} ({out.stat().st_size:,} bytes)")
    elif args.cmd == "audit":
        for y in args.years:
            passed, _ = audit_paper(y)
            ok = ok and passed
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
