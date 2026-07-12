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
   echo "WEEKLY-REVIEW SELF-TEST: routable=$routable readme-match=<yes|no> index-match=<yes|no> convergence-fields=<n>/$routable sources-curated=<YYYY-MM-DD> expired-claims=<n> => <OK|DRIFT>"
   ```
   `OK` means every comparison matched and nothing is overdue; any mismatch or overdue item makes it `DRIFT` and the drifted checks must already appear in PLAN.md priorities from step 7. If the line cannot be printed with real values, the review did not actually run its checks.

10. **Commit**:
    ```
    git add PLAN.md README.md INDEX.md
    git commit -m "📋 Weekly review [date]"
    ```
    (Include README.md/INDEX.md only if step 3 changed them.)

## Expected Outcome

PLAN.md reflects the week's accomplishments and next week's priorities, the README corpus counts match what is on disk, SOURCES freshness and convergence-field coverage have been checked against the table above, and the run printed its one-line self-test.
