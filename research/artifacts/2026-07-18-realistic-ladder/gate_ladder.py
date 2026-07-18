#!/usr/bin/env python3
"""Transcript gate for ladder agents: per-turn served model, guide Read, hygiene."""
import json
import re
import sys
from pathlib import Path

TASKS = Path("/tmp/claude-1000/-home-jerem-claude-code-project-best-practices/ca4ee1d1-304e-4c91-9528-02a7c82e0abf/tasks")
HERE = Path(__file__).parent
AGENTS = json.load(open(HERE / "agents_map.json"))

EXPECT = {"fable": "claude-fable-5", "opus": "claude-opus-4-8"}

rows = {}
for label, aid in sorted(AGENTS.items()):
    p = TASKS / f"{aid}.output"
    if not p.exists():
        rows[label] = {"error": "no transcript"}
        continue
    models = {}
    reads = []
    writes = []
    compaction = 0
    assist_text_blocks = 0
    for ln in p.read_text(errors="replace").splitlines():
        try:
            e = json.loads(ln)
        except Exception:
            continue
        msg = e.get("message") or {}
        if msg.get("model"):
            models[msg["model"]] = models.get(msg["model"], 0) + 1
        if "compact" in json.dumps(e)[:300].lower():
            compaction += 1
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
    model_key = label.split("-")[0]
    exp = EXPECT[model_key]
    all_expected = set(models) == {exp}
    guide_reads = [r for r in reads if "GUIDE-" in r]
    is_treatment = "-K" in label
    rung = re.search(r"-K(\d+)-", label + "-")
    guide_ok = (not is_treatment) or any(f"GUIDE-{rung.group(1)}.md" in r for r in guide_reads)
    guide_contam = (not is_treatment) and bool(guide_reads)
    rows[label] = {
        "models": models, "all_expected_model": all_expected,
        "guide_read_ok": guide_ok, "baseline_guide_contamination": guide_contam,
        "n_reads": len(reads), "n_writes": len(writes),
        "assist_text_blocks": assist_text_blocks, "compaction_markers": compaction,
        "GATE": "PASS" if (all_expected and guide_ok and not guide_contam and compaction == 0) else "FAIL",
    }

print(json.dumps(rows, indent=1))
json.dump(rows, open(HERE / "gate_results.json", "w"), indent=1)
fails = [k for k, v in rows.items() if v.get("GATE") != "PASS"]
print(f"\nGATE FAIL: {fails if fails else 'none'}")
