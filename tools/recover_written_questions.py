#!/usr/bin/env python3
"""Recover verified large-question crops directly from a historical Git blob."""
import argparse
import io
import json
import re
import subprocess
from pathlib import Path

from PIL import Image, ImageChops


REPO = Path(__file__).resolve().parent.parent
SOURCE = REPO / "data" / "written_historical_seeds.json"


def historical_image(commit, path):
    blob = subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=REPO)
    return Image.open(io.BytesIO(blob)).copy()


def crop_box(geometry):
    match = re.fullmatch(r"(\d+)x(\d+)\+(\d+)\+(\d+)", geometry)
    if not match:
        raise ValueError(f"bad crop geometry: {geometry}")
    width, height, left, top = map(int, match.groups())
    return left, top, left + width, top + height


def same_pixels(left, right):
    if left.size != right.size:
        return False
    return ImageChops.difference(left.convert("RGBA"), right.convert("RGBA")).getbbox() is None


def recover(check_only=False):
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    commit = data["source_commit"]
    sources = {}
    stale = []
    for qid, item in data["questions"].items():
        source_path = item["source_path"]
        if source_path not in sources:
            sources[source_path] = historical_image(commit, source_path)
        recovered = sources[source_path].crop(crop_box(item["crop"]))
        year, number = qid.split("-")
        target = REPO / "bank" / year / f"q{number}.png"
        if check_only:
            if not target.exists():
                stale.append(target.relative_to(REPO).as_posix())
                continue
            with Image.open(target) as current:
                matches = same_pixels(recovered, current)
            if not matches:
                stale.append(target.relative_to(REPO).as_posix())
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        recovered.save(target, format="PNG", optimize=True)

    if stale:
        raise SystemExit("recovered large-question images are stale or missing:\n" + "\n".join(stale))
    action = "verified" if check_only else "recovered"
    print(f"{action}: {len(data['questions'])} complete large questions from {commit[:8]}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    recover(check_only=args.check)


if __name__ == "__main__":
    main()
