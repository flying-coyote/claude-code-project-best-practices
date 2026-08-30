#!/usr/bin/env python3
"""Per-model tokenizer re-baselining from harness transcripts.

No tokenizer library or count_tokens endpoint is reachable from this session, so token
counts are recovered from the harness's own accounting: on each assistant turn,
`usage.cache_creation_input_tokens` is the number of NEW input tokens appended since the
previous turn — i.e. the previous assistant message plus the tool result it produced.
Reading a fixed file as the only action of a turn therefore prices that file, plus a small
per-turn assistant overhead.

Two estimators are reported because they trade off differently:
  large-only     the raw delta for the 48 KB fixture. Overhead is <3% of the total.
  paired (L-S)   delta(large) - delta(small) for the same corpus, which cancels a constant
                 per-turn overhead but is noisier when a model's thinking length varies
                 between the two turns.

The cross-generation comparison uses Haiku 4.5 as the only 4.x-generation model this
harness can serve. Anthropic's published figure is Sonnet 5 vs Sonnet 4.6 specifically, so
Haiku 4.5 is a PROXY for the 4.x tokenizer, not the same comparison.

Usage: tok_measure.py --tasks DIR
"""
import argparse
import json
import statistics
from pathlib import Path

# label -> transcript id. Two independent replications per model.
PROBES = {
    "opus5-rep1": "a8b63c1b7b631dec1", "opus5-rep2": "a601cda97e09bcec6",
    "sonnet5-rep1": "ae09dff3ec22d06e3", "sonnet5-rep2": "ae532422d370ece4d",
    "fable5-rep1": "ae7859f2252c88b45", "fable5-rep2": "a5d7f6b6b6ba47fa5",
    "haiku45-rep1": "a2b67a3e65a32f7ef", "haiku45-rep2": "a51f20c13c33b37a8",
}
FIXTURES = ["EN-small.txt", "EN-large.txt", "PY-small.txt", "PY-large.txt"]
BYTES = {"EN-small.txt": 8000, "EN-large.txt": 48000,
         "PY-small.txt": 8000, "PY-large.txt": 48000}


def deltas(path):
    """Return {fixture: new-input-tokens attributable to reading it} plus served models."""
    turns = []
    for ln in Path(path).read_text(errors="replace").splitlines():
        try:
            e = json.loads(ln)
        except Exception:
            continue
        msg = e.get("message") or {}
        if msg.get("role") != "assistant":
            continue
        u = msg.get("usage") or {}
        reads = []
        if isinstance(msg.get("content"), list):
            for b in msg["content"]:
                if b.get("type") == "tool_use" and b.get("name") == "Read":
                    reads.append((b.get("input") or {}).get("file_path", "").split("/")[-1])
        turns.append({"model": msg.get("model"),
                      "cw": u.get("cache_creation_input_tokens") or 0,
                      "reads": reads})

    models = {}
    for t in turns:
        if t["model"]:
            models[t["model"]] = models.get(t["model"], 0) + 1

    # The cost of a Read lands in the cache_creation of the NEXT distinct turn. Turns can
    # be duplicated in the transcript (same usage repeated), so walk distinct steps.
    out, pending = {}, None
    seen = set()
    for t in turns:
        sig = (t["cw"], tuple(t["reads"]))
        if sig in seen and not t["reads"]:
            continue
        seen.add(sig)
        if pending is not None and t["cw"]:
            out.setdefault(pending, t["cw"])
            pending = None
        if len(t["reads"]) == 1 and t["reads"][0] in BYTES:
            pending = t["reads"][0]
        elif len(t["reads"]) > 1:
            out["_BATCHED_"] = True
    return out, models


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tasks", required=True)
    a = ap.parse_args()
    tasks = Path(a.tasks)

    per = {}
    print(f"{'probe':16} {'served model':28} " + " ".join(f"{f.split('.')[0]:>10}" for f in FIXTURES))
    for label, aid in PROBES.items():
        p = tasks / f"{aid}.output"
        if not p.exists():
            print(f"{label:16} MISSING TRANSCRIPT")
            continue
        d, models = deltas(p)
        if d.get("_BATCHED_"):
            print(f"{label:16} EXCLUDED — batched Reads in one turn")
            continue
        if len(models) != 1:
            print(f"{label:16} EXCLUDED — mixed served models {models}")
            continue
        served = next(iter(models))
        per[label] = {"served": served, **{f: d.get(f) for f in FIXTURES}}
        print(f"{label:16} {served:28} " + " ".join(f"{str(d.get(f)):>10}" for f in FIXTURES))

    fam = {}
    for label, v in per.items():
        fam.setdefault(label.split("-")[0], []).append(v)

    print(f"\n{'model':10} {'EN large-only':>14} {'EN paired':>11} {'PY large-only':>14} {'PY paired':>11}")
    est = {}
    for m, rows in fam.items():
        def mean(fn):
            vals = [fn(r) for r in rows if all(r[f] is not None for f in FIXTURES)]
            return statistics.mean(vals) if vals else None
        e = {
            "EN_large": mean(lambda r: r["EN-large.txt"]),
            "EN_paired": mean(lambda r: r["EN-large.txt"] - r["EN-small.txt"]),
            "PY_large": mean(lambda r: r["PY-large.txt"]),
            "PY_paired": mean(lambda r: r["PY-large.txt"] - r["PY-small.txt"]),
            "served": rows[0]["served"], "n": len(rows),
        }
        est[m] = e
        print(f"{m:10} {e['EN_large']:>14.0f} {e['EN_paired']:>11.0f} "
              f"{e['PY_large']:>14.0f} {e['PY_paired']:>11.0f}")

    if "haiku45" in est:
        h = est["haiku45"]
        print("\nratio vs Haiku 4.5 (4.x-generation proxy for the pre-Claude-5 tokenizer):")
        print(f"{'model':10} {'EN large-only':>14} {'EN paired':>11} {'PY large-only':>14} {'PY paired':>11}")
        for m, e in est.items():
            if m == "haiku45":
                continue
            print(f"{m:10} {e['EN_large']/h['EN_large']:>14.3f} {e['EN_paired']/h['EN_paired']:>11.3f} "
                  f"{e['PY_large']/h['PY_large']:>14.3f} {e['PY_paired']/h['PY_paired']:>11.3f}")

        c5 = [m for m in est if m != "haiku45"]
        print("\nwithin-Claude-5 agreement (max spread as % of mean):")
        for field in ("EN_large", "PY_large"):
            vals = [est[m][field] for m in c5]
            print(f"  {field:10} {(max(vals)-min(vals))/statistics.mean(vals)*100:.2f}%  "
                  f"({', '.join(f'{m}={est[m][field]:.0f}' for m in c5)})")

    json.dump({"per_probe": per, "estimates": est, "fixture_bytes": BYTES},
              open(Path(__file__).parent / "tokenizer_results.json", "w"), indent=1)


if __name__ == "__main__":
    main()
