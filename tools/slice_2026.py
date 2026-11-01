#!/usr/bin/env python3
"""Slice all 47 questions from 2026 408 exam paper into bank/2026/qNN.png."""
import os, sys, re, json
from pathlib import Path
import fitz
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from imgtrim import trim_file, remove_page_gap

PDF_PATH = ROOT / "past_papers" / "2026年计算机408统考真题.pdf"
OUT_DIR = ROOT / "bank" / "2026"
OUT_DIR.mkdir(parents=True, exist_ok=True)

DPI = 200
ZOOM = DPI / 72.0

def slice_2026():
    doc = fitz.open(PDF_PATH)
    markers = {}
    # Skip page 0 (cover page with 考生注意事项 1..5)
    for pno in range(1, len(doc)):
        page = doc[pno]
        pw = page.rect.width
        words = page.get_text("words")
        words.sort(key=lambda w: (w[1], w[0]))
        for w in words:
            if w[0] < pw * 0.25:
                m = re.match(r"^(\d{2})\.$", w[4])
                if m:
                    qn = int(m.group(1))
                    if qn not in markers and 1 <= qn <= 47:
                        markers[qn] = (pno, w[1])

    assert len(markers) == 47, f"Found only {len(markers)} markers"
    print("Found all 47 question markers.")

    def render_piece(pno, top, bottom):
        page = doc[pno]
        clip = fitz.Rect(0, max(0, top), page.rect.width, min(page.rect.height, bottom))
        pix = page.get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM), clip=clip, alpha=False)
        return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)

    # 1. Slice choice questions 1..40
    for qn in range(1, 41):
        p_curr, y_curr = markers[qn]
        if qn < 40:
            p_next, y_next = markers[qn + 1]
            if p_curr == p_next:
                end_y = y_next - 4
            else:
                end_y = 675.0
        else: # Q40
            # Q40 ends before Section II heading on page 7
            end_y = 215.0
        
        im = render_piece(p_curr, y_curr - 4, end_y)
        out_path = OUT_DIR / f"q{qn:02d}.png"
        im.save(out_path)
        trim_file(out_path)
        print(f"Saved {out_path.name}")

    # 2. Slice written questions 41..47
    for qn in range(41, 48):
        p_curr, y_curr = markers[qn]
        if qn < 47:
            p_next, y_next = markers[qn + 1]
            end_p = p_next
            end_y = y_next - 4
        else: # Q47
            end_p = p_curr
            end_y = 675.0

        pieces = []
        for p in range(p_curr, end_p + 1):
            top = y_curr - 4 if p == p_curr else 44.0
            bottom = end_y if p == end_p else 675.0
            pieces.append(render_piece(p, top, bottom))

        if len(pieces) == 1:
            im = pieces[0]
        else:
            w = max(p.width for p in pieces)
            h = sum(p.height for p in pieces)
            im = Image.new("RGB", (w, h), (255, 255, 255))
            y_offset = 0
            for p in pieces:
                im.paste(p, (0, y_offset))
                y_offset += p.height
            im, _ = remove_page_gap(im)

        out_path = OUT_DIR / f"q{qn:02d}.png"
        im.save(out_path)
        trim_file(out_path)
        print(f"Saved {out_path.name}")

    # 3. Update data/written_markers.json
    wm_path = ROOT / "data" / "written_markers.json"
    if wm_path.exists():
        wm = json.loads(wm_path.read_text())
        wm["years"]["2026"] = {
            str(q): [markers[q][0], round(markers[q][1], 1)]
            for q in range(41, 48)
        }
        wm_path.write_text(json.dumps(wm, indent=2, ensure_ascii=False) + "\n")
        print("Updated data/written_markers.json for 2026.")

if __name__ == "__main__":
    slice_2026()
