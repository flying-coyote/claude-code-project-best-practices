#!/usr/bin/env python3
"""
Check for expired measurement claims in analysis/.

Adapted 2026-11-10 (ported back from securing-ai-best-practices) with one
change: a --changed-files argument. In that repo the job failed for every
expired claim anywhere, so a cohort of docs written together turned the
default branch red together and the check blocked unrelated pull requests,
including the ones that would have fixed the expiry. With --changed-files the
exit code is non-zero only when an expired claim sits in one of the named
files; the full expired count still prints on one summary line for the weekly
review. Passing --changed-files with no paths therefore never fails, which is
what CI does on push and scheduled runs.

Usage:
    python scripts/check-measurement-expiry.py                      # fail on any expired claim
    python scripts/check-measurement-expiry.py --changed-files a.md # fail only for a.md
    python scripts/check-measurement-expiry.py --changed-files      # report only
    python scripts/check-measurement-expiry.py --create-issue
"""

import argparse
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional

import yaml


class MeasurementExpiryChecker:
    """Check measurement claims for expiry dates."""

    def __init__(self, patterns_dir: Path):
        self.patterns_dir = patterns_dir
        self.expired_claims = []
        self.expiring_soon = []  # Within 30 days
        self.frozen_claims = []  # revalidate: never — deliberately unrepeatable
        # Files whose claims could not be read. Upstream printed a warning and
        # carried on, so an unreadable claim counted as current: the fail-open
        # shape. Here an error is reported and fails the run (scoped like an
        # expiry when --changed-files is given).
        self.errors = []

    def check_all_patterns(self) -> Dict:
        """Scan all pattern files for expired measurement claims."""
        print(f"🔍 Checking measurement claims in {self.patterns_dir}...")

        pattern_files = sorted(p for p in self.patterns_dir.rglob("*.md")
                               if p.name != "CANONICAL-DOC-TEMPLATE.md")
        print(f"   Found {len(pattern_files)} pattern files")

        today = datetime.now().date()

        for pattern_file in pattern_files:
            self._check_pattern_file(pattern_file, today)

        return {
            "frozen": self.frozen_claims,
            "errors": self.errors,
            "expired": self.expired_claims,
            "expiring_soon": self.expiring_soon,
            "checked_files": len(pattern_files),
            "check_date": today.isoformat(),
        }

    def _check_pattern_file(self, pattern_file: Path, today):
        """Check a single pattern file for expired measurements."""
        try:
            content = pattern_file.read_text()

            # Extract YAML frontmatter
            frontmatter = self._extract_frontmatter(content)

            if not frontmatter:
                return  # No frontmatter, skip

            # Check for measurement-claims field
            if "measurement-claims" not in frontmatter:
                return  # No measurement claims, skip

            claims = frontmatter["measurement-claims"]
            if not isinstance(claims, list):
                print(f"   ⚠️  Invalid measurement-claims format in {pattern_file}")
                return

            # Check each claim
            for claim in claims:
                self._check_claim(pattern_file, claim, today)

        except Exception as e:
            print(f"   ⚠️  Error checking {pattern_file}: {e}")
            self.errors.append({"file": str(pattern_file), "error": str(e)})

    def _extract_frontmatter(self, content: str) -> Optional[Dict]:
        """Extract YAML frontmatter from markdown file."""
        # Look for --- ... --- blocks
        frontmatter_pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL | re.MULTILINE)
        match = frontmatter_pattern.search(content)

        if not match:
            return None

        # A YAML error propagates to _check_pattern_file, which records it as an
        # error rather than treating the file as having no claims.
        return yaml.safe_load(match.group(1))

    def _check_claim(self, pattern_file: Path, claim: Dict, today):
        """Check a single measurement claim for expiry."""
        if not isinstance(claim, dict):
            return

        # Required fields
        claim_text = claim.get("claim", "Unknown claim")
        source = claim.get("source", "Unknown source")
        date_str = claim.get("date")
        revalidate_str = claim.get("revalidate")

        if not revalidate_str:
            # No revalidate date, skip
            return

        # `revalidate: never` marks a measurement that CANNOT be re-run — the
        # measured artifact is gone, private, or was mutated by a later step.
        # Without this, such a claim expires every quarter and re-enters the
        # queue forever as an item nobody can close, which trains readers to
        # ignore the marker. Frozen is a verdict, not a missing date: it is
        # reported separately, and it never counts as expired.
        if str(revalidate_str).strip().lower() == "never":
            self.frozen_claims.append({
                "file": str(pattern_file),
                "claim": claim_text,
                "source": source,
                "date": date_str,
            })
            return

        # PyYAML parses an unquoted YYYY-MM-DD into a datetime.date. Upstream
        # passed that to strptime, which raised TypeError, and the outer handler
        # swallowed it, so every unquoted date was silently never checked.
        if isinstance(revalidate_str, date):
            revalidate_date = revalidate_str
            revalidate_str = revalidate_date.isoformat()
        else:
            try:
                revalidate_date = datetime.strptime(str(revalidate_str).strip(), "%Y-%m-%d").date()
            except ValueError:
                raise ValueError(f"invalid revalidate date {revalidate_str!r}")
        if isinstance(date_str, date):
            date_str = date_str.isoformat()

        # Check if expired
        if revalidate_date < today:
            days_expired = (today - revalidate_date).days
            self.expired_claims.append({
                "file": str(pattern_file),
                "claim": claim_text,
                "source": source,
                "date": date_str,
                "revalidate": revalidate_str,
                "days_expired": days_expired,
            })

        # Check if expiring soon (within 30 days)
        elif revalidate_date <= today + timedelta(days=30):
            days_until_expiry = (revalidate_date - today).days
            self.expiring_soon.append({
                "file": str(pattern_file),
                "claim": claim_text,
                "source": source,
                "date": date_str,
                "revalidate": revalidate_str,
                "days_until_expiry": days_until_expiry,
            })


def generate_issue_body(results: Dict) -> str:
    """Generate GitHub issue body for expired measurements."""
    body = []
    body.append("## Expired Measurement Claims\n\n")
    body.append(f"**Check Date**: {results['check_date']}\n")
    body.append(f"**Checked Files**: {results['checked_files']}\n\n")

    expired = results["expired"]
    expiring_soon = results["expiring_soon"]

    if expired:
        body.append(f"### ⚠️ Expired ({len(expired)} claims)\n\n")
        body.append("| Claim | Source | Expired | Days Overdue | File |\n")
        body.append("|-------|--------|---------|--------------|------|\n")

        for claim in expired:
            file_name = Path(claim["file"]).stem
            claim_short = claim["claim"][:50]
            if len(claim["claim"]) > 50:
                claim_short += "..."
            body.append(f"| {claim_short} | {claim['source']} | {claim['revalidate']} | {claim['days_expired']} | {file_name} |\n")

        body.append("\n**Action Required**:\n")
        body.append("1. Re-run the measurement at its source (the lab run or standard the claim cites)\n")
        body.append("2. Update measurement claim if result changed\n")
        body.append("3. Set a new `revalidate` date (three months for ATLAS-dependent claims, up to eight otherwise)\n")
        body.append(
            "4. If the measurement is no longer valid, mark it historical rather than deleting it "
            "— see `analysis/evidence-tiers.md` \u00a7 Expired but not invalid. If it can never be "
            "re-run, use `revalidate: never` (same section). If the whole doc is going, "
            "`CONTRIBUTING.md` \u00a7 Retiring a Doc.\n\n"
        )

    if expiring_soon:
        body.append(f"### ⏰ Expiring Soon ({len(expiring_soon)} claims)\n\n")
        body.append("| Claim | Source | Expires | Days Remaining | File |\n")
        body.append("|-------|--------|---------|----------------|------|\n")

        for claim in expiring_soon:
            file_name = Path(claim["file"]).stem
            claim_short = claim["claim"][:50]
            if len(claim["claim"]) > 50:
                claim_short += "..."
            body.append(f"| {claim_short} | {claim['source']} | {claim['revalidate']} | {claim['days_until_expiry']} | {file_name} |\n")

        body.append("\n**Upcoming Action**:\n")
        body.append("- Plan to re-validate these measurements before expiry\n")
        body.append(
            "- Add to the review cadence: the weekly review\n\n"
        )

    frozen = results.get("frozen", [])
    if frozen:
        body.append(f"### 🧊 Frozen — cannot be re-measured ({len(frozen)} claims)\n\n")
        body.append("These carry `revalidate: never`. They are dated historical records whose\n")
        body.append("underlying measurement is not repeatable. **No action is possible or expected.**\n\n")
        body.append("| Claim | Source | Measured | File |\n")
        body.append("|-------|--------|----------|------|\n")
        for claim in frozen:
            file_name = Path(claim["file"]).stem
            claim_short = claim["claim"][:50]
            if len(claim["claim"]) > 50:
                claim_short += "..."
            body.append(f"| {claim_short} | {claim['source']} | {claim['date']} | {file_name} |\n")
        body.append("\n")

    if not expired and not expiring_soon:
        body.append("✅ All measurement claims are current. No action required.\n\n")

    body.append("---\n\n")
    body.append("**Generated by**: `scripts/check-measurement-expiry.py`\n")
    body.append(f"**Timestamp**: {datetime.now().isoformat()}\n")

    return "".join(body)


def main():
    parser = argparse.ArgumentParser(description="Check for expired measurement claims")
    parser.add_argument("--create-issue", action="store_true", help="Create GitHub issue for expired claims")
    parser.add_argument("--patterns-dir", default="analysis", help="Directory of docs carrying measurement-claims frontmatter (default: analysis)")
    parser.add_argument("--changed-files", nargs="*", default=None, metavar="PATH",
                        help="Fail only for expired claims in these files (a PR's changed files). "
                             "Given with no paths, report the full count and never fail.")
    args = parser.parse_args()

    # A missing directory must not read as "no expired claims"; rglob on a
    # nonexistent path yields nothing and raises nothing.
    if not Path(args.patterns_dir).is_dir():
        print(f"error: {args.patterns_dir} is not a directory; refusing to report a count "
              "for a path that was never scanned.")
        return 2

    # Check for expired measurements
    checker = MeasurementExpiryChecker(Path(args.patterns_dir))
    results = checker.check_all_patterns()

    # Print summary
    expired_count = len(results["expired"])
    expiring_soon_count = len(results["expiring_soon"])

    print(f"\n📊 Summary:")
    print(f"   ⚠️  Expired: {expired_count} claims")
    print(f"   ⏰ Expiring soon (30 days): {expiring_soon_count} claims")

    if expired_count > 0:
        print(f"\n⚠️  EXPIRED CLAIMS FOUND:")
        for claim in results["expired"]:
            file_name = Path(claim["file"]).stem
            print(f"   - {file_name}: {claim['claim'][:60]}... ({claim['days_expired']} days overdue)")

    # Generate issue body
    issue_body = generate_issue_body(results)

    if args.create_issue:
        # NOTE: nothing consumes this file automatically. CI runs this script
        # (test-instruments, scoped to changed files) but never reads the issue
        # file, and no job files issues (DECISIONS.md, Decision 9). The flag
        # writes a body for a human to paste.
        issue_file = Path("measurement-expiry-issue.md")
        issue_file.write_text(issue_body)
        print(f"\n✅ Issue body written to {issue_file}")
        print("   Nothing reads this file automatically; no job files issues.")
        print("   Paste it into a new issue by hand, or pipe it somewhere useful.")
    else:
        print("\n📝 Issue Body Preview:")
        print("=" * 60)
        print(issue_body)
        print("=" * 60)
        print("\n💡 Run with --create-issue to generate issue file")

    # Scope the failure. Paths are compared resolved, so "analysis/x.md" from
    # git diff and the checker's own relative paths match regardless of cwd.
    if args.changed_files is not None:
        changed = {Path(f).resolve() for f in args.changed_files}
        in_scope = [c for c in results["expired"] if Path(c["file"]).resolve() in changed]
        err_scope = [e for e in results["errors"] if Path(e["file"]).resolve() in changed]
        print(f"\nexpired-claims total={expired_count} in-changed-files={len(in_scope)} "
              f"unreadable total={len(results['errors'])} in-changed-files={len(err_scope)} "
              f"files-checked={results['checked_files']} date={results['check_date']}")
        if err_scope:
            print("\n❌ Unreadable measurement-claims in files this change touches (exit code 1):")
            for e in err_scope:
                print(f"   - {e['file']}: {e['error']}")
            return 1
        if in_scope:
            print("\n❌ Expired claims in files this change touches (exit code 1):")
            for c in in_scope:
                print(f"   - {c['file']}: {c['claim'][:60]} (revalidate {c['revalidate']})")
            return 1
        print("\n✅ No expired claims in the changed files (exit code 0)")
        return 0

    if results["errors"]:
        print(f"\n❌ {len(results['errors'])} file(s) with unreadable measurement-claims (exit code 1)")
        return 1

    # Exit with error code if expired claims found
    if expired_count > 0:
        print("\n❌ Expired claims found (exit code 1)")
        return 1

    print("\n✅ All measurement claims current (exit code 0)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
