#!/usr/bin/env python3
"""Show the already-compiled ability-line node for one date."""
import argparse
import datetime as dt
import json
import re
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
CHAINS = [
    ("choice", REPO / "data" / "question_chain.json"),
    ("written", REPO / "data" / "written_chain.json"),
]


def date_key(raw):
    if re.fullmatch(r"\d{4}", raw):
        return raw
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw):
        return raw[5:7] + raw[8:10]
    raise SystemExit("date must be MMDD or YYYY-MM-DD")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=dt.date.today().strftime("%m%d"))
    args = parser.parse_args()
    key = date_key(args.date)
    available = []
    node = None
    mode = None
    for chain_mode, path in CHAINS:
        if not path.exists():
            continue
        chain = json.loads(path.read_text(encoding="utf-8"))
        available.append(f"{chain['nodes'][0]['key']}..{chain['nodes'][-1]['key']}")
        candidate = next((item for item in chain["nodes"] if item["key"] == key), None)
        if candidate is not None:
            node = candidate
            mode = chain_mode
            break
    if node is None:
        ranges = ", ".join(available) if available else "no compiled chains"
        raise SystemExit(f"{key} is outside the compiled question chains ({ranges})")
    print(f"{node['key']} · {node['title']}")
    print(node["file"])
    print(" ".join(node["questions"]))
    print(f"讲解：src/{key}-answer.md")
    print("先独立作答；复做记录写新事件，不覆盖历史首次作答。")



if __name__ == "__main__":
    main()
