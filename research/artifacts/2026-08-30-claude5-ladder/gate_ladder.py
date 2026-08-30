#!/usr/bin/env python3
"""Transcript gate for ladder agents: per-turn served model, guide Read, effort, hygiene.

Generalised from the 2026-07-18 gate, which hard-coded one machine's transcript path and
knew only two model strings. Transcript dir comes from --tasks or $CLAUDE_TASKS_DIR.

Usage: gate_ladder.py [--tasks DIR] [--run DIR]
"""
import argparse
import json
import re
import sys
from pathlib import Path

# label prefix -> expected served-model string. An arm whose transcript carries any other
# model string on any turn fails: the 2026-07-17 probe caught a silent fallback this way.
EXPECT = {
    "opus5": "claude-opus-5",
    "sonnet5": "claude-sonnet-5",
    "fable5": "claude-fable-5",
    "fable": "claude-fable-5",
    "opus": "claude-opus-4-8",
}

DELIVERABLES = ("lumen.py", "README.md", "CHANGELOG.md")

# Compaction detection. The 2026-07-18 gate scanned the first 300 chars of each event's
# JSON for the substring "compact", which both (a) false-positives on a deliverable that
# merely uses the word and (b) misses a marker past char 300. Structural fields alone
# would be worse: a clean transcript carries only type user/attachment/assistant, so a
# type-only check can never fire — a fail-open gate. This checks named structural flags
# AND the event envelope, and `--selftest` proves it fires.
COMPACT_KEYS = ("isCompactSummary", "compact_boundary", "compactMetadata")


def compaction_markers(e):
    """Return the compaction markers present in one transcript event."""
    hits = []
    for k in COMPACT_KEYS:
        if k in e and e.get(k):
            hits.append(k)
    for field in ("type", "subtype"):
        v = str(e.get(field) or "")
        if "compact" in v.lower():
            hits.append(f"{field}={v}")
    return hits


def selftest():
    """Positive control: the detector must fire on each marker shape and stay quiet on a
    clean event. Without this the compaction gate is unexercised and fails open."""
    cases = [
        ({"type": "assistant", "message": {"model": "claude-opus-5"}}, False),
        ({"type": "user", "message": {"content": "the digest is compact and tidy"}}, False),
        ({"type": "system", "subtype": "compact_boundary"}, True),
        ({"type": "compaction"}, True),
        ({"type": "user", "isCompactSummary": True}, True),
    ]
    ok = True
    for ev, want in cases:
        got = bool(compaction_markers(ev))
        flag = "ok " if got == want else "FAIL"
        if got != want:
            ok = False
        print(f"  [{flag}] expected={want} got={got}  {json.dumps(ev)[:70]}")
    print("selftest:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tasks", default=None, help="dir holding <agentid>.output transcripts")
    ap.add_argument("--run", default=None, help="run dir (agents_map.json, out/); default: script dir")
    ap.add_argument("--selftest", action="store_true", help="prove the compaction detector fires")
    a = ap.parse_args()

    if a.selftest:
        sys.exit(selftest())

    here = Path(a.run) if a.run else Path(__file__).parent
    tasks = Path(a.tasks) if a.tasks else None
    if tasks is None:
        import os
        env = os.environ.get("CLAUDE_TASKS_DIR")
        if not env:
            sys.exit("no transcript dir: pass --tasks DIR or set CLAUDE_TASKS_DIR")
        tasks = Path(env)
    if not tasks.is_dir():
        sys.exit(f"transcript dir not found: {tasks}")

    agents = json.load(open(here / "agents_map.json"))
    rows = {}
    for label, aid in sorted(agents.items()):
        p = tasks / f"{aid}.output"
        if not p.exists():
            rows[label] = {"error": "no transcript", "GATE": "FAIL"}
            continue
        models, efforts = {}, {}
        reads, writes = [], []
        compaction_hits = []
        assist_text_blocks = 0
        for ln in p.read_text(errors="replace").splitlines():
            try:
                e = json.loads(ln)
            except Exception:
                continue
            msg = e.get("message") or {}
            if msg.get("model"):
                models[msg["model"]] = models.get(msg["model"], 0) + 1
            # effort lives on the event envelope, not the message
            m = re.search(r'"effort"\s*:\s*"([a-z]+)"', ln)
            if m:
                efforts[m.group(1)] = efforts.get(m.group(1), 0) + 1
            compaction_hits.extend(compaction_markers(e))
            if isinstance(msg.get("content"), list):
                for blk in msg["content"]:
                    if blk.get("type") == "tool_use":
                        inp = blk.get("input") or {}
                        if blk.get("name") == "Read":
                            reads.append(inp.get("file_path", ""))
                        if blk.get("name") in ("Write", "Edit"):
                            writes.append(inp.get("file_path", ""))
                    elif blk.get("type") == "text" and msg.get("role") == "assistant":
                        if (blk.get("text") or "").strip():
                            assist_text_blocks += 1

        exp = EXPECT[label.split("-")[0]]
        all_expected = set(models) == {exp}
        guide_reads = [r for r in reads if "GUIDE-" in r]
        is_treatment = "-K" in label
        rung = re.search(r"-K(\d+)-", label + "-")
        guide_ok = (not is_treatment) or any(
            f"GUIDE-{rung.group(1)}.md" in r for r in guide_reads)
        guide_contam = (not is_treatment) and bool(guide_reads)
        outdir = here / "out" / label
        missing = [f for f in DELIVERABLES if not (outdir / f).exists()]

        rows[label] = {
            "models": models, "all_expected_model": all_expected, "effort": efforts,
            "guide_read_ok": guide_ok, "baseline_guide_contamination": guide_contam,
            "n_reads": len(reads), "n_writes": len(writes),
            "assist_text_blocks": assist_text_blocks,
            "compaction_markers": compaction_hits,
            "missing_deliverables": missing,
            "GATE": "PASS" if (all_expected and guide_ok and not guide_contam
                               and not compaction_hits and not missing) else "FAIL",
        }

    json.dump(rows, open(here / "gate_results.json", "w"), indent=1)
    for k, v in sorted(rows.items()):
        print(f"{k:22} {v.get('GATE'):5} models={list(v.get('models', {}))} "
              f"effort={list(v.get('effort', {}))} missing={v.get('missing_deliverables')}")
    fails = [k for k, v in rows.items() if v.get("GATE") != "PASS"]
    print(f"\nGATE FAIL ({len(fails)}): {fails if fails else 'none'}")


if __name__ == "__main__":
    main()
