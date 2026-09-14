#!/usr/bin/env python3
"""Cut complete written questions 41-47 from the local paper PDFs.

Existing verified historical crops are preserved by default. Missing questions
are bounded by the next question number, so a question that crosses a page is
stitched into one indivisible image.
"""
import argparse
import json
import os
from pathlib import Path

import fitz
from PIL import Image

from imgtrim import remove_page_gap_file, trim_file


ROOT = Path(__file__).resolve().parent.parent
MARKERS = ROOT / "data" / "written_markers.json"
DPI = 200
ZOOM = DPI / 72.0


def paper_for(year):
    matches = sorted((ROOT / "past_papers").glob(f"{year}*.pdf"))
    if len(matches) != 1:
        raise RuntimeError(f"expected one PDF for {year}, found {len(matches)}")
    return matches[0]


def render_piece(doc, page_number, top, bottom):
    page = doc[page_number]
    clip = fitz.Rect(0, max(0, top), page.rect.width, min(page.rect.height, bottom))
    pix = page.get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM), clip=clip, alpha=False)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def cut(doc, start, end, target):
    start_page, start_y = start
    end_page, end_y = end
    pieces = []
    for page_number in range(start_page, end_page + 1):
        page = doc[page_number]
        top = start_y - 4 if page_number == start_page else 0
        bottom = end_y if page_number == end_page else page.rect.height
        pieces.append(render_piece(doc, page_number, top, bottom))

    width = max(piece.width for piece in pieces)
    height = sum(piece.height for piece in pieces)
    stitched = Image.new("RGB", (width, height), "white")
    offset = 0
    for piece in pieces:
        stitched.paste(piece, (0, offset))
        offset += piece.height

    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_suffix(".building.png")
    stitched.save(temporary, format="PNG")
    if len(pieces) > 1:
        remove_page_gap_file(temporary)
    trim_file(temporary)
    with Image.open(temporary) as image:
        image.verify()
    os.replace(temporary, target)


def valid_png(path):
    try:
        with Image.open(path) as image:
            image.verify()
        return True
    except (OSError, SyntaxError):
        return False


def validate_markers(data):
    expected_years = {str(year) for year in range(2009, 2026)}
    if set(data["years"]) != expected_years:
        raise RuntimeError("marker table must cover every year from 2009 through 2025")
    for year, item in data["years"].items():
        questions = [int(key) for key in item if key != "end"]
        if questions != list(range(41, 48)):
            raise RuntimeError(f"{year}: expected markers 41-47, got {questions}")
        positions = [tuple(item[str(q)]) for q in questions]
        if positions != sorted(positions):
            raise RuntimeError(f"{year}: markers are not in reading order")


def build(years=None, replace_preserved=False, check=False, repair=False):
    data = json.loads(MARKERS.read_text(encoding="utf-8"))
    validate_markers(data)
    preserved = set(data["preserve_existing"])
    selected = years or sorted(data["years"])
    made = kept = 0

    for year in selected:
        item = data["years"][year]
        with fitz.open(paper_for(year)) as doc:
            for question in range(41, 48):
                qid = f"{year}-{question}"
                target = ROOT / "bank" / year / f"q{question}.png"
                if check:
                    if not valid_png(target):
                        raise RuntimeError(f"missing or invalid {target.relative_to(ROOT)}")
                    continue
                if repair and valid_png(target):
                    continue
                if target.exists() and qid in preserved and not replace_preserved:
                    kept += 1
                    continue
                start = item[str(question)]
                if question < 47:
                    end = item[str(question + 1)]
                else:
                    end = item.get("end", [len(doc) - 1, doc[-1].rect.height])
                cut(doc, start, end, target)
                made += 1

    total = len(selected) * 7
    print(f"written bank: {total} slots; generated {made}; preserved {kept}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("years", nargs="*", help="optional years, e.g. 2024 2025")
    parser.add_argument("--replace-preserved", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--repair", action="store_true", help="only rebuild missing or invalid PNG files")
    args = parser.parse_args()
    build(args.years, args.replace_preserved, args.check, args.repair)


if __name__ == "__main__":
    main()
