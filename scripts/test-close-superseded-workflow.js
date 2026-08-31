#!/usr/bin/env node
/**
 * Tests the apply-loop of .github/workflows/close-superseded-auto-issues.yml
 * against a simulated repository, by extracting the inline github-script body
 * straight out of the YAML and running it with mocked github/context/core.
 *
 *   node scripts/test-close-superseded-workflow.js
 *
 * WHY THIS EXISTS
 * ---------------
 * A workflow that closes hundreds of issues in one pass is not something you
 * debug in production. The first version of this loop fired every request
 * back-to-back with retries:0; at the measured 878 matches that bursts through
 * GitHub's secondary rate limit (~80 content-generating requests/minute), 403s,
 * and fails the job mid-drain. Nothing caught it, because nothing ran it.
 *
 * The safety invariants below are the ones that actually matter — a mass-close
 * that catches a human's issue is not recoverable by re-running anything.
 */

const fs = require('fs');
const path = require('path');

const YAML = path.join(__dirname, '..', '.github', 'workflows', 'close-superseded-auto-issues.yml');

// Minimal extraction of the `script: |` block — avoids a yaml dependency.
function extractScript(yamlText) {
  const lines = yamlText.split('\n');
  const start = lines.findIndex(l => /^\s*script:\s*\|\s*$/.test(l));
  if (start === -1) throw new Error('could not find `script: |` in ' + YAML);
  const indent = lines[start + 1].match(/^\s*/)[0].length;
  const body = [];
  for (let i = start + 1; i < lines.length; i++) {
    const l = lines[i];
    if (l.trim() && l.match(/^\s*/)[0].length < indent) break;
    body.push(l.slice(indent));
  }
  return body.join('\n');
}

const BODY = extractScript(fs.readFileSync(YAML, 'utf8'));

function makeRepo() {
  const issues = [];
  // 878 auto-filed matching, 2 with a human comment, 54 genuinely-human + 1
  // standing, 5 PRs.
  //
  // The two families added to autoTitles on 2026-08-29 are the ones the real
  // backlog is actually made of and no pattern matched: 49 "Community
  // engagement triage" and 6 "Expired Measurement Claims Detected". Both are
  // machine output (github-actions[bot]), yet this fixture's 54
  // "Real human issue about N" entries encoded the belief that the residue was
  // human — the same wrong assumption PLAN.md and .github/workflows/README.md
  // carried. The fixture kept the suite passing while the real drain matched 0
  // of 61 and reported the backlog drained.
  //
  // The warning sign is U+26A0 U+FE0F. Verified against the real title fetched
  // from the API: a bare U+26A0 matches nothing.
  let n = 1000;
  const autoTitles = [
    '🔗 Broken links detected in documentation',
    '📋 Daily source review — 2026-05-01',
    '📊 Documentation maintenance 2026-04-02',
    '🔍 Review awesome-claude-code updates',
    '📚 Review potential new Anthropic blog post',
    '📚 Review Claude Code v2.1.99 release',
    '📋 Weekly source review 2026-03-01',
    '✅ Self-compliance audit 2026-02-01',
    '🚨 CRITICAL: Tier A sources inaccessible',
    '🤝 Community engagement triage - May 12, 2026',
    '⚠️ Expired Measurement Claims Detected',
  ];
  for (let i = 0; i < 878; i++)
    issues.push({number: n--, title: autoTitles[i % autoTitles.length], comments: 0});
  for (let i = 0; i < 2; i++)
    issues.push({number: n--, title: '🔗 Broken links detected in documentation', comments: 3});
  for (let i = 0; i < 54; i++)
    issues.push({number: n--, title: `Real human issue about ${i}`, comments: i % 2});
  issues.push({number: n--, title: '🔗 Standing report: broken links in documentation', comments: 0});
  for (let i = 0; i < 5; i++)
    issues.push({number: n--, title: 'A pull request', comments: 0, pull_request: {}});
  return issues;
}

async function run({apply, limit, comment, delay_ms, rateLimitAfter, viaEnv = false,
                    failAfter, failStatus, failMessage, failEvery, issues,
                    // Listing-completeness knobs, added 2026-08-31. `hideFromListing`
                    // makes listForRepo silently omit the last N open issues while
                    // repos.get() still counts them — which is exactly what the real
                    // API did on runs 13 and 14 (56 of 61, then 1 of 6, the same five
                    // missing both times). `repoMetaThrows` models the endpoint being
                    // unavailable, where "unverified" must not read as "verified".
                    hideFromListing = 0, repoMetaThrows = false}) {
  // `issues` overrides the default fixture, so a test can exercise a repo shape
  // makeRepo() does not produce — e.g. one where nothing is unmatched, which is
  // the only way to prove the all-clear branch is still reachable.
  const repo = issues || makeRepo();
  const open = new Map(repo.map(i => [i.number, i]));
  const closedSet = new Set(); const commented = new Set();
  let contentCalls = 0;
  const notices = [], warnings = [], infos = [];

  const liveIssues = () => repo.filter(i => !closedSet.has(i.number) && !i.pull_request);
  const livePRs = () => repo.filter(i => !closedSet.has(i.number) && i.pull_request);
  const github = {rest: {
    repos: {
      get: async () => {
        if (repoMetaThrows) { const e = new Error('Not Found'); e.status = 404; throw e; }
        // open_issues_count counts issues AND pull requests, and it is derived
        // from the repository record rather than from the issues listing — which
        // is the whole point of using it to cross-check.
        return {data: {open_issues_count: liveIssues().length + livePRs().length}};
      },
    },
    pulls: {
      list: async ({per_page, page}) => ({data: livePRs().slice((page-1)*per_page, page*per_page)}),
    },
    issues: {
    listForRepo: async ({per_page, page}) => {
      let live = repo.filter(i => !closedSet.has(i.number));
      // Drop the tail so the listing under-returns while repos.get() does not.
      if (hideFromListing > 0) live = live.slice(0, Math.max(0, live.length - hideFromListing));
      return {data: live.slice((page-1)*per_page, page*per_page)};
    },
    createComment: async ({issue_number}) => {
      contentCalls++;
      if (rateLimitAfter && contentCalls > rateLimitAfter) {
        const e = new Error('You have exceeded a secondary rate limit'); e.status = 403; throw e;
      }
      // Arbitrary-status injection: the 2026-08-29 overlap surfaced the content
      // cap as 422 Validation Failed, which the original predicate missed.
      if (failAfter && contentCalls > failAfter) {
        const e = new Error(failMessage || 'Validation Failed'); e.status = failStatus || 422; throw e;
      }
      // Scattered independent failures, for the circuit breaker.
      if (failEvery && contentCalls % failEvery !== 0) {
        const e = new Error('Some unrelated per-issue error'); e.status = 500; throw e;
      }
      commented.add(issue_number);
    },
    update: async ({issue_number, state, state_reason}) => {
      if (state !== 'closed' || state_reason !== 'not_planned') throw new Error('bad close args');
      closedSet.add(issue_number);
    },
  }}};
  // viaEnv models the `inputs.*` context (passed through step env); otherwise the
  // value arrives only on the event payload. Both paths must behave identically.
  const envKeys = ['APPLY_INPUT', 'LIMIT_INPUT', 'COMMENT_INPUT', 'DELAY_INPUT'];
  const saved = envKeys.map(k => [k, process.env[k]]);
  for (const k of envKeys) delete process.env[k];
  if (viaEnv) {
    if (apply !== undefined) process.env.APPLY_INPUT = apply;
    if (limit !== undefined) process.env.LIMIT_INPUT = limit;
    if (comment !== undefined) process.env.COMMENT_INPUT = comment;
    if (delay_ms !== undefined) process.env.DELAY_INPUT = delay_ms;
  }
  const context = {repo: {owner: 'o', repo: 'r'},
    payload: {inputs: viaEnv ? {} : {apply, limit, comment, delay_ms}}};
  const core = {
    info: m => infos.push(m), notice: m => notices.push(m), warning: m => warnings.push(m),
  };
  const fn = new Function('github', 'context', 'core', `return (async () => { ${BODY} })()`);
  try {
    await fn(github, context, core);
  } finally {
    for (const [k, v] of saved) { if (v === undefined) delete process.env[k]; else process.env[k] = v; }
  }

  const closedTitles = [...closedSet].map(nn => open.get(nn).title);
  return {
    closed: closedSet.size, commented: commented.size, notices, warnings,
    closedHumanIssue: closedTitles.some(t => /Real human issue/.test(t)),
    closedStanding: closedTitles.some(t => /Standing report/.test(t)),
    closedWithComments: [...closedSet].some(nn => open.get(nn).comments > 0),
    closedPR: [...closedSet].some(nn => open.get(nn).pull_request),
    infos, warningsList: warnings,
  };
}

(async () => {
  let fail = 0, total = 0;
  const check = (name, cond, extra='') => {
    total++;
    console.log(`${cond ? 'PASS' : 'FAIL'}  ${name}${extra ? '  ' + extra : ''}`);
    if (!cond) fail++;
  };

  // The apply input is a dropdown. Every value that is NOT the apply option must
  // be inert — this shipped as a text box defaulting to 'false' and produced three
  // consecutive accidental dry runs, so the safe side is the one worth pinning.
  // 'apply=false' is the one that matters: a prefix match on /^apply/ reads it as
  // APPLY and mass-closes when the operator plainly meant not to.
  for (const v of ['dry-run (list only, closes nothing)', 'false', '', 'FALSE', 'yes',
                   'apply=false', 'apply=true', 'applyx', 'no', 'dry-run']) {
    const r = await run({apply: v, limit: '250', comment: 'true', delay_ms: '0'});
    check(`inert for apply=${JSON.stringify(v)}`, r.closed === 0, `closed=${r.closed}`);
  }
  // ...and every value that IS the apply option must work, including the legacy string.
  for (const v of ['APPLY - actually close the matched issues',
                   '  apply - ACTUALLY close the matched issues  ', 'true', 'apply']) {
    const r = await run({apply: v, limit: '3', comment: 'true', delay_ms: '0'});
    check(`applies for apply=${JSON.stringify(v)}`, r.closed === 3, `closed=${r.closed}`);
  }

  // The `inputs.*` context path must behave exactly like the event-payload path.
  // Five production runs were dry runs with no way to tell which source was live.
  for (const v of ['APPLY - actually close the matched issues', 'true']) {
    const r = await run({apply: v, limit: '3', comment: 'true', delay_ms: '0', viaEnv: true});
    check(`env path applies for ${JSON.stringify(v)}`, r.closed === 3, `closed=${r.closed}`);
  }
  for (const v of ['dry-run (list only, closes nothing)', 'apply=false']) {
    const r = await run({apply: v, limit: '250', comment: 'true', delay_ms: '0', viaEnv: true});
    check(`env path inert for ${JSON.stringify(v)}`, r.closed === 0, `closed=${r.closed}`);
  }
  // Missing everywhere must be a dry run, not a crash.
  const none = await run({limit: '250', comment: 'true', delay_ms: '0', viaEnv: true});
  check('absent input is a dry run, not a crash', none.closed === 0);

  // The diagnostic that ends the ambiguity: log both sources and the resolved mode.
  const diag = await run({apply: 'APPLY - actually close the matched issues', limit: '2', comment: 'true', delay_ms: '0', viaEnv: true});
  check('logs both input sources', diag.infos.some(m => /input apply ->.*inputs context.*event payload/.test(m)),
        diag.infos.find(m => /input apply/.test(m)) || '(missing)');
  check('logs the resolved mode', diag.infos.some(m => /resolved mode: APPLY/.test(m)),
        diag.infos.find(m => /resolved mode/.test(m)) || '(missing)');

  const dry = await run({apply: 'dry-run (list only, closes nothing)', limit: '250', comment: 'true', delay_ms: '0'});
  check('dry run closes nothing', dry.closed === 0);
  check('dry run reports true match total + runs needed', /878 match/.test(dry.notices[0]) && /~4 run\(s\)/.test(dry.notices[0]), dry.notices[0]);
  check('dry run says nothing was closed and names the Mode option', /nothing was closed/.test(dry.notices[0]) && /Mode/.test(dry.notices[0]), dry.notices[0]);

  const one = await run({apply: 'APPLY - actually close the matched issues', limit: '250', comment: 'true', delay_ms: '0'});
  check('closes exactly the limit', one.closed === 250, `closed=${one.closed}`);
  check('comments on each', one.commented === 250);
  check('never closes a human issue', !one.closedHumanIssue);
  check('never closes the standing issue', !one.closedStanding);
  check('never closes an issue with comments', !one.closedWithComments);
  check('never closes a PR', !one.closedPR);
  check('reports remaining + re-run', /628 still match/.test(one.notices[0]) && /re-run/i.test(one.notices[0]), one.notices[0]);

  const nc = await run({apply: 'APPLY - actually close the matched issues', limit: '900', comment: 'false', delay_ms: '0'});
  check('comment=false closes all 878 in one pass', nc.closed === 878, `closed=${nc.closed}`);
  check('comment=false posts no comments', nc.commented === 0);
  // The fixture's 54 genuinely-human issues match nothing, which is CORRECT --
  // so the completion notice must reconcile rather than claim a bare all-clear.
  // Before 2026-08-29 this asserted /backlog is drained/ unconditionally, and
  // that expectation is exactly what let the real drain print "the backlog is
  // drained" on a run that matched 0 of 61 open issues.
  check('completion notice reconciles unmatched issues instead of claiming drained',
        /54 open issue\(s\) matched no pattern/.test(nc.notices[0]) &&
        !/every open issue was accounted for/.test(nc.notices[0]), nc.notices[0]);
  check('the notice names both readings of an unmatched issue',
        /right outcome if they are human/.test(nc.notices[0]) &&
        /missing generator/.test(nc.notices[0]));

  // 422 Validation Failed is how GitHub surfaced the content cap when two drains
  // ran concurrently on 2026-08-29. Treating it as an ordinary per-issue error
  // meant the loop skipped 25 issues and reported success.
  const rl422 = await run({apply: 'APPLY - actually close the matched issues', limit: '900',
                           comment: 'true', delay_ms: '0', failAfter: 60, failStatus: 422,
                           failMessage: 'Validation Failed'});
  check('422 is treated as a rate limit and stops the run', rl422.closed === 60, `closed=${rl422.closed}`);
  check('422 stop is reported as stopped-early', /stopped early on a rate limit/.test(rl422.notices[0]), rl422.notices[0]);

  // A systemic non-throttle fault should trip the breaker, not grind through.
  const brk = await run({apply: 'APPLY - actually close the matched issues', limit: '900',
                         comment: 'true', delay_ms: '0', failEvery: 1000});
  check('5 consecutive unrelated failures trip the breaker', brk.closed === 0, `closed=${brk.closed}`);
  check('breaker says why', brk.warningsList.some(w => /Stopping after 5 consecutive failures/.test(w)),
        brk.warningsList.slice(-1)[0] || '(none)');
  check('breaker does not claim the backlog is drained',
        !/backlog is drained/.test(brk.notices[0] || ''), brk.notices[0]);
  // The stop reason must be the REAL one. A breaker trip is not a rate limit,
  // and a notice that says otherwise sends the operator to wait out an hour
  // for a fault that will still be there.
  check('breaker notice names repeated failures, not a rate limit',
        /repeated failures/.test(brk.notices[0]) && !/rate limit/.test(brk.notices[0]), brk.notices[0]);

  const rl = await run({apply: 'APPLY - actually close the matched issues', limit: '900', comment: 'true', delay_ms: '0', rateLimitAfter: 137});
  check('rate limit stops cleanly, does not throw', rl.closed === 137, `closed=${rl.closed}`);
  check('rate limit warns with the count', rl.warnings.some(w => /Rate limit hit after 137/.test(w)));
  check('rate limit notice says stopped early + wait', /stopped early on a rate limit/.test(rl.notices[0]), rl.notices[0]);
  check('progress preserved (741 remain)', /741 still match/.test(rl.notices[0]));

  // The other side of the reconciliation: when every open issue IS accounted
  // for, the all-clear must still be reachable. A check that can only ever say
  // "not drained" is as useless as the one that could only ever say "drained".
  {
    const onlyAuto = [];
    let m = 500;
    for (let i = 0; i < 12; i++)
      onlyAuto.push({number: m--, title: '\u{1F91D} Community engagement triage - May 12, 2026', comments: 0});
    onlyAuto.push({number: m--, title: '\u{1F517} Standing report: broken links in documentation', comments: 0});
    const clean = await run({apply: 'APPLY - actually close the matched issues', limit: '900',
                             comment: 'false', delay_ms: '0', issues: onlyAuto});
    check('all-clear IS reachable when nothing is unmatched',
          /every open issue was accounted for/.test(clean.notices[0]), clean.notices[0]);
    check('the standing issue alone does not block the all-clear',
          clean.closed === 12, `closed=${clean.closed}`);
  }

  // LISTING COMPLETENESS — added 2026-08-31, from a defect observed in production.
  //
  // Runs 13 and 14 of this workflow scanned 56 of 61 and then 1 of 6 open issues,
  // missing the SAME five both times (#689, #683, #646, #561, #554: all
  // pattern-matching, all comment-free, all untouched since May 2026). Both runs
  // printed "every open issue was accounted for — the backlog is drained".
  //
  // The 2026-08-29 reconciliation could not catch it: it compares matched against
  // scanned, and when the listing under-returns, `unmatched` is 0 and every
  // internal count agrees. Only a cross-check against a DIFFERENT endpoint sees it.
  {
    const mk = () => {
      const arr = []; let m = 700;
      for (let i = 0; i < 10; i++)
        arr.push({number: m--, title: '\u{1F91D} Community engagement triage - May 12, 2026', comments: 0});
      arr.push({number: m--, title: '\u{1F517} Standing report: broken links in documentation', comments: 0});
      return arr;
    };
    const APPLY = 'APPLY - actually close the matched issues';

    // Listing hides 4 open issues that repos.get() still counts.
    const blind = await run({apply: APPLY, limit: '900', comment: 'false', delay_ms: '0',
                             issues: mk(), hideFromListing: 4});
    check('under-returning listing does NOT claim the backlog is drained',
          !/backlog is drained/.test(blind.notices[0] || ''), blind.notices[0]);
    check('under-returning listing names the unscanned count',
          /never scanned/.test(blind.notices[0] || ''), blind.notices[0]);
    check('under-returning listing raises a LISTING INCOMPLETE warning',
          blind.warningsList.some(w => /LISTING INCOMPLETE/.test(w)),
          JSON.stringify(blind.warningsList));

    // Unverifiable must not read as verified.
    const unver = await run({apply: APPLY, limit: '900', comment: 'false', delay_ms: '0',
                             issues: mk(), repoMetaThrows: true});
    check('unverifiable completeness does NOT claim the backlog is drained',
          !/backlog is drained/.test(unver.notices[0] || ''), unver.notices[0]);
    check('unverifiable completeness says so explicitly',
          /could NOT be verified/i.test(unver.notices[0] || ''), unver.notices[0]);
    check('unverifiable completeness warns',
          unver.warningsList.some(w => /Could not verify listing completeness/.test(w)),
          JSON.stringify(unver.warningsList));

    // ...and the check must not fire when the listing IS complete, or it would be
    // a check that can only ever say "not drained".
    const ok = await run({apply: APPLY, limit: '900', comment: 'false', delay_ms: '0',
                          issues: mk()});
    check('complete listing still reaches the all-clear',
          /every open issue was accounted for/.test(ok.notices[0] || ''), ok.notices[0]);
    check('complete listing raises no completeness warning',
          !ok.warningsList.some(w => /LISTING INCOMPLETE|Could not verify/.test(w)),
          JSON.stringify(ok.warningsList));
  }

  // The two families that made up 55 of the real 61-issue backlog and that no
  // pattern matched until 2026-08-29. Asserted against titles fetched from the
  // API, so a future edit that drops a pattern — or that retypes the warning
  // sign without its U+FE0F variation selector — fails here instead of silently
  // reporting "the backlog is drained" again.
  {
    const y = fs.readFileSync(YAML, 'utf8');
    const blk = y.split('const PATTERNS = [')[1].split('];')[0];
    const pats = blk.split('\n').map(l => l.trim())
                    .filter(l => l.startsWith('/^'))
                    .map(l => eval(l.replace(/,$/, '')));
    const real = [
      ['\u{1F91D} Community engagement triage - June 5, 2026', 'triage family'],
      ['\u26A0\uFE0F Expired Measurement Claims Detected', 'expiry family (U+26A0 U+FE0F)'],
    ];
    for (const [title, label] of real)
      check(`PATTERNS matches the ${label}`, pats.some(p => p.test(title)), JSON.stringify(title));

    // And the standing issue must still be refused by KEEP, not matched away.
    const standing = '\u{1F517} Standing report: broken links in documentation';
    check('the standing issue is still never matched for closure',
          !pats.some(p => p.test(standing)));
  }

  console.log(fail ? `\n${fail} of ${total} FAILED`
                   : `\nAll ${total} checks passed.`);
  process.exit(fail ? 1 : 0);
})();
