# Measurement session 2026-07-18 — reverification sweep, MCP token-economics wire re-measure, realistic-prose adherence ladder

**Session**: 2026-07-18, Claude Code harness, main session on `claude-fable-5`, ultracode
(session effort xhigh). Three work streams, each two-lens adversarially verified
(confound + overclaim, default-refute) before recording; per-claim verdicts and the
corrections applied are summarized in each part's verification trail. Instruments archived
under `research/artifacts/2026-07-18-mcp-wire/` and
`research/artifacts/2026-07-18-realistic-ladder/`. Continues the probe program recorded in
[fable-probe-session-2026-07-16.md](fable-probe-session-2026-07-16.md).

---

## Part 1 — Web reverification sweep

Five parallel research agents (Workflow spawn path — acceptable here because no claim
depends on which model served them) checked: the two lapsed OWASP-survey rows in
mcp-patterns.md, the Playwright CLI 114K/27K figure, long-context benchmark coverage of
Opus 4.8/Claude 5, the tracked academic follow-ups, and vendor currency. Draft claims
C1-C8 went through both lenses; no claim was refuted outright, but the lenses found two
outright factual errors in my drafts (the C5 session-server miscount and the
"default since v2.1.121" version peg — the changelog puts tool-search auto mode default-on
at v2.1.7, with per-server `alwaysLoad` at v2.1.121; the repo's own stale-flags carried the
same wrong peg and were corrected this session) plus tier-discipline and superlative
corrections. Everything below is the post-verification wording; the corrected claims were
applied to mcp-patterns.md, plugins-and-extensions.md, SOURCES.md,
model-migration-anti-patterns.md, and PLAN.md the same day.

Headline outcomes:

- **~43% command injection (lapsed 2026-03-20)** — reverified. Primary source was Equixly
  (2025-03-29, undisclosed N, Tier C; the "OWASP audit" and "Docker data" attributions were
  mis-citations via Nate B. Jones). Re-cited to BlueRock's MCP Trust Registry (2026-07-17
  product page, Tier C vendor scan, flag bias): 42% of 12,000+ scanned public servers —
  different population and method from Equixly, so context for the rate, not a replication.
- **"~10 of 5,960+ genuinely trustworthy" — withdrawn as never-a-measurement.** Provenance:
  the numerator was Jones's editorial aside ("spoiler: about ten", Tier D), the denominator
  PulseMCP's mid-2025 directory count. Mid-2026 listing counts: PulseMCP 22,300+ (verified
  2026-07-18), mcp.so ~20,222, Glama ~22,775, official registry 9,652 latest records at a
  2026-05-24 pull (dedup-dependent).
- **OWASP statuses**: MCP Top 10 still Phase 3 beta (MCP01:2025-MCP10:2025); third-party
  usage guide still v1.0 (2025-11-04). Beta note added at the doc's citation site.
- **Playwright 114K/27K "4x, measured, Microsoft" — unsupported.** Absent from the repo
  README (current and commit fa6f6bc, late Feb 2026) and playwright.dev docs; earliest
  pairing found is a 2026-02-24 Medium post asserting unlinked "Microsoft's benchmarks"
  (its author's own run: ~89K vs ~24K, ~3.7x); later sources cite it in a loop. One
  independent benchmark found (Outpost/Ranger 2026-04-03): ~2x tokens, MCP ~2x faster
  wall-clock. playwright-mcp v0.0.78 (2026-07-09, distilled snapshots) stales earlier
  MCP-side workflow measurements. Docs restated as community benchmarks, ~2-3.7x
  task-dependent, Tier C; the misapplied stale-flag on this figure (tool search defers
  definitions; CLI-vs-MCP cuts per-call output — orthogonal levers) removed.
- **MRCR carried item — closed as superseded.** Anthropic dropped MRCR after the Opus 4.7
  card; the 4.8 card (2026-05-28 §8.9) and Fable 5/Mythos 5 card (2026-06-09 §8.13) report
  GraphWalks with 256K/1M split (zero MRCR mentions, verified by direct grep of both PDFs).
  Mythos 5 (same weights as Fable 5 + blocking classifiers): BFS 91.1→79.4, Parents
  99.96→97.5 — shallowest Parents drop of the six tabulated models; on BFS, Mythos
  Preview's absolute drop is marginally shallower, so no across-the-board superlative
  (caught by the overclaim lens against the card's own Table 8.13.A). GPT-5.5 rows are
  Anthropic's amended scoring — attribute to the card, not OpenAI. No independent
  long-context coverage of 4.8/Claude 5 found as of 2026-07-18 (open residual).
- **Academic checks**: ACE = ICLR 2026 poster (2026-04-25), camera-ready retitled, 226
  S2-floor citations. Meta-Harness still v1 preprint (no ICML entry; watch NeurIPS 2026).
  MCE (arXiv:2601.21557 — ID verified against the abs page this session) registered Tier B
  preprint-with-claimed-venue: the ICML 2026 tag is the authors' own, the abstract reports
  5.6-53.8% relative over agentic-CE baselines (mean 16.9%); the repo-README
  "+18.4%/+33.0% over ACE" numbers are against the authors' own ACE reimplementation,
  unverified.
- **Vendor currency**: Claude Code 2.1.214 (npm 2026-07-18); tool search default-on
  unchanged; 2.1.212 MCP auto-background >2 min + session caps + Task-mode deprecation;
  2.1.214 permission-hardening batch. anthropic.com/engineering's newest post remains
  2026-04-23; claude.com/blog is where Claude Code posts now appear — its 2026-07-16
  migration post (rulebook-first, small-model implementers + large-model reviewers,
  verification loops) registered Tier A with a self-reported-practices note, and added as a
  third convergence exemplar on model-migration-anti-patterns.md.

**Verification trail (batch 1)**: confound lens — C2/C3/C8 SURVIVES, C4 survives with
carried qualifiers, C1/C5/C6 SURVIVES-IF-WEAKENED, C7's MCE element near-refuted as
drafted (venue + delta sourcing); it independently re-fetched BlueRock, Equixly, the
playwright-cli README, PulseMCP, the OWASP index, the migration post, and the arXiv page,
re-derived the C5 arithmetic, and grepped the local system-card texts. Overclaim lens — no
FAILs; C3 PASS; the rest PASS-WITH-CORRECTIONS with lift-ready strictest wordings (applied
verbatim where possible): "refuted"→"withdrawn as never-a-measurement",
"wrong"→"unsupported", "~2-4x"→"~2-3.7x measured", the C6 superlative scoped to Parents,
BlueRock held at Tier C per the repo rubric, the migration post graded A per the rubric's
direct-from-Anthropic line with the bias note explicit. Batch-level lesson both lenses
converged on: the errors lived in my claim-file compression, not the underlying agent
reports — quote the reports' hedges forward instead of re-summarizing them.

---

## Part 2 — MCP token-economics wire re-measure

**Instrument** (`research/artifacts/2026-07-18-mcp-wire/`): raw JSON-RPC over stdio —
initialize, initialized, `tools/list` — against locally-configured MCP servers; the
`tools/list` result is the schema payload a static-loading client embeds at session start.
Estimator: chars/4 over the raw JSON (a floor — schema-dense JSON likely tokenizes denser,
and the harness adds `mcp__server__` prefixes and rendering framing). A first attempt to
measure schemas from a ToolSearch-loader agent's transcript failed informatively: the
transcript records ToolSearch results as metadata (`matches` + query) only — the injected
schema text is not persisted — so transcript accounting cannot measure schema size.

**Results (2026-07-18, versions unpinned via uvx/npx, single-day snapshot)**:

| Server | Tools | tools/list JSON | est. tokens (chars/4) | Notes |
|---|---|---|---|---|
| workspace-mcp (`gworkspace`) | 51 | 115,062 chars | ~28.8k | input schemas 66% of payload; `batch_update_doc` alone 23,602 chars ≈ ~5.9k |
| @playwright/mcp@latest | 24 | 19,433 chars | ~4.9k | measured out-of-session as a stand-in for the doc's "~20K" table row |
| best-practices (project .mcp.json) | — | — | — | failed to launch: config pointed at a venv deleted when the server was archived (dangling entry removed from `.mcp.json` this session) |

Deferred-loading comparison: the session itself carried **82 MCP tool names** (5 servers:
gworkspace + 4 claude.ai-hosted — Gmail 13, Calendar 8, Drive 8, Mermaid 2) at ~3.6k chars
≈ **~0.9k est. tokens** names-only. Scope: 1 of the session's 5 servers was
wire-measurable; the 4 claude.ai-hosted ones were not. The measured gworkspace instance's
51-tool set matches the session's deferred name list exactly, which is what licenses it as
the session stand-in.

**Recorded implications** (applied to mcp-patterns.md and plugins-and-extensions.md):
the valgard 81,986-token figure is a historical static-loading data point; the "~20K
Playwright MCP" row is superseded (not "drifted" — it never had a stated version, tool
count, or tokenizer); schema cost concentrates heavily in a few complex tools; the
H-MCP-CONTEXT-01 89%-reduction claim is directionally supported, not re-measured.
Version pegs corrected repo-wide: auto mode default-on v2.1.7 (10%-of-context threshold),
`alwaysLoad` v2.1.121, Vertex default-off v2.1.119.

---

## Part 3 — Realistic-prose adherence ladder (the durable open item from the Fable probe program)

### Instrument

`research/artifacts/2026-07-18-realistic-ladder/` — built to the spec left by the
2026-07-16 adversarial verdicts: realistic rule diversity, no numbered-block scaffolding, a
positive control (the prior ladders never demonstrated they could detect failure), rungs
past 150, and a same-instrument Opus comparison arm.

- **Task**: implement `lumen`, a small stdlib-only CSV summary CLI, plus README.md and
  CHANGELOG.md, in an assigned output directory. Same functional prompt in every arm.
- **Fixture**: a "Lumen contributor guide" rendered as unnumbered flowing prose across 9
  topical sections (seeded sentence shuffling within sections, 2-3 phrasing variants per
  rule), from a 200-rule bank across 12 mechanically-checkable types (terminology 13,
  required-content 26, readme-structure 15, markdown-style 15, prose-style 7,
  python-naming 10, python-idiom 19, python-structure 7, cli-behavior 8, changelog 9,
  word-ban 68, file-inventory 3). Tokens legislated by the inherited global CLAUDE.md were
  deliberately avoided (the 2026-07-16 literalization confound); semicolon rules avoided
  (the 2026-07-16 scoring-artifact lesson). Rungs strictly nested: 25 ⊂ 50 ⊂ 100 ⊂ 200.
  Guide sizes ~750/1,084/1,824/3,370 est. tokens — single Read call each; this is an
  in-context adherence measure, not a long-context one.
- **Controls**: (i) baseline arms — same task, no guide, n=3 per model, scored against the
  full bank → per-rule spontaneous compliance; pre-registered informative criterion:
  satisfied in ≤2 of the 6 pooled baseline runs. (ii) golden fixture — a hand-built
  deliverable set scoring 199 SAT + 1 NA (`md-ordered-paren`, conditional on an ordered
  list the fixture lacks), constructively demonstrating 199 rules jointly satisfiable in
  one artifact (the 200th exhibited only vacuously) and that the checker does not
  false-positive on this compliant fixture.
- **Arms**: fable (main-loop Agent spawns, default model) and opus (`model: "opus"`), 3
  reps × {baseline, K25, K50, K100, K200} each = 30 agents, same day (15:37-15:55Z), same
  prompts modulo guide/outdir. Per-turn served-model gate + guide-Read gate + no-compaction
  gate from transcripts (`gate_ladder.py`); scoring mechanical (`score_ladder.py`);
  pre-registered aggregate (`aggregate_ladder.py`).

### Runs, gates, exclusions

All 15 fable transcripts all-turns `claude-fable-5`; all gated opus transcripts all-turns
`claude-opus-4-8`; `"effort":"xhigh"` on every turn checked in both arms (session-inherited
— the Agent tool has no effort override). Three opus reps terminated early on a session
usage limit ("resets 4pm America/New_York"), each with a single `<synthetic>` terminal turn
in the transcript, clustered 15:54:50-15:55:06Z: **opus-K200-r2/r3** died before writing
CHANGELOG.md (excluded — incomplete deliverables) and **opus-K100-r2** completed all three
files but never finished its run (excluded from headline Ns, reported as supplementary; it
scored identically to its gated siblings). Headline Ns: fable 3/rung; opus 3/3/2/1 at
K25/K50/K100/K200.

### Results (final adjudicated scoring)

| Arm | K25 | K50 | K100 | K200 |
|---|---|---|---|---|
| Fable 5 | 1.0, 1.0, 1.0 | 1.0, 1.0, 1.0 | 1.0, 1.0, 1.0 | 1.0, 1.0, 1.0 |
| Opus 4.8 | 1.0, 1.0, 1.0 | 1.0, 1.0, 1.0 | 0.979, 0.979 (+r2 suppl. 0.979) | 1.0 (n=1) |

Adherence = SAT/(SAT+VIOL) over the rung's informative rules (78/200 informative; core-25
24/25 — `prose-no-contractions` spontaneously satisfied 6/6 at baseline). Raw unfiltered
adherence shows the same picture (fable 12/12 at 1.0 raw — the ceiling is not
filter-manufactured). Baseline runs violate a mean of ~79 rules each (89 violated by ≥1
run, 65 by all six); the informative-set size of 78 coincides with the per-run mean by
accident, not construction.

The **only** surviving informative-rule violation in the gated data: `content-stdlib` at
opus K100 — the guide sentence "The phrase standard library only appears in the README."
— which all three opus K100 reps paraphrased ("uses only the Python standard library",
"draws only on the Python standard library" / "standard library alone", "standard library
alone") while all twelve fable treatment reps and the golden fixture render the literal
phrase, and opus K200 rendered it literally in 3/3 attempts (1 gated + 2 excluded).

### Adjudication and amendments log

Six checker amendments, each individually recorded, each judged prose-faithful (score the
rule as written, not the regex's literalism), each applied symmetrically via the single
shared checker with all arms re-scored under the final version: (1) nested-paren `round`
pattern; (2) f-string inner-quote tokenization (Py3.12); (3) wrapped-phrase normalization
for required phrases — *required* for joint satisfiability, since `md-line-length` forces
wraps that can split phrases, so the bank's "conflict-free by construction" comment was
false in rendered form until this amendment; (4) epilog-URL constant indirection; (5)
round-to-4 constant indirection; (6) `content-issue-first` clause reorder (the rule prose
never demanded an ordering). Symmetry held in effect, not just letter: (3) and (4) rescued
*fable* SATs (11/12 fable reps interpolate a URL constant into the epilog; fable's
required phrases were hard-wrapped), (1), (5) and (6) rescued opus.

**The adjudication that decides the headline, disclosed per the confound lens**:
`content-stdlib` was held to the strict-verbatim reading while six other regex-vs-prose
gaps were liberalized. The strict reading is defensible ("The phrase … appears" points at
a specific string) but it is an adjudication, and four things make the sentence
contestable: it lacks the "in exactly those words" rider its sibling rules carry; the
section lead the agents read says "verbatim or nearly so"; the unquoted sentence is
syntactically ambiguous; and the task prompt itself plants the competing phrasing ("use
only the Python standard library"), which opus-K100-r1 near-echoed. Under the lenient
adjudication, opus is 1.0 everywhere gated and the instrument discriminates nothing.

### Strictest surviving wording (what the docs may cite)

1. **Instrument**: failure-capable in both directions on this fixture (golden 199 SAT +
   1 vacuous NA; baselines violate ~79 rules/run), realistic-diversity, unnumbered prose,
   nested rungs past 150, same-instrument two-model design — the three items the
   behavioral-insights re-measure flag demanded, plus the positive control and
   no-scaffolding items from the wider 2026-07-16 adversarial record. 1.0 on this
   instrument means adherence to the checker's reading of 200 surface-checkable
   constraints on one small greenfield task under verify-and-fix behavior at xhigh —
   semantic, conditional, and genuinely conflicting rules are outside its reach.
2. **Fable 5**: descriptive ceiling — 12/12 gated treatment reps at 1.0 (raw and
   informative) at every rung through 200 realistic-diversity rules. No Fable failure
   observed; the cap for realistic instructions remains unlocated; this neither
   replicates, bounds, nor refutes the Opus-era ~150 figure.
3. **Between-model observation**: the program's first sub-ceiling score on any
   adherence-ladder instrument, and its first same-instrument between-model score
   difference — but it is **adjudication-dependent literalization discrimination, not an
   adherence miss simpliciter**: under the strict-verbatim reading of one ambiguous rule
   sentence, fable rendered the mandated phrase 6/6 times (K100+K200) where opus rendered
   it 0/3 at K100 and 3/3 at K200; under the lenient reading both models are at ceiling
   everywhere gated. Consistent in direction with the 2026-07-16 emphatic-literalization
   finding (Fable enforces named tokens harder than the prose strictly requires). One
   rule, one rung, n tiny, K confounded with rendering (each rung's guide is one
   seed-locked rendering, so sentence-adjacency effects cannot be separated from load) —
   NOT a cap observation, NOT a model ranking.
4. **Conditions**: xhigh effort both arms (config-asserted; per-turn `effort` field
   confirmed in spot-checked transcripts); verify-and-fix interaction style in both arms
   with an asymmetric profile (opus 3-13 pre-final text blocks vs fable 1-5; the lone
   clean opus K200 rep is also the heaviest fix-loop profile in the run — 45 turns, 8 file
   writes); informative set is session-relative (agents carry the inherited global
   CLAUDE.md); anaphora defect (two rules' sentences can lose their antecedent under
   shuffling; one opus agent explicitly flagged and sensibly resolved the resulting
   contradiction); three opus reps lost environmentally (timeline analysis refutes a
   throttling-degradation rival: the longest opus run finished clean four minutes before
   the first termination, and the dying reps had written the contested phrase correctly).
5. **Guide provenance**: the on-disk guides were regenerated after the runs (checker-spec
   edits re-ran the generator); the confound lens extracted the guide text from the
   Read-tool results embedded in four transcripts (one per rung) and diffed — byte-identical
   in all four cases. Recorded here because the archive alone does not prove what the
   agents read; `research/artifacts/2026-07-18-realistic-ladder/PROVENANCE.md` carries the
   check.

### Verification trail (batch 2)

Confound lens: L2 and L4 SURVIVES as written (it re-ran the scorer on golden,
fable-K100-r1, opus-K100-r1 with zero disagreement; re-parsed all 30 transcripts with its
own parser and matched the gate exactly; performed the guide-provenance repair above;
refuted the throttling rival on the timeline; audited all six amendments for symmetry in
effect and the filter for ceiling-manufacture — only 3/78 informative rules sit at the 2/6
borderline, no treatment violation anywhere was hidden by the filter); L1/L3/L5
SURVIVES-IF-WEAKENED with the content-stdlib adjudication disclosed and "verbatim
phrase/sub-ceiling adherence" reworded to adjudication-dependent literalization
discrimination — applied above. Overclaim lens: no FAILs; every load-bearing numeric
(199+1, 78, 24/25, 12/12, 3/3, 2/2+suppl., n=1 K200, single-rule miss) re-derived exactly;
both L3 superlatives rescoped (applied); the "~78" disambiguation, vacuous-NA calibration,
pre-registration scope (criterion pre-fixed; realized set computed under the final
amended checker), and the L4 additions (interaction asymmetry, synthetic-turn gate
mechanism, strict nesting) all applied above.

### Replacement reps (same day, evening wave) — the three environmental losses re-run

The three usage-limit casualties were re-run after the 4pm ET reset as opus-K100-r2b,
opus-K200-r2b, opus-K200-r3b (evening wave, ~18:30-18:45 ET, ~7h after the morning wave,
**opus-only** — no contemporaneous fable reps exist to control a wave effect). All three
gate PASS (all-turns claude-opus-4-8, guide read, zero compaction). Fixture identity for
both waves is certified by transcript-extracted Read results
(`research/artifacts/2026-07-18-realistic-ladder/guides-as-read/`, byte-identical in all
checks) — necessary because the on-disk guides were regenerated twice after the runs by
checker-spec edits re-running the seeded generator.

With the replacements, the opus arm reaches n=3 gated at every rung, with the K100 and
K200 cells wave-mixed (2 morning + 1 evening; 1 morning + 2 evening): 1.0 at K25/K50/K200
and 46/47 (0.979), 46/47, 1.0 at K100. Fable remains 12/12 at 1.0. The K200 1.0 depends on
**checker amendment 7** for one rep: r3b returns `STATUS_MISSING = 2` on OSError,
satisfying the rule as written ("A missing or unreadable source table exits with status 2"
— a behavior statement; the guide separately establishes `run`'s int return as the process
exit status) though not the original regex. Same indirection class as the prior
amendments; the confound lens's exhaustive flip-scan across all 33 outdirs plus golden
found exactly three rule-level flips (opus-K200-r3b, and fable-K50-r2/opus-K50-r2 in
unselected cells — direct proof the amendment class rescues fable code just as readily),
no baseline flips, informative set unchanged at 78, golden unchanged. Disclosures: the
amendment was triggered by and only benefits an opus artifact (symmetry held but had no
bite), and without it r3b would post a second sub-ceiling opus observation (77/78); this
is also the seventh SAT-direction liberalization while content-stdlib remains the sole
strict-reading VIOL-direction call — the asymmetry-of-scrutiny disclosure gains a data
point.

The `content-stdlib` paraphrase is confined to the morning K100 wave (3/3 including the
supplementary rep); the single evening K100 replacement rendered the phrase literally —
a word-order variant of the morning sentence ("uses the Python standard library only" vs
morning's "uses only the Python standard library"), from the rep with the arm's heaviest
verify-and-fix telemetry (39 turns / 4 writes / 13 pre-final text blocks vs 19-22 / 3 / 6
for the morning gated reps), so extra fix cycles rival wave/timing as the explanation, and
at n=1 the data cannot distinguish wave-linked serving drift from sampling variance of a
stable propensity (morning 0/3 literal is unremarkable at a ~0.4 literal rate). Either
way the rung-linked reading is dead: K200 rendered the phrase literally 3/3 across both
waves (and the morning K200 casualties' partial artifacts agree with their replacements —
no selective-rerun bias signature). Gated literal-phrase rendering stands at **fable 6/6
vs opus 4/6**; the between-model observation is smaller in point estimate and no longer
uniform within the rung (2/3 gated K100 reps vs the original 3/3).

**Framing correction (overclaim lens, superseding the compressed "adjudication-dependent"
phrase above where they conflict)**: two different adjudications are in play and the
record keeps them separate. The difference that survives scoring exists only under the
strict-verbatim *interpretation* of the ambiguous rule sentence (contestable: no exactness
rider, "verbatim or nearly so" section lead, prompt-echo interference) — but *within* that
interpretation it is not a checker artifact, because no prose-faithful amendment can
rescue a missing required phrase. What amendment 7 makes adjudication-dependent is the
opus arm's 1.0 at K200, not the existence of the between-model observation. Cite it as an
interpretation-dependent literalization-propensity difference that is
checker-artifact-robust.

**Verification trail (addendum)**: both ladder lenses were resumed with context intact.
Confound: items 1-3 SURVIVES (scores, gates, and tallies independently re-derived;
amendment-7 flip-scan by exhaustion; guides-as-read extraction), items 4-5
SURVIVES-IF-WEAKENED (no wave-effect insinuation; fable-has-no-evening-arm and
double-regeneration provenance disclosures) — applied above. Overclaim: (a) numerals PASS
with the 46/47 precision upgrade, (b)-(c)-(e) PASS-WITH-CORRECTIONS (word-order variant +
fix-loop telemetry riders; "smaller in point estimate and no longer uniform"; wave-mixed
cells + amendment-7 dependence of the K200 1.0), (d) amendment 7 prose-faithful PASS, and
the compressed "adjudication-dependent difference" phrase FAILED as worded — replaced by
the framing correction above.

### What stays open

Locating an actual Fable failure region on realistic instructions — the residual
open item (PLAN.md row 39). The instrument now demonstrably registers model-level
differences, but a Fable cap needs a design Fable can fail at this measurement's
conditions: candidates from this session's evidence — genuinely conflicting or semantic
rules (outside the current checker's reach), one-pass/low-effort regimes (the ceiling here
includes verify-and-fix at xhigh), multiple renderings per rung (to unconfound adjacency),
and distractor load.

---

## Standing lessons (adds to the 2026-07-16/17 instrument rules)

1. Transcript `toolUseResult` for ToolSearch records matches only, not the injected
   schemas — schema-size measurement needs the wire (`tools/list`), not transcripts.
2. Model-specific usage limits can kill one arm of a two-model design mid-run; the
   termination appears as a `<synthetic>` turn (which the per-turn served-model gate
   already catches). Schedule the non-default-model arm first, or check limit clocks.
3. Regenerating a seeded fixture after post-run checker edits silently breaks archive
   provenance — either freeze fixture files at run time or record a transcript-vs-archive
   identity check (done here; see Part 3 §5).
4. Verbatim-phrase rules need an explicit exactness rider in the fixture prose, or the
   strict scoring is an adjudication — write "in exactly those words" on every
   phrase-literal rule in future banks.
5. Claim-file compression is where wording errors enter — carry raw-report hedges forward
   verbatim into draft claims (both batch-1 lenses independently localized every factual
   error to the compression step, not the reports).
