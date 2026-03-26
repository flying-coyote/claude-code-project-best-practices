# TypeScript Library (Example)

## Purpose
Utility library for string manipulation, date formatting, and validation.

## Commands
- `npm test` - Run Jest tests (must pass before commits)
- `npm run test:coverage` - Check coverage (target 90%+)
- `npm run build` - TypeScript compilation to dist/
- `npm run lint` - ESLint (auto-fixes on save via hook)

## Known Gotchas
- Import paths must use .js extension (TypeScript module resolution)
- Test files must match *.test.ts pattern (not *.spec.ts)
- dist/ directory is gitignored but required for publishing
- Date utils use UTC by default (caused 3 timezone bugs in development)

## Current Focus
Adding validation helpers for v1.0 release
