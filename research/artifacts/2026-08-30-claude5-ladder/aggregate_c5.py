#!/usr/bin/env python3
"""Extended reporting over the ladder scores. The 2026-07-18 `aggregate_ladder.py` is left
untouched and still runs its own pre-registered analysis; this adds the three informative-set
views PREREG.md fixed in advance:

  A. session-relative, literal prereg threshold  (SAT in <= 2 of this run's baselines)
  B. session-relative, proportional robustness   (SAT in <= 1/3 of this run's baselines)
  C. frozen 2026-07-18 informative set (78 rules), for cross-date comparability

Adherence = SAT/(SAT+VIOL); NA excluded from denominators; ERR reported and excluded.
Usage: aggregate_c5.py [--run DIR] [--gated-only]
"""
import argparse
import json
from pathlib import Path


def adherence(res, ids):
    sat = sum(1 for i in ids if res.get(i) == "SAT")
    viol = [i for i in ids if res.get(i) == "VIOL"]
    err = [i for i in ids if str(res.get(i, "")).startswith("ERR")]
    den = sat + len(viol)
    return sat, viol, err, (sat / den if den else None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", default=None)
    ap.add_argument("--gated-only", action="store_true",
                    help="restrict to arms whose gate verdict is PASS")
    ap.add_argument("--adjudicated", action="store_true",
                    help="use _score_adjudicated.json (prose-faithful amendments) instead of strict")
    a = ap.parse_args()
    here = Path(a.run) if a.run else Path(__file__).parent

    key = json.load(open(here / "guides" / "ladder_key.json"))
    fname = "_score_adjudicated.json" if a.adjudicated else "_score.json"
    scores = {d.name: json.load(open(d / fname))
              for d in sorted((here / "out").iterdir()) if (d / fname).exists()}
    print(f"scoring source: {fname}\n")

    gate = {}
    gp = here / "gate_results.json"
    if gp.exists():
        gate = json.load(open(gp))
    if a.gated_only and gate:
        scores = {k: v for k, v in scores.items() if gate.get(k, {}).get("GATE") == "PASS"}

    baselines = {k: v for k, v in scores.items() if "-base-" in k}
    treats = {k: v for k, v in scores.items() if "-K" in k}
    if not baselines:
        print("WARNING: no baseline arms scored — session-relative views unavailable")

    base_sat = {rid: sum(1 for v in baselines.values() if v.get(rid) == "SAT")
                for rid in key["rules"]}
    nb = len(baselines)
    setA = {r for r, n in base_sat.items() if n <= 2}
    setB = {r for r, n in base_sat.items() if n <= nb / 3.0} if nb else set()
    setC = set(json.load(open(here / "informative_2026-07-18.json")))
    core25 = set(key["core25"])

    # positive-control health: how many rules does an unguided run actually violate?
    print(f"baseline arms: {nb}")
    for k, v in sorted(baselines.items()):
        viol = sum(1 for x in v.values() if x == "VIOL")
        print(f"  {k:22} violates {viol} of {len(v)} rules")
    print(f"\ninformative sets:  A(<=2/{nb})={len(setA)}   "
          f"B(<={nb/3.0:.1f}/{nb})={len(setB)}   C(frozen 2026-07-18)={len(setC)}")
    print(f"core25 informative: A={len(core25 & setA)} B={len(core25 & setB)} C={len(core25 & setC)}\n")

    hdr = f"{'arm':22} {'gate':5} {'raw':>7} {'infA':>7} {'infB':>7} {'infC':>7}  violations"
    print(hdr)
    print("-" * len(hdr))
    rows = []
    for label in sorted(treats, key=lambda s: (s.split("-")[0], int(s.split("-K")[1].split("-")[0]), s)):
        k = label.split("-K")[1].split("-")[0]
        ids = key["rungs"][k]["ids"]
        res = treats[label]
        g = gate.get(label, {}).get("GATE", "?")
        out = {"arm": label, "model": label.split("-")[0], "K": int(k), "gate": g}
        cells = []
        for name, s in (("raw", None), ("infA", setA), ("infB", setB), ("infC", setC)):
            sel = ids if s is None else [i for i in ids if i in s]
            sat, viol, err, adh = adherence(res, sel)
            out[name] = round(adh, 4) if adh is not None else None
            out[name + "_viol"] = viol
            out[name + "_err"] = err
            cells.append(f"{adh:.4f}" if adh is not None else "  n/a ")
        allviol = sorted(set(out["raw_viol"]))
        out["violated_rules"] = allviol
        rows.append(out)
        print(f"{label:22} {g:5} " + " ".join(f"{c:>7}" for c in cells) + f"  {allviol if allviol else ''}")

    json.dump({"informative": {"A": sorted(setA), "B": sorted(setB), "C": sorted(setC)},
               "baseline_violation_counts": {k: sum(1 for x in v.values() if x == "VIOL")
                                             for k, v in baselines.items()},
               "rows": rows},
              open(here / ("aggregate_results_adjudicated.json" if a.adjudicated else "aggregate_results.json"), "w"), indent=1)

    print("\nper-model / per-rung mean adherence (informative set A):")
    bym = {}
    for r in rows:
        if a.gated_only and r["gate"] != "PASS":
            continue
        bym.setdefault(r["model"], {}).setdefault(r["K"], []).append(r["infA"])
    for m in sorted(bym):
        cells = []
        for K in (25, 50, 100, 200):
            vals = [v for v in bym[m].get(K, []) if v is not None]
            cells.append(f"K{K}: " + (", ".join(f"{v:.3f}" for v in vals) if vals else "-"))
        print(f"  {m:9} " + " | ".join(cells))


if __name__ == "__main__":
    main()
