---
lens: memory-autonomy-policy
prompts: ["Fable #4 memory-that-compounds", "Fable #6 autonomy-ladder", "Fable #12 decisions-into-policy"]
date: 2026-06-21
---

# Self-Audit Lens 3: Memory / Autonomy / Policy

This lens applies Daniel Miessler's Fable prompts #4 (memory that compounds), #6 (the
autonomy ladder — what runs unattended vs. what escalates), and #12 (recurring judgment
calls promoted into stated policy) to the best-practices repo *itself*. The headline: the
repo's compounding-knowledge and decisions-into-policy story is strong at the prose and
routing layer, but its automation-script layer decayed silently when the v2.0 reposition
moved `patterns/ → analysis/` and never moved the scripts that enforce the cadence. The
honor-system failure the repo's own revalidation doc warns against is live in the repo.

---

## What is genuinely working (do not "fix")

The compounding and policy machinery is real, not aspirational:

- **DECISIONS.md is a true append-only decision log.** Ten numbered decisions plus dated
  in-line decisions (`Decision 8` SDD adoption, the 2026-03-06 tier-removal pair, the
  2026-06-06 curate-references pass, `Decision 10` 2026-06-15 loop-engineering). Each
  carries Context / Alternatives Considered / Decision / Trade-offs, and several
  explicitly record *what was rejected and why* (the loop-engineering "new paradigm doc"
  rejection at `DECISIONS.md:639`). This is exactly the Fable #12 shape — a recurring call
  resolved once, then cited rather than re-litigated.
- **CONTRIBUTING.md encodes the lifecycle as policy, not lore.** The status ladder
  `EMERGING → PRODUCTION → RETIRING → RETIRED` (`CONTRIBUTING.md:99`) and the "Retiring a
  Doc (Replacement Readiness)" section (`CONTRIBUTING.md:93`) turn the recurring "should
  this doc still exist?" judgment into a stated rule with a tombstone-not-delete policy.
  The Integration Checklist (`:68`) makes required frontmatter (`evidence-tier`,
  `applies-to-signals`, `last-verified`, `revalidate-by`, `status`) a gate.
- **AUDIT-CONTEXT.md is the best policy artifact in the repo for this lens.** It states a
  *signal-vocabulary invariant* (`AUDIT-CONTEXT.md:242`), an Anti-Bloat Rule
  (`:203`), silent Edge-Case handling (`:70`), and an Always-Fetch set that pins
  `evidence-based-revalidation.md` into *every* audit (`:93`) on the stated grounds that
  "every claim has a half-life." That is a recurring judgment call (surface stale-claim
  risk) promoted into unconditional policy.
- **The autonomy ladder is explicitly analyzed, with blast-radius.**
  `analysis/scheduled-and-looping-primitives.md` is the repo's own treatment of Fable #6:
  a three-way Cloud-Routine / Desktop-task / in-session-`/loop` comparison keyed on "who,
  if anyone, is watching" (`:49`), a `cron-disabled` negative guard that correctly
  suppresses *only local* rows while still emitting the cloud-Routine operator question
  (`:90`), and honest open gaps (runaway-loop economics; pure-cloud Routines invisible to
  a repo-local audit, `:108`). The detection predicates were measured, not assumed — the
  `harness-goal-completion-loop` anchor went 80%→0% false-positive after testing (`:89`).
- **memory-system-patterns.md is a clean "memory that compounds" doctrine.** It states the
  four memory types, the save-vs-derive boundary (`:128`), and the staleness diagnostic
  ("memory that's wrong is worse than no memory," `:154`) — the Fable #4 discipline, with
  the OKF `type:` external spec now cited (`:74`).

These should be cited as the positive baseline; the findings below are concentrated and
specific, not a wholesale rework.

---

## Findings

### Finding 1 — The measurement-expiry gate is silently dead: it scans the deleted `patterns/` dir, so the revalidation cadence is unenforced (HIGH)

`scripts/check-measurement-expiry.py` defaults to `--patterns-dir patterns`
(`check-measurement-expiry.py:196`, `:30` in the tracker generator). The v2.0 reposition
(`DECISIONS.md:459`, "Archive 24 v1 patterns... focus on 14 analysis documents") moved all
content to `analysis/`, and `patterns/` no longer exists in the repo. Running the script
with its default confirms the no-op:

```
🔍 Checking measurement claims in patterns...
   Found 0 pattern files
   ⚠️  Expired: 0 claims
```

But the 27 docs that actually carry `measurement-claims` live in `analysis/`. Pointed
there, the same script finds **2 genuinely expired claims** (revalidate date `2026-03-20`,
~3 months overdue as of 2026-06-21) it has been letting through. This is the exact
honor-system anti-pattern the repo's own revalidation doc names —
`evidence-based-revalidation.md:188`: *"`revalidate-by` dates pass silently; stale
generated values ship → Pre-commit drift gate..."* The gate exists but checks the wrong
directory, so the cadence is enforced by nobody.

The gate is wired into CI (`.github/workflows/tools-evolution-tracker.yml:60` calls the
script with no `--patterns-dir`, so it inherits the dead default), runs daily, and reports
"All measurement claims current" — a false all-clear in the GitHub issue path.

**Recommendation**: Change the default to `analysis` in
`check-measurement-expiry.py` (and the `PATTERNS_DIR = Path("patterns")` constant in
`generate-tools-tracker.py:30`), or pass `--patterns-dir analysis` in the workflow step.
Then triage the 2 already-expired claims (revalidate or mark historical). This is a
one-line fix that restores the single mechanical guard the repo built for its own
revalidation policy.

### Finding 2 — The tools-evolution workflow auto-commits a file generated from an empty scan, with `contents: write` autonomy on a broken generator (HIGH)

This is the one workflow on the *autonomous* rung of the autonomy ladder:
`tools-evolution-tracker.yml` runs daily (`cron: '0 6 * * *'`), holds `contents: write`,
and auto-commits `TOOLS-TRACKER.md`/`TOOLS-TRACKER.json` with no human in the loop
(`tools-evolution-tracker.yml:51-55`). But `generate-tools-tracker.py` scans the
nonexistent `patterns/` dir (`:30`), and neither `TOOLS-TRACKER.md` nor `.json` exists in
the repo today. So the workflow either commits an empty/degenerate tracker generated from
zero input, or no-ops while presenting itself as live automation. Granting unattended
write to a generator that reads a deleted directory is precisely the blast-radius the
repo's own `scheduled-and-looping-primitives.md` flags about Desktop tasks that "commit/PR
against uncommitted state" (`:86`) — the repo doesn't apply its own autonomy-ladder lens
to its own CI.

Contrast the *correct* rung: every job in `source-monitoring.yml` and the RSS workflow is
`issues: write` / `contents: read` (escalate-to-human via a GitHub issue), and
`check-anthropic-rss.py` deliberately stops at human review — its cache holds posts "seen
before but not in SOURCES.md yet, waiting for human review" (`check-anthropic-rss.py:131`).
That is a well-designed autonomy ladder: *read + escalate* for the judgment-laden source
intake, *write* reserved for the deterministic tracker. The defect is that the one
write-rung job rests on a broken generator.

**Recommendation**: Either (a) fix the generator's scan dir (Finding 1) and let the
auto-commit stand, or (b) demote `tools-evolution-tracker.yml` to `issues: write` until the
generator is verified, so it can't autonomously commit a degenerate artifact. State the
chosen rung in DECISIONS.md so the autonomy choice is policy, not an accident of YAML.

### Finding 3 — PLAN.md's Review Cadence claims automation that is partly dead, with no "known-stale" note (MEDIUM)

PLAN.md's Review Cadence table (`PLAN.md`, "Review Cadence") lists
`anthropic-blog-rss.yml` as the automation backing weekly Anthropic-blog monitoring, and
the High-Priority items mark "Keep SOURCES.md current" and "Update analysis docs when new
evidence emerges" as "Ongoing." The RSS workflow does exist and is plausibly live, but the
*expiry/tracker* half of the automation (Findings 1–2) is dead, and nothing in PLAN.md,
DECISIONS.md, or a DEPRECATIONS file records that. A reader trusts the cadence table as a
statement of what runs; here it overstates coverage.

Compounding this: `check-measurement-expiry.py:165` and `:181` instruct contributors to
"see DEPRECATIONS.md" and "see DOGFOODING-GAPS.md" — both files were confirmed absent from
the repo. So the script's own escalation copy points at documentation that doesn't exist,
breaking the "decision → recorded policy" chain at the moment a human is asked to act.

**Recommendation**: Add a one-line "automation status" note to PLAN.md's cadence table
distinguishing live (RSS issue-creation) from dormant (tracker/expiry, pending Finding 1),
and either create the referenced `DEPRECATIONS.md` (the tier-removal decision at
`DECISIONS.md:416` already says one is owed: *"Add note to DEPRECATIONS.md explaining tier
language removed"* — a promise never kept) or update the two script messages to point at
DECISIONS.md instead.

### Finding 4 — The scripts' module docstrings describe a `patterns/` architecture the repo abandoned, so the code's self-documentation lies (MEDIUM)

Beyond the runtime defaults, the *prose* in the scripts is stale:
`check-measurement-expiry.py:3` ("Check for expired measurement claims in patterns/."),
`generate-tools-tracker.py:3` and `:6` ("from patterns/ directory… Recursively scans
patterns/"), and `check-anthropic-rss.py`'s issue body telling a maintainer to "Run
`scripts/analyze-blog-post.py`… Update affected pattern files" (`:182-186`). A contributor
reading these scripts would reconstruct a directory layout the repo deleted in v2.0. The
repo's stated value is *evidence that doesn't drift*; its automation tier drifted and
narrates the pre-reposition world.

**Recommendation**: Sweep the three `scripts/*.py` docstrings and the RSS issue-body
template to say `analysis/`. Low effort, but it closes the gap between the repo's
"planned-obsolescence / no-drift" posture and its own tooling. Consider adding a single
`scripts/README.md` (none exists) stating which scripts are live, which dir they target,
and which workflow invokes each — the missing policy artifact for the automation layer.

### Finding 5 — Recurring judgment calls in the autonomy docs are well-stated but not yet promoted into a single "unattended-execution policy" the audit can cite (LOW)

The autonomy reasoning is excellent but distributed: the blast-radius judgments live in
`scheduled-and-looping-primitives.md`, the controls (7-day expiry, `CLAUDE_CODE_DISABLE_CRON`
kill-switch, no-permission-prompt cloud Routines) live partly there and partly in
`safety-and-sandboxing.md`, the ONE-LINE-PROMPT output has an "Unattended Execution
Exposure" section (`ONE-LINE-PROMPT.md:93`), and the routing lives in AUDIT-CONTEXT. The
recurring call — *"a token/$ budget ceiling is the blast-radius control that matters, not
just a time bound"* (`scheduled-and-looping-primitives.md:106`) — is stated as a Tier-D
gap, not yet as a recommendation the audit emits. For a lens whose whole point is
decisions-into-policy, this is the cleanest promotion candidate: the repo has done the
analysis and could state, as policy, the default operator questions and the budget-ceiling
recommendation, rather than leaving them as a gap note.

**Recommendation**: When the runaway-loop economics gap upgrades from Tier D to Tier B
(needs one measured `/hr from a bounded`/loop`), promote the budget-ceiling guidance from
"Gap" to a stated recommendation in the doc and a required output line in
ONE-LINE-PROMPT.md's Unattended Execution section. This directly feeds the new
intent/RETHINK layer: the intent of every unattended primitive is "run until <bound>," and
the policy the repo is closest to stating is *what bounds it* (condition + budget + who
escalates).

---

## How this informs the intent / RETHINK layer

The repo already separates *intent* (what a doc/script is for, in DECISIONS.md and the
status frontmatter) from *mechanism* (the routing predicates, the cron schedules). The
failure mode this lens surfaces is **intent-mechanism drift on the script side**: the prose
layer re-stated its intent at v2.0 (analytical layer over `analysis/`), but the enforcement
scripts kept the old mechanism (`patterns/` glob) and the old self-description. A RETHINK
layer should treat *the directory a script scans* and *the autonomy rung a workflow holds*
as first-class declared intent, checkable against reality — exactly the drift gate the repo
recommends to others but didn't run on itself. The autonomy ladder is the right model and is
already documented; the gap is that the repo grades external projects against it without
grading its own CI.
