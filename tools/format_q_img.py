#!/usr/bin/env python3
"""Helper script to calculate exact standard image tag for any 408 question."""
import re
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent


def _load_src_styles():
    styles = {}
    for p in (ROOT / "src").glob("*.md"):
        if p.name == "README.md":
            continue
        for m in re.finditer(
            r'<img\s+src="[^\"]*bank/(\d{4})/q(\d+)\.png"[^>]*style="([^\"]*)"[^>]*>',
            p.read_text(),
        ):
            year, q, style = m.group(1), f"{int(m.group(2)):02d}", m.group(3)
            styles[f"{year}-{q}"] = style
    return styles


_STYLES = _load_src_styles()


def get_image_tag(year: str, qnum: str, alt_text: str = None, prefix: str = "../") -> str:
    qn = f"{int(qnum):02d}"
    key = f"{year}-{qn}"
    img_path = ROOT / f"bank/{year}/q{qn}.png"
    if not img_path.exists():
        return f"<!-- Missing image: {img_path} -->"

    alt = alt_text or key
    if key in _STYLES:
        style = _STYLES[key]
    else:
        im = Image.open(img_path)
        w, _ = im.size
        w_em = round(w / 26.0, 2)
        style = f"display: block; width: {w_em}em; max-width: 100%; height: auto; margin: 12px 0;"

    return f'<img src="{prefix}bank/{year}/q{qn}.png" alt="{alt}" style="{style}">'


if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 3:
        print(get_image_tag(sys.argv[1], sys.argv[2]))
    else:
        print("Usage: python3 format_q_img.py <year> <qnum>")
