#!/usr/bin/env python3
"""Aggregate ladder scores. Pre-registered analysis (fixed before any treatment
run was scored):
  - informative rule := satisfied in <= 2 of the 6 baseline runs (pooled models)
  - primary load-effect metric: adherence on the informative subset of CORE25,
    which every rung shares, per model across rung sizes
  - secondary: adherence on all informative rules of the rung; raw adherence
  - NA excluded from denominators; ERR reported separately, excluded
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
LKEY = json.load(open(HERE / "guides" / "ladder_key.json"))
OUT = HERE / "out"
BASE_THRESH = 2

scores = {}
for d in sorted(OUT.iterdir()):
    f = d / "_score.json"
    if f.exists():
        scores[d.name] = json.load(open(f))

baselines = {k: v for k, v in scores.items() if "-base-" in k}
treats = {k: v for k, v in scores.items() if "-K" in k}

base_sat = {}
for rid in LKEY["rules"]:
    base_sat[rid] = sum(1 for v in baselines.values() if v.get(rid) == "SAT")
informative = {rid for rid, n in base_sat.items() if n <= BASE_THRESH}
core25 = set(LKEY["core25"])
core_inf = core25 & informative

print(f"baseline runs: {len(baselines)}; informative rules (<= {BASE_THRESH} baseline SAT): "
      f"{len(informative)}/{len(base_sat)}; core25 informative: {len(core_inf)}/25")
print("core25 dropped as uninformative:", sorted(core25 - informative))


def adherence(res, ids):
    sat = sum(1 for i in ids if res.get(i) == "SAT")
    viol = [i for i in ids if res.get(i) == "VIOL"]
    err = [i for i in ids if str(res.get(i, "")).startswith("ERR")]
    den = sat + len(viol)
    return sat, viol, err, (sat / den if den else None)


rows = []
for label in sorted(treats):
    model = label.split("-")[0]
    k = label.split("-K")[1].split("-")[0]
    ids = LKEY["rungs"][k]["ids"]
    res = treats[label]
    sat_r, viol_r, err_r, adh_raw = adherence(res, ids)
    ids_inf = [i for i in ids if i in informative]
    sat_i, viol_i, err_i, adh_inf = adherence(res, ids_inf)
    idsc = [i for i in ids if i in core_inf]
    sat_c, viol_c, err_c, adh_core = adherence(res, idsc)
    rows.append({"label": label, "model": model, "K": int(k),
                 "raw": round(adh_raw, 4) if adh_raw is not None else None,
                 "informative": round(adh_inf, 4) if adh_inf is not None else None,
                 "n_inf": len(ids_inf) - len(err_i),
                 "core25_inf": round(adh_core, 4) if adh_core is not None else None,
                 "viol_informative": viol_i, "err": err_r})

for r in sorted(rows, key=lambda x: (x["model"], x["K"], x["label"])):
    print(f"{r['label']:16s} raw={r['raw']} inf={r['informative']} (n={r['n_inf']}) "
          f"core25={r['core25_inf']} viol_inf={r['viol_informative']} err={r['err']}")

# per-rule violation tally across treatments
tally = {}
for r in rows:
    for v in r["viol_informative"]:
        tally.setdefault(v, []).append(r["label"])
if tally:
    print("\ninformative-rule violations by rule:")
    for rid, who in sorted(tally.items(), key=lambda x: -len(x[1])):
        print(f"  {rid}: {len(who)} ({', '.join(who)})")

# baseline detail: what informative rules look like at baseline (sanity)
if "--base-detail" in sys.argv:
    for label, res in sorted(baselines.items()):
        sat, viol, err, adh = adherence(res, list(informative))
        print(f"baseline {label}: informative-rule spontaneous adherence {adh} ({sat} SAT)")

json.dump({"base_sat": base_sat, "informative": sorted(informative),
           "core25_informative": sorted(core_inf), "rows": rows},
          open(HERE / "aggregate_results.json", "w"), indent=1)
