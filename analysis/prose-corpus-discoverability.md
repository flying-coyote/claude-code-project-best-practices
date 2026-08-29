---
version-requirements:
  claude-code: "v2.1.0+"
version-last-verified: "2026-08-28"
measurement-claims:
  - claim: "External 703-file / 6.07M-word prose vault following published Claude Code advice measured 12 files reachable by link from any entry point a session loads, while type coverage sat at 96% and the health check reported green after all 191 commits"
    source: "Contributor-reported three-day production run; not independently reproduced"
    date: "2026-08-28"
    revalidate: "2027-02-28"
  - claim: "This repository: 169 of 181 markdown files (93.4%) reachable from the auto-loaded entry point. Decomposed by lane with the generated INDEX.md excluded — the only reading that means anything — guidance prose is 50 of 50 (100%), while mechanism (2/16), data (1/14) and scratch (2/4) are link-unreachable by design. On currency, of 96 archive/ files 12 correctly declared themselves superseded, 17 asserted a live status in their own frontmatter, 67 said nothing; the 17 plus three executable v1 prompts were corrected (taking the lane to correct=31 WRONG=0 absent=65), and a follow-up commit the same day marked the remaining 65 silent files, so the instrument reports correct=96 (100%) WRONG=0 absent=0 as of 2026-08-29"
    source: "Direct measurement, scripts/measure-link-reachability.py, with determinism regression test scripts/test-measure-link-reachability.py"
    date: "2026-08-28"
    revalidate: "2027-02-28"
status: EMERGING
last-verified: "2026-08-28"
evidence-tier: Mixed
convergence: single-source
applies-to-signals: [corpus-unreachable-docs, corpus-unmarked-supersession, md-corpus-large, md-corpus-very-large, project-type-docs, project-type-research]
revalidate-by: 2027-02-28
---

# Prose Corpus Discoverability: Why "Claude Can Figure It Out" Is a Code Assumption

**Evidence Tier**: Mixed (A–B) — direct instrumented measurement of this repository (Tier A, reproducible from a clean checkout) plus one contributor-reported production vault (Tier B, single practitioner, not independently reproduced).

## Purpose

This document identifies a specific assumption inside Claude Code context guidance, states the class of project where it does not hold, and supplies an instrument that turns the resulting failure from a matter of taste into a measured number. It is for anyone whose project's primary artifact is prose — a documentation set, a research vault, an analytical corpus, a decision log — rather than code.

---

## Core Problem: the assumption is derivability, not a single loading surface

It is tempting to read the failure below as "the advice assumes everything must fit in CLAUDE.md." That reading is wrong, and worth discarding early. First-party guidance plainly describes a multi-surface loading model: `@` imports, subdirectory `CLAUDE.md` files loaded on demand, path-scoped rules, skills that load when a task matches, and — since the Claude 5-generation context-engineering guidance — progressive disclosure by name (Tier A — Anthropic, ["The new rules of context engineering for Claude 5 generation models"](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models), 2026-07-24; see [`claude-md-progressive-disclosure.md`](claude-md-progressive-disclosure.md) for this repo's sourcing caveat on that post). Nobody is being told to put everything in one file.

The assumption that actually carries the weight is about **the unloaded remainder**. The guidance's own exclude column reads *anything Claude can figure out by reading code*, and its discovery model is *let Claude fetch what it needs*. Both sentences assume the remainder is **derivable on demand** — that not loading something is safe because it can be found when required.

Derivability holds for code, for three reasons that are properties of code rather than of the agent:

| Property of code | Consequence for discovery |
|---|---|
| Identifiers are unique tokens | `grep` on a symbol finds every definition and every use. Retrieval is *complete* with respect to the query. |
| Stale code fails loudly | A superseded function does not compile, fails its tests, or breaks its callers. Staleness is self-reporting. |
| Dead code is visibly dead | A module nothing imports is detectable by static analysis without reading it. Deadness is structural. |

**None of the three holds for prose**, and the second is the one that breaks the model:

> The discriminating property of a prose file is its **authority and currency**, and retrieval cannot see either. A superseded document stays well-formed. It matches a query exactly as confidently as the document that superseded it. Nothing in its text degrades.

A retired code path announces itself by failing. A retired paragraph reads like advice. So for a prose corpus, discovery cannot be delegated to search-on-demand the way it can for code: the **explicit pointer graph** (can a session get here?) and the **in-file currency marker** (should it believe what it finds?) *are* the discovery mechanism, not a nicety layered on top of one.

Both are measurable. That is the contribution.

---

## Relationship to Prior Art in This Repository

This corpus already carries the *structural* insight, twice, at two other scales. Stating that plainly is the point: what follows is a third instance and an instrument, not a new idea.

| Existing doc | What it already says | Scale | What it does not say |
|---|---|---|---|
| [`intent-alignment-audit.md`](intent-alignment-audit.md) | "you cannot grep for 'this glob points at the directory the project no longer means to use'"; drift is "*emergent with no error code* — there is no exception, no failing test, no red badge" | **mechanisms** (a glob, a permission, a doc count) | that the same blindness applies to *documents*, or why prose specifically is exposed |
| [`evidence-based-revalidation.md`](evidence-based-revalidation.md) | a `--divergence` report "flagging a *retired* value still presented as current on reader-facing 'product' surfaces" | **claims** (a generated number cited past its retirement) | that a whole *document* can assert a live lifecycle status it no longer has, and that nothing here checks for it |
| [`CONTRIBUTING.md`](../CONTRIBUTING.md) + [`DECISIONS.md`](../DECISIONS.md) | reachability as a hard invariant — "without this, the doc is unreachable by the audit prompt"; Decision 12 records a routing-invariant violation that left six docs unreachable by their declared signals | the **routing** edge (signal → doc) | the **reader's** edge (session → doc), which nothing measures |

The delta this document adds is three things and no more:

1. **The explanation.** The prior docs observe that certain failures have no error code. This names *why* prose has none where code does — the three self-reporting properties of code in the table above — which converts a set of local observations into a property you can predict from corpus type before you measure it.
2. **The instrument.** Reachability and currency-marking as measured numbers, with a committed script, rather than qualitative judgments.
3. **The self-audit result.** The 2026-06 self-audit found the freshness gate "scans a `patterns/` directory archived in the v2.0 reposition and reports all-clear while verifying the empty set." The finding below is the mirror image of that one and was still open: the expiry checker points *away* from `archive/`, so the lane guaranteed to hold stale prose is the lane no instrument reads.

---

## The Instrument

[`scripts/measure-link-reachability.py`](../scripts/measure-link-reachability.py) measures the first property; a frontmatter/banner scan measures the second. Full method and raw output: [`research/corpus-reachability-2026-08-28.md`](../research/corpus-reachability-2026-08-28.md).

**Reachability** is BFS over pointer edges from the entry points a session actually loads. Three modes, each strictly more generous than the last, so every figure is an *upper bound* on what a session would follow:

| Mode | Followable pointer |
|---|---|
| `links` | markdown links and `@` imports only |
| `refs` | + backticked and bare paths that resolve |
| `dirs` | + a directory mention expands to the files inside it |

Three entry tiers: `E1` auto-loaded (`.claude/CLAUDE.md` and root `CLAUDE.md`/`AGENTS.md`), `E2` + `.claude/` config surfaces, `E3` + `README.md`. **Report `E1/refs`** — E1 because that is what a session actually loads, `refs` because a corpus that points by backticked path (as this one does) is not broken, and strict link-mode would score it a false zero.

**Currency marking** is a *three-way* classification (`--currency`), not marked/unmarked. The first pass of this measurement used the binary test and got it wrong: seventeen files passed it while carrying a marker that said the opposite of the truth. Marker presence is not marker correctness.

| Verdict | Meaning |
|---|---|
| `correct` | declares itself superseded — a dead `status:` value or a supersession banner |
| `WRONG` | asserts a **live** status while sitting in a dead lane — worse than silence, because it defeats the check a careful reader runs |
| `absent` | says nothing either way |

---

## Measured: two corpora, failing on opposite axes

| | External vault | This repository |
|---|---|---|
| Files | 703 markdown, 6.07M words | 181 markdown |
| Session under measurement | 359,985 words, 191 commits | — |
| **Reachable from session-loaded entry points** | **12 of 703 (1.7%)** (reported) | 169 of 181 (93.4%) (measured) |
| — guidance prose only, generated index excluded | not reported | **50 of 50 (100%)** |
| Frontmatter `type:` coverage | 96% | — |
| **Dead-lane files correctly declaring supersession** | not measured | **12 of 96 (12%)** |
| **Dead-lane files asserting a LIVE status** | not measured | **17** |
| **Dead-lane files silent either way** | not measured | **67 of 96 (70%)** |
| Project health check / lint | green after all 191 commits | green |

**Read the two columns as different kinds of evidence, not as one comparison.** They did not come from the same instrument. The vault's 12 is contributor-reported from a three-day production run, was not produced by this instrument, and is **not independently reproduced here** — it is one unverified number. The repository column is measured by the committed instrument and reproduces deterministically. Placing them in adjacent columns is a presentational convenience that overstates their comparability; the honest form of the contrast is *"a corpus can score near-zero on this property while every other health signal reads green"*, for which the vault is an existence claim and this repository is the worked measurement.

The two rows that matter are the last two. **Every conventional health signal was green on both corpora, and both corpora had a real defect**, because neither signal measures either property. A green lint on a prose corpus tells you the markdown parses.

### What the repository got right, and it is not writing style

93.4% reachability is not an accident of careful prose. It is produced by three *maintenance instruments*, and a project without them will not reproduce the result no matter how well it writes:

| Mechanism | Effect on the pointer graph |
|---|---|
| [`INDEX.md`](../INDEX.md) | generated full inventory, auto-regenerated by the `PostToolUse` hook — one reachable file that link-reaches everything |
| [`AUDIT-CONTEXT.md`](../AUDIT-CONTEXT.md) | signal → doc routing map; a routing row is **mandatory** in the CONTRIBUTING integration checklist |
| [`ABSORPTION-MAP.md`](../ABSORPTION-MAP.md) | one row per routable doc |

The repository already treats reachability as a hard invariant *in one graph*: CONTRIBUTING states that without an `AUDIT-CONTEXT.md` row "the doc is unreachable by the audit prompt," and DECISIONS records a routing-invariant violation that left six memory-archetype docs unreachable by their declared signals. This document generalizes that invariant from the routing edge to the reader's edge, and supplies the *why* — the code/prose asymmetry — that makes it a general property rather than a local rule.

### What the repository got wrong

Twelve of 96 files in the dead lane correctly declared themselves superseded. Seventeen asserted the opposite. Sixty-seven said nothing:

```
$ python3 scripts/measure-link-reachability.py --currency
archive/  n=96   correct=12 (12%)   WRONG=17   absent=67
```

Meanwhile all 25 live `analysis/` docs carry `status:` and `last-verified:`, and 21 carry a collapse banner. **The discipline exists and is applied rigorously — to the lane that needs it least.** Two worked collisions:

- `archive/patterns-v1/progressive-disclosure.md` carries `status: "PRODUCTION"`, `last-verified: "2026-02-16"`, and a `measurement-claims` block asserting "Token savings: 50-77%" with an unexpired `revalidate: 2026-11-01`. It is a `grep` hit for "progressive disclosure" alongside the live [`claude-md-progressive-disclosure.md`](claude-md-progressive-disclosure.md) — though "alongside" undersells it: that query returns **34 files, 18 of them in `archive/`**, so the reader is not choosing between two candidates but filtering a crowd. Nothing in the returned text distinguishes them but the path.
- `archive/prompts-v1/AUDIT-EXISTING-PROJECT.md` is the *only* file in the repository matching "audit existing project". The live replacement, [`ONE-LINE-PROMPT.md`](../ONE-LINE-PROMPT.md), does not use that phrase. The obvious query returns exclusively superseded instructions, opening "Copy everything below the line and paste it into Claude Code."

The seventeen are corrected in this change (`status: ARCHIVED` plus a tombstone banner, matching the convention already used on the docs evicted in 2026-07), along with the three `archive/prompts-v1/` files that adversarial review identified as the highest residual severity — unmarked, 348–810 lines, and **executable** rather than descriptive. `--currency` reported `correct=31 WRONG=0 absent=65` at that point under the tightened banner test (25 by dead `status:`, only 6 by body banner). The 65 silent files were **not** fixed in that change and were left as the open item — the point of the measurement is the number, not the patch.

> **That intermediate figure held for about two hours.** A follow-up commit the same day (`2d5476a`) marked all 65, and the instrument has reported **`correct=96 (100%) WRONG=0 absent=0`** ever since. The `correct=31` number stood in five live locations for a day afterwards, phrased as what re-running *today* would report — including in this document, in its own frontmatter, and in the routing table that sends readers here. A doc about prose outliving its referent, outlived by its own headline number. Corrected 2026-08-29; the pre-fix state is reproducible from git.

The mechanism behind all of it splits in two, and the second half is the more useful finding.

**The currency checks are scoped to the live lane.** `markdownlint` excludes `archive` by glob; `check-measurement-expiry.py` defaults to `analysis`; the stop hook checks two root files' mtimes. Each exclusion is individually sensible — you do not lint a tombstone. The aggregate is that nothing checks whether the dead lane says it is dead. In a code project that lane self-reports; here it went unreported for the six months since the v2.0 repositioning moved those files.

**But the check that does cover everything fires into a void.** `.github/workflows/link-checker.yml` runs daily across *all* markdown, `archive/` included. It is not live-lane-scoped, and it works. As of 2026-08-28 the repository carries **916 open issues labelled `documentation`**; the ten most recent are the same auto-filed "🔗 Broken links detected" issue, one per day, **each with zero comments and no edit since creation**. Meanwhile 214 internal links stay dangling.

Two conclusions, and they generalize past this repository:

1. **A firing check is not a working check.** An alarm nobody can act on is, in outcome, indistinguishable from no alarm. This repo has diagnosed exactly this before — the 2026-07 reduction deleted the RSS and source-monitoring watchers because *"their GitHub issues sat unread — hundreds open, zero triage."* The link checker survived that cull and reproduced the failure.
2. **Link resolution and link authority are different questions, and only the first has a checker.** Whether a link resolves is a *mechanical* property — exactly the code-like property that survives translation to prose, which is why a checker for it exists and works. A link to `archive/patterns-v1/progressive-disclosure.md` resolves perfectly and goes green every day; the file it resolves to spent six months asserting `status: PRODUCTION`. No checker asked the second question because nothing framed it as a question.

---

## Diagnostic Framework

| Signal you can verify | Command | What it means | Remediation |
|---|---|---|---|
| Low `E1/refs` reachability on a corpus ≥50 files | `measure-link-reachability.py --entry E1 --mode refs` | Sessions cannot get to most of the corpus without already knowing it exists | Add a generated inventory *and link to it from the auto-loaded entry point*; add a routing map if the corpus is topic-routed |
| Entry point points by bare path only | `grep -c '](.*\.md)' .claude/CLAUDE.md` returns 0 | Recoverable, but strict link-checkers score it zero and link-rot goes undetected | Convert the resource map to markdown links; then link-checking works |
| A dead lane exists with no marker | `measure-link-reachability.py --currency` reports a high `absent` count | Superseded prose returns from search indistinguishable from live prose | Tombstone banner + `status: ARCHIVED` in every file in the lane |
| A dead-lane file asserts a live status | `measure-link-reachability.py --currency` reports `WRONG > 0` | **Severe.** Defeats the check a careful reader runs | Rewrite the status field to the dead value; the original stays in git history |
| Dead lane excluded from the currency checks | read the lint globs and script defaults | The lane most likely to rot is the lane nothing inspects | Keep the *style* exclusions; add a *currency* pass over the dead lane |
| A check fires on a cadence into an untriaged queue | count open auto-filed issues; check `comments` and `updated_at` on them | A firing check is not a working check — in outcome it equals no check, while reading as coverage | Make it block something, aggregate it into one standing issue, or delete it; an alarm nobody acts on is worse than none because it looks like coverage |
| Automated pointer enrichment emits non-resolving links | run a link checker over generated footers | The mechanism built to enrich the graph is degrading it | Emit paths relative to the containing file |

### Anti-Patterns

| Anti-Pattern | Symptom | Fix |
|---|---|---|
| Treating "let Claude fetch it" as sufficient for prose | Agent cites a superseded doc with full confidence and no hedge | Pointer graph + currency markers as infrastructure, not prose hygiene |
| Archiving by *moving* only | Path says `archive/`; file body and frontmatter still say live | Marker in the file, because retrieval returns the body, not the directory listing |
| Excluding the dead lane from all checks | Green lint, rotting archive | Split style checks (exclude) from currency checks (include) |
| Currency markers only on the lane that is already current | `analysis/` fully marked; 12 of 96 in `archive/` | Mark the lane that *needs* the marker |
| A link checker read as a discoverability check | green link check, superseded prose still returned as current | Link *resolution* is mechanical and checkable; link *authority* is neither. Check both, and do not let the first stand in for the second |
| A generated index counted as discoverability | 100% reachability, zero authority signal | Report reachability *and* marking; one without the other is theatre |

---

## Counter-Evidence / What This Does *Not* Mean

**This is not an argument that grep is weak, and it is not an argument against progressive disclosure.**

*Grep is genuinely strong, and this repo's own sources say so.* Sen et al. found grep generally yields higher accuracy than vector retrieval across agent harnesses (Tier B — [arXiv:2605.15184](https://arxiv.org/abs/2605.15184), already cited in [`memory-systems-archetype-a-curated-kb.md`](memory-systems-archetype-a-curated-kb.md)). Nothing here contradicts that. The claim is **orthogonal**: those results measure whether retrieval *finds* the relevant content, in corpora where the relevant content is not shadowed by a well-formed superseded twin. Authority-blindness is a different axis from accuracy. Grep can be the best available retrieval mechanism *and* be unable to rank two matching documents by currency — because currency is not in the text it searches.

*Path inference is a real mitigation, and it degrades gracefully rather than failing cleanly.* An agent seeing `archive/patterns-v1/` in a result may well infer supersession, which makes the hazard probabilistic rather than certain. But it depends on the directory being legibly named, and it does not survive the cases that matter: a root-level `SOURCE-REFRESH-2026-07-09-cowork.md` gives no lifecycle signal from its path; `drafts/` and `research/` are ambiguous by construction; and Collision B above returns a single hit whose path an agent has no live alternative to compare against.

*Reachability alone is a weak and gameable metric.* A reviewer took this repo to **100.0%** by appending *one line* of thirteen backticked paths to `.claude/CLAUDE.md` — a line no reader would ever act on. The metric is also **sign-inverted against its own thesis** (adding tombstones *raises* it), so hazard exposure is reported separately and never folded into the numerator, and seeds are excluded from it since they were loaded rather than reached.

*And the corpus-wide percentage was itself the metric's worst distortion — corrected 2026-08-28.* This document previously reported "**92 of 179 (51%)** excluding the generated inventory" and read it as *the corpus is well-indexed and about half-linked, which is the property that carries authority*. **That reading was wrong**, because a single denominator lumped together files with completely different reachability obligations. Decomposed:

```
E1/refs: by lane, index excluded — guidance 50/50 | mechanism 2/16 | data 1/14 | scratch 2/4
```

| Lane | Owes the reader a pointer? | Result |
|---|---|---|
| **guidance** — prose meant to be found and acted on (`analysis/`, root docs, research records) | **yes — this is the only lane where the number means anything** | **50 of 50, 100%** |
| **mechanism** — `.claude/` skills, commands, rules | **no.** The runtime loads these by its own rules; nothing links to a rules file and nothing should. Link-unreachable is the *correct* state | 2 of 16 |
| **data** — frozen fixtures and transcripts under `research/artifacts/` | no; reached through their own provenance file if at all | 1 of 14 |
| **scratch** — `drafts/` | no | 2 of 4 |

So every guidance document in this repository is reachable from the auto-loaded entry point **without** the generated index. The 51% was almost entirely harness config and frozen experimental data being scored against an obligation they do not have.

The instrument now prints this decomposition on every run. **Report the guidance lane, index excluded** — a corpus-wide reachability percentage is close to meaningless, and this document published one for a day. The general lesson is the one worth carrying: *a reachability metric needs a denominator built from files that actually owe the reader a pointer,* and a corpus that mixes prose, config, and data will flatter or damn itself at random depending on their ratio.

*Three of five realistic queries hit a **coverage gap wearing a currency-marking costume**, and marking harder makes those answers worse.* An adversarial pass ran five questions a user might actually ask this repo. For hooks, spec-driven development, and session learning, the archived file is not *competing* with live prose — it is the **only** prose. There is no `analysis/*hook*` doc at all. An agent that correctly reads `archive/`, correctly distrusts it, and stops is left with nothing, and is worse off than one that had read it. Currency marking is the right instrument only where a live alternative exists; where it does not, the honest marker says "uncovered", not "superseded" — which is why one banner added by this change was rewritten to say exactly that after the successor it named turned out not to cover the subject.

*And in this repository `archive/` is not a tombstone store at all.* Nine live files link into it across ~130 links, and [`orchestration-comparison.md`](orchestration-comparison.md) points at the archived spec-driven-development doc calling it "the foundational methodology underlying all of these." A lane that live docs cite as authoritative is load-bearing infrastructure that happens to live under `archive/`. That weakens "the dead lane is where stale prose is guaranteed to live" into something narrower and truer: *a lane excluded from the currency checks accumulates unverifiable claims, whether or not it is actually dead.* The instrument's own default of excluding `archive/` inherits this mistake and is documented as a limitation rather than a principle.

*The marker does not travel with the excerpt.* A banner at line 12 is invisible to a content grep that lands at line 30, which is the more common retrieval shape. Verified on three files after the remediation in this change: the returned lines carry no currency signal at all, and the only surviving discriminator is the path. Top-of-file marking fixes the whole-file read and does not fix the grep hit — so path legibility, not the banner, is doing most of the real work.

*Which narrows the hazard honestly.* The strong form — "retrieval surfaces superseded prose with full confidence and no distinguishing signal" — was true for the 17 files that asserted a live status and is now true for none. The residual is a path-visible, signposted archive whose real problem is that it is doing live work while excluded from every currency check. Severity: moderate, not high. The sharpest surviving instance is not prose at all but the three multi-hundred-line **executable** v1 prompts in `archive/prompts-v1/`, where acting on superseded content means pasting retired methodology into a live project — those are marked in this change.

*This does not generalize to code repositories.* A code project whose docs are a thin README is not exposed to this; the three self-reporting properties of code do the work. The finding is scoped to projects whose primary artifact is prose.

---

## Gaps

- **Gap: n=2 corpora.** One measured directly, one contributor-reported. This repo's own bar for Tier B is production validation across 3+ projects, so the doc ships `EMERGING` and `Mixed`, not `PRODUCTION`/`B`. **Needs**: the instrument run against at least one more large prose corpus, ideally one not authored by a contributor to this repository.
- **Gap: no calibrated threshold.** 1.7% is plainly bad and 93.4% is plainly fine; nothing here calibrates the middle, so the diagnostic table says "low" rather than naming a number. **Needs**: reachability distributions across ten or more prose corpora before any threshold is asserted.
### Naming a successor is the error-prone step, and single-pass judgment fails at it

Marking a dead lane is two jobs, and only the first is mechanical. Setting `status: ARCHIVED` is bookkeeping. Saying *what replaced it* is a research claim, and it is the one that goes wrong.

Measured while marking the 65 unmarked files here: agents mapped each archived file's subject, searched the live corpus, and proposed a successor. Every non-trivial claim then went to an independent adversarial pass instructed to refute it. **35 of 39 successor claims were overturned** — roughly 90%. One file survived as a clean `SUCCEEDED`. Twenty-four collapsed to genuine coverage gaps where no live doc covers the subject at all.

The failure mode is uniform: **topic adjacency read as coverage.** A doc named `plugins-and-extensions.md` looks like the successor to a skills-authoring guide until you grep it and find it kept only adoption evaluation and token economics, having handed authoring mechanics to first-party docs. An earlier pass in this same work made exactly this error unverified, pointing `session-learning.md` at `memory-system-patterns.md`, which contains none of its subject.

This matters beyond tidiness. A confident false successor is the hazard this document is about, wearing the fix's clothes: the reader follows the pointer, finds a live well-formed doc, and concludes the material is covered when it is not. It is strictly worse than leaving the file unmarked.

**The discipline**: never write "the live successor is X" from a single judgment. Grep the candidate for the archived doc's distinctive terms and require a hit, or write "nothing live replaces this." The honest banner for a coverage gap is *uncovered*, never *superseded* — and after verification, 46 of 96 files in this repo's dead lane needed exactly that wording.

- **Gap: currency marking presupposes a live alternative.** Where the archived doc is the only coverage, marking it correctly removes the agent's only source and makes the answer worse. This document has no principled way to tell a currency gap from a coverage gap, and the diagnostic table does not distinguish them. **Needs**: a companion check that asks, for each dead-lane file, whether any live doc covers its subject — cheap to approximate (successor named and topic-terms present in the successor), and the thing that would have caught the false successor pointer this change first introduced.
- **Gap: harm is argued, not measured.** The causal step — an agent retrieves superseded prose, and its answer is *worse* than it would have been — is demonstrated by construction (Collisions A and B) but never measured as an outcome. This is the weakest link in the argument and should be read as such. **Needs**: a paired eval — identical questions against the same corpus with and without supersession marking, scoring answer correctness — which is exactly the shape of instrument [`agent-evaluation.md`](agent-evaluation.md) describes.
- **Gap: currency correctness is only checkable where the lane contradicts the file.** `--currency` catches a `PRODUCTION` marker inside `archive/` because the *path* supplies ground truth. It cannot tell whether a `last-verified: 2026-08-13` on a live doc is honest, which is the larger and harder question. **Needs**: a marker-vs-content check — comparing a doc's asserted verification date against the last substantive edit to the claims it verifies.
- **Gap: the index-file confound is unquantified.** Reachability-via-generated-index and reachability-via-curated-pointers are counted identically, and they are not equally useful to a reader. **Needs**: a mode that reports reachability with the generated inventory excluded from the edge set.
- **Gap: entry-point definition is Claude-Code-specific.** `E1` encodes one harness's loading rules. DeepSeek Harness reads `AGENTS.md` and `CLAUDE.md` under a `maxBytes` budget that drops whole broader files (Tier A, verified 2026-08-19; see [`claude-md-progressive-disclosure.md`](claude-md-progressive-disclosure.md) § AGENTS.md Interop), so E1 is runtime-dependent. **Needs**: an entry-point profile per runtime before cross-harness comparison means anything.

---

## Related Analysis

- [`claude-md-progressive-disclosure.md`](claude-md-progressive-disclosure.md) — the loading-surface model this document takes as given, and the first-party progressive-disclosure adoption it builds on
- [`domain-knowledge-architecture.md`](domain-knowledge-architecture.md) — **the closest overlap in the corpus; read both.** Its § The Resource Map Pattern already owns the pointer half (*"a lightweight index that tells the LLM where to look, not what the answer is"*) and states the currency half (*"a presence-based resource map can't tell you which target has gone stale"*), and its § Typed Knowledge carries the OKF `type:` substrate. **The boundary**: that doc *prescribes* the resource map and asserts it goes stale; this one *measures* whether the map actually reaches the corpus and whether the files declare their own currency, and explains why prose specifically needs both where code does not. If you are designing the map, start there. If you are auditing whether an existing one works, start here
- [`memory-system-patterns.md`](memory-system-patterns.md) — the staleness failure mode for memory files; this is the corpus-scale analogue, and its "Derive from Code (Do NOT Save)" table is the derivability assumption stated explicitly for the memory layer
- [`memory-systems-archetype-a-curated-kb.md`](memory-systems-archetype-a-curated-kb.md) — typed frontmatter and the registry+guard hygiene layer; `type:` makes a corpus queryable, `status:` makes it trustworthy, and §A1b's 127-types drift is the same class of ungoverned-metadata failure
- [`intent-alignment-audit.md`](intent-alignment-audit.md) — RETHINK asks whether a mechanism still serves its intent; this asks whether a *document* still claims an authority it has
- [`evidence-based-revalidation.md`](evidence-based-revalidation.md) — revalidation dates are a currency marker; this measures their coverage rather than their expiry
- [`cross-project-synchronization.md`](cross-project-synchronization.md) — a portfolio multiplies entry points; per-repo reachability is the per-spoke instance of this measurement

---

## Sources

### Tier A (Primary / Direct Observation)

- **This repository, measured 2026-08-28** — 181 markdown files; **169 reachable** under `E1/refs` (93.4%); decomposed by lane with the generated index excluded, **guidance 50/50 (100%)**, mechanism 2/16, data 1/14, scratch 2/4; of 96 `archive/` files **12 correct / 17 WRONG / 67 absent** on currency marking; 1,318 internal links classified — after the 2026-08-28 repair: 1,224 resolve, **0 root-relative, 0 outside-repo, 0 dangling in the live lane**, 90 dangling in the dead lane (70 of which would need a successor judgment, not a rewrite) — link totals shift as these docs are edited, since they sit inside the corpus they measure, so read them against the commit. Instrument, test, and raw record: [`scripts/measure-link-reachability.py`](../scripts/measure-link-reachability.py), [`scripts/test-measure-link-reachability.py`](../scripts/test-measure-link-reachability.py), [`research/corpus-reachability-2026-08-28.md`](../research/corpus-reachability-2026-08-28.md).
  - **Reproducible, and that had to be earned.** The first figures published here came from a nondeterministic instrument (a set literal in `_resolve` let `PYTHONHASHSEED` decide which of two valid resolutions the BFS followed; repeated runs returned 168–171) against a stale corpus count that excluded this doc's own two files. Both are fixed and a regression test now runs the instrument under eight hash seeds, verified to fail against the pre-fix version. The episode is recorded rather than repaired silently because it is this document's own thesis one level up: an instrument that ran green and was not measuring what it claimed. See the correction notice at the top of the raw record.
  - **The 17 `WRONG` files are a historical measurement, already remediated in-tree.** They were corrected in the same change that published this doc, taking the lane to `correct=31 WRONG=0 absent=65`; a follow-up commit the same day marked the remaining 65, so `--currency` reports **`correct=96 (100%) WRONG=0 absent=0`** as of 2026-08-29. Anyone re-running it now and expecting 17 will find zero; the pre-fix state is reproducible from git at the parent of that commit.

- Anthropic — [CLAUDE.md best practices](https://code.claude.com/docs/en/best-practices), § "Write an effective CLAUDE.md" (the ❌ Exclude column) and § "Provide rich content" (the fetch-on-demand bullet), **verified 2026-08-28**. Source of the *anything Claude can figure out by reading code* exclude guidance and the *let Claude fetch what it needs* discovery model this document scopes. The guidance is about CLAUDE.md authoring and makes no claim about prose corpora; this document scopes its warrant rather than disputing it.
- Anthropic / Thariq Shihipar, ["The new rules of context engineering for Claude 5 generation models"](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) (2026-07-24) — progressive disclosure named as a recommended shift; the 80%-system-prompt-reduction claim. **Mirror-verified 2026-08-13, direct fetch blocked**; inherits the sourcing caveat recorded in [`claude-md-progressive-disclosure.md`](claude-md-progressive-disclosure.md).

### Tier B (Validated / Expert Practitioner)

- **External prose vault, three-day production run** — 703 markdown files, 6.07M words, 359,985 words added across 191 commits; 12 files reachable by link from any entry point a session loads; 96% frontmatter `type:` coverage; health check green after every commit. **One practitioner, one project, contributor-reported, not independently reproduced here.** Recorded at the same tier this repository gives other single-practitioner production evidence (cf. the project1 OKF case study in `memory-systems-archetype-a-curated-kb.md` §A1b).
- Sen, Kasturi, Lumer, Gulati, Subbiah, ["Is Grep All You Need? How Agent Harnesses Reshape Agentic Search"](https://arxiv.org/abs/2605.15184) (arXiv:2605.15184, 2026-05-14) — cited here as **counter-evidence**: grep generally outperforms vector retrieval across harnesses. Used to scope this document's claim to authority-blindness rather than retrieval accuracy. Preprint, not peer-reviewed.

### Tier C (Vendor-Published Standard)

- [Google Cloud — Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) — its sole required frontmatter field is `type:`. Relevant as a boundary: OKF standardizes what a note *is*, and deliberately leaves lifecycle to the producer. The vault's 96% `type:` coverage alongside 12-file reachability is a direct illustration that type conformance and discoverability are independent properties.

---

*Last updated: 2026-08-28 (initial).*
