---
lens: devloop-and-public
convergence: converged
prompts:
  - "Fable #15 — Steinberger dev-loop (tight write-loop with gates)"
  - "Fable #16 — blog/content consolidation (public-surface coherence; local-origin — the verified Miessler primary carries 15 prompts, this 16th is ours)"
date: 2026-06-21
auditor: subagent (devloop-and-public lens)
scope: self-audit of claude-code-project-best-practices repo
---

# Lens 6: Dev-loop & Public Surface

This audit applies two "Fable" prompts to the best-practices repo itself: Miessler's #15 (does the
repo practice a tight write-loop with working gates — lint, INDEX regen, RSS/expiry checks?) and
#16 (is the repo's public surface — README, ONE-LINE-PROMPT, INDEX — coherent and consolidated,
or scattered and duplicative?). One provenance note: the verified Miessler primary carries 15
prompts, so #15 is his and #16 is a local-origin addition kept under the same numbering. The repo
is itself a public knowledge product, so both lenses are fair to apply to it.

## Summary judgment

The write-loop has real gates and most of them work, and the public surface is genuinely strong —
README, ONE-LINE-PROMPT, and AUDIT-CONTEXT are tightly coordinated and the count discipline
(42 routable + 1 template) is honest and self-explained. The biggest gap is an *aspirational
loop that has rotted*: two of the four maintenance scripts (`check-measurement-expiry.py`,
`generate-tools-tracker.py`) still point at the v1 `patterns/` directory that the v1→v2 migration
archived, so the repo's own staleness gate scans a directory that no longer exists while the 43
live `analysis/` docs — which all carry exactly the `measurement-claims` / `revalidate` frontmatter
the gate was built to read — go unchecked. That is the highest-value fix, and it is a quiet one
because the workflow runs green (the scripts exit cleanly on an empty/missing dir) while doing
nothing useful.

## Findings

### Finding 1 — The measurement-expiry gate scans an archived, empty directory (the loop's own freshness check is a no-op)

**Severity: high**

`scripts/check-measurement-expiry.py` defaults to `--patterns-dir patterns` (line 196:
`parser.add_argument("--patterns-dir", default="patterns", ...)`), and `tools-evolution-tracker.yml`
calls it as `python scripts/check-measurement-expiry.py --create-issue` with no override (step at
`.github/workflows/tools-evolution-tracker.yml:57-61`). But the root `patterns/` directory does not
exist — it was archived to `archive/patterns-v1/` in the v1→v2 migration. Meanwhile the live
`analysis/` docs are exactly where the dated claims now live: all 43 `analysis/*.md` carry the
`measurement-claims` / `revalidate` frontmatter the gate parses (e.g.
`analysis/harness-engineering.md:1-12` has `measurement-claims:` with `revalidate: "2026-08-01"`).
So the repo built a real expiry gate for time-bound claims, then archived the only directory it
looks at, and now the daily job runs green while checking nothing. This is the gated-loop failure
mode in miniature: a gate that exists, runs, and silently verifies the empty set. (Provenance: the
tight-loop diagnosis traces to a single Steinberger X post, which Osmani quotes for one line inside
his own loop-engineering framing; the gate schema itself is this repo's own formalization.)

Evidence:
- `scripts/check-measurement-expiry.py:196` (`default="patterns"`), `:36` (`self.patterns_dir.glob("*.md")`)
- `.github/workflows/tools-evolution-tracker.yml:57-73` (calls expiry check, opens an issue on failure — but failure can't fire on an empty dir)
- `analysis/harness-engineering.md:1-12` (live frontmatter the gate should be reading; 43/43 analysis docs carry `revalidate-by`/`revalidate`)
- root `patterns/` confirmed absent; content lives at `archive/patterns-v1/` (24 docs per `INDEX.md:209-234`)

**Recommendation:** Repoint the expiry gate at `analysis/`. Either change the script default to
`analysis` or pass `--patterns-dir analysis` in `tools-evolution-tracker.yml:60`, and confirm the
frontmatter shape matches (the script expects a `measurement-claims:` list with `revalidate:` dates,
which `analysis/` docs already use). This converts a dead daily job into the freshness gate the
`revalidate-by` frontmatter was clearly designed to drive — and it ties directly to the `PLAN.md`
"Next Review" cadence and the `evidence-based-revalidation.md` doctrine, closing the loop between
the stated revalidation discipline and an automated check that actually enforces it.

### Finding 2 — `generate-tools-tracker.py` writes to a path that only exists under archive/ (orphaned generator)

**Severity: medium**

`scripts/generate-tools-tracker.py` hardcodes `PATTERNS_DIR = Path("patterns")` (line 30) and
writes `TOOLS-TRACKER.md` to the repo root (line 32), and `tools-evolution-tracker.yml:32-55`
runs it daily and commits `TOOLS-TRACKER.md` / `TOOLS-TRACKER.json` if changed. But `patterns/`
is gone, so the scan is empty, and the only `TOOLS-TRACKER.md` in the repo lives at
`archive/docs-v1/TOOLS-TRACKER.md` — a v1 artifact, not something this workflow regenerates into
the live surface. So the daily commit step is wired to (re)create a root-level `TOOLS-TRACKER.md`
from an empty scan, which is at best a no-op and at worst would commit an empty tracker over time.

Evidence:
- `scripts/generate-tools-tracker.py:30` (`PATTERNS_DIR = Path("patterns")`), `:32` (`TOOLS_TRACKER_FILE = Path("TOOLS-TRACKER.md")`)
- `.github/workflows/tools-evolution-tracker.yml:32-55` (generates + commits a root `TOOLS-TRACKER.md`)
- `find` shows the only live copy is `archive/docs-v1/TOOLS-TRACKER.md` (`INDEX.md:142`)

**Recommendation:** Decide whether TOOLS-TRACKER is a live product or a retired v1 artifact, and
make the workflow match the decision. If retired (most likely — it lives in `archive/docs-v1/` and
the v2 audit doesn't reference it), disable or delete `tools-evolution-tracker.yml` and the two
scripts it drives, or move the whole tracker concern to the ARCHIVE. If live, repoint
`PATTERNS_DIR` at `analysis/` and surface the regenerated tracker from the README. Right now it is
a third state — running daily but disconnected from both the live docs and the public surface.

### Finding 3 — `.github/workflows/README.md` is stale and undercounts the workflow set (documents 3 of 5)

**Severity: medium**

The workflows README (`.github/workflows/README.md`, footer "Last Updated: February 2026")
documents three workflows — `claude-code.yml`, `source-monitoring.yml`, `link-checker.yml` — but
the directory actually holds five: those three plus `anthropic-blog-rss.yml` (every 6 hours, Claude-
API-powered blog analysis) and `tools-evolution-tracker.yml` (daily TOOLS-TRACKER + expiry check).
The two undocumented ones are the more interesting automations (one calls the Anthropic API with a
secret; the other is the broken expiry/tracker pair from Findings 1–2), and they are exactly the
ones a reader of the workflows README would not know to look at. The "Monitoring Schedule" table
(`:137-142`) and the PLAN.md cross-reference (`:232-240`) are both built only from the three
documented workflows, so an operator reading either would not know the blog-RSS job exists or that
it consumes `secrets.ANTHROPIC_API_KEY` (`anthropic-blog-rss.yml:52-53`).

Evidence:
- `.github/workflows/README.md` documents 3 workflows; footer "Last Updated: February 2026"
- directory actually contains 5 `.yml` files including `anthropic-blog-rss.yml`, `tools-evolution-tracker.yml`
- `anthropic-blog-rss.yml:52-53` uses `ANTHROPIC_API_KEY` — undocumented in the "Secrets Required: None" section (`README.md:246-248`)

**Recommendation:** Regenerate the workflows README to cover all five, add the blog-RSS and
tools-evolution-tracker rows to the Monitoring Schedule table, and correct the "Secrets Required:
None" claim (the blog-RSS job needs `ANTHROPIC_API_KEY`). This is a documentation-currency gate the
repo preaches (its own `stop-doc-check.sh` warns on stale ARCHITECTURE/PLAN) but does not apply to
its own `.github/` docs.

### Finding 4 — INDEX regeneration works but is invisible to the public-facing toolchain (not an npm script, not in CI)

**Severity: low**

The INDEX loop is genuinely good in one direction: `post-tool-use.sh:52-87` regenerates `INDEX.md`
via `automation/generate_index.py` on structure-changing tool calls, and prints a notice when it
changes — a clean local write-loop. But the regeneration is *only* wired to the local PostToolUse
hook. It is not an npm script (`package.json` exposes only `lint` and `lint:fix`), and no CI job
regenerates or verifies INDEX freshness, so a contributor working without the hook (the common
case for an external PR — the hook lives in `.claude/`, which a fork may not run) can land a doc
without INDEX updating, and nothing catches it. The CONTRIBUTING integration checklist
(`CONTRIBUTING.md:77`) even acknowledges this by listing INDEX as "auto-regenerated… or leave for
the next maintenance pass," which is an honest admission that the gate is best-effort, not enforced.

Evidence:
- `.claude/hooks/post-tool-use.sh:52-87` (local regen, works)
- `package.json:9-12` (only `lint`/`lint:fix`; no `index` script)
- `automation/generate_index.py` not referenced in `package.json` or any `.github/workflows/*.yml`
- `CONTRIBUTING.md:77` ("auto-regenerated. Run the regenerator skill … or leave for the next maintenance pass")

**Recommendation:** Add `"index": "python3 automation/generate_index.py"` to `package.json` scripts
and a CI check (in `link-checker.yml`'s PR path, which already runs on `.md` changes) that runs the
generator and fails if `git diff --exit-code INDEX.md` is non-empty. That makes INDEX freshness a
real gate for external contributors, not a hook that only fires for the maintainer locally.

### Finding 5 — Public surface (README / ONE-LINE-PROMPT / AUDIT-CONTEXT) is coherent and well-consolidated — confirm, do not change

**Severity: low (positive finding)**

On the #16 consolidation lens the repo is in good shape and should not be "fixed." The three
public entry points are tightly coordinated rather than duplicative: `README.md:53-67` carries the
copy-paste audit prompt and explicitly defers the full output format to `ONE-LINE-PROMPT.md`, which
in turn carries the structured-output schema and defers routing to `AUDIT-CONTEXT.md` — a clean
single-source-per-concern split with no obvious copy-paste drift between the README's prompt and
ONE-LINE-PROMPT's prompt (both updated to `model-version-4-8`, both reference the same anti-bloat
rule). The doc-count discipline is honest and self-documenting: README states "42 routable + 1
template = 43 files" (`README.md:82-84`) and the live `analysis/` count is exactly 43, so the
public claim matches reality. The SOURCES.md / SOURCES-QUICK-REFERENCE.md split is a deliberate
full-vs-top-30 tiering (`README.md:137-138`), not accidental duplication, and CONTRIBUTING gives an
explicit rule for when an entry goes in QUICK-REFERENCE (Authority 3+) vs SOURCES only
(`CONTRIBUTING.md:74`). This is the consolidation Fable #16 asks for, already done.

Evidence:
- `README.md:53-67` (prompt) defers format to `ONE-LINE-PROMPT.md:21-140`; routing to `AUDIT-CONTEXT.md`
- `README.md:82-84` count claim ("42 … plus CANONICAL-DOC-TEMPLATE.md") matches actual 43 `analysis/*.md`
- `CONTRIBUTING.md:68-80` Integration Checklist enforces cross-file coherence (SOURCES + AUDIT-CONTEXT + README + INDEX) on every new doc
- `CONTRIBUTING.md:74` rule for SOURCES vs SOURCES-QUICK-REFERENCE placement

**Recommendation:** No change. Keep the per-concern single-source split and the honest count
discipline. If anything, the Integration Checklist in CONTRIBUTING is the mechanism that keeps this
coherent — protect it, and make sure new-doc PRs actually run it (it is currently human-enforced,
not CI-enforced; see Finding 4 for the INDEX half of that).

### Finding 6 — `package.json` metadata is internally inconsistent (cosmetic, but it is part of the public surface)

**Severity: low**

`package.json` carries stale/contradictory metadata for a repo whose public identity matters:
`version: "1.0.0"` (line 3) while README and PLAN both call the project v2.1; `license: "ISC"`
(line 19) while README, CONTRIBUTING, and the repo's stated terms all say MIT (`README.md:201-203`,
`CONTRIBUTING.md:357`); `main: "index.js"` (line 5) for a repo with no `index.js` (it is a docs
product, not a JS package); and empty `author` / `keywords`. None of this breaks the loop, but
`package.json` is machine-readable public metadata (npm, GitHub's sidebar, tooling), and the
license mismatch in particular is the kind of thing a careful adopter will notice.

Evidence:
- `package.json:3` (`"version": "1.0.0"`) vs `README.md:188` / `PLAN.md:10` ("v2.1")
- `package.json:19` (`"license": "ISC"`) vs `README.md:201-203` + `CONTRIBUTING.md:357` ("MIT License")
- `package.json:5` (`"main": "index.js"`) — no such file in a docs-only repo

**Recommendation:** Reconcile `package.json` to MIT, bump version to match the v2.1 line (or drop
the version field if it is not meaningfully tracked), clear or fix `main`, and fill `author`. Small,
but it is the one place the public metadata directly contradicts the repo's own stated license.

## What's working well (confirm, don't change)

- **The hook-driven local write-loop is real and disciplined.** `post-tool-use.sh` regenerates INDEX
  and auto-formats code on Write/Edit; `stop-doc-check.sh` warns on stale ARCHITECTURE/PLAN and on
  uncommitted/unpushed work at session end; `credential-scan.sh` runs PreToolUse. That is a genuine
  gated write-loop for the maintainer's local sessions, inspired by Steinberger's tight-loop
  diagnosis though the gate instrument itself is homegrown.
- **Lint is a working gate.** `package.json:10-11` defines `lint`/`lint:fix` over all markdown with a
  sensible ignore set, and `link-checker.yml` runs markdownlint + link-check in CI on `.md` PRs.
- **The public surface is consolidated, not scattered** (Finding 5) — README/ONE-LINE-PROMPT/AUDIT-
  CONTEXT split cleanly by concern, the doc count is honest, and CONTRIBUTING's Integration Checklist
  is the right mechanism to keep it that way.
- **Source-freshness automation is partly live and useful**: `source-monitoring.yml`,
  `link-checker.yml`, and `anthropic-blog-rss.yml` all run on cron and open issues — the input side
  of the loop (catch new Anthropic content) works even though the output side (expiry/tracker,
  Findings 1–2) has rotted.

## Top recommendation

Repoint `check-measurement-expiry.py` (and decide the fate of `generate-tools-tracker.py`) from the
archived `patterns/` directory to the live `analysis/` directory, so the repo's own staleness gate
actually scans the 43 docs whose `revalidate` frontmatter it was built to read. Right now the gate
runs daily and verifies nothing — the single highest-value fix for closing the repo's own write-loop,
and it directly operationalizes the `evidence-based-revalidation.md` discipline the project preaches.
