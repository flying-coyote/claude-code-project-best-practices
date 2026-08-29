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

import re
import subprocess
import sys
import tempfile
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

    # 8. The CI gate's own parser, against real instrument output.
    #
    # This suite had ZERO coverage of how link-checker.yml reads this
    # instrument, and that gap hid a real defect for a day: the gate used
    # `awk '/^dangling/{print $2}'`, while the instrument prints a SECOND line
    # starting with "dangling" -- the detail header -- but only when the live
    # lane actually has a broken link. So the gate parsed correctly in the
    # healthy case and broke in the one case it exists for, reporting the
    # INSTRUMENT as unparseable while the instrument was fine and the CORPUS
    # was broken.
    #
    # The awk is extracted from the workflow rather than copied, so this test
    # guards the shipped command. A copy would have passed while the real gate
    # stayed broken -- the same class of mistake one level up.
    wf = (ROOT / ".github" / "workflows" / "link-checker.yml").read_text()
    m = re.search(r"DANGLING=\$\(awk ('[^']*') /tmp/links\.txt\)", wf)
    ok &= check("the gate's awk is extractable from the workflow", bool(m))

    if m:
        awk_prog = m.group(1)[1:-1]

        def gate_count(instrument_output):
            """Run the workflow's awk over instrument output, then its guard."""
            got = subprocess.run(["awk", awk_prog], input=instrument_output,
                                 capture_output=True, text=True).stdout.strip()
            return got

        # 8a. Healthy corpus: one `dangling` row, no detail header.
        clean = run(["--links"])
        got = gate_count(clean)
        ok &= check("gate parses a clean corpus to a bare integer",
                    re.fullmatch(r"[0-9]+", got) is not None, f"got {got!r}")
        ok &= check("gate reads 0 on a corpus with no dangling live links",
                    got == "0", f"got {got!r}")

        # 8b. Broken corpus: the detail header is present. Built as a fixture
        #     rather than by copying the repo, so it stays fast and hermetic.
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / ".claude").mkdir()
            (root / ".claude" / "CLAUDE.md").write_text("# seed\n\n[a](../a.md)\n")
            (root / "a.md").write_text("# a\n\n[gone](nowhere-at-all.md)\n")
            broken = subprocess.run(
                [sys.executable, str(SCRIPT), "--root", str(root), "--links"],
                capture_output=True, text=True, check=True).stdout

            header_lines = [ln for ln in broken.splitlines()
                            if ln.startswith("dangling")]
            ok &= check("a broken corpus really does print two 'dangling' lines",
                        len(header_lines) == 2, f"{len(header_lines)} line(s)")

            got = gate_count(broken)
            ok &= check("gate parses a BROKEN corpus to a bare integer "
                        "(the defect: used to yield '1\\nin')",
                        re.fullmatch(r"[0-9]+", got) is not None, f"got {got!r}")
            ok &= check("gate reports a non-zero count so the PR-failing step fires",
                        got not in ("", "0"), f"got {got!r}")

    print("\nAll tests passed." if ok else "\nFAILURES above.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
