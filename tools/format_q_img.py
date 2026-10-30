#!/usr/bin/env python3
"""Helper script to calculate exact standard image tag for any 408 question."""
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data/image_display_widths.json"
DATA = json.loads(DATA_FILE.read_text(encoding="utf-8"))["images"]

def get_image_tag(year: str, qnum: str, alt_text: str = None) -> str:
    key = f"{year}-{qnum}"
    info = DATA.get(key, {})
    img_path = ROOT / f"bank/{year}/q{qnum}.png"
    if not img_path.exists():
        return f"<!-- Missing image: {img_path} -->"

    im = Image.open(img_path)
    w, h = im.size
    g = info.get("glyph_height_px") or 26.0
    w_em = round(w / g, 2)
    alt = alt_text or key
    return f'<img src="../bank/{year}/q{qnum}.png" alt="{alt}" style="display: block; width: {w_em}em; max-width: 100%; height: auto; margin: 12px 0;">'

if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 3:
        print(get_image_tag(sys.argv[1], sys.argv[2]))
    else:
        print("Usage: python3 format_q_img.py <year> <qnum>")
