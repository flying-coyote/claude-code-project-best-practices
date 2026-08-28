#!/usr/bin/env python3
"""Measure how much of a markdown corpus is reachable by following explicit
pointers from the entry points a Claude Code session actually loads.

Why this exists
---------------
Discovery advice for coding projects assumes the unloaded remainder is
*derivable*: "let Claude fetch what it needs", "anything Claude can figure out
by reading code". For code that holds, because grep on an identifier finds every
use. For a prose corpus it does not, because the discriminating property of a
prose file is authority and currency, and grep cannot see either: a superseded
document stays well-formed and matches a query exactly as confidently as the
document that superseded it. So for prose the pointer graph -- not the grep --
is the discovery mechanism, and its coverage is a measurable property.

This script measures that coverage. It is deliberately generous to the corpus:
every mode counts more than the previous one, so the reported reachability is an
upper bound on what an agent would actually follow, never an understatement.

Two measurements, not one
--------------------------
Reachability answers "can a session get here?". Currency answers "once it does,
does the file say whether to believe it?". They fail independently, so a single
"discoverability score" would hide the interesting case. Report both.

Currency is a THREE-way classification, not marked/unmarked -- because the worst
case is not a missing marker but a wrong one. A file in a dead lane whose own
frontmatter says `status: PRODUCTION` defeats the very check a careful reader
runs, so it is counted separately from a file that says nothing.

  correct  declares itself superseded (dead status: value, or a banner)
  WRONG    asserts a LIVE status while sitting in a dead lane
  absent   says nothing either way

Modes (cumulative)
------------------
  links      markdown links [t](p) and @imports only.
  refs       + backticked and bare paths that resolve to a real file.
  dirs       + directory mentions expand to the .md files directly inside them
             (an agent told about `analysis/` can ls it).

Entry-point tiers (cumulative)
------------------------------
  E1 auto    .claude/CLAUDE.md (+ CLAUDE.md, AGENTS.md at root if present):
             loaded unconditionally in every session.
  E2 config  + .claude/rules/, .claude/skills/, .claude/commands/, .claude/agents/:
             surfaced to the session as metadata or on trigger.
  E3 front   + README.md: the human front door, not session-loaded.

Usage
-----
  python3 scripts/measure-link-reachability.py                 # summary table
  python3 scripts/measure-link-reachability.py --mode refs --entry E1 --list-unreachable
  python3 scripts/measure-link-reachability.py --json
  python3 scripts/measure-link-reachability.py --currency archive old deprecated
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections import deque
from pathlib import Path

# Directories excluded from the measured corpus. archive/ is excluded by default
# because it is explicitly a tombstone store, not live advice; --include-archive
# puts it back.
DEFAULT_EXCLUDES = {".git", "node_modules", ".graphify-venv", "graphify-out",
                    ".understand-anything", ".venv"}

MD_LINK = re.compile(r"\[[^\]]*\]\(\s*<?([^)>\s]+)")
AT_IMPORT = re.compile(r"(?:^|\s)@([A-Za-z0-9_./-]+\.md)\b")
BACKTICK = re.compile(r"`([^`\n]+)`")
# A bare path mentioned in prose: at least one slash or a .md suffix.
BARE_PATH = re.compile(r"(?<![\w`/([])((?:[A-Za-z0-9_.-]+/)*[A-Za-z0-9_.-]+\.md)\b")
BARE_DIR = re.compile(r"(?<![\w`/([])((?:[A-Za-z0-9_.-]+/)+)")

ENTRY_TIERS = {
    "E1": ["auto"],
    "E2": ["auto", "config"],
    "E3": ["auto", "config", "front"],
}
MODES = ["links", "refs", "dirs"]


def repo_markdown(root: Path, include_archive: bool) -> set[str]:
    """Every markdown file in the corpus, as posix paths relative to root."""
    try:
        tracked = subprocess.run(
            ["git", "-C", str(root), "ls-files", "*.md", "**/*.md"],
            capture_output=True, text=True, check=True).stdout.split()
        files = {p for p in tracked if p.endswith(".md")}
    except (subprocess.CalledProcessError, FileNotFoundError):
        files = {
            str(p.relative_to(root)) for p in root.rglob("*.md")
            if not any(part in DEFAULT_EXCLUDES for part in p.relative_to(root).parts)
        }
    files = {f for f in files if not any(part in DEFAULT_EXCLUDES for part in Path(f).parts)}
    if not include_archive:
        files = {f for f in files if not f.startswith("archive/")}
    return files


def entry_points(root: Path, corpus: set[str], kinds: list[str]) -> set[str]:
    found: set[str] = set()
    if "auto" in kinds:
        for cand in (".claude/CLAUDE.md", "CLAUDE.md", "AGENTS.md"):
            if cand in corpus:
                found.add(cand)
    if "config" in kinds:
        for f in corpus:
            if f.startswith(".claude/") and f not in {".claude/CLAUDE.md"}:
                found.add(f)
    if "front" in kinds:
        if "README.md" in corpus:
            found.add("README.md")
    return found


def _normalise(raw: str) -> str | None:
    raw = raw.strip().strip("<>").split("#", 1)[0].split("?", 1)[0].strip()
    if not raw or raw.startswith(("http://", "https://", "mailto:", "file://", "#")):
        return None
    return raw


def _resolve(src: str, target: str, corpus: set[str], dirs: set[str]) -> tuple[set[str], bool]:
    """Resolve one reference. Returns (md files hit, whether it named a directory)."""
    base = Path(src).parent
    for cand in ({os.path.normpath(base / target), os.path.normpath(target)}
                 if not target.startswith("/") else {target.lstrip("/")}):
        cand = cand.replace(os.sep, "/")
        if cand in corpus:
            return {cand}, False
        if cand.rstrip("/") in dirs:
            return set(), True
    return set(), False


def outgoing(src: str, root: Path, corpus: set[str], dirs: set[str], mode: str
             ) -> tuple[set[str], set[str]]:
    """(md files pointed at, directories pointed at) from one source file."""
    try:
        text = (root / src).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return set(), set()

    raw: list[str] = [m for m in MD_LINK.findall(text)] + list(AT_IMPORT.findall(text))
    if mode in ("refs", "dirs"):
        raw += list(BACKTICK.findall(text))
        raw += list(BARE_PATH.findall(text))
        raw += list(BARE_DIR.findall(text))

    hit_files: set[str] = set()
    hit_dirs: set[str] = set()
    for r in raw:
        t = _normalise(r)
        if t is None:
            continue
        files, is_dir = _resolve(src, t, corpus, dirs)
        hit_files |= files
        if is_dir:
            d = os.path.normpath(os.path.join(Path(src).parent, t)).replace(os.sep, "/").rstrip("/")
            hit_dirs.add(d if d in dirs else t.rstrip("/"))
    return hit_files, hit_dirs


def reachable(root: Path, corpus: set[str], entries: set[str], mode: str) -> set[str]:
    dirs = {str(Path(f).parent).replace(os.sep, "/") for f in corpus}
    dirs |= {"." }
    for f in corpus:                      # every ancestor directory counts
        p = Path(f).parent
        while str(p) not in (".", ""):
            dirs.add(str(p).replace(os.sep, "/"))
            p = p.parent

    seen = set(entries)
    queue = deque(entries)
    while queue:
        cur = queue.popleft()
        files, hit_dirs = outgoing(cur, root, corpus, dirs, mode)
        if mode == "dirs":
            for d in hit_dirs:
                prefix = "" if d in (".", "") else d + "/"
                files |= {f for f in corpus
                          if f.startswith(prefix) and "/" not in f[len(prefix):]}
        for f in files:
            if f not in seen:
                seen.add(f)
                queue.append(f)
    return seen & corpus


LIVE_STATUS = {"PRODUCTION", "EMERGING", "REFERENCE", "STABLE", "ACTIVE", "CURRENT"}
DEAD_STATUS = {"ARCHIVED", "RETIRED", "RETIRING", "DEPRECATED", "SUPERSEDED"}
BANNER = re.compile(
    r"(?i)\b(archived|superseded|retired|tombstone|do not use|no longer current"
    r"|historical (record|value|comparison)|merged into|replaced by"
    r"|evicted to archive|collapsed)\b")
STATUS_FIELD = re.compile(r"^status:\s*[\"']?([A-Za-z]+)", re.M)


def classify_currency(text: str) -> str:
    """correct | WRONG | absent -- see the module docstring.

    WRONG is the load-bearing bucket: a file in a dead lane asserting a live
    status is worse than an unmarked one, because it survives the check.
    """
    front = ""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end > 0:
            front = text[3:end]
    m = STATUS_FIELD.search(front)
    status = m.group(1).upper() if m else None
    if status in LIVE_STATUS:
        return "WRONG"
    if status in DEAD_STATUS or BANNER.search("\n".join(text.splitlines()[:40])):
        return "correct"
    return "absent"


def report_currency(root: Path, lanes: list[str]) -> int:
    """Classify every markdown file in each named dead lane."""
    any_lane = False
    worst: list[str] = []
    for lane in lanes:
        d = root / lane
        if not d.is_dir():
            continue
        any_lane = True
        files = sorted(d.rglob("*.md"))
        counts = {"correct": 0, "WRONG": 0, "absent": 0}
        for f in files:
            try:
                verdict = classify_currency(f.read_text(encoding="utf-8", errors="replace"))
            except OSError:
                continue
            counts[verdict] += 1
            if verdict == "WRONG":
                worst.append(str(f.relative_to(root)))
        n = len(files) or 1
        print(f"{lane}/  n={len(files)}   "
              f"correct={counts['correct']} ({100*counts['correct']//n}%)   "
              f"WRONG={counts['WRONG']}   absent={counts['absent']}")
    if not any_lane:
        print("no dead lane found among: " + ", ".join(lanes))
        return 0
    if worst:
        print("\nfiles asserting a LIVE status while in a dead lane "
              "(severe -- these defeat the reader's own check):")
        for f in worst:
            print(f"  {f}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".", help="repo root (default: cwd)")
    ap.add_argument("--mode", choices=MODES, help="report a single edge mode")
    ap.add_argument("--entry", choices=sorted(ENTRY_TIERS), help="report a single entry tier")
    ap.add_argument("--include-archive", action="store_true",
                    help="count archive/ as part of the live corpus")
    ap.add_argument("--list-unreachable", action="store_true",
                    help="print the unreachable files for the selected cell")
    ap.add_argument("--currency", nargs="*", metavar="LANE",
                    help="instead of reachability, classify currency markers in these dead "
                         "lanes (default: archive old deprecated legacy)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    root = Path(args.root).resolve()

    if args.currency is not None:
        return report_currency(root, args.currency or
                               ["archive", "old", "deprecated", "legacy"])

    corpus = repo_markdown(root, args.include_archive)
    if not corpus:
        print("no markdown found", file=sys.stderr)
        return 1

    tiers = [args.entry] if args.entry else sorted(ENTRY_TIERS)
    modes = [args.mode] if args.mode else MODES

    results = {}
    for tier in tiers:
        entries = entry_points(root, corpus, ENTRY_TIERS[tier])
        for mode in modes:
            reach = reachable(root, corpus, entries, mode)
            results[f"{tier}/{mode}"] = {
                "entry_points": sorted(entries),
                "corpus": len(corpus),
                "reachable": len(reach),
                "pct": round(100 * len(reach) / len(corpus), 1),
                "unreachable": sorted(corpus - reach),
            }

    if args.json:
        print(json.dumps(results, indent=2))
        return 0

    print(f"corpus: {len(corpus)} markdown files"
          f"{'' if args.include_archive else ' (archive/ excluded)'}\n")
    width = max(len(k) for k in results)
    print(f"{'entry/mode'.ljust(width)}  reachable  of corpus")
    for k, v in results.items():
        print(f"{k.ljust(width)}  {str(v['reachable']).rjust(9)}  {str(v['pct']).rjust(6)}%")

    if args.list_unreachable:
        for k, v in results.items():
            print(f"\n--- unreachable under {k} ({len(v['unreachable'])}) ---")
            for f in v["unreachable"]:
                print(f"  {f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
