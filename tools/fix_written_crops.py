#!/usr/bin/env python3
"""Safely clean written-question image tails without touching internal whitespace.

Two images known to have lost sparse content are first rebuilt from the reviewed
PDF marker table. Every written image is then inspected only at its tail: a
small footer isolated near the bottom may be removed, followed by pure trailing
white space. No rows inside the question body are deleted.
"""
from __future__ import annotations

import argparse
import io
import json
from pathlib import Path

import fitz
import numpy as np
from PIL import Image


ROOT = Path(__file__).resolve().parent.parent
MARKERS = ROOT / "data" / "written_markers.json"
AUDIT = ROOT / "data" / "written_crop_audit.json"
DPI = 200
ZOOM = DPI / 72.0
PAD = 14
INK_THRESHOLD = 236
RESTORE = (("2017", 41), ("2013", 44))


def paper_for(year: str) -> Path:
    papers = sorted((ROOT / "past_papers").glob(f"{year}*.pdf"))
    if len(papers) != 1:
        raise RuntimeError(f"expected one PDF for {year}, found {len(papers)}")
    return papers[0]


def active_rows(arr: np.ndarray) -> np.ndarray:
    return (arr < INK_THRESHOLD).sum(axis=1) >= 2


def row_groups(active: np.ndarray, bridge: int = 6) -> list[tuple[int, int]]:
    indexes = np.flatnonzero(active)
    if not len(indexes):
        return []
    groups = []
    start = previous = int(indexes[0])
    for raw in indexes[1:]:
        row = int(raw)
        if row - previous > bridge + 1:
            groups.append((start, previous + 1))
            start = row
        previous = row
    groups.append((start, previous + 1))
    return groups


def footer_cut(im: Image.Image) -> int | None:
    """Return the row before a highly isolated, footer-shaped final cluster."""
    gray = np.asarray(im.convert("L"))
    groups = row_groups(active_rows(gray))
    if len(groups) < 2:
        return None
    previous, candidate = groups[-2], groups[-1]
    gap = candidate[0] - previous[1]
    height = candidate[1] - candidate[0]
    if gap < max(70, im.height // 18):
        return None
    if height > max(55, im.height // 30):
        return None
    if candidate[0] < int(im.height * 0.76):
        return None
    ys, xs = np.where(gray[candidate[0]:candidate[1]] < INK_THRESHOLD)
    if not len(xs):
        return None
    width = int(xs.max() - xs.min() + 1)
    if width > int(im.width * 0.45):
        return None
    return min(im.height, previous[1] + PAD)


def trim_outer(im: Image.Image) -> Image.Image:
    gray = np.asarray(im.convert("L"))
    ys, xs = np.where(gray < INK_THRESHOLD)
    if not len(xs):
        return im
    left = max(0, int(xs.min()) - PAD)
    right = min(im.width, int(xs.max()) + 1 + PAD)
    top = max(0, int(ys.min()) - PAD)
    bottom = min(im.height, int(ys.max()) + 1 + PAD)
    return im.crop((left, top, right, bottom))


def clean_tail(im: Image.Image) -> tuple[Image.Image, bool]:
    cut = footer_cut(im)
    work = im.crop((0, 0, im.width, cut)) if cut else im
    gray = np.asarray(work.convert("L"))
    rows = np.flatnonzero(active_rows(gray))
    if not len(rows):
        return im, False
    bottom = min(work.height, int(rows[-1]) + 1 + PAD)
    result = work.crop((0, 0, work.width, bottom))
    return result, result.size != im.size


def render_piece(page: fitz.Page, top: float, bottom: float) -> Image.Image:
    # Strip only the fixed physical page margins on cross-page fragments.
    clip = fitz.Rect(0, max(0, top), page.rect.width, min(page.rect.height, bottom))
    pix = page.get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM), clip=clip, alpha=False)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def restore_question(year: str, number: int, markers: dict) -> Path:
    item = markers["years"][year]
    start_page, start_y = item[str(number)]
    end = item[str(number + 1)] if number < 47 else item.get("end")
    pieces = []
    with fitz.open(paper_for(year)) as doc:
        if end is None:
            end = (len(doc) - 1, doc[-1].rect.height)
        end_page, end_y = end
        for page_number in range(start_page, end_page + 1):
            page = doc[page_number]
            top = start_y - 4 if page_number == start_page else 32
            bottom = end_y if page_number == end_page else page.rect.height - 32
            piece = trim_outer(render_piece(page, top, bottom))
            pieces.append(piece)

    width = max(piece.width for piece in pieces)
    gap = 18
    height = sum(piece.height for piece in pieces) + gap * (len(pieces) - 1)
    stitched = Image.new("RGB", (width, height), "white")
    offset = 0
    for piece in pieces:
        stitched.paste(piece, (0, offset))
        offset += piece.height + gap

    target = ROOT / "bank" / year / f"q{number}.png"
    stitched.save(target, format="PNG", optimize=True)
    return target


def all_written_images() -> list[Path]:
    return [
        ROOT / "bank" / str(year) / f"q{number}.png"
        for year in range(2009, 2026)
        for number in range(41, 48)
    ]


def run() -> dict:
    markers = json.loads(MARKERS.read_text(encoding="utf-8"))
    before = {}
    corrupt = []
    for path in all_written_images():
        if not path.exists():
            raise RuntimeError(f"missing written image: {path.relative_to(ROOT)}")
        try:
            with Image.open(path) as im:
                before[path] = im.size
                im.load()
        except (OSError, SyntaxError):
            corrupt.append(path)

    restored = {restore_question(year, number, markers) for year, number in RESTORE}
    for path in corrupt:
        restored.add(restore_question(path.parent.name, int(path.stem[1:]), markers))
    changed = []
    for path in all_written_images():
        try:
            with Image.open(path) as source:
                original = source.convert("RGB")
        except (OSError, SyntaxError) as exc:
            raise RuntimeError(f"cannot decode {path.relative_to(ROOT)}: {exc}") from exc
        cleaned, tail_changed = clean_tail(original)
        if path in restored or tail_changed:
            cleaned.save(path, format="PNG", optimize=True)
        with Image.open(path) as checked:
            checked.verify()
        after_size = cleaned.size
        if before[path] != after_size or path in restored:
            changed.append({
                "path": path.relative_to(ROOT).as_posix(),
                "before": list(before[path]),
                "after": list(after_size),
                "restored_from_pdf": path in restored,
            })

    audit = {
        "method": "targeted PDF restore; footer-shaped final cluster removal; trailing whitespace crop",
        "scope": "2009-2025 q41-q47",
        "guardrail": "no internal image rows are deleted",
        "count_checked": len(all_written_images()),
        "restored": [
            f"{path.parent.name}-{int(path.stem[1:])}" for path in sorted(restored)
        ],
        "changed": changed,
    }
    AUDIT.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"checked 119 images; changed {len(changed)}; restored 2")
    return audit


def check() -> None:
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    if audit["count_checked"] != 119:
        raise RuntimeError("audit does not cover 119 written images")
    for path in all_written_images():
        with Image.open(path) as im:
            im.verify()
    print("verified 119 written images and crop audit")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    check() if args.check else run()


if __name__ == "__main__":
    main()
