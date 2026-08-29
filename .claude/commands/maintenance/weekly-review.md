# Weekly Maintenance Review

Conduct the weekly review of project status and documentation currency. This prompt is standalone: run it in a fresh session with the working directory at the repo root, and everything it needs is either in this file or derivable from disk. Derive counts and dates from disk every time rather than trusting what a doc says about itself.

## Steps

1. **Gather week's activity**:
   ```bash
   git log --since="7 days ago" --oneline
   git diff --stat HEAD~10..HEAD 2>/dev/null || git diff --stat
   ```

2. **Review accomplishments**:
   - What analysis docs were added, collapsed, or updated?
   - What issues were resolved?
   - What quality improvements were made?

3. **Re-derive the corpus count** (derive from disk, compare to README, fix README if drifted):
   ```bash
   total=$(ls analysis/*.md | wc -l)
   routable=$((total - 1))   # CANONICAL-DOC-TEMPLATE.md is non-routable and excluded from the routable count
   grep -nE "of (the )?[0-9]+ analysis docs|[0-9]+ documents\)|[0-9]+ \`?\.md\`? files|[0-9]+ routable" README.md
   grep -nE "^\| analysis \|" INDEX.md
   ```
   Compare the derived `total` and `routable` against every count README states (the routing sentence, the "What You Get" table row, the "Core Analysis" heading, and the routable-vs-template note under it) and against the `analysis` row in INDEX.md. If any stated number disagrees with the derived one, fix README by hand and regenerate the index with `python3 automation/generate_index.py`, because the README is the public claim surface and a drifted count there is exactly the self-model drift this repo audits other projects for.

4. **SOURCES freshness check**:
   - Read the `**Last curated**` line near the top of SOURCES.md and compute its age. If it is older than 45 days, add "SOURCES curation pass" to next week's priorities.
   - Confirm SOURCES-QUICK-REFERENCE.md's "Last Updated" footer names the same curation pass as SOURCES.md; if they diverge, flag which one is behind.
   - Skim the **Unverified / pending revalidation** section at the end of SOURCES.md for items whose stated revalidation condition has come due this week.
   - Run `python3 scripts/check-measurement-expiry.py` and note any expired measurement claims.

5. **Convergence-field upkeep** (owner ruling 2026-07-12: every routable analysis doc carries a `convergence:` frontmatter field):
   ```bash
   for f in analysis/*.md; do
     [ "$f" = "analysis/CANONICAL-DOC-TEMPLATE.md" ] && continue
     grep -q "^convergence:" "$f" || echo "MISSING convergence: $f"
   done
   ```
   Any doc added since the last review must get a field, and its value must be justified by the ratified function table below. Check for drift both ways: a doc whose rating disagrees with the table, and two docs covering the same function that disagree with each other. An upgrade (single-source → emerging, emerging → converged) requires verified external adoption evidence recorded in the doc itself; never invent adoption evidence, and when in doubt the value is `single-source`.

   | Function | Status | Basis (verified 2026-07-12) |
   |---|---|---|
   | recurring agent scheduling | converged | vendor-native Claude scheduled tasks + Hermes Agent (~213K stars) + RunAgent Pulse + Osmani native-tooling list |
   | inbox/feed triage | emerging | one vendor-official exemplar (Microsoft WorkIQ) |
   | AI-PKM | emerging, with a license-risk note | Obsidian Smart Connections ~786K downloads, but the Jan-2026 switch to a proprietary license is a standing adoption caveat |
   | approval gating / human-in-the-loop | emerging | vendor direction is classifier-plus-escalation; external support for decisions-first surfacing |
   | agent-to-human backlog bridging | single-source | no external evidence survived verification |
   | drift/staleness detection for docs | single-source | no external evidence survived verification |
   | anything not listed above | single-source by default | `converged` only when the practice is obviously converged (vendor-native plus independent mass adoption, with the evidence cited in the doc) |

   The binding adoption rule this feeds is in AUDIT-CONTEXT.md ("adoption requires converged status or an explicit owner exception"). The evidence axis is Tier A-D only; the 1-5 axis is retired and any new prose reaching for it gets rewritten onto A-D.

5b. **Absorption-map consistency** (mechanical greps only — no WebFetch here; judgment about absorbers happens in quarterly absorption scans, `drafts/ABSORPTION-SCAN-*.md`, not in this weekly pass):
   ```bash
   map_rows=$(grep -c '^| \[`analysis/' ABSORPTION-MAP.md)
   # exclude the template — its schema block carries both fields at line start (same exclusion as step 5's loop)
   follows_docs=$(grep -l "^follows:" analysis/*.md 2>/dev/null | grep -v CANONICAL-DOC-TEMPLATE | wc -l)
   retiring_docs=$(grep -l "^replacement-by:" analysis/*.md 2>/dev/null | grep -v CANONICAL-DOC-TEMPLATE | wc -l)
   lane_conflicts=$(grep -l "^follows:" analysis/*.md 2>/dev/null | grep -v CANONICAL-DOC-TEMPLATE | xargs -r grep -l "^replacement-by:" | wc -l)
   # head -1 is load-bearing. That ABSORPTION-MAP line carries TWO dates (the
   # sweep, then an interim liveness refresh), so grep -oE emitted both and
   # map_verified became the two-line string '2026-07-16\n2026-08-13' — which
   # parses as no date at all, so the ">100 days old" check below could never
   # fire. Dead since the line was authored 2026-07-16; fixed 2026-08-29.
   map_verified=$(grep -m1 "Last verified sweep" ABSORPTION-MAP.md | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}' | head -1)
   ```
   Checks, all mechanical: `map_rows` must equal `$routable` (one row per routable doc); every doc with `follows:` must have a `follow`-lane row and every `replacement-by:` doc a `retire-toward`-lane row (spot-check names against the map, not just counts); `lane_conflicts` must be 0 (`follows:` and `replacement-by:` are mutually exclusive — see CONTRIBUTING.md § Following a Canon); and if `map_verified` is more than 100 days old, add "absorption sweep" to next week's priorities. The map is derived — on any conflict, per-doc frontmatter wins and the map gets corrected to match it, never the reverse.

5c. **Corpus discoverability** (mechanical; the instrument does the work — see [`analysis/prose-corpus-discoverability.md`](../../../analysis/prose-corpus-discoverability.md)):
   ```bash
   python3 scripts/measure-link-reachability.py --links      > /tmp/wr-links.txt
   python3 scripts/measure-link-reachability.py --currency   > /tmp/wr-currency.txt
   python3 scripts/measure-link-reachability.py --entry E1 --mode refs > /tmp/wr-reach.txt
   dangling_live=$(awk '/^dangling/{print $2}' /tmp/wr-links.txt)
   wrong_status=$(grep -oE 'WRONG=[0-9]+' /tmp/wr-currency.txt | cut -d= -f2 | paste -sd+ | bc)
   guidance=$(grep -oE 'guidance [0-9]+/[0-9]+' /tmp/wr-reach.txt | tail -1)
   # ~2m20s: 11 checks x 8 PYTHONHASHSEED values x 5 modes over the whole corpus.
   # That is past a 120s foreground tool timeout, so RUN IT IN THE BACKGROUND and
   # read the result when it lands. Do not shorten it to fit — the 8-seed sweep is
   # the determinism guard, and a `set` literal in the resolver once made this
   # instrument return 168-171 links depending on the hash seed while the docs
   # called it reproducible.
   python3 scripts/test-measure-link-reachability.py >/dev/null && instrument=OK || instrument=BROKEN
   ```
   Three checks, each with a hard target.

   **`dangling_live` must be 0.** Any non-zero value is a live document pointing at
   something that is not there. This is the single most common way the corpus rots,
   and deprecation and doc-removal are the two activities that cause it.

   **`wrong_status` must be 0.** A file in the dead lane asserting `status: PRODUCTION`
   is worse than an unmarked one: it defeats the check a careful reader runs. Seventeen
   of these persisted for six months before anything looked.

   **`guidance` must be `n/n`.** Read the *guidance* lane, never the corpus-wide
   percentage — that denominator mixes prose with `.claude/` config the runtime loads
   by its own rules and with frozen fixtures, neither of which owes the reader a
   pointer. Reporting it undecomposed once produced a headline wrong by roughly a
   factor of two.

   `instrument=BROKEN` means the measurement itself is untrustworthy and the three
   numbers above must not be recorded — the instrument shipped nondeterministic once
   (a set literal let `PYTHONHASHSEED` pick the answer) and a single run cannot detect that.

   **Scope note**: the style checks deliberately skip `archive/` (`markdownlint` via
   `'!archive'`, `check-measurement-expiry.py` via its `analysis` default). Do not
   "fix" that — you do not lint a tombstone. But the *currency* check above must keep
   covering the dead lane, because a lane excluded from every check is exactly where
   unverifiable claims accumulate.

5d. **Declared-gap inventory** (enumerative, deliberately non-gating):
   ```bash
   python3 scripts/list-declared-gaps.py
   declared_gaps=$(python3 scripts/list-declared-gaps.py --json | python3 -c 'import json,sys; print(json.load(sys.stdin)["count"])')
   ```
   `analysis/CANONICAL-DOC-TEMPLATE.md` defines a `**Needs**:` convention for
   declaring what a document does not know. Twenty declarations followed it across
   five docs and, until 2026-08-29, **nothing read them** — no script, no workflow,
   no hook, and no step of this review. Each was discoverable only by opening the
   document that contained it, which is the same unreachability
   [`analysis/prose-corpus-discoverability.md`](../../../analysis/prose-corpus-discoverability.md)
   measures in the corpus at large, applied to the repo's own record of its open
   questions.

   **This check has no target and never forces `DRIFT`.** A rising count is not a
   defect: declaring a gap and choosing not to close it is a legitimate, honest
   outcome, and gating on the number would reward deleting the declaration over
   doing the work. Read the list, decide whether any gap has become closable since
   last week (a new source, a shipped instrument, an upstream release), and route
   those into step 7. `--untracked` filters to gaps whose topic words are absent
   from PLAN.md, but it is word overlap and not semantics, so treat a hit as
   "probably mentioned somewhere" and never as "tracked".

5e. **Root-doc currency markers** (mechanical; compare each marker to git, not to itself):
   ```bash
   stale_markers=0
   for f in DECISIONS.md AUDIT-CONTEXT.md SOURCES.md PLAN.md CONTRIBUTING.md README.md; do
     [ -f "$f" ] || continue
     # OLDEST marker in the file, not the newest. SOURCES.md carried a fresh
     # header and a 16-day-stale footer at the same time; taking the max hid it.
     oldest=$(grep -oiE 'last (updated|curated)[^0-9]{0,4}(([0-9]{4}-[0-9]{2}-[0-9]{2})|([A-Z][a-z]+ [0-9]{1,2}, [0-9]{4}))' "$f" \
              | grep -oE '([0-9]{4}-[0-9]{2}-[0-9]{2})|([A-Z][a-z]+ [0-9]{1,2}, [0-9]{4})' \
              | while read -r d; do date -d "$d" +%Y-%m-%d 2>/dev/null; done | sort | head -1)
     [ -z "$oldest" ] && continue          # no marker is fine; a WRONG one is not
     edited=$(git log -1 --format=%ad --date=short -- "$f")
     if [[ "$oldest" < "$edited" ]]; then
       echo "STALE MARKER  $f  says $oldest, last edited $edited"
       stale_markers=$((stale_markers + 1))
     fi
   done
   ```
   `stale_markers` must be 0. A currency marker that a content edit does not update
   is worse than no marker: it certifies the staleness it is hiding, and a reader
   checking currency the careful way is the one it misleads. Note the date formats
   differ across these files (`2026-08-29` vs `August 29, 2026`) — that is why the
   loop normalises through `date -d` instead of comparing strings, and it is why a
   naive ISO-only grep missed PLAN.md's marker entirely.

   Two of these are load-bearing beyond this repo. **AUDIT-CONTEXT.md** is fetched
   by the audit prompt into *other* repositories, so its marker is a claim made to
   consumers; it sat at 2026-07-16 through ten commits, six of them substantive.
   **SOURCES.md** carries two markers — `**Last curated**` at line 11 and the
   changelog footer — and line 11 is authoritative when they disagree. All three
   root markers were repaired on 2026-08-29; this check exists so the next drift is
   caught in a week rather than in six. It was verified failure-capable before being
   written down — replayed against the three real pre-repair states (`2026-07-16` ISO,
   the fresh-header/stale-footer pair, and the `August 28, 2026` prose form) it flags
   3 of 3. A guard that has only ever returned 0 has not been tested.

   `ABSORPTION-MAP.md` is deliberately excluded: its "Last verified sweep" dates a
   *sweep*, not the file, so an edit that does not re-sweep should not touch it.
   Step 5b applies the right check there (>100 days ⇒ DRIFT).

6. **Identify blockers**:
   - Any docs waiting for sources or primary verification?
   - Any skills needing validation?
   - Any structural issues discovered?

7. **Set next week priorities**:
   - What analysis should be added or updated next?
   - What documentation needs refresh?
   - Anything flagged by steps 3-5 that was not fixable in this pass?

8. **Update PLAN.md**:
   - Add completed items to "Completed This Cycle" section
   - Update current priorities
   - Note any blockers
   - Update metrics if counts changed, using the numbers step 3 derived from disk
   - Update "Last Updated" date

9. **Print the self-test line.** The run must end by printing exactly one line in this shape, with every value derived during this run:
   ```bash
   echo "WEEKLY-REVIEW SELF-TEST: routable=$routable readme-match=<yes|no> index-match=<yes|no> convergence-fields=<n>/$routable absorption-rows=$map_rows/$routable follows=$follows_docs lane-conflicts=$lane_conflicts map-verified=$map_verified sources-curated=<YYYY-MM-DD> expired-claims=<n> dangling-live=$dangling_live wrong-status=$wrong_status guidance=$guidance instrument=$instrument declared-gaps=$declared_gaps stale-markers=$stale_markers => <OK|DRIFT>"
   ```
   `OK` means every comparison matched and nothing is overdue; any mismatch or overdue item makes it `DRIFT` and the drifted checks must already appear in PLAN.md priorities from step 7. A non-zero `lane_conflicts` or a `map-verified` date older than 100 days also forces `DRIFT`. So does a non-zero `dangling-live` or `wrong-status`, a `guidance` figure that is not `n/n`, or `instrument=BROKEN`. `declared-gaps` is reported, never gated — see step 5d for why a target there would be counterproductive. A non-zero `stale-markers` forces `DRIFT`. If the line cannot be printed with real values, the review did not actually run its checks.

10. **Commit**:
    ```
    git add PLAN.md README.md INDEX.md ABSORPTION-MAP.md
    git commit -m "📋 Weekly review [date]"
    ```
    (Include README.md/INDEX.md/ABSORPTION-MAP.md only if steps 3/5b changed them.)

## Expected Outcome

PLAN.md reflects the week's accomplishments and next week's priorities, the README corpus counts match what is on disk, SOURCES freshness and convergence-field coverage have been checked against the table above, the absorption map is row-consistent with per-doc frontmatter (step 5b), the corpus has zero dangling live links and zero dead-lane files asserting a live status with the guidance lane fully reachable (step 5c), the repository's own declared evidence gaps have been enumerated and read rather than left to sit unread in the documents that declare them (step 5d), no root doc claims a currency date its own later edits have passed (step 5e), and the run printed its one-line self-test.
