#!/usr/bin/env python3
"""Transcript telemetry for wf_5b0b492d-cda: verify probe self-reports against ground truth."""
import json
import glob
import re
from pathlib import Path

TDIR = Path("/home/jerem/.claude/projects/-home-jerem-claude-code-project-best-practices/0ae1ac5a-4390-4786-8ee1-c5025f5a0325/subagents/workflows/wf_5b0b492d-cda")
KEY = json.load(open("/tmp/claude-1000/-home-jerem-claude-code-project-best-practices/0ae1ac5a-4390-4786-8ee1-c5025f5a0325/scratchpad/fixtures/answer_key.json"))
ALL_VALUES = [f["value"] for v in KEY.values() for f in v["facts"]]

for path in sorted(TDIR.glob("agent-*.jsonl")):
    tool_calls = []   # (name, file_path, offset, limit)
    leaked = 0        # registry values appearing in assistant text/thinking BEFORE the final structured output
    n_assist_text = 0
    compaction = 0
    lines = path.read_text(errors="replace").splitlines()
    events = []
    for ln in lines:
        try:
            events.append(json.loads(ln))
        except Exception:
            pass
    # find index of the StructuredOutput call (final answer)
    so_idx = None
    for i, e in enumerate(events):
        msg = e.get("message") or {}
        for blk in (msg.get("content") or []) if isinstance(msg.get("content"), list) else []:
            if blk.get("type") == "tool_use":
                name = blk.get("name", "")
                inp = blk.get("input") or {}
                tool_calls.append((name, inp.get("file_path", ""), inp.get("offset"), inp.get("limit")))
                if "StructuredOutput" in name or name == "structured_output":
                    so_idx = i
    for i, e in enumerate(events):
        if so_idx is not None and i >= so_idx:
            break
        msg = e.get("message") or {}
        if (msg.get("role") == "assistant") and isinstance(msg.get("content"), list):
            for blk in msg["content"]:
                if blk.get("type") in ("text", "thinking"):
                    t = blk.get("text") or blk.get("thinking") or ""
                    n_assist_text += 1
                    leaked += sum(1 for v in ALL_VALUES if v in t)
        if "compact" in json.dumps(e).lower()[:200]:
            compaction += 1
    reads = [(c[1], c[2], c[3]) for c in tool_calls if c[0] == "Read"]
    other = sorted({c[0] for c in tool_calls} - {"Read"})
    files = sorted({r[0].split("/")[-1] for r in reads})
    offsets = [r[1] for r in reads]
    seq_ok = all(offsets[i] == (offsets[i-1] or 1) + 300 for i in range(1, len(offsets))) if len(offsets) > 1 else True
    mono_ok = offsets == sorted(offsets) and len(set(offsets)) == len(offsets)
    print(f"{path.name}: reads={len(reads)} files={files} first_off={offsets[0] if offsets else None} "
          f"seq+300={seq_ok} monotone_norepeat={mono_ok} other_tools={other} "
          f"values_in_pre-answer_text/thinking={leaked} compaction_markers={compaction}")
