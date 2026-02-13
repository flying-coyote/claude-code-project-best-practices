# Workflow Issues to Fix

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
