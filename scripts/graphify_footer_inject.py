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


def edges_by_file(graph: dict) -> dict[str, list[dict]]:
    """Aggregate cross-file relationships. For each source_file, collect the
    target *files* of all outbound edges (skipping intra-file edges).

    Prose corpora produce many concept nodes per markdown file, so file-level
    aggregation is what produces a useful "Related" footer. The earlier
    node-id-keyed lookup only worked when graphify modelled each doc as a
    single node, which it doesn't for prose.
    """
    nodes = {n.get("id"): n for n in (graph.get("nodes") or [])}
    by_file: dict[str, dict[str, dict]] = defaultdict(dict)
    edges = graph.get("edges") or graph.get("links") or []

    for edge in edges:
        src = edge.get("source") or edge.get("from")
        dst = edge.get("target") or edge.get("to")
        if not src or not dst:
            continue
        src_file = (nodes.get(src) or {}).get("source_file")
        dst_file = (nodes.get(dst) or {}).get("source_file")
        if not src_file or not dst_file or src_file == dst_file:
            continue

        # graphify v0.5.x emits `confidence` as the EXTRACTED/INFERRED string and
        # `confidence_score` as the numeric. Older/alt schemas used `provenance`
        # and `weight`. Tolerate both.
        prov_raw = edge.get("provenance") or edge.get("kind")
        if not prov_raw:
            cval = edge.get("confidence")
            prov_raw = cval if isinstance(cval, str) else "INFERRED"
        prov = str(prov_raw).upper()
        score = edge.get("confidence_score")
        if score is None:
            cval = edge.get("confidence")
            score = cval if isinstance(cval, (int, float)) else edge.get("weight")

        key = dst_file
        existing = by_file[src_file].get(key)
        prov_rank = {"EXTRACTED": 0, "INFERRED": 1, "AMBIGUOUS": 2}
        # Keep the strongest evidence we've seen for this src→dst file pair,
        # plus a count of how many node-level edges contribute.
        if existing is None or prov_rank.get(prov, 3) < prov_rank.get(existing["provenance"], 3) or (
            prov == existing["provenance"]
            and (score or 0) > (existing["confidence"] or 0)
        ):
            by_file[src_file][key] = {
                "target": dst_file,
                "provenance": prov,
                "confidence": score,
                "label": edge.get("label") or edge.get("relation"),
                "count": (existing["count"] + 1) if existing else 1,
            }
        else:
            existing["count"] += 1

    return {src: list(targets.values()) for src, targets in by_file.items()}


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
        count = f" ×{e['count']}" if e.get("count", 1) > 1 else ""
        label = f" — {e['label']}" if e["label"] else ""
        lines.append(f"- [`{e['target']}`]({e['target']}) [{e['provenance']}{conf}{count}]{label}")
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


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--graph", type=Path, default=DEFAULT_GRAPH)
    p.add_argument("--target", type=Path, default=DEFAULT_TARGET)
    p.add_argument("--write", action="store_true", help="actually rewrite files")
    args = p.parse_args()

    graph = load_graph(args.graph)
    by_file = edges_by_file(graph)

    files = sorted(args.target.glob("*.md"))
    changed = 0
    no_edges = 0
    for f in files:
        # graphify stores source_file as the path relative to the repo root
        # (or whatever it was invoked on). Try a few keys to match.
        candidates = [str(f), f.name, str(f.relative_to(Path("."))) if Path(".") in f.parents else str(f)]
        edges: list[dict] = []
        for cid in candidates:
            if cid in by_file:
                edges = by_file[cid]
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
