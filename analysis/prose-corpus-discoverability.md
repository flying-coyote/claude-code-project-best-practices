---
version-requirements:
  claude-code: "v2.1.0+"
version-last-verified: "2026-08-28"
measurement-claims:
  - claim: "External 703-file / 6.07M-word prose vault following published Claude Code advice measured 12 files reachable by link from any entry point a session loads, while type coverage sat at 96% and the health check reported green after all 191 commits"
    source: "Contributor-reported three-day production run; not independently reproduced"
    date: "2026-08-28"
    revalidate: "2027-02-28"
  - claim: "This repository: 168 of 179 markdown files (94%) reachable from the auto-loaded entry point, but of 96 archive/ files only 12 correctly declared themselves superseded, 17 asserted a live status in their own frontmatter, and 67 said nothing"
    source: "Direct measurement, scripts/measure-link-reachability.py, reproducible from a clean checkout"
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
| Files | 703 markdown, 6.07M words | 179 markdown |
| Session under measurement | 359,985 words, 191 commits | — |
| **Reachable from session-loaded entry points** | **12 (1.7%)** | 168 (94%) |
| Frontmatter `type:` coverage | 96% | — |
| **Dead-lane files correctly declaring supersession** | not measured | **12 of 96 (12%)** |
| **Dead-lane files asserting a LIVE status** | not measured | **17** |
| **Dead-lane files silent either way** | not measured | **67 of 96 (70%)** |
| Project health check / lint | green after all 191 commits | green |

Vault figures are contributor-reported from a three-day production run and are **not independently reproduced here**; they are recorded at the tier this repo gives single-practitioner production evidence. Repository figures are measured here and reproduce from a clean checkout.

The two rows that matter are the last two. **Every conventional health signal was green on both corpora, and both corpora had a real defect**, because neither signal measures either property. A green lint on a prose corpus tells you the markdown parses.

### What the repository got right, and it is not writing style

94% reachability is not an accident of careful prose. It is produced by three *maintenance instruments*, and a project without them will not reproduce the result no matter how well it writes:

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

- `archive/patterns-v1/progressive-disclosure.md` carries `status: "PRODUCTION"`, `last-verified: "2026-02-16"`, and a `measurement-claims` block asserting "Token savings: 50-77%" with an unexpired `revalidate: 2026-11-01`. It is a `grep` hit for "progressive disclosure" alongside the live [`claude-md-progressive-disclosure.md`](claude-md-progressive-disclosure.md). Nothing in the returned text distinguishes them but the path.
- `archive/prompts-v1/AUDIT-EXISTING-PROJECT.md` is the *only* file in the repository matching "audit existing project". The live replacement, [`ONE-LINE-PROMPT.md`](../ONE-LINE-PROMPT.md), does not use that phrase. The obvious query returns exclusively superseded instructions, opening "Copy everything below the line and paste it into Claude Code."

The seventeen are corrected in this change (`status: ARCHIVED` plus a tombstone banner naming the live successor, matching the convention already used on the docs evicted in 2026-07; `--currency` now reports `correct=29 WRONG=0 absent=67`). The 67 silent files are **not** fixed and remain the open item — the point of the measurement is the number, not the patch.

The mechanism behind all of it is systematic, not sloppy: **every automated instrument in the repository is scoped to the live lane.** `markdownlint` excludes `archive` by glob; `check-measurement-expiry.py` defaults to `analysis`; the stop hook checks two root files' mtimes. Each exclusion is individually sensible — you do not lint a tombstone. The aggregate is that the one lane where stale prose is *guaranteed* to live is the one lane nothing inspects. In a code project the dead lane self-reports. Here it went unreported for the six months since the v2.0 repositioning moved those files.

---

## Diagnostic Framework

| Signal you can verify | Command | What it means | Remediation |
|---|---|---|---|
| Low `E1/refs` reachability on a corpus ≥50 files | `measure-link-reachability.py --entry E1 --mode refs` | Sessions cannot get to most of the corpus without already knowing it exists | Add a generated inventory *and link to it from the auto-loaded entry point*; add a routing map if the corpus is topic-routed |
| Entry point points by bare path only | `grep -c '](.*\.md)' .claude/CLAUDE.md` returns 0 | Recoverable, but strict link-checkers score it zero and link-rot goes undetected | Convert the resource map to markdown links; then link-checking works |
| A dead lane exists with no marker | `measure-link-reachability.py --currency` reports a high `absent` count | Superseded prose returns from search indistinguishable from live prose | Tombstone banner + `status: ARCHIVED` in every file in the lane |
| A dead-lane file asserts a live status | `measure-link-reachability.py --currency` reports `WRONG > 0` | **Severe.** Defeats the check a careful reader runs | Rewrite the status field to the dead value; the original stays in git history |
| Dead lane excluded from every automated check | read the lint globs and script defaults | The lane most likely to rot is the lane nothing inspects | Run *currency* checks over the dead lane even while excluding it from *style* checks |
| Automated pointer enrichment emits non-resolving links | run a link checker over generated footers | The mechanism built to enrich the graph is degrading it | Emit paths relative to the containing file |

### Anti-Patterns

| Anti-Pattern | Symptom | Fix |
|---|---|---|
| Treating "let Claude fetch it" as sufficient for prose | Agent cites a superseded doc with full confidence and no hedge | Pointer graph + currency markers as infrastructure, not prose hygiene |
| Archiving by *moving* only | Path says `archive/`; file body and frontmatter still say live | Marker in the file, because retrieval returns the body, not the directory listing |
| Excluding the dead lane from all checks | Green lint, rotting archive | Split style checks (exclude) from currency checks (include) |
| Currency markers only on the lane that is already current | `analysis/` 100% marked, `archive/` 31% | Mark the lane that *needs* the marker |
| A generated index counted as discoverability | 100% reachability, zero authority signal | Report reachability *and* marking; one without the other is theatre |

---

## Counter-Evidence / What This Does *Not* Mean

**This is not an argument that grep is weak, and it is not an argument against progressive disclosure.**

*Grep is genuinely strong, and this repo's own sources say so.* Sen et al. found grep generally yields higher accuracy than vector retrieval across agent harnesses (Tier B — [arXiv:2605.15184](https://arxiv.org/abs/2605.15184), already cited in [`memory-systems-archetype-a-curated-kb.md`](memory-systems-archetype-a-curated-kb.md)). Nothing here contradicts that. The claim is **orthogonal**: those results measure whether retrieval *finds* the relevant content, in corpora where the relevant content is not shadowed by a well-formed superseded twin. Authority-blindness is a different axis from accuracy. Grep can be the best available retrieval mechanism *and* be unable to rank two matching documents by currency — because currency is not in the text it searches.

*Path inference is a real mitigation, and it degrades gracefully rather than failing cleanly.* An agent seeing `archive/patterns-v1/` in a result may well infer supersession, which makes the hazard probabilistic rather than certain. But it depends on the directory being legibly named, and it does not survive the cases that matter: a root-level `SOURCE-REFRESH-2026-07-09-cowork.md` gives no lifecycle signal from its path; `drafts/` and `research/` are ambiguous by construction; and Collision B above returns a single hit whose path an agent has no live alternative to compare against.

*Reachability alone is a weak and gameable metric.* One generated index file takes any corpus to 100% while conveying nothing about authority — which is precisely what happened here: this repository scores 94% and still had seventeen files lying about their status. Report both numbers or neither. A single-number "discoverability score" would be worse than nothing.

*The direction of first-party guidance is toward less upfront context, and this is consistent with that, not against it.* Anthropic removed over 80% of Claude Code's system prompt for the Claude 5 generation with no measured loss on coding evals, and names progressive disclosure a recommended shift. Pruning upfront context does not weaken this document's claim — it **raises the stakes on it**, because everything pruned now depends on the pointer graph and the currency marker to be recoverable and trustworthy. The remedy proposed here is not "load more"; it is "make the unloaded remainder actually reachable, and make it declare whether it is still true."

*This does not generalize to code repositories.* A code project whose docs are a thin README is not exposed to this; the three self-reporting properties of code do the work. The finding is scoped to projects whose primary artifact is prose.

---

## Gaps

- **Gap: n=2 corpora.** One measured directly, one contributor-reported. This repo's own bar for Tier B is production validation across 3+ projects, so the doc ships `EMERGING` and `Mixed`, not `PRODUCTION`/`B`. **Needs**: the instrument run against at least one more large prose corpus, ideally one not authored by a contributor to this repository.
- **Gap: no calibrated threshold.** 1.7% is plainly bad and 94% is plainly fine; nothing here calibrates the middle, so the diagnostic table says "low" rather than naming a number. **Needs**: reachability distributions across ten or more prose corpora before any threshold is asserted.
- **Gap: harm is argued, not measured.** The causal step — an agent retrieves superseded prose, and its answer is *worse* than it would have been — is demonstrated by construction (Collisions A and B) but never measured as an outcome. This is the weakest link in the argument and should be read as such. **Needs**: a paired eval — identical questions against the same corpus with and without supersession marking, scoring answer correctness — which is exactly the shape of instrument [`agent-evaluation.md`](agent-evaluation.md) describes.
- **Gap: currency correctness is only checkable where the lane contradicts the file.** `--currency` catches a `PRODUCTION` marker inside `archive/` because the *path* supplies ground truth. It cannot tell whether a `last-verified: 2026-08-13` on a live doc is honest, which is the larger and harder question. **Needs**: a marker-vs-content check — comparing a doc's asserted verification date against the last substantive edit to the claims it verifies.
- **Gap: the index-file confound is unquantified.** Reachability-via-generated-index and reachability-via-curated-pointers are counted identically, and they are not equally useful to a reader. **Needs**: a mode that reports reachability with the generated inventory excluded from the edge set.
- **Gap: entry-point definition is Claude-Code-specific.** `E1` encodes one harness's loading rules. DeepSeek Harness reads `AGENTS.md` and `CLAUDE.md` under a `maxBytes` budget that drops whole broader files (Tier A, verified 2026-08-19; see [`claude-md-progressive-disclosure.md`](claude-md-progressive-disclosure.md) § AGENTS.md Interop), so E1 is runtime-dependent. **Needs**: an entry-point profile per runtime before cross-harness comparison means anything.

---

## Related Analysis

- [`claude-md-progressive-disclosure.md`](claude-md-progressive-disclosure.md) — the loading-surface model this document takes as given, and the first-party progressive-disclosure adoption it builds on
- [`domain-knowledge-architecture.md`](domain-knowledge-architecture.md) — the resource-map pattern: pointing rather than containing. This document measures whether the pointing actually connects
- [`memory-system-patterns.md`](memory-system-patterns.md) — the staleness failure mode for memory files; this is the corpus-scale analogue, and its "Derive from Code (Do NOT Save)" table is the derivability assumption stated explicitly for the memory layer
- [`memory-systems-archetype-a-curated-kb.md`](memory-systems-archetype-a-curated-kb.md) — typed frontmatter and the registry+guard hygiene layer; `type:` makes a corpus queryable, `status:` makes it trustworthy, and §A1b's 127-types drift is the same class of ungoverned-metadata failure
- [`intent-alignment-audit.md`](intent-alignment-audit.md) — RETHINK asks whether a mechanism still serves its intent; this asks whether a *document* still claims an authority it has
- [`evidence-based-revalidation.md`](evidence-based-revalidation.md) — revalidation dates are a currency marker; this measures their coverage rather than their expiry
- [`cross-project-synchronization.md`](cross-project-synchronization.md) — a portfolio multiplies entry points; per-repo reachability is the per-spoke instance of this measurement

---

## Sources

### Tier A (Primary / Direct Observation)

- **This repository, measured 2026-08-28** — 179 markdown files; 168 reachable under `E1/refs`; 80 of 179 carrying a currency marker; 30 of 96 in `archive/`; 17 `archive/` files asserting a live frontmatter status; 1,275 internal links classified. Instrument and raw record: [`scripts/measure-link-reachability.py`](../scripts/measure-link-reachability.py), [`research/corpus-reachability-2026-08-28.md`](../research/corpus-reachability-2026-08-28.md). **Reproducible from a clean checkout** — this is the strongest form of evidence available for a claim about a public corpus.
- Anthropic — official CLAUDE.md guidance (include/exclude table, imports, child files, "prune ruthlessly") and `/init`. Source of the *anything Claude can figure out by reading code* exclude guidance and the *let Claude fetch what it needs* discovery model that this document scopes.
- Anthropic / Thariq Shihipar, ["The new rules of context engineering for Claude 5 generation models"](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) (2026-07-24) — progressive disclosure named as a recommended shift; the 80%-system-prompt-reduction claim. **Mirror-verified 2026-08-13, direct fetch blocked**; inherits the sourcing caveat recorded in [`claude-md-progressive-disclosure.md`](claude-md-progressive-disclosure.md).

### Tier B (Validated / Expert Practitioner)

- **External prose vault, three-day production run** — 703 markdown files, 6.07M words, 359,985 words added across 191 commits; 12 files reachable by link from any entry point a session loads; 96% frontmatter `type:` coverage; health check green after every commit. **One practitioner, one project, contributor-reported, not independently reproduced here.** Recorded at the same tier this repository gives other single-practitioner production evidence (cf. the project1 OKF case study in `memory-systems-archetype-a-curated-kb.md` §A1b).
- Sen, Kasturi, Lumer, Gulati, Subbiah, ["Is Grep All You Need? How Agent Harnesses Reshape Agentic Search"](https://arxiv.org/abs/2605.15184) (arXiv:2605.15184, 2026-05-14) — cited here as **counter-evidence**: grep generally outperforms vector retrieval across harnesses. Used to scope this document's claim to authority-blindness rather than retrieval accuracy. Preprint, not peer-reviewed.

### Tier C (Vendor-Published Standard)

- [Google Cloud — Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) — its sole required frontmatter field is `type:`. Relevant as a boundary: OKF standardizes what a note *is*, and deliberately leaves lifecycle to the producer. The vault's 96% `type:` coverage alongside 12-file reachability is a direct illustration that type conformance and discoverability are independent properties.

---

*Last updated: 2026-08-28 (initial).*
