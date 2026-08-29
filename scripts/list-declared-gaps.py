#!/usr/bin/env python3
"""
Enumerate the repository's own declared evidence gaps.

    python3 scripts/list-declared-gaps.py
    python3 scripts/list-declared-gaps.py --json
    python3 scripts/list-declared-gaps.py --untracked   # not mentioned in PLAN.md

WHY THIS EXISTS
---------------
`analysis/CANONICAL-DOC-TEMPLATE.md:89` defines a convention for declaring what a
document does not know:

    - **Gap: {topic}**. {Description}. **Needs**: {what would close it}.

On 2026-08-29, twenty declarations followed it across five analysis docs and
**nothing read them**: no script, no workflow, no hook, and neither
CONTRIBUTING.md nor any weekly-review step mentioned the convention. Each gap was
discoverable only by opening the document that contained it. (Run the script for
the current count — this paragraph is a dated record of why it exists, not a
live figure.)

That is this repository's own subject matter turned on itself. `analysis/prose-
corpus-discoverability.md` argues that prose whose discriminating property is
authority or currency cannot be found by retrieval — and the repo's structured
record of its own open questions sat in exactly that condition: well-formed,
conventional, and unreachable by any instrument.

This script does not judge or schedule. It enumerates, so a human or a weekly
review can. Deliberately dumb: a gap that is declared is listed, whether or not
anyone intends to close it. Declaring a gap and never revisiting it is a
legitimate choice; not being able to list them is not.
"""

import argparse
import json
import re
import sys
from pathlib import Path

# The template DEFINES the convention and carries worked examples in block
# quotes. Counting those as real gaps would inflate every total by three.
SKIP = {"CANONICAL-DOC-TEMPLATE.md"}

# The `**Needs**:` clause is what anchors a match. It is the only part the
# convention actually requires, and the only part that states what would close
# the gap, so it — not the lead-in — defines a declaration.
NEEDS = re.compile(r"\*\*Needs\*\*:\s*(?P<needs>.+?)\s*$")

# The lead-in is the bolded span that opens the list item. Three of the five
# docs write the template's literal `- **Gap: topic.**`; the other two write a
# plain bolded title (`- **Runaway-loop economics.**`). Anchoring on the
# leading bold span catches both, where matching only `**Gap:` silently
# dropped the topic on six of twenty declarations.
LEAD = re.compile(r"^\s*[-*]\s+\*\*(?P<topic>[^*]+?)\*\*")
GAP_PREFIX = re.compile(r"^Gap\s*\d*\s*[:.]?\s*", re.IGNORECASE)


def scan(root: Path, dirs) -> list[dict]:
    out = []
    for d in dirs:
        # A missing directory must not read as "no gaps". `Path.glob` on a
        # nonexistent path yields nothing and raises nothing, so a typo in
        # --dirs would otherwise print a clean report from an instrument that
        # never looked at anything — the fail-open shape this repository keeps
        # finding in its own checks.
        if not (root / d).is_dir():
            raise SystemExit(
                f"error: {root / d} is not a directory — refusing to report "
                f"a gap count for a path that was never scanned."
            )
        for path in sorted((root / d).glob("*.md")):
            if path.name in SKIP:
                continue
            lines = path.read_text(encoding="utf-8", errors="replace").split("\n")
            for i, line in enumerate(lines, 1):
                m = NEEDS.search(line)
                if not m:
                    continue
                lead = LEAD.match(line)
                topic = ""
                if lead:
                    topic = GAP_PREFIX.sub("", lead.group("topic").strip())
                    topic = topic.strip().rstrip(".")
                out.append({
                    "file": str(path.relative_to(root)),
                    "line": i,
                    "topic": topic,
                    "needs": m.group("needs").strip(),
                })
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--root", default=".", help="repository root")
    ap.add_argument("--dirs", nargs="*", default=["analysis"],
                    help="directories to scan (default: analysis)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--untracked", action="store_true",
                    help="only gaps whose topic words do not appear in PLAN.md. "
                         "A WEAK heuristic — word overlap, not semantics — so treat "
                         "a hit as 'probably mentioned somewhere', never as 'tracked'.")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    gaps = scan(root, args.dirs)

    if args.untracked:
        plan_path = root / "PLAN.md"
        plan = plan_path.read_text(encoding="utf-8", errors="replace").lower() \
            if plan_path.exists() else ""
        kept = []
        for g in gaps:
            words = re.findall(r"[a-z]{7,}", (g["topic"] + " " + g["needs"]).lower())[:5]
            if sum(1 for w in words if w in plan) < 2:
                kept.append(g)
        gaps = kept

    if args.json:
        print(json.dumps({"count": len(gaps), "gaps": gaps}, indent=2))
        return 0

    if not gaps:
        print("no declared gaps found "
              f"(scanned {', '.join(args.dirs)}/ for the **Needs**: convention)")
        return 0

    by_file: dict[str, list[dict]] = {}
    for g in gaps:
        by_file.setdefault(g["file"], []).append(g)

    for f, items in by_file.items():
        print(f"\n{f}")
        for g in items:
            head = f"  :{g['line']}"
            if g["topic"]:
                head += f"  {g['topic']}"
            print(head)
            print(f"      needs: {g['needs']}")

    print(f"\n{len(gaps)} declared gap(s) across {len(by_file)} document(s).")
    print("Declared, not scheduled — this script enumerates, it does not judge.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
