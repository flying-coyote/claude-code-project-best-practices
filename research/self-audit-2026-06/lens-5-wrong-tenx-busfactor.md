---
lens: wrong-tenx-busfactor
prompts:
  - "Fable #10 — where am I most wrong"
  - "Fable #11 — what 10xs and what dies"
  - "Fable #14 — bus-factor"
date: 2026-06-21
scope: self-audit of the best-practices repo through one integrated lens
convergence: single-source
---

# Lens 5 — Where the repo is most wrong, what would 10x, and the bus-factor

This applies three of Miessler's Fable prompts to the best-practices repo itself: where is the
guidance most likely wrong today, which capability would matter most if it 10x'd (and which docs are
dead weight), and what the single-maintainer risk is in keeping it current. Git inspection was
blocked by the maintainer's no-git guardrail, so the bus-factor read is built from on-disk
automation, cadence language, and freshness markers rather than `git shortlog`. Where a claim needs
a contributor count or commit cadence I could not verify, I say so.

## Headline

The single most-wrong thing in the repo today is not a stale *claim* — the analysis docs are
genuinely current (every `revalidate-by` is in the future, the routing map and INDEX were touched
2026-06-15/19, the model-migration docs already carry Opus 4.8 and the Fable-5 suspension). It is a
stale *mechanism*: the daily-scheduled GitHub Action that is supposed to enforce the revalidation
discipline scans `patterns/`, a directory that was archived to `archive/patterns-v1/` in the March
2026 v2.0 reposition. The automation that exists to catch the exact failure this lens looks for has
been silently no-op-ing against live content for roughly three months. That is the finding I'd act on
first, because it is the one place where the repo's own quality system is lying to its maintainer.

---

## Findings

### 1. The measurement-expiry / tools-tracker automation scans the archived `patterns/` dir, not live `analysis/` — silent daily no-op (HIGH)

`scripts/check-measurement-expiry.py` defaults `--patterns-dir patterns` and globs
`self.patterns_dir.glob("*.md")` (lines 27-36, 196-201). `scripts/generate-tools-tracker.py`
hard-codes `PATTERNS_DIR = Path("patterns")` and scans it recursively (lines 30, 56). Both are run
daily (cron `0 6 * * *`) by `.github/workflows/tools-evolution-tracker.yml`, which invokes
`python scripts/generate-tools-tracker.py --detect-deprecations` and
`python scripts/check-measurement-expiry.py --create-issue` with **no `--patterns-dir analysis`
override** (lines 34, 60). But the repo's live content moved to `analysis/` in the v2.0 reposition
(DECISIONS.md "Reposition as Analytical Layer — v2.0", which archived 24 v1 patterns to
`archive/patterns-v1/`). There is no `patterns/` directory at the repo root anymore. So the workflow
that is supposed to open an issue when a `revalidate-by` date passes finds zero files and reports
clean every day — the revalidation safety net is disconnected from the thing it protects.

Corroborating detail: `git diff --quiet TOOLS-TRACKER.md` in the same workflow (line 39) checks a
root-level `TOOLS-TRACKER.md` that now exists only at `archive/docs-v1/TOOLS-TRACKER.md`, so the diff
gate is also pointed at a path the generator can't write to under the current layout.

- Evidence: `scripts/check-measurement-expiry.py:3,27-36,196-201`; `scripts/generate-tools-tracker.py:30,56`; `.github/workflows/tools-evolution-tracker.yml:5-6,34,39,60`; `archive/docs-v1/TOOLS-TRACKER.md`; DECISIONS.md "Reposition as Analytical Layer — v2.0".
- Severity: HIGH — this is precisely the "stale advice slips through because the guard is broken" risk, and it is the maintainer's only automated revalidation enforcement.
- Recommendation: Repoint both scripts at `analysis/` — pass `--patterns-dir analysis` in the workflow (or change the script default and the hard-coded `PATTERNS_DIR`), and update the `TOOLS-TRACKER.md` diff path. Then run `check-measurement-expiry.py` once by hand against `analysis/` to confirm it actually parses the current frontmatter schema (`revalidate-by:`); the v1 frontmatter it was written for may differ from the canonical schema in `analysis/CANONICAL-DOC-TEMPLATE.md`, so verify the parse before trusting the green checkmark.

### 2. ARCHITECTURE.md is the one genuinely stale doc — frozen at the April v2.1 "26 documents" snapshot while everything else moved to 42 (MEDIUM)

ARCHITECTURE.md is stamped "Last Updated: April 13, 2026" and states "26 analysis documents" in four
places (lines 4, 33, 46, 108, 133), with a directory tree that lists the 26-doc layout and omits the
16 memory-systems / dapr / scheduled-looping / model-migration docs added since. README.md, PLAN.md,
INDEX.md, DECISIONS.md and AUDIT-CONTEXT.md all agree on 42 routable docs (INDEX shows 43 files in
`analysis/`, i.e. 42 + the non-routable `CANONICAL-DOC-TEMPLATE.md`). The repo's own CLAUDE-style
gotcha — "ARCHITECTURE.md and PLAN.md require manual updates (prone to staleness)" — names this exact
risk; PLAN.md was kept current but ARCHITECTURE.md was not. A reader who starts from ARCHITECTURE.md
(a natural entry point) gets a two-versions-old mental model of the repo's size and scope, and the
"Three-Project Ecosystem" table there still says ECC = 110K stars while README says 119K (see
finding 4).

- Evidence: `ARCHITECTURE.md:4,33,46,108,133`; vs `PLAN.md:19` (42), `INDEX.md:59` (analysis 43), `README.md:82-84`.
- Severity: MEDIUM — it's a meta-doc, not routed content, so it doesn't corrupt audit output; but it's the most-wrong single file and an easy correctness win.
- Recommendation: Update ARCHITECTURE.md to v2.1-current: 42 routable docs, refreshed directory tree (or replace the hand-maintained tree with a pointer to INDEX.md, which is auto-generated and already correct), and reconcile the ECC star count. Given the documented staleness-proneness, consider demoting ARCHITECTURE.md to a thin pointer at INDEX.md + DECISIONS.md rather than re-maintaining a parallel structure listing.

### 3. The `.github/workflows/README.md` documents a workflow set that no longer matches what's on disk (MEDIUM)

`.github/workflows/README.md` (stamped "Last Updated: February 2026") describes three workflows in
detail — `claude-code.yml`, `source-monitoring.yml`, `link-checker.yml` — and a "Monitoring
Schedule" table built around them. But the actual workflow files are `anthropic-blog-rss.yml`,
`claude-code.yml`, `link-checker.yml`, `source-monitoring.yml`, and `tools-evolution-tracker.yml`.
The two workflows that actually run the Python scripts (`anthropic-blog-rss.yml` →
`analyze-blog-post.py` + `check-anthropic-rss.py`; `tools-evolution-tracker.yml` →
`generate-tools-tracker.py` + `check-measurement-expiry.py`) are entirely undocumented in this
README. So the one place a second maintainer would look to understand the automation surface omits
the half of it that touches finding 1. This is a bus-factor amplifier: the broken automation in
finding 1 is invisible *and* undocumented.

- Evidence: `.github/workflows/README.md:7-110,137-142,278` vs `ls .github/workflows/*.yml`; script-to-workflow map confirms `anthropic-blog-rss.yml` and `tools-evolution-tracker.yml` are the script runners.
- Severity: MEDIUM.
- Recommendation: Regenerate the workflows README from the actual file set; document `tools-evolution-tracker.yml` and `anthropic-blog-rss.yml` (including which scripts they run and against which directory), and fix the schedule table. Folding this into the same pass as finding 1 is natural since both touch that workflow.

### 4. License is asserted three different ways and there is no LICENSE file (MEDIUM)

README.md says "MIT License — use freely" (line 203) and the v2.1 status / contributing sections
lean on MIT. CONTRIBUTING.md line 358-359 says contributions are licensed "under the MIT License."
But `package.json` declares `"license": "ISC"` (line 19), and there is **no LICENSE / LICENSE.md /
LICENSE.txt file anywhere in the repo**. For a public repo whose entire value proposition is being
copy-pasted and WebFetched into other people's projects (the README's headline use case), the
licensing ambiguity is a real adoption and reuse risk, not a cosmetic one — a careful downstream user
can't tell which license actually governs the content.

- Evidence: `README.md:203`; `CONTRIBUTING.md:358-359`; `package.json:19` (`"license": "ISC"`); `ls LICENSE*` → no file.
- Severity: MEDIUM.
- Recommendation: Pick one (MIT is what the prose intends), add a top-level `LICENSE` file, and set `package.json` `"license": "MIT"`. While there, fill the empty `"author"` field — an empty author on a single-maintainer public repo is a small bus-factor tell.

### 5. ECC headline metrics drift across files — 110K vs 119K stars, repeated "125+ skills, 28+ agents" snapshots (LOW)

The everything-claude-code comparison numbers are inconsistent: README.md says "119K+ stars" (lines
47, 180); ARCHITECTURE.md says 110K (line 106); DECISIONS.md says "110K+" (line 449); SOURCES.md says
"110K+ (as of March 2026)" (line 1159). These are the kind of upstream-mirror numbers that
DECISIONS.md Decision 9 ("point to living sources instead of mirroring them", 2026-06-06) explicitly
warns about — a hard count restated in five places is five things to keep in sync and a guaranteed
drift source. The repo already made the right call in principle (Decision 9) but didn't apply it to
its own competitor-comparison numbers.

- Evidence: `README.md:47,180`; `ARCHITECTURE.md:106`; `DECISIONS.md:449`; `SOURCES.md:1159,1172`.
- Severity: LOW — doesn't affect audit correctness, but it's a self-consistency / decaying-snapshot smell the repo's own doctrine flags.
- Recommendation: Apply Decision 9 to these too: state ECC's role qualitatively ("the maximalist tooling repo"), drop the precise star count to a single "as of {date}, ~{N}K" in SOURCES.md only, and have README/ARCHITECTURE/DECISIONS reference the role, not the number.

### 6. What would 10x: the adaptive routing audit is the crown jewel, and its currency depends on one fragile thing — the signal→doc sync (10X / structural)

The capability that, if it 10x'd, would matter most is the **adaptive routing audit** (AUDIT-CONTEXT.md
→ ONE-LINE-PROMPT.md). It is the repo's most distinctive asset, though the truthful provenance
frame is narrower than the README's "Where Else? Nowhere" column suggests: the diagnosis the audit
acts on is inspired by external practitioners, and what is genuinely ours is the instrument, the
routing formalization and the evidence-tier system. Everything else
(the 42 analysis docs) is raw material the audit refines. A 10x here is not "more docs"; it's making
the audit reproducible and trustworthy enough that someone other than the maintainer can run it and
get the same answer. The current design is strong (the two-level memory-index sub-route, the
anti-bloat rule, the `model-version-fable-mythos` volatile guard all show real care). The fragility
is that the whole thing rests on the hand-maintained invariant that every routable doc's
`applies-to-signals` frontmatter matches a signal key in AUDIT-CONTEXT.md, and that invariant is
enforced by prose ("A sync linter must whitelist these classes", AUDIT-CONTEXT.md:242) rather than by
a committed linter. The CONTRIBUTING integration checklist is six manual cross-file edits per new
doc. That's the 10x lever and the bus-factor risk in one: a committed sync-check that fails CI when a
doc's signals and the routing map diverge would both protect the crown jewel and let a second person
contribute without silently breaking routing.

- Evidence: `AUDIT-CONTEXT.md:9-10,242` ("Routing rows and doc frontmatter must stay in sync"; "A sync linter must whitelist these classes" — described, not implemented); `CONTRIBUTING.md:68-80` (6-file manual integration checklist); `README.md:16-23` (the "Nowhere" uniqueness column).
- Severity: structural / 10X-lever (not a defect today — the sync is currently correct per finding's INDEX/AUDIT-CONTEXT cross-read — but it's the highest-leverage thing to harden).
- Recommendation: Write the sync linter the docs already promise: parse `applies-to-signals` across `analysis/*.md`, parse the signal keys in AUDIT-CONTEXT.md, assert bidirectional coverage with the documented whitelist (`commit-low-activity`, `cron-disabled`, `audit-always-fetch`, `contributing-new-analysis`, and the index-internal sub-routing tokens), and wire it into a workflow. This is the single change that most reduces single-maintainer risk because it moves the audit's correctness from "the maintainer remembers the checklist" to "CI blocks the merge."
  One binding note: this function class is currently single-source (no external adoption evidence
  has survived verification), so adopting it as standing infrastructure requires converged status or
  an explicit owner exception.

### 7. Dead weight is minimal and mostly already handled — only two genuinely orphaned items (LOW)

The "what dies" half of Fable #11 mostly comes up empty, which is a good sign: the repo runs an
active retirement lane (CONTRIBUTING "Retiring a Doc", `session-quality-tools.md` already
`RETIRING`, `dapr-durable-agents.md` correctly tagged `REFERENCE`), and the v1 corpus is cleanly
archived rather than rotting in `analysis/`. The only true dead weight I found:

- `scripts/graphify_footer_inject.py` and `scripts/graphify_contradiction_lint.py` are wired into **no**
  workflow (every other script is). DECISIONS.md (2026-04-28) describes them as "committed as documented
  patterns for downstream consumers," so they may be intentional reference artifacts rather than active
  tooling — but nothing in the repo says so at the file or directory level, so a maintainer can't tell a
  deliberate reference script from a forgotten one.
- `V2-COMPLIANCE-MATRIX.md` (root, dated March 31, untouched since) is a v2.0-migration compliance
  artifact whose job is presumably finished; it sits in root alongside the live strategy docs with no
  status marker.

- Evidence: orphan-script scan (only the two `graphify_*` scripts are referenced by no workflow); `DECISIONS.md` 2026-04-28 decision; `V2-COMPLIANCE-MATRIX.md` (root, mtime 2026-03-31).
- Severity: LOW.
- Recommendation: Add a one-line header to the two `graphify_*` scripts (or a `scripts/README.md`) marking them "reference pattern, not run in CI" so their orphan status reads as intentional; and either archive `V2-COMPLIANCE-MATRIX.md` to `archive/` or stamp it DONE so it stops looking like live work.

---

## Bus-factor assessment

Git history was not inspectable (no-git guardrail), so I can't give a hard contributor count or commit
cadence — flagging that as UNVERIFIED. From the on-disk signals, the single-maintainer risk reads as
**moderate, and well-mitigated on the content side, under-mitigated on the mechanism side**:

- *Mitigated:* the daily source-monitoring / blog-RSS / link-checker workflows automate the "did
  something upstream change" watch, so currency of *inputs* doesn't depend on the maintainer
  remembering to check. The retirement-lane discipline and the per-doc `revalidate-by` dates mean the
  content has a built-in decay clock.
- *Under-mitigated:* the two highest-leverage correctness mechanisms are not actually enforced. The
  revalidation automation is pointed at a dead directory (finding 1), and the signal-sync invariant
  that keeps the audit honest is documented-but-not-implemented (finding 6). Both are the kind of thing
  that only one person knows is load-bearing, and both fail silently. The PLAN.md "Next Review" block is
  a single dense paragraph of carry-forward items in one person's working voice — legible to the author,
  opaque to a successor. There is no LICENSE and no named author (finding 4), which are small but real
  hand-off frictions for a public repo.

The honest summary for this lens: the repo is *content-current* and *not meaningfully wrong in its
claims* as of 2026-06-21 — the maintainer has kept the routed docs fresh. Where it is wrong is in its
machinery (a daily cron enforcing nothing) and its meta-docs (ARCHITECTURE two versions behind), and
the bus-factor exposure is concentrated in exactly those un-enforced, un-documented mechanisms rather
than in the analysis itself.
