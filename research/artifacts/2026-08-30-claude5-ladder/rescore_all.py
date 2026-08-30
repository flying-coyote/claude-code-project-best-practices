#!/usr/bin/env python3
"""Score every complete arm under BOTH checkers and write _score.json (strict) and
_score_adjudicated.json. Reporting both is the point: the adjudicated reading is never
published in place of the strict one.

Usage: rescore_all.py [--run DIR]
"""
import argparse
import importlib.util
import json
import sys
from pathlib import Path

DELIVERABLES = ("lumen.py", "README.md", "CHANGELOG.md")


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", default=None)
    a = ap.parse_args()
    here = Path(a.run) if a.run else Path(__file__).parent

    strict = load("s_strict", here / "score_ladder.py")
    adj = load("s_adj", here / "score_ladder_adjudicated.py")

    done = skipped = 0
    for d in sorted((here / "out").iterdir()):
        if not d.is_dir():
            continue
        if any(not (d / f).exists() for f in DELIVERABLES):
            skipped += 1
            continue
        rung = "ALL" if "-base-" in d.name else d.name.split("-K")[1].split("-")[0]
        json.dump(strict.score(str(d), rung), open(d / "_score.json", "w"), indent=1)
        json.dump(adj.score(str(d), rung), open(d / "_score_adjudicated.json", "w"), indent=1)
        done += 1
    print(f"scored {done} arms under both checkers; {skipped} incomplete/skipped")


if __name__ == "__main__":
    main()
