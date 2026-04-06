<!-- .claude/rules/code-style.md
     This rule file loads when Claude edits source files.
     Customize the globs in settings.json to control when it loads. -->

# Code Style Rules

<!-- Replace these with your project's actual conventions.
     Only include rules Claude gets wrong — don't restate the linter config. -->

## Naming
- Files: {{convention, e.g., kebab-case.ts, snake_case.py}}
- Functions: {{convention}}
- Constants: {{convention}}

## Patterns
- Prefer {{pattern}} over {{anti-pattern}} for {{reason}}
- Error handling: {{convention, e.g., "raise exceptions, don't return error codes"}}
- Imports: {{convention, e.g., "absolute imports only, no relative imports beyond one level"}}

## Testing
- Test file naming: `test_{{module}}.py` or `{{module}}.test.ts`
- Each test function tests one behavior
- Use {{test framework}} assertions, not raw assert
