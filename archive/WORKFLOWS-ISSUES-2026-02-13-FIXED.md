# Workflow Issues to Fix

> **ARCHIVED — a dated record, not guidance.** Archived in the v2.0 repositioning (March 2026, DECISIONS.md § Reposition as Analytical Layer) or a later reduction. A closed defect checklist, applied at the time, against workflow files that no longer exist in the audited form — source-monitoring.yml, the file with six of the reported defects, was deleted in the 2026-07 reduction. It records a point in time and needs no successor — nobody should be looking here for current guidance. (Marked 2026-08-28; successor determined by mapping plus adversarial verification, which overturned 35 of 39 successor claims — see `analysis/prose-corpus-discoverability.md`.)

## Problem

The GitHub Actions workflow files have YAML syntax errors due to JavaScript template literals with multi-line markdown content.

## Specific Issues

1. **.github/workflows/source-monitoring.yml** - Multiple script blocks use template literals (backticks) with multi-line markdown content containing special characters (`, *, #, [, ]) that YAML interprets as syntax
2. **.github/workflows/link-checker.yml** - Likely similar issues

## YAML Errors Found

```
yaml.scanner.ScannerError: while scanning an alias
expected alphabetic or numeric character, but found '*'
```

Lines with issues: 61, 121, 192, 292, 412, 529, 663

## Solution Required

Convert all multi-line template literals to string concatenation:

**BEFORE** (causes YAML errors):
```javascript
body: `Title: **${variable}**

**URL**: ${url}

## Section
Content here`
```

**AFTER** (YAML-safe):
```javascript
const body = 'Title: **' + variable + '**\n\n' +
  '**URL**: ' + url + '\n\n' +
  '## Section\n' +
  'Content here';

...
body: body
```

## Status

- [ ] Fix all template literals in source-monitoring.yml (6 locations)
- [ ] Fix any template literals in link-checker.yml
- [ ] Validate YAML syntax: `python3 -c "import yaml; yaml.safe_load(open('file.yml'))"`
- [ ] Test workflows manually: `gh workflow run <workflow-name>`
- [ ] Commit fixes

## Next Steps

1. Systematically go through both workflow files
2. Convert all multi-line template literals to string concatenation
3. Validate YAML
4. Commit and push
5. Test workflows

## Temporary Workaround

Workflows will run on schedule (Monday/Sunday) but cannot be manually triggered until fixed.
