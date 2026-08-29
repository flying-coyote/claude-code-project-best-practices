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
  // 878 auto-filed matching, 2 with a human comment, 55 human issues, 5 PRs
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

async function run({apply, limit, comment, delay_ms, rateLimitAfter}) {
  const repo = makeRepo();
  const open = new Map(repo.map(i => [i.number, i]));
  const closedSet = new Set(); const commented = new Set();
  let contentCalls = 0;
  const notices = [], warnings = [], infos = [];

  const github = {rest: {issues: {
    listForRepo: async ({per_page, page}) => {
      const live = repo.filter(i => !closedSet.has(i.number));
      return {data: live.slice((page-1)*per_page, page*per_page)};
    },
    createComment: async ({issue_number}) => {
      contentCalls++;
      if (rateLimitAfter && contentCalls > rateLimitAfter) {
        const e = new Error('You have exceeded a secondary rate limit'); e.status = 403; throw e;
      }
      commented.add(issue_number);
    },
    update: async ({issue_number, state, state_reason}) => {
      if (state !== 'closed' || state_reason !== 'not_planned') throw new Error('bad close args');
      closedSet.add(issue_number);
    },
  }}};
  const context = {repo: {owner: 'o', repo: 'r'}, payload: {inputs: {apply, limit, comment, delay_ms}}};
  const core = {
    info: m => infos.push(m), notice: m => notices.push(m), warning: m => warnings.push(m),
  };
  const fn = new Function('github', 'context', 'core', `return (async () => { ${BODY} })()`);
  await fn(github, context, core);

  const closedTitles = [...closedSet].map(nn => open.get(nn).title);
  return {
    closed: closedSet.size, commented: commented.size, notices, warnings,
    closedHumanIssue: closedTitles.some(t => /Real human issue/.test(t)),
    closedStanding: closedTitles.some(t => /Standing report/.test(t)),
    closedWithComments: [...closedSet].some(nn => open.get(nn).comments > 0),
    closedPR: [...closedSet].some(nn => open.get(nn).pull_request),
  };
}

(async () => {
  let fail = 0;
  const check = (name, cond, extra='') => {
    console.log(`${cond ? 'PASS' : 'FAIL'}  ${name}${extra ? '  ' + extra : ''}`);
    if (!cond) fail++;
  };

  const dry = await run({apply: 'false', limit: '250', comment: 'true', delay_ms: '0'});
  check('dry run closes nothing', dry.closed === 0);
  check('dry run reports true match total + runs needed', /878 match/.test(dry.notices[0]) && /~4 run\(s\)/.test(dry.notices[0]), dry.notices[0]);

  const one = await run({apply: 'true', limit: '250', comment: 'true', delay_ms: '0'});
  check('closes exactly the limit', one.closed === 250, `closed=${one.closed}`);
  check('comments on each', one.commented === 250);
  check('never closes a human issue', !one.closedHumanIssue);
  check('never closes the standing issue', !one.closedStanding);
  check('never closes an issue with comments', !one.closedWithComments);
  check('never closes a PR', !one.closedPR);
  check('reports remaining + re-run', /628 still match/.test(one.notices[0]) && /re-run/i.test(one.notices[0]), one.notices[0]);

  const nc = await run({apply: 'true', limit: '900', comment: 'false', delay_ms: '0'});
  check('comment=false closes all 878 in one pass', nc.closed === 878, `closed=${nc.closed}`);
  check('comment=false posts no comments', nc.commented === 0);
  check('drained message when nothing remains', /backlog is drained/.test(nc.notices[0]), nc.notices[0]);

  const rl = await run({apply: 'true', limit: '900', comment: 'true', delay_ms: '0', rateLimitAfter: 137});
  check('rate limit stops cleanly, does not throw', rl.closed === 137, `closed=${rl.closed}`);
  check('rate limit warns with the count', rl.warnings.some(w => /Rate limit hit after 137/.test(w)));
  check('rate limit notice says stopped early + wait', /stopped early on a rate limit/.test(rl.notices[0]), rl.notices[0]);
  check('progress preserved (741 remain)', /741 still match/.test(rl.notices[0]));

  console.log(fail ? `\n${fail} FAILED` : '\nAll checks passed.');
  process.exit(fail ? 1 : 0);
})();
