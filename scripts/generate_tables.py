#!/usr/bin/env python3
"""
generate_tables.py — turn data/hardware.yaml into (a) a Markdown table injected
into hardware-comparison/README.md and (b) docs/picker/hardware.json for the
interactive picker.

This is the fix for hand-edited, misaligned spec tables: the data lives in ONE
YAML file, and every rendered view is generated from it, so columns can never
drift out of alignment again.

Usage
-----
    pip install pyyaml
    python scripts/generate_tables.py            # regenerate everything
    python scripts/generate_tables.py --check    # exit 1 if outputs are stale
                                                 # (use in CI to enforce regen)

The README table is written between these markers (they must already exist):
    <!-- HW-TABLE:START -->
    ... generated ...
    <!-- HW-TABLE:END -->
Prose outside the markers is preserved.
"""

import argparse
import json
import pathlib
import sys

import yaml

# Repo root = parent of the scripts/ directory this file lives in.
ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "hardware.yaml"
README = ROOT / "hardware-comparison" / "README.md"
PICKER_JSON = ROOT / "docs" / "picker" / "hardware.json"

START = "<!-- HW-TABLE:START -->"
END = "<!-- HW-TABLE:END -->"

# claim_type -> marker used in the "Src" column
CLAIM_MARK = {"independent": "🔬", "vendor": "©"}


def load_items():
    """Load and lightly validate the hardware list."""
    items = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    if not isinstance(items, list):
        raise SystemExit(f"{DATA} must contain a YAML list")
    required = {"id", "name", "vendor", "ai_perf", "power_w", "claim_type", "status"}
    for i in items:
        missing = required - set(i)
        if missing:
            raise SystemExit(f"entry {i.get('id', '?')} missing fields: {sorted(missing)}")
    return items


def perf_str(i):
    p = i["ai_perf"]
    return f'{p["value"]} {p["unit"]} ({p["precision"]})'


def power_str(i):
    lo, hi = i["power_w"]["min"], i["power_w"]["max"]
    return f"{lo} W" if lo == hi else f"{lo}–{hi} W"


def price_str(i):
    p = i.get("price_usd")
    return f"${p}" if p else "—"


def rows(items):
    for i in items:
        yield (
            f'| {i["name"]} '
            f'| {i["vendor"]} '
            f'| {perf_str(i)} '
            f'| {power_str(i)} '
            f'| {i.get("memory", "—")} '
            f'| {"✅" if i.get("genai_capable") else "❌"} '
            f'| {price_str(i)} '
            f'| {i["status"]} '
            f'| {CLAIM_MARK.get(i["claim_type"], "?")} |'
        )


def build_table(items):
    header = (
        "| Part | Vendor | AI perf (peak) | Power | Memory | GenAI | Price | Status | Src |"
    )
    sep = "|" + "---|" * 9
    legend = (
        "\n\n> **Src:** 🔬 = independent third-party benchmark · © = vendor claim. "
        "**AI perf** is a peak figure at the stated precision; INT4/INT8/FP4 are not comparable. "
        "`status: samples` = announced/sampling, not generally shipping."
    )
    body = "\n".join(rows(items))
    note = "<!-- AUTO-GENERATED from data/hardware.yaml by scripts/generate_tables.py — do not edit by hand -->"
    return f"{note}\n\n{header}\n{sep}\n{body}{legend}"


def inject(text, block):
    if START not in text or END not in text:
        raise SystemExit(
            f"markers {START} / {END} not found in {README}. Add them where the "
            "generated table should go."
        )
    pre = text.split(START)[0]
    post = text.split(END)[1]
    return f"{pre}{START}\n{block}\n{END}{post}"


def picker_payload(items):
    """Trim each entry to the fields the picker needs (keeps hardware.json small)."""
    keep = (
        "id", "name", "vendor", "category", "ai_perf", "power_w", "memory",
        "genai_capable", "price_usd", "best_for", "claim_type", "status",
    )
    return [{k: i.get(k) for k in keep} for i in items]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="verify outputs are up to date; exit 1 if not (for CI)")
    args = ap.parse_args()

    items = load_items()
    block = build_table(items)
    new_readme = inject(README.read_text(encoding="utf-8"), block)
    new_json = json.dumps(picker_payload(items), indent=2, ensure_ascii=False) + "\n"

    if args.check:
        stale = []
        if README.read_text(encoding="utf-8") != new_readme:
            stale.append(str(README.relative_to(ROOT)))
        if not PICKER_JSON.exists() or PICKER_JSON.read_text(encoding="utf-8") != new_json:
            stale.append(str(PICKER_JSON.relative_to(ROOT)))
        if stale:
            print("Stale (run: python scripts/generate_tables.py):")
            for s in stale:
                print(f"  - {s}")
            return 1
        print("Tables and picker JSON are up to date.")
        return 0

    README.write_text(new_readme, encoding="utf-8")
    PICKER_JSON.parent.mkdir(parents=True, exist_ok=True)
    PICKER_JSON.write_text(new_json, encoding="utf-8")
    print(f"Wrote {README.relative_to(ROOT)} and {PICKER_JSON.relative_to(ROOT)} "
          f"({len(items)} parts).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
