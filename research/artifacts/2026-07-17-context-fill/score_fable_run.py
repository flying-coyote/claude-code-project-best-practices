#!/usr/bin/env python3
"""Score + gate the 2026-07-17 Fable-path (main-loop Agent spawn) context-fill run."""
import json
import re
from pathlib import Path

TASKS = Path("/tmp/claude-1000/-home-jerem-claude-code-project-best-practices/ab049ad2-af9f-4683-a41a-545b8ae1a965/tasks")
KEY = json.load(open("/tmp/claude-1000/-home-jerem-claude-code-project-best-practices/0ae1ac5a-4390-4786-8ee1-c5025f5a0325/scratchpad/fixtures/answer_key.json"))
ALL_VALUES = [f["value"] for v in KEY.values() for f in v["facts"]]

AGENTS = [
    ("CAL-pos1", "CAL", "ae6289cfd7aae517e"), ("CAL-pos2", "CAL", "a2dd703a8521f2e20"),
    ("R40-1", "R40", "aec9374cc2bd6f397"), ("R40-2", "R40", "acb79157699c9b5af"), ("R40-3", "R40", "aceeafd5c36fa7df2"),
    ("R100-1", "R100", "a8e39338f6d2aafa0"), ("R100-2", "R100", "a4e4e52c45c39d6e4"), ("R100-3", "R100", "a50252237f7715d8f"),
    ("R140-1", "R140", "a611644dd9b651021"), ("R140-2", "R140", "ad09f7a10b0ea53e5"), ("R140-3", "R140", "a30a732bf3a0e1dda"),
    ("NEG-1", None, "a7fb88967b39a765c"), ("NEG-2", None, "ae65918c634f286c1"),
]

norm = lambda s: re.sub(r"[`'\"\s]", "", str(s or "")).lower()

for label, rung, aid in AGENTS:
    p = TASKS / f"{aid}.output"
    models, tool_calls, texts_pre_final, leaked, compaction = {}, [], 0, 0, 0
    final_text = None
    events = []
    for ln in p.read_text(errors="replace").splitlines():
        try:
            events.append(json.loads(ln))
        except Exception:
            pass
    # last assistant text block = final report
    assist_texts = []
    for e in events:
        msg = e.get("message") or {}
        m = msg.get("model")
        if m:
            models[m] = models.get(m, 0) + 1
        if isinstance(msg.get("content"), list):
            for blk in msg["content"]:
                if blk.get("type") == "tool_use":
                    inp = blk.get("input") or {}
                    tool_calls.append((blk.get("name"), inp.get("file_path", ""), inp.get("offset")))
                elif blk.get("type") in ("text", "thinking") and msg.get("role") == "assistant":
                    t = blk.get("text") or blk.get("thinking") or ""
                    if t.strip():
                        assist_texts.append((blk["type"], t))
        if '"compact' in json.dumps(e)[:300].lower():
            compaction += 1
    final_text = assist_texts[-1][1] if assist_texts else ""
    # pre-final text/thinking blocks: count + value leakage
    pre = assist_texts[:-1] if assist_texts else []
    pre_text_blocks = sum(1 for typ, t in pre if typ == "text")
    leaked = sum(1 for typ, t in pre for v in ALL_VALUES if v in t)
    # parse final JSON
    jmatch = re.search(r"\{.*\}", final_text, re.S)
    result = json.loads(jmatch.group(0)) if jmatch else {}
    reads = [(c[1].split("/")[-1], c[2]) for c in tool_calls if c[0] == "Read"]
    other = sorted({c[0] for c in tool_calls} - {"Read"})
    offsets = [r[1] for r in reads]
    seq_ok = all(offsets[i] == (offsets[i - 1] or 1) + 300 for i in range(1, len(offsets)))
    files = sorted({r[0] for r in reads})
    if rung:
        facts = KEY[rung]["facts"]
        rep = [norm(e.get("value")) for e in result.get("entries", [])]
        hits = sum(1 for f in facts if norm(f["value"]) in rep)
        markers = (norm(result.get("begin_marker")) == norm(KEY[rung]["begin_marker"]) and norm(result.get("end_marker")) == norm(KEY[rung]["end_marker"]))
        extra = len(rep) - hits
        print(f"{label:9s} model={models} hits={hits}/10 extra={extra} markers_ok={markers} reads={len(reads)} files={files} seq+300={seq_ok} other_tools={other} pre_final_text_blocks={pre_text_blocks} values_leaked_pre_final={leaked} compaction={compaction}")
    else:
        vals = {norm(f["value"]) for f in KEY["R40"]["facts"]}
        ans = result.get("answers", [])
        hits = sum(1 for a in ans if norm(a.get("value")) in vals)
        unk = sum(1 for a in ans if norm(a.get("value")) == "unknown")
        print(f"{label:9s} model={models} hits={hits}/10 unknowns={unk}/{len(ans)} tools={len(tool_calls)} compaction={compaction}")
