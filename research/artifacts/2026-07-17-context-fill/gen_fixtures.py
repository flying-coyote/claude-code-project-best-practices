#!/usr/bin/env python3
"""Context-fill probe fixture generator (Gap 317 instrument, 2026-07-17 re-run).

Fix applied per research/fable-probe-session-2026-07-16.md: filler is
human-authored repo prose (analysis/ + archive/ + root docs), NOT machine-
generated deterministic filler, which tripped a harness safety classifier.

Fixtures: CAL ~5k tokens (positive control), R40 ~40k, R100 ~100k, R140 ~140k.
10 registry facts per fixture at 5%..95% char depth; BEGIN/END marker tokens.
Seeded (317) for reproducibility. Emits answer_key.json.
"""
import json
import random
import re
from pathlib import Path

REPO = Path("/home/jerem/claude-code-project-best-practices")
OUT = Path("/tmp/claude-1000/-home-jerem-claude-code-project-best-practices/0ae1ac5a-4390-4786-8ee1-c5025f5a0325/scratchpad/fixtures")
OUT.mkdir(parents=True, exist_ok=True)

rng = random.Random(317)

# --- collect filler prose ---
files = sorted(
    p for p in REPO.rglob("*.md")
    if "node_modules" not in p.parts and ".git" not in p.parts
)
rng.shuffle(files)
corpus_parts = []
for p in files:
    try:
        corpus_parts.append(p.read_text(encoding="utf-8", errors="replace"))
    except Exception:
        pass
corpus = "\n\n".join(corpus_parts)

# wrap to <=200-char lines so Read never line-truncates and token/line is stable
def wrap(text, width=200):
    out = []
    for raw in text.splitlines():
        line = raw.rstrip()
        while len(line) > width:
            cut = line.rfind(" ", 0, width)
            if cut <= 0:
                cut = width
            out.append(line[:cut])
            line = line[cut:].lstrip()
        out.append(line)
    return out

lines = wrap(corpus)
# drop blank-run excess to keep density predictable
dense = []
blank = 0
for ln in lines:
    if ln.strip() == "":
        blank += 1
        if blank > 1:
            continue
    else:
        blank = 0
    dense.append(ln)
lines = dense
total_chars = sum(len(l) + 1 for l in lines)
print(f"filler pool: {len(files)} files, {len(lines)} lines, {total_chars} chars (~{total_chars//4} tokens)")

ALPHA = "abcdefghjkmnpqrstuvwxyz23456789"  # no lookalikes

def token(n=12):
    s = "".join(rng.choice(ALPHA) for _ in range(n))
    return f"{s[:4]}-{s[4:8]}-{s[8:]}"

def build(name, target_chars, n_facts=10):
    # take a contiguous slice of the pool, rotated per fixture so content differs
    start = rng.randrange(len(lines))
    body = []
    chars = 0
    i = start
    while chars < target_chars:
        ln = lines[i % len(lines)]
        body.append(ln)
        chars += len(ln) + 1
        i += 1
    begin_tok = token()
    end_tok = token()
    facts = []
    # depth targets 5%..95% by line index (chars are ~uniform per line after wrap)
    for k in range(n_facts):
        depth = 0.05 + 0.10 * k
        key = f"{name}-{rng.randrange(100,999)}"
        val = token()
        facts.append({"key": key, "value": val, "depth": round(depth, 2)})
    # insert from deepest first so earlier indices stay valid
    for f in sorted(facts, key=lambda x: -x["depth"]):
        idx = int(f["depth"] * len(body))
        body.insert(idx, f"Registry note (probe fixture): the value for registry key {f['key']} is `{f['value']}`.")
    body.insert(0, f"BEGIN-OF-FIXTURE MARKER `{begin_tok}` — this file is a reading-comprehension fixture assembled from this repository's own documentation for an internal context-retention measurement. Read every line in order.")
    body.append(f"END-OF-FIXTURE MARKER `{end_tok}` — you have reached the end of the fixture.")
    path = OUT / f"{name}.txt"
    text = "\n".join(body) + "\n"
    path.write_text(text, encoding="utf-8")
    # recompute actual line numbers of facts for the record
    for f in facts:
        pat = re.compile(re.escape(f"registry key {f['key']} is"))
        for lineno, ln in enumerate(text.splitlines(), 1):
            if pat.search(ln):
                f["line"] = lineno
                break
    return {
        "name": name, "path": str(path), "chars": len(text),
        "lines": text.count("\n"), "est_tokens": len(text) // 4,
        "begin_marker": begin_tok, "end_marker": end_tok, "facts": facts,
    }

key = {
    "CAL": build("CAL", 20_000),
    "R40": build("R40", 160_000),
    "R100": build("R100", 400_000),
    "R140": build("R140", 560_000),
}
(OUT / "answer_key.json").write_text(json.dumps(key, indent=2))
for k, v in key.items():
    print(f"{k}: {v['chars']} chars, {v['lines']} lines, ~{v['est_tokens']} tokens, facts at lines {[f['line'] for f in v['facts']]}")
