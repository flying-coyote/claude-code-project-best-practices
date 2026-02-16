#!/usr/bin/env python3
"""
Check for expired measurement claims in patterns/.

Scans pattern files for YAML frontmatter with measurement claims,
identifies claims past their re-validation date, and creates GitHub
issues for expired measurements.

Usage:
    python scripts/check-measurement-expiry.py
    python scripts/check-measurement-expiry.py --create-issue
"""

import argparse
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional

import yaml


class MeasurementExpiryChecker:
    """Check measurement claims for expiry dates."""

    def __init__(self, patterns_dir: Path):
        self.patterns_dir = patterns_dir
        self.expired_claims = []
        self.expiring_soon = []  # Within 30 days

    def check_all_patterns(self) -> Dict:
        """Scan all pattern files for expired measurement claims."""
        print(f"🔍 Checking measurement claims in {self.patterns_dir}...")

        pattern_files = list(self.patterns_dir.glob("*.md"))
        print(f"   Found {len(pattern_files)} pattern files")

        today = datetime.now().date()

        for pattern_file in pattern_files:
            self._check_pattern_file(pattern_file, today)

        return {
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

    def _extract_frontmatter(self, content: str) -> Optional[Dict]:
        """Extract YAML frontmatter from markdown file."""
        # Look for --- ... --- blocks
        frontmatter_pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL | re.MULTILINE)
        match = frontmatter_pattern.search(content)

        if not match:
            return None

        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError as e:
            print(f"   ⚠️  YAML parsing error: {e}")
            return None

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

        try:
            revalidate_date = datetime.strptime(revalidate_str, "%Y-%m-%d").date()
        except ValueError:
            print(f"   ⚠️  Invalid revalidate date format in {pattern_file}: {revalidate_str}")
            return

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
        body.append("1. Re-run benchmarks/tests with current Claude Code version\n")
        body.append("2. Update measurement claim if result changed\n")
        body.append("3. Update `revalidate` date to 1 year from today\n")
        body.append("4. If measurement no longer valid, mark as historical (see DEPRECATIONS.md)\n\n")

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
        body.append("- Add to quarterly audit checklist (see DOGFOODING-GAPS.md)\n\n")

    if not expired and not expiring_soon:
        body.append("✅ All measurement claims are current. No action required.\n\n")

    body.append("---\n\n")
    body.append("**Generated by**: `scripts/check-measurement-expiry.py`\n")
    body.append(f"**Timestamp**: {datetime.now().isoformat()}\n")

    return "".join(body)


def main():
    parser = argparse.ArgumentParser(description="Check for expired measurement claims")
    parser.add_argument("--create-issue", action="store_true", help="Create GitHub issue for expired claims")
    parser.add_argument("--patterns-dir", default="patterns", help="Patterns directory")
    args = parser.parse_args()

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
        # Write issue body to file (GitHub Actions will create issue from this)
        issue_file = Path("measurement-expiry-issue.md")
        issue_file.write_text(issue_body)
        print(f"\n✅ Issue body written to {issue_file}")
        print("   GitHub Actions will create issue from this file")
    else:
        print("\n📝 Issue Body Preview:")
        print("=" * 60)
        print(issue_body)
        print("=" * 60)
        print("\n💡 Run with --create-issue to generate issue file")

    # Exit with error code if expired claims found
    if expired_count > 0:
        print("\n❌ Expired claims found (exit code 1)")
        return 1

    print("\n✅ All measurement claims current (exit code 0)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
