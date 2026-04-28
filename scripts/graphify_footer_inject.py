#!/usr/bin/env python3
"""
Append a "Related (from graph)" footer to each analysis/*.md based on
graphify-out/graph.json. Edges are tagged INFERRED|EXTRACTED|AMBIGUOUS;
the footer is regenerated on each run between markers so the script
is idempotent.

Usage:
    python scripts/graphify_footer_inject.py                # dry run
    python scripts/graphify_footer_inject.py --write         # rewrite files
    python scripts/graphify_footer_inject.py --graph PATH    # custom graph.json
    python scripts/graphify_footer_inject.py --target DIR    # custom target dir
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

START_MARKER = "<!-- graphify-footer:start -->"
END_MARKER = "<!-- graphify-footer:end -->"
DEFAULT_GRAPH = Path("graphify-out/graph.json")
DEFAULT_TARGET = Path("analysis")


def load_graph(path: Path) -> dict:
    if not path.exists():
        sys.exit(
            f"graph file not found: {path}\n"
            "Run `graphify .` first (or pass --graph). "
            "If graphify hasn't been run because of egress concerns, "
            "skip this script — it's a no-op without a graph."
        )
    with path.open() as f:
        return json.load(f)


def edges_by_source(graph: dict) -> dict[str, list[dict]]:
    """Group edges by source node id. Tolerant of graphify schema variations."""
    by_src: dict[str, list[dict]] = defaultdict(list)
    edges = graph.get("edges") or graph.get("links") or []
    for edge in edges:
        src = edge.get("source") or edge.get("from")
        dst = edge.get("target") or edge.get("to")
        if not src or not dst:
            continue
        by_src[str(src)].append(
            {
                "target": str(dst),
                "provenance": edge.get("provenance") or edge.get("kind") or "INFERRED",
                "confidence": edge.get("confidence") or edge.get("weight"),
                "label": edge.get("label") or edge.get("relation"),
            }
        )
    return by_src


def render_footer(edges: list[dict]) -> str:
    if not edges:
        return ""
    edges_sorted = sorted(
        edges,
        key=lambda e: (
            {"EXTRACTED": 0, "INFERRED": 1, "AMBIGUOUS": 2}.get(e["provenance"], 3),
            -(e["confidence"] or 0) if isinstance(e["confidence"], (int, float)) else 0,
        ),
    )
    lines = ["", START_MARKER, "", "## Related (from graph)", ""]
    for e in edges_sorted[:15]:
        conf = f" ({e['confidence']:.2f})" if isinstance(e["confidence"], (int, float)) else ""
        label = f" — {e['label']}" if e["label"] else ""
        lines.append(f"- `{e['target']}` [{e['provenance']}{conf}]{label}")
    lines.extend(["", END_MARKER, ""])
    return "\n".join(lines)


def upsert_footer(path: Path, footer: str) -> tuple[bool, str]:
    """Return (changed, new_text). Replaces existing footer block or appends."""
    text = path.read_text()
    if START_MARKER in text and END_MARKER in text:
        before, _, rest = text.partition(START_MARKER)
        _, _, after = rest.partition(END_MARKER)
        new_text = before.rstrip() + ("\n" + footer.strip() + "\n" if footer else "\n") + after.lstrip()
    else:
        new_text = text.rstrip() + "\n\n" + footer.strip() + "\n" if footer else text
    return new_text != text, new_text


def doc_id(path: Path, target: Path) -> str:
    """Identifier graphify likely used for this doc — try a few forms."""
    return str(path.relative_to(target.parent)) if target.parent != Path(".") else str(path)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--graph", type=Path, default=DEFAULT_GRAPH)
    p.add_argument("--target", type=Path, default=DEFAULT_TARGET)
    p.add_argument("--write", action="store_true", help="actually rewrite files")
    args = p.parse_args()

    graph = load_graph(args.graph)
    by_src = edges_by_source(graph)

    files = sorted(args.target.glob("*.md"))
    changed = 0
    no_edges = 0
    for f in files:
        candidates = [
            doc_id(f, args.target),
            str(f),
            f.name,
            f.stem,
        ]
        edges: list[dict] = []
        for cid in candidates:
            if cid in by_src:
                edges = by_src[cid]
                break

        if not edges:
            no_edges += 1
            continue

        footer = render_footer(edges)
        will_change, new_text = upsert_footer(f, footer)
        if not will_change:
            continue
        if args.write:
            f.write_text(new_text)
        changed += 1
        print(f"{'wrote' if args.write else 'would change'}: {f}")

    print(
        f"\n{len(files)} files scanned, "
        f"{changed} would change, "
        f"{no_edges} have no edges in graph."
    )
    if not args.write:
        print("Dry run. Re-run with --write to apply.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
