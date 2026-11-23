#!/usr/bin/env python3
"""Verify 100% lossless coverage of outline/ topics and sprint40 questions in lineages/."""

import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST_PATH = os.path.join(ROOT, "lineages", "manifest.json")
SCHEDULE_PATH = os.path.join(ROOT, "sprint40", "content", "schedule.json")


def main() -> int:
    errors = []

    with open(MANIFEST_PATH, encoding="utf-8") as f:
        manifest = json.load(f)
    with open(SCHEDULE_PATH, encoding="utf-8") as f:
        schedule = json.load(f)

    # 1. Collect all outline topic files (exclude README.md and outline/audit/*)
    actual_outlines = set()
    for p in glob.glob(os.path.join(ROOT, "outline", "0*", "*", "*.md")):
        rel = os.path.relpath(p, ROOT).replace("\\", "/")
        actual_outlines.add(rel)

    # 2. Collect all sprint40 unique choice groups, choice questions, and written questions
    group_to_qs = {}
    actual_choices = set()
    actual_written = set()
    for day in schedule["days"]:
        for g in day["groups"]:
            src = g["source"]
            group_to_qs.setdefault(src, set()).update(g["questions"])
            actual_choices.update(g["questions"])
        actual_written.update(day["written"])

    # 3. Audit manifest
    mapped_outlines = []
    mapped_groups = []
    mapped_choices = set()
    mapped_written = []
    authored = 0
    total_lineages = 0

    for subj in manifest["subjects"]:
        for lin in subj["lineages"]:
            total_lineages += 1
            for o in lin["outlines"]:
                mapped_outlines.append(o)
                if not os.path.exists(os.path.join(ROOT, o)):
                    errors.append(f"Missing outline file referenced in {lin['id']}: {o}")
            for g in lin["choice_groups"]:
                mapped_groups.append(g)
                if g not in group_to_qs:
                    errors.append(f"Unknown choice group in {lin['id']}: {g}")
                else:
                    mapped_choices.update(group_to_qs[g])
            for w in lin["written"]:
                mapped_written.append(w)

            # Check authored file links if file exists
            fpath = os.path.join(ROOT, "lineages", lin["file"])
            if os.path.exists(fpath):
                authored += 1
                with open(fpath, encoding="utf-8") as f:
                    content = f.read()
                for m in re.finditer(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]+)?\)", content):
                    target = m.group(1)
                    if target.startswith(("http://", "https://", "mailto:")):
                        continue
                    resolved = os.path.normpath(os.path.join(os.path.dirname(fpath), target))
                    if not os.path.exists(resolved):
                        errors.append(f"Broken link in lineages/{lin['file']}: {target}")

    # Check outline coverage
    outline_set = set(mapped_outlines)
    if len(mapped_outlines) != len(outline_set):
        dups = [x for x in outline_set if mapped_outlines.count(x) > 1]
        errors.append(f"Duplicate outline mappings: {dups}")
    missing_outlines = sorted(actual_outlines - outline_set)
    extra_outlines = sorted(outline_set - actual_outlines)
    if missing_outlines:
        errors.append(f"Unmapped outline topics ({len(missing_outlines)}): {missing_outlines}")
    if extra_outlines:
        errors.append(f"Extra non-topic outlines ({len(extra_outlines)}): {extra_outlines}")

    # Check choice group & question coverage
    group_set = set(mapped_groups)
    if len(mapped_groups) != len(group_set):
        dups = [x for x in group_set if mapped_groups.count(x) > 1]
        errors.append(f"Duplicate choice group mappings: {dups}")
    missing_groups = sorted(set(group_to_qs.keys()) - group_set)
    if missing_groups:
        errors.append(f"Unmapped choice groups: {missing_groups}")
    missing_choices = sorted(actual_choices - mapped_choices)
    if missing_choices:
        errors.append(f"Unmapped choice questions ({len(missing_choices)}): {missing_choices}")

    # Check written question coverage
    written_set = set(mapped_written)
    if len(mapped_written) != len(written_set):
        dups = [x for x in written_set if mapped_written.count(x) > 1]
        errors.append(f"Duplicate written mappings: {dups}")
    missing_written = sorted(actual_written - written_set)
    extra_written = sorted(written_set - actual_written)
    if missing_written:
        errors.append(f"Unmapped written questions ({len(missing_written)}): {missing_written}")
    if extra_written:
        errors.append(f"Unknown written questions ({len(extra_written)}): {extra_written}")

    print(f"Lineages: {total_lineages} total ({authored} authored)")
    print(f"Outlines: {len(outline_set)}/{len(actual_outlines)} mapped")
    print(f"Choice groups: {len(group_set)}/{len(group_to_qs)} mapped ({len(mapped_choices)}/{len(actual_choices)} unique choices)")
    print(f"Written questions: {len(written_set)}/{len(actual_written)} mapped")
    print(f"Total unique 2020-2026 questions: {len(mapped_choices) + len(written_set)}/{len(actual_choices) + len(actual_written)}")

    if errors:
        print("\nFAIL:")
        for e in errors:
            print("  -", e)
        return 1

    print("\nPASS: 100% lossless coverage verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
