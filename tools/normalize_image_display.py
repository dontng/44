#!/usr/bin/env python3
"""Apply reviewed per-image display widths without rebuilding study prose."""
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PATTERN = re.compile(r'<img\b[^>]*\bsrc="(?P<html>[^\"]*bank/\d{4}/q\d{2}\.png)"[^>]*>|!\[(?P<alt>[^\]]*)\]\((?P<md>[^\s)]*bank/\d{4}/q\d{2}\.png)\)')


def normalize(path, text, images):
    def replace(match):
        rel = match['html'] or match['md']
        image = (path.parent / rel).resolve()
        key = f'{image.parent.name}-{int(image.stem[1:]):02d}'
        width = images[key]['width_em']
        alt = match['alt'] if match['md'] else re.search(r'alt="([^"]*)"', match[0]).group(1)
        tag = f'<img src="{rel}" alt="{alt}" style="display:block; width:{width:.2f}em; max-width:none; height:auto;">'
        if match['html']:
            return tag
        return '<div style="max-width:100%; max-height:min(90vh, 72em); overflow:auto;">\n' + tag + '\n</div>'
    return PATTERN.sub(replace, text)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    images = json.loads((ROOT / 'data/image_display_widths.json').read_text())['images']
    for key, item in images.items():
        image = ROOT / item['path']
        if hashlib.sha256(image.read_bytes()).hexdigest() != item['sha256']:
            raise SystemExit(f'Recalibrate changed image: {key}')
    changed = []
    for path in sorted((ROOT / 'src').rglob('*.md')):
        text = path.read_text()
        result = normalize(path, text, images)
        if text != result:
            changed.append(str(path.relative_to(ROOT)))
            if not args.check:
                path.write_text(result)
    if args.check and changed:
        raise SystemExit('Inconsistent display widths: ' + ', '.join(changed))
    print(f'{len(images)} calibrated original images; {len(changed)} Markdown files ' + ('need changes' if args.check else 'updated'))


if __name__ == '__main__':
    main()
