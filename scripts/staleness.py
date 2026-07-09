#!/usr/bin/env python3
"""
staleness.py — write stale.md listing hardware entries whose `last_verified`
date is older than a threshold (default 180 days).

The data.yml workflow feeds stale.md into a SINGLE rolling "🕒 Stale data check"
issue that is updated in place — deliberately not one-issue-per-row, which would
spam the tracker. Run it manually any time:

    python scripts/staleness.py --today 2026-07-09 --days 180
    cat stale.md

`--today` is required in CI so the run is deterministic and reproducible; when
omitted it falls back to the system date for local convenience.
"""

import argparse
import datetime
import pathlib

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "hardware.yaml"
OUT = ROOT / "stale.md"


def parse_date(s):
    return datetime.date.fromisoformat(str(s))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--days", type=int, default=180,
                    help="staleness threshold in days (default 180)")
    ap.add_argument("--today", help="reference date YYYY-MM-DD (default: system date)")
    args = ap.parse_args()

    today = parse_date(args.today) if args.today else datetime.date.today()
    cutoff = today - datetime.timedelta(days=args.days)

    items = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    stale = []
    for i in items:
        lv = i.get("last_verified")
        if lv and parse_date(lv) < cutoff:
            age = (today - parse_date(lv)).days
            stale.append((age, i))
    stale.sort(reverse=True)  # oldest first

    lines = [
        "## 🕒 Stale data check",
        "",
        f"Entries in `data/hardware.yaml` not verified since **{cutoff.isoformat()}** "
        f"(> {args.days} days as of {today.isoformat()}).",
        "",
    ]
    if not stale:
        lines.append("✅ Nothing stale — every tracked part was verified within the window.")
    else:
        lines.append("| Part | Last verified | Age (days) | Source |")
        lines.append("|---|---|---|---|")
        for age, i in stale:
            lines.append(
                f'| {i["name"]} | {i["last_verified"]} | {age} | {i.get("source_url", "—")} |'
            )
        lines.append("")
        lines.append("Re-check each against its primary source, update `last_verified` "
                     "(and any changed figures), then run `python scripts/generate_tables.py`.")

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} — {len(stale)} stale ent(y/ies).")


if __name__ == "__main__":
    main()
