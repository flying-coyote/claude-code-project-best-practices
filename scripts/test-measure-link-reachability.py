#!/usr/bin/env python3
"""Regression tests for measure-link-reachability.py.

The first of these exists because the instrument was NOT deterministic when it
shipped: `_resolve` iterated a two-element *set* of candidate paths, so when a
reference resolved both relative-to-source and relative-to-repo-root, which one
the BFS followed depended on PYTHONHASHSEED. The reported figure varied 168-171
between runs on an unchanged tree, which quietly falsified the doc's own
"reproducible from a clean checkout" claim. A single run cannot catch that;
only running under several hash seeds can.

Usage:  python3 scripts/test-measure-link-reachability.py
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "measure-link-reachability.py"
SEEDS = ["0", "1", "2", "3", "7", "42", "99", "12345"]


def run(args, seed=None):
    env = {"PATH": "/usr/bin:/bin", "PYTHONHASHSEED": seed} if seed else None
    out = subprocess.run([sys.executable, str(SCRIPT), *args],
                         capture_output=True, text=True, cwd=ROOT, env=env, check=True)
    return out.stdout


def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'}  {name}{'  ' + detail if detail else ''}")
    return ok


def main():
    ok = True

    # 1. Determinism under hash randomisation -- the regression this file exists for.
    for args in (["--include-archive"], [], ["--currency"]):
        outs = {run(args, seed) for seed in SEEDS}
        ok &= check(f"deterministic across {len(SEEDS)} hash seeds: {args or ['(live)']}",
                    len(outs) == 1,
                    "" if len(outs) == 1 else f"got {len(outs)} distinct outputs")

    # 2. Determinism across repeat runs in one process-per-run loop.
    outs = {run(["--include-archive"]) for _ in range(5)}
    ok &= check("stable across 5 consecutive runs", len(outs) == 1)

    # 3. Monotonicity: each mode counts at least as much as the previous.
    txt = run(["--include-archive", "--entry", "E1"])
    vals = {ln.split()[0].split("/")[1]: int(ln.split()[1])
            for ln in txt.splitlines()
            if ln.startswith("E1/") and not ln.startswith("E1/refs:")
            and ":" not in ln.split()[0]}
    ok &= check("modes are cumulative (links <= refs <= dirs)",
                vals["links"] <= vals["refs"] <= vals["dirs"], str(vals))

    # 4. Monotonicity across entry tiers at a fixed mode.
    tiers = {t: int([ln for ln in run(["--include-archive", "--mode", "refs", "--entry", t])
                     .splitlines()
                     if ln.startswith(t + "/") and ":" not in ln.split()[0]][0].split()[1])
             for t in ("E1", "E2", "E3")}
    ok &= check("entry tiers are cumulative (E1 <= E2 <= E3)",
                tiers["E1"] <= tiers["E2"] <= tiers["E3"], str(tiers))

    # 5. Currency buckets partition the lane exactly.
    line = [ln for ln in run(["--currency"]).splitlines() if ln.startswith("archive/")][0]
    n = int(line.split("n=")[1].split()[0])
    got = sum(int(line.split(f"{k}=")[1].split()[0].split("(")[0])
              for k in ("correct", "WRONG", "absent"))
    ok &= check("currency buckets sum to the lane size", got == n, f"{got} vs n={n}")

    # 6. The gameability disclosure must be present -- the headline percentage
    #    is not publishable without it.
    txt = run(["--include-archive", "--entry", "E1", "--mode", "refs"])
    ok &= check("reports the generated-inventory-excluded figure",
                "excluding generated inventory" in txt)
    ok &= check("reports hazard exposure separately from the numerator",
                "hazard exposure" in txt)
    # 7. The lane decomposition. A corpus-wide percentage lumps prose that owes
    #    the reader a pointer together with config the runtime loads by its own
    #    rules; reporting it undecomposed produced a headline that was wrong by
    #    a factor of two in the direction of alarm.
    ok &= check("reports the by-lane decomposition", "by lane, index excluded" in txt)
    ok &= check("names the guidance lane explicitly", "guidance" in txt)

    print("\nAll tests passed." if ok else "\nFAILURES above.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
