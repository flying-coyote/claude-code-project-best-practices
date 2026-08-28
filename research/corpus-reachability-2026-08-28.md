---
convergence: single-source
---

# Corpus Reachability & Currency Self-Audit — 2026-08-28

**Purpose**: Raw measurement record behind [`analysis/prose-corpus-discoverability.md`](../analysis/prose-corpus-discoverability.md). Two corpora measured with the same instrument: an external 703-file prose vault (contributor-reported) and this repository (measured here, reproducible by anyone who clones it).

**Instrument**: [`scripts/measure-link-reachability.py`](../scripts/measure-link-reachability.py), committed with this record, with a determinism regression test at [`scripts/test-measure-link-reachability.py`](../scripts/test-measure-link-reachability.py).

> **Correction, 2026-08-28 (same day, post-review).** The figures first published here were produced by a **nondeterministic** instrument and were wrong by 1–3 files. `_resolve` iterated a two-element *set* of candidate paths, so when a reference resolved both relative-to-source and relative-to-repo-root, which one the BFS followed depended on `PYTHONHASHSEED`: repeated runs on an unchanged tree returned 168, 169, 170, or 171. The published `168` was one draw from that distribution. The corpus size was also stale — `179` counted the tree *before* this record and its analysis doc were added, so the measurement silently excluded itself.
>
> Both are fixed. `_resolve` now iterates an ordered list preferring relative-to-source (correct markdown semantics), the corpus is counted at the tree being measured, and a regression test runs the instrument under eight hash seeds and fails if any two disagree — verified to fail against the pre-fix version. **All figures below are the corrected ones.** The pre-correction figures are preserved in git.
>
> This is worth stating plainly rather than quietly repairing, because it is exactly the failure this document describes one level up: an instrument that ran green, looked authoritative, and was not measuring what it claimed. A single run could not detect it.

**Why this record exists**: this repository's identity is measurements and instruments no other lane publishes (README § Where This Sits). The claim under test — that a prose corpus's discoverability is a *measurable* property rather than a stylistic one — is only worth making if it comes with the measurement. This file is the measurement; the analysis doc is the argument.

---

## 1. What is being measured, and why two numbers not one

A prose file has two properties a retrieval system cannot infer from its text:

1. **Reachability** — can a session get to this file by following pointers from what it actually loads, without already knowing the file exists?
2. **Currency** — if it gets there, does the file tell it whether this is live guidance or superseded guidance? And is what it says *true*? A marker that asserts the wrong thing is worse than none, because it survives the check a careful reader runs.

These fail independently. A corpus can be almost fully reachable and yet barely marked (this repository), or well-typed and unreachable (the vault). Both failures are invisible to the checks a code project would run, for the reason set out in the analysis doc: superseded prose stays well-formed.

### Reachability: modes and entry tiers

The instrument is deliberately **generous** — each mode counts strictly more than the previous, so every reported figure is an *upper bound* on what a session would actually follow.

| Mode | Counts as a followable pointer |
|---|---|
| `links` | markdown links `[t](p)` and `@imports` only |
| `refs` | + backticked and bare paths that resolve to a real file |
| `dirs` | + a directory mention expands to the `.md` files directly inside it |

| Entry tier | Seeds |
|---|---|
| `E1 auto` | `.claude/CLAUDE.md` (+ root `CLAUDE.md` / `AGENTS.md` if present) — loaded in every session, unconditionally |
| `E2 config` | + `.claude/rules/`, `skills/`, `commands/`, `agents/` — surfaced as metadata or on trigger |
| `E3 front` | + `README.md` — the human front door, *not* session-loaded |

E1 is the tier that answers the question actually asked: what can a session reach from what it loads.

---

## 2. Corpus 1 — external prose vault (contributor-reported, Tier B)

Reported from a three-day production run; **not independently reproduced here** (the vault is not in this repository). Recorded at the tier the repo gives single-practitioner production evidence.

| Property | Value |
|---|---|
| Files | 703 markdown |
| Words | 6,070,000 |
| Session added | 359,985 words across 191 commits |
| Claude Code setup | following published advice |
| **Reachable by link from any entry point a session loads** | **12** |
| Frontmatter `type:` coverage | 96% |
| Project health check after every one of 191 commits | green |

The pairing is the finding: 96% type coverage and 191/191 green health checks, alongside 12 reachable files. No instrument in the setup was looking at the pointer graph, so nothing reported a defect.

---

## 3. Corpus 2 — this repository (measured 2026-08-28, Tier A, reproducible)

Measured at the tree that contains this record: **181 tracked markdown files** (26 `analysis/`, 96 `archive/`, 16 `.claude/`, 24 `research/`, 14 root, 4 `drafts/`, 1 `.github/`). The earlier `179` counted the parent commit and so excluded this file and its analysis doc.

### 3.1 Reachability — the repository passes

```
$ python3 scripts/measure-link-reachability.py --include-archive
corpus: 181 markdown files

entry/mode  reachable  of corpus
E1/links          1     0.6%
E1/refs         171    94.5%
E1/dirs         172    95.0%
E2/links        177    97.8%
E2/refs         181   100.0%
E2/dirs         181   100.0%
E3/links        177    97.8%
E3/refs         181   100.0%
E3/dirs         181   100.0%
```

Excluding `archive/` (85 live files): E1/links 1 (1.2%), E1/refs **71 (83.5%)**, E2/refs 85 (100%).

**Headline: 171 of 181 files (94.5%) are reachable from the auto-loaded entry point alone.** Against the vault's 12 of 703 (1.7%), this repository does not have the disease at the reachability level.

Note which half moved under the determinism fix: the live-only figure was **stable at 71/85 across every run, before and after**. All the variance lived inside `archive/`, in three `archive/examples-v1/*/README.md` files whose backticked `` `.claude/CLAUDE.md` `` resolves both to their own nested copy and to the repo-root one. The ambiguity was real; the coin-flip resolution of it was the bug.

Three mechanisms explain the gap, and all three are *maintenance instruments*, not writing style:

| Mechanism | What it does |
|---|---|
| [`INDEX.md`](../INDEX.md) | full generated inventory, auto-regenerated by the `PostToolUse` hook — one file that link-reaches everything |
| [`AUDIT-CONTEXT.md`](../AUDIT-CONTEXT.md) | signal → doc routing map; a routing row is **mandatory** per CONTRIBUTING § Integration Checklist |
| [`ABSORPTION-MAP.md`](../ABSORPTION-MAP.md) | one row per routable doc, with lane and delta |

### 3.2 The `E1/links` = 1 result is not noise

`.claude/CLAUDE.md` contains **zero** markdown links to other repository markdown files:

```
$ grep -oE '\[[^]]*\]\([^)]*\)' .claude/CLAUDE.md | wc -l
0
```

Its Resource Map points by backticked bare path instead — `ABSORPTION-MAP.md`, `SOURCES.md`, `AUDIT-CONTEXT.md`, `DECISIONS.md`, `SOURCES-QUICK-REFERENCE.md`, `.claude/review-protocol.md`, `analysis/`, `archive/` (8 resolvable references, verified). An agent follows those fine, which is why `E1/refs` is 171. The number is recorded because it fixes the instrument's calibration: *strict* link-reachability understates a corpus that points by path, so `refs` — not `links` — is the mode to report, and any threshold must be set against `refs`.

### 3.3 Currency marking — the repository fails

The first pass of this measurement used a binary marked/unmarked test (does the file carry `status:`, `last-verified:`, or a banner?). That test is wrong, and finding out why is part of the result: **17 files passed it while carrying a marker that said the opposite of the truth.** Marker *presence* is not marker *correctness*, and the worst case is not silence but a confident false statement.

The instrument therefore classifies three ways (`--currency`):

| Verdict | Meaning |
|---|---|
| `correct` | declares itself superseded — a dead `status:` value (`ARCHIVED`/`RETIRED`/`DEPRECATED`) or a supersession banner |
| `WRONG` | asserts a **live** status (`PRODUCTION`/`EMERGING`/`REFERENCE`/…) while sitting in a dead lane |
| `absent` | says nothing either way |

```
$ python3 scripts/measure-link-reachability.py --currency
archive/  n=96   correct=12 (12%)   WRONG=17   absent=67
```

**Twelve of 96 files in the dead lane correctly declared themselves superseded.** Seventeen actively asserted the opposite. Sixty-seven said nothing.

For comparison, the live lane: all 25 `analysis/` docs carry `status:` and `last-verified:`, and 21 carry a collapse/absorption banner. The discipline exists and is applied rigorously — to the lane that needs it least.

Whole-corpus marker presence by area (the looser binary test, retained because it shows where the discipline stops):

| Area | Files | `status:` | `last-verified:` | banner |
|---|---:|---:|---:|---:|
| `analysis/` | 25 | 25 | 25 | 21 |
| `archive/` | 96 | 25 | 24 | 13 |
| `research/` | 23 | 1 | 0 | 12 |
| root | 14 | 0 | 0 | 6 |
| `.claude/` | 16 | 0 | 0 | 3 |
| `drafts/` | 4 | 3 | 0 | 3 |
| `.github/` | 1 | 0 | 0 | 0 |

### 3.4 The severe case: 17 archived files asserted that they were live

These carried their own frontmatter asserting a live lifecycle status, using the identical machine-readable fields the live `analysis/` docs use. All seventeen are in `archive/patterns-v1/`:

| status | last-verified | file |
|---|---|---|
| PRODUCTION | 2026-03-23 | `advanced-hooks.md` |
| PRODUCTION | 2026-02-16 | `advanced-tool-use.md` |
| PRODUCTION | 2026-02-16 | `context-engineering.md` |
| PRODUCTION | 2026-02-16 | `documentation-maintenance.md` |
| PRODUCTION | 2026-02-16 | `github-actions-integration.md` |
| PRODUCTION | 2026-02-16 | `gsd-orchestration.md` |
| PRODUCTION | 2026-02-16 | `johari-window-ambiguity.md` |
| PRODUCTION | 2026-02-16 | `memory-architecture.md` |
| PRODUCTION | 2026-02-16 | `parallel-sessions.md` |
| PRODUCTION | 2026-02-16 | `planning-first-development.md` |
| EMERGING | 2026-02-27 | `productivity-tooling.md` |
| PRODUCTION | 2026-02-16 | `progressive-disclosure.md` |
| PRODUCTION | 2026-02-16 | `project-infrastructure.md` |
| PRODUCTION | 2026-02-16 | `session-learning.md` |
| PRODUCTION | 2026-02-16 | `skills-domain-knowledge.md` |
| PRODUCTION | 2026-02-16 | `spec-driven-development.md` |
| PRODUCTION | 2026-02-16 | `subagent-orchestration.md` |

Counting note: a plain `grep -rlE '^status: *"?(PRODUCTION|EMERGING|REFERENCE)' archive/` returns **18**. The extra hit is `archive/prompts-v1/MAKE-PROJECT-RECOMMENDATIONS.md` line 610, a *template example* inside a prompt body rather than that file's own frontmatter. The instrument parses the frontmatter block only; 17 is correct.

The departure is historical, not deliberate. These files were moved into `archive/patterns-v1/` in the v2.0 repositioning (March 2026) with their v1 frontmatter intact, and the tombstone-banner convention the repository later adopted — visible on `archive/security-data-pipeline.md` and its siblings as `> **EVICTED TO ARCHIVE (2026-07-10, …)**`, and recorded in `ARCHIVE.md` Phase 5 — was applied to the docs evicted *after* it existed, never backfilled to the ones evicted before.

**Remediated in this change** (separable commit): all 17 corrected to `status: ARCHIVED` with a tombstone banner naming the live successor where one exists. Frontmatter is otherwise byte-identical; the v1 `measurement-claims` blocks are preserved as recorded, now explicitly framed as a v1-era snapshot. Post-remediation:

```
$ python3 scripts/measure-link-reachability.py --currency
archive/  n=96   correct=29 (30%)   WRONG=0   absent=67
```

The 67 `absent` files are **not** fixed by this change and remain the open item. The pre-remediation state stays reproducible from git:

```
git worktree add --detach /tmp/pre <commit-before-this-change>
python3 scripts/measure-link-reachability.py --root /tmp/pre --currency
```

### 3.5 Two worked collisions

**Collision A — a superseded doc claims the live doc's topic.**

```
grep -rl "progressive disclosure" --include=*.md .
```
returns 18 files. Among them, both `analysis/claude-md-progressive-disclosure.md` (live, `status: PRODUCTION`, `last-verified: 2026-08-13`) and `archive/patterns-v1/progressive-disclosure.md` (superseded, `status: "PRODUCTION"`, `last-verified: "2026-02-16"`). The archived file additionally carries a `measurement-claims` block asserting "Token savings: 50-77% reduction from progressive disclosure" with `revalidate: 2026-11-01` — a live-looking, not-yet-expired revalidation date on a retired claim. Nothing in the returned text distinguishes the two except the path.

**Collision B — only the superseded doc matches the query.**

```
grep -rli "audit.*existing project" --include=*.md .
./archive/prompts-v1/AUDIT-EXISTING-PROJECT.md
```
One hit, and it is the v1 prompt. The live replacement is [`ONE-LINE-PROMPT.md`](../ONE-LINE-PROMPT.md), which does not use that phrasing. An agent asked to "audit an existing project against this repo's practices" and reaching for the obvious query gets *exclusively* superseded instructions, with no in-file signal — the archived prompt opens "Copy everything below the line and paste it into Claude Code."

### 3.6 Why nothing caught it — two different failures, not one

The first draft of this record claimed "every automated instrument is scoped to the live lane." That is **wrong**, and the correction is more interesting than the claim.

**Failure 1 — the currency checks are live-lane-scoped.**

| Instrument | Scope | Reads `archive/`? |
|---|---|---|
| `markdownlint-cli2` (`npm run lint`) | glob carries `'!archive'` | **no** — explicitly excluded |
| `scripts/check-measurement-expiry.py` | `--patterns-dir` default `analysis` | **no** |
| `.claude/hooks/stop-doc-check.sh` | `ARCHITECTURE.md` + `PLAN.md` mtime | no |
| `weekly-review` step 5b | absorption-map consistency greps | no |
| `automation/generate_index.py` (PostToolUse) | lists paths; asserts nothing about status | lists only |

Each exclusion is individually reasonable — you do not lint a tombstone. The aggregate is that nothing checks whether the dead lane *says* it is dead.

**Failure 2 — the check that does cover the whole corpus fires into a void.**

`.github/workflows/link-checker.yml` runs `gaurav-nelson/github-action-markdown-link-check` daily on cron and on every markdown PR, across **all** markdown including `archive/`. It is not live-lane-scoped. It works. And on the scheduled path it opens a GitHub issue titled "🔗 Broken links detected in documentation".

As of 2026-08-28 the repository has **916 open issues carrying the `documentation` label** (exact count via the issues API, `state=OPEN`). The ten most recent are all that same auto-filed broken-link issue, one per day from 2026-08-18 through 2026-08-27, **every one with zero comments and `updated_at` equal to `created_at`**. The oldest open issue dates to 2026-02-13.

So the link checker has been reporting for months into a queue nobody reads. This is a pathology this repository has already diagnosed once and acted on — the 2026-07 reduction deleted the RSS and source-monitoring watchers with the note that *"their GitHub issues sat unread — hundreds open, zero triage"* (PLAN.md, Review Cadence). The link checker survived that cull and reproduced the same failure.

Two things follow, and they are the useful part:

1. **A firing check is not a working check.** An alarm that cannot be acted on is indistinguishable, in outcome, from no alarm. The 214 dangling internal links in §3.7 have been individually detectable, daily, for months.
2. **The link checker cannot see the thing that matters anyway.** It asks whether a link *resolves* — a mechanical property, and precisely the code-like property that *does* survive the translation to prose. It cannot ask whether the target is *authoritative*. A link to `archive/patterns-v1/progressive-disclosure.md` resolves perfectly and is green every single day; the file it resolves to spent six months asserting `status: PRODUCTION`. Link resolution and link authority are different questions, and only the first has a checker.

### 3.7 Pointer decay in the live lane

Reproducible with `python3 scripts/measure-link-reachability.py --links`. Fenced blocks and inline code are stripped first, so prose that *describes* link syntax is not scored as a broken link — without that, this very record self-reports two false positives.

```
internal markdown links (code spans stripped): 1331

class               live   archive   total
resolves             835       179    1014
root-relative         54        17      71
outside-repo          28         0      28
placeholder            1         3       4
dangling              11       203     214
```

`root-relative` resolves only if read as repo-root-relative; `outside-repo` is a `file://` URL or a path that still escapes the repo root after normalisation.

The totals move as this record is edited — it is inside the corpus it measures, so adding a link here increments the count. That is not noise to suppress but a property of self-measurement worth naming: quote these figures with the commit they were taken at, never as standing constants.

Three sub-findings in the live lane:

- **54 root-relative links in 19 of 25 `analysis/` docs are emitted by this repo's own footer injector.** [`scripts/graphify_footer_inject.py:114`](../scripts/graphify_footer_inject.py) renders `` [`{target}`]({target}) `` where `target` is repo-root-relative (per its own comment at line 145), but writes it into files under `analysis/`. So `analysis/behavioral-insights.md` inside `analysis/domain-knowledge-architecture.md` resolves to `analysis/analysis/behavioral-insights.md`. The mechanism built to *enrich* the pointer graph is emitting pointers that do not resolve. A one-line `os.path.relpath` fixes it.
- **28 links point outside the repository** — `file:///home/jerem/project1/...` and `../../project1/...`. These are the OKF and loop-engineering case-study citations. They are honest provenance for the author and unresolvable for every other reader of a public repository.
- **11 dangling links in live files** (10 distinct source→target pairs): `SOURCES.md` → `analysis/dapr-durable-agents.md`, `analysis/mcp-client-integration.md`, `analysis/agent-principles.md`, `research/memory-systems-tools-inventory.md` (all removed in the 2026-07 reduction); `CONTRIBUTING.md` → `AUDIT-2026-02-27.md` (moved to `archive/`); and five in `.claude/skills/*/SKILL.md` written at the wrong relative depth (`../../analysis/…` from a two-deep skill directory lands at `.claude/analysis/…`).

---

## 4. Summary: the two corpora fail on opposite axes

| | vault (703 files) | this repo (179 files) |
|---|---|---|
| Reachable from session-loaded entry points | **12 of 703 (1.7%)** | 171 of 181 (94.5%) |
| Dead-lane files correctly declaring supersession | not measured | **12 of 96 (12%)** |
| Dead-lane files **asserting a live status** | not measured | **17** |
| Dead-lane files silent either way | not measured | **67 of 96 (70%)** |
| Health check / lint reporting a defect | green, 191/191 | lint green; the one check that *did* fire (daily link checker) has 916 open, untriaged issues |

Neither corpus's existing health signals reported either failure, because neither failure is what those signals measure. That is the point of the instrument.

---

## 5. Reproduction

```bash
python3 scripts/measure-link-reachability.py --include-archive        # 171/181
python3 scripts/measure-link-reachability.py                          # live only, 71/85
python3 scripts/measure-link-reachability.py --currency               # correct/WRONG/absent
python3 scripts/measure-link-reachability.py --links                  # link classification
python3 scripts/test-measure-link-reachability.py                     # determinism + invariants
grep -coE '\[[^]]*\]\([^)]*\)' .claude/CLAUDE.md                    # expect 0
```

Run the test before trusting any figure above. It executes the instrument under eight `PYTHONHASHSEED` values and fails if any two disagree — the check that would have caught the original defect, and which fails against the pre-fix instrument.

---

## Related

- [`analysis/prose-corpus-discoverability.md`](../analysis/prose-corpus-discoverability.md) — the analysis this record supports
- [`research/self-audit-2026-06/AUDIT-FINDINGS.md`](self-audit-2026-06/AUDIT-FINDINGS.md) — the prior self-audit (six lenses, 2026-06)

---

*Measured: 2026-08-28. Instrument: `scripts/measure-link-reachability.py`.*
