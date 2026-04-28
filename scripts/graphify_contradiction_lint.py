#!/usr/bin/env python3
"""
Advisory lint: flag analysis/*.md claims that assert an EXTRACTED-strength
relationship the graph doesn't have.

Heuristic at this stage: scan markdown for claim patterns of the form
"X verified Y" / "X confirmed Y" / "X = Y (verified ...)" — anywhere a
prose claim asserts strong (EXTRACTED-equivalent) ground truth. Then
check whether graphify's graph.json contains a matching EXTRACTED edge.
If not, surface the line as a candidate for review.

Designed to be near-zero-signal at this repo's 28-doc scale (that's
expected; this is a pattern stub for downstream consumers running at
~500-doc scale where it earns its keep).

Usage:
    python scripts/graphify_contradiction_lint.py
    python scripts/graphify_contradiction_lint.py --graph PATH --target DIR
    python scripts/graphify_contradiction_lint.py --json   # machine-readable
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

DEFAULT_GRAPH = Path("graphify-out/graph.json")
DEFAULT_TARGET = Path("analysis")

CLAIM_PATTERNS = [
    re.compile(r"\b([A-Z][\w./-]+)\s+(?:is|=)\s+([A-Z][\w./-]+)\s*\(verified", re.I),
    re.compile(r"\b([A-Z][\w./-]+)\s+verified\s+(?:as\s+)?([A-Z][\w./-]+)", re.I),
    re.compile(r"\b([A-Z][\w./-]+)\s+confirmed\s+(?:to be\s+|as\s+)?([A-Z][\w./-]+)", re.I),
]


def load_graph(path: Path) -> dict:
    if not path.exists():
        print(
            f"graph file not found: {path}\n"
            "Lint requires graphify-out/graph.json. Skipping (no-op).",
            file=sys.stderr,
        )
        return {"edges": []}
    with path.open() as f:
        return json.load(f)


def extracted_edges(graph: dict) -> set[tuple[str, str]]:
    """Edges marked EXTRACTED in either schema variant.

    graphify v0.5.x stores the EXTRACTED/INFERRED label in `confidence`
    (string) with the numeric in `confidence_score`. Older / alt schemas
    used `provenance` (or `kind`). Accept both.
    """
    edges = graph.get("edges") or graph.get("links") or []
    out: set[tuple[str, str]] = set()
    for e in edges:
        prov = (e.get("provenance") or e.get("kind") or "")
        if not prov:
            cval = e.get("confidence")
            if isinstance(cval, str):
                prov = cval
        if str(prov).upper() != "EXTRACTED":
            continue
        src = e.get("source") or e.get("from")
        dst = e.get("target") or e.get("to")
        if src and dst:
            out.add((str(src).lower(), str(dst).lower()))
            out.add((str(dst).lower(), str(src).lower()))
    return out


def scan_file(path: Path, ground_truth: set[tuple[str, str]]) -> list[dict]:
    findings: list[dict] = []
    for lineno, line in enumerate(path.read_text().splitlines(), start=1):
        for pat in CLAIM_PATTERNS:
            m = pat.search(line)
            if not m:
                continue
            subj, obj = m.group(1).strip().lower(), m.group(2).strip().lower()
            if (subj, obj) in ground_truth:
                continue
            findings.append(
                {
                    "file": str(path),
                    "line": lineno,
                    "subject": subj,
                    "object": obj,
                    "text": line.strip(),
                }
            )
    return findings


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--graph", type=Path, default=DEFAULT_GRAPH)
    p.add_argument("--target", type=Path, default=DEFAULT_TARGET)
    p.add_argument("--json", action="store_true", help="emit JSON output")
    args = p.parse_args()

    graph = load_graph(args.graph)
    ground_truth = extracted_edges(graph)

    findings: list[dict] = []
    for f in sorted(args.target.glob("*.md")):
        findings.extend(scan_file(f, ground_truth))

    if args.json:
        print(json.dumps({"ground_truth_size": len(ground_truth), "findings": findings}, indent=2))
        return 0

    if not findings:
        print(
            f"No candidate contradictions in {args.target}/ "
            f"(graph EXTRACTED edges: {len(ground_truth) // 2}). "
            "At small scale this is expected — the pattern earns its keep at ~500 docs."
        )
        return 0

    for fnd in findings:
        print(f"{fnd['file']}:{fnd['line']}: claim '{fnd['subject']} → {fnd['object']}' has no EXTRACTED edge")
        print(f"   {fnd['text']}")
    print(f"\n{len(findings)} candidate contradiction(s). Advisory only — review and dismiss false positives.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
