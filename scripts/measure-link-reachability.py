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

# Directories excluded from the measured corpus.
#
# archive/ is excluded by default as a convenience, NOT on the theory that it is
# a tombstone store. In the repository this was built against that theory turned
# out to be false: nine live docs link into archive/ across ~130 links, and one
# cites an archived doc as "the foundational methodology". Treat the default as
# "the lane you are probably not asking about", and pass --include-archive
# whenever the question is about the whole corpus. A lane excluded from the
# currency checks accumulates unverifiable claims whether or not it is dead.
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
        # Only surfaces the harness itself presents: rule files (path-triggered),
        # skill/agent/command DEFINITIONS (descriptions always in context). NOT
        # second-level progressive-disclosure bodies -- a skill's workflows/ or
        # references/ leaf is reached only if the skill body reads it, so
        # seeding it would be the single-loading-surface error this instrument
        # exists to reject, inverted.
        for f in corpus:
            if not f.startswith(".claude/") or f == ".claude/CLAUDE.md":
                continue
            parts = f.split("/")
            if parts[1] == "rules":
                found.add(f)
            elif parts[1] in ("skills", "agents", "commands") and (
                    parts[-1] in ("SKILL.md", "AGENT.md") or len(parts) == 3):
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
    # An ORDERED list, never a set. A set literal here made the whole instrument
    # nondeterministic: when a reference resolves both relative-to-source and
    # relative-to-repo-root, set iteration order depends on PYTHONHASHSEED, so
    # which target the BFS followed changed between runs on an unchanged tree
    # (observed spread: 168-171 reachable). Relative-to-source is correct
    # markdown semantics and is tried first; repo-root is the fallback that
    # rescues generated footers written with root-relative paths.
    if target.startswith("/"):
        candidates = [target.lstrip("/")]
    else:
        candidates = [os.path.normpath(base / target), os.path.normpath(target)]
    for cand in candidates:
        cand = cand.replace(os.sep, "/")
        if cand in corpus:
            return {cand}, False
        if cand.rstrip("/") in dirs:
            return set(), True
    return set(), False


FENCE = re.compile(r"^```.*?^```", re.M | re.S)
INLINE_CODE = re.compile(r"`[^`\n]*`")
PLACEHOLDER = re.compile(r"\{|XXX|YYY|ZZZ|path/to/|^doc-name\.md$|^file\.md$")


def strip_fences(text: str) -> str:
    """Remove fenced blocks only, keeping inline code spans.

    For reachability this is the right cut: a path inside a fenced example is
    an illustration, not a pointer, but a BACKTICKED path in prose is exactly
    how this repo's own CLAUDE.md points at things -- it is what `refs` mode
    exists to follow. Stripping inline spans here would delete the edges.
    """
    return FENCE.sub(lambda m: "\n" * m.group(0).count("\n"), text)


def strip_code(text: str) -> str:
    """Remove fenced blocks and inline code before extracting links.

    Without this, prose that *describes* link syntax -- a doc explaining
    `[t](p)` -- is scored as a broken link. Fences collapse to newlines so
    line numbers survive.
    """
    text = FENCE.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    return INLINE_CODE.sub("", text)


def outgoing(src: str, root: Path, corpus: set[str], dirs: set[str], mode: str
             ) -> tuple[set[str], set[str]]:
    """(md files pointed at, directories pointed at) from one source file."""
    try:
        # Same code-span stripping as --links: a doc that *describes* a path in a
        # fenced example is not pointing at it.
        text = strip_fences((root / src).read_text(encoding="utf-8", errors="replace"))
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


BANNER_SCAN_LINES = 8   # a self-declaration sits at the top, not buried at line 39
LIVE_STATUS = {"PRODUCTION", "EMERGING", "REFERENCE", "STABLE", "ACTIVE", "CURRENT"}
DEAD_STATUS = {"ARCHIVED", "RETIRED", "RETIRING", "DEPRECATED", "SUPERSEDED"}
# A banner must be a SELF-REFERENTIAL DECLARATION near the top -- a leading
# blockquote or bold run in the first few lines -- not merely a keyword
# anywhere in the first 40. The loose version over-credited exactly where it
# was applied: a deprecation archive is the corpus most likely to contain
# "superseded"/"deprecated" for reasons unrelated to self-declaration. Three of
# four banner-only "correct" verdicts were false positives: a doc *about*
# supersession, a legend row in a status-key table, and a template placeholder.
BANNER_WORDS = re.compile(
    r"(?i)\b(archived|superseded|retired|tombstone|do not use|no longer current"
    r"|not current guidance|historical (record|value|comparison)|merged into"
    r"|replaced by|evicted to archive|collapsed)\b")
BANNER_FORM = re.compile(r"^\s{0,3}(>|\*\*|__)")
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
    if status in DEAD_STATUS:
        return "correct"
    # Body banner: a declaration, in declarative form, in the first few lines
    # after any frontmatter and the H1.
    body = text.splitlines()
    if body and body[0].startswith("---"):
        for i, ln in enumerate(body[1:], 1):
            if ln.startswith("---"):
                body = body[i + 1:]
                break
    for ln in body[:BANNER_SCAN_LINES]:
        if BANNER_FORM.match(ln) and BANNER_WORDS.search(ln):
            return "correct"
    return "absent"


def report_links(root: Path, corpus: set[str]) -> int:
    """Classify every internal markdown link. Counts are reproducible.

    Buckets, in precedence order:
      resolves       target exists relative to the containing file
      root-relative  only resolves if read as repo-root-relative (a generated
                     footer written with root paths, dropped into a subdir)
      outside-repo   file:// or a path escaping the repo -- unresolvable to
                     any other reader
      placeholder    a template stand-in ({target}, path/to/file.md)
      dangling       target exists nowhere
    """
    counts = {k: {"live": 0, "archive": 0}
              for k in ("resolves", "root-relative", "outside-repo",
                        "placeholder", "dangling")}
    dangling_live: list[str] = []
    total = 0
    for f in sorted(corpus):
        lane = "archive" if f.startswith("archive/") else "live"
        try:
            text = strip_code((root / f).read_text(encoding="utf-8", errors="replace"))
        except OSError:
            continue
        for raw in MD_LINK.findall(text):
            tgt = raw.strip().strip("<>").split("#", 1)[0].split("?", 1)[0].strip()
            if not tgt or tgt.startswith(("http://", "https://", "mailto:", "#")):
                continue
            total += 1
            cand = os.path.normpath(Path(f).parent / tgt).replace(os.sep, "/")
            # outside-repo means exactly that: a file:// URL, or a path that
            # still escapes the repo root once normalised. A "../../x.md" that
            # lands back INSIDE the repo at a path that does not exist is a
            # plain dangling link (wrong relative depth), not an external one.
            if tgt.startswith("file://") or cand.startswith(".."):
                counts["outside-repo"][lane] += 1
                continue
            if cand in corpus or (root / cand).exists():
                counts["resolves"][lane] += 1
            elif PLACEHOLDER.search(tgt):
                counts["placeholder"][lane] += 1
            elif os.path.normpath(tgt).replace(os.sep, "/") in corpus:
                counts["root-relative"][lane] += 1
            else:
                counts["dangling"][lane] += 1
                if lane == "live":
                    dangling_live.append(f"{f}  ->  {tgt}")

    print(f"internal markdown links (code spans stripped): {total}\n")
    print(f"{'class':16}{'live':>8}{'archive':>10}{'total':>8}")
    for k, v in counts.items():
        print(f"{k:16}{v['live']:>8}{v['archive']:>10}{v['live'] + v['archive']:>8}")
    if dangling_live:
        uniq = sorted(set(dangling_live))
        print(f"\ndangling in live docs: {len(dangling_live)} "
              f"({len(uniq)} distinct source->target pairs):")
        for d in uniq:
            print(f"  {d}")
    return 0


# Not every file owes the reader a pointer. Lumping them into one percentage
# was the metric's biggest distortion: a corpus-wide 51% read as "half the prose
# is unfindable" when in fact every guidance document was reachable and the
# shortfall was entirely config and frozen data.
#
#   guidance   prose a reader is meant to find and act on. Pointer reachability
#              is a real obligation here, and the only place the headline means
#              anything.
#   mechanism  harness config (.claude/): skills, commands, rules. The runtime
#              loads these by its own rules; nothing links to a rules file and
#              nothing should. Link-unreachable is the CORRECT state.
#   data       frozen fixtures, transcripts, generated artifacts. Reached
#              through their own provenance file, if at all.
#   scratch    drafts and work-in-progress.
def lane_of(path: str) -> str:
    if path.startswith(".claude/"):
        return "mechanism"
    if path.startswith("research/artifacts/"):
        return "data"
    if path.startswith("drafts/"):
        return "scratch"
    if path.startswith("archive/"):
        return "dead"
    return "guidance"


def report_currency(root: Path, lanes: list[str]) -> int:
    """Classify every markdown file in each named dead lane."""
    any_lane = False
    worst: list[str] = []
    for lane in lanes:
        d = root / lane
        if not d.is_dir():
            continue
        any_lane = True
        tracked = repo_markdown(root, include_archive=True)
        files = sorted(root / f for f in tracked
                       if f == lane or f.startswith(lane.rstrip("/") + "/"))
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
    ap.add_argument("--links", action="store_true",
                    help="instead of reachability, classify every internal markdown "
                         "link (resolves / root-relative / outside-repo / dangling)")
    ap.add_argument("--currency", nargs="*", metavar="LANE",
                    help="instead of reachability, classify currency markers in these dead "
                         "lanes (default: archive old deprecated legacy)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    root = Path(args.root).resolve()

    if args.currency is not None:
        return report_currency(root, args.currency or
                               ["archive", "old", "deprecated", "legacy"])

    corpus = repo_markdown(root, args.include_archive or args.links)
    if args.links:
        return report_links(root, corpus)

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

    # Three disclosures the headline percentage hides. Reported always, because
    # each one moves the number in a direction the headline flatters.
    print()
    for k, v in results.items():
        tier = k.split("/")[0]
        seeds = set(v["entry_points"])
        reach = set(corpus) - set(v["unreachable"])
        net_n, net_d = len(reach - seeds), len(corpus) - len(seeds)
        # (a) seeds are not an achievement: they were loaded, not reached.
        line = (f"{k}: net of seeds {net_n}/{net_d} "
                f"({round(100 * net_n / net_d, 1) if net_d else 0}%)")
        # (b) a generated inventory can carry the whole corpus on one edge, so
        #     the metric is gameable by one line nobody will ever act on.
        inv = {f for f in corpus if Path(f).name in
               ("INDEX.md", "SUMMARY.md", "TOC.md")}
        if inv:
            without = reachable(root, corpus - inv, seeds & (corpus - inv),
                                k.split("/")[1])
            line += (f" | excluding generated inventory "
                     f"{len(without - seeds)}/{len(corpus - inv - seeds)}")
        # (c) reaching a tombstone is a debit, not a credit. Never folded in.
        dead = {f for f in reach if f.startswith("archive/")}
        if dead:
            line += f" | hazard exposure (reachable dead-lane files) {len(dead)}"
        print(line)
        del tier

    # (d) the decomposition that makes the headline mean something. Report the
    #     guidance lane separately, with the generated inventory excluded --
    #     that single figure is the one worth acting on.
    print()
    for k, v in results.items():
        seeds = set(v["entry_points"])
        inv = {f for f in corpus if Path(f).name in ("INDEX.md", "SUMMARY.md", "TOC.md")}
        reach = reachable(root, corpus - inv, seeds & (corpus - inv), k.split("/")[1])
        buckets: dict[str, list[int]] = {}
        for f in corpus - inv:
            b = buckets.setdefault(lane_of(f), [0, 0])
            b[1] += 1
            if f in reach:
                b[0] += 1
        parts = [f"{ln} {n}/{d}" for ln, (n, d) in sorted(buckets.items())]
        print(f"{k}: by lane, index excluded — " + " | ".join(parts))

    if args.list_unreachable:
        for k, v in results.items():
            print(f"\n--- unreachable under {k} ({len(v['unreachable'])}) ---")
            for f in v["unreachable"]:
                print(f"  {f}")
    return 0


if __name__ == "__main__":
    # Piping to `head` closes stdout early; exit quietly rather than tracebacking.
    try:
        raise SystemExit(main())
    except BrokenPipeError:
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
        raise SystemExit(0)
