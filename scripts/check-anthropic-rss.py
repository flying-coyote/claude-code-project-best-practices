#!/usr/bin/env python3
"""
Check Anthropic blog RSS feed for new posts.

Fetches RSS feed, compares with SOURCES.md, and identifies new posts
that should be analyzed for Claude Code best practices updates.

Usage:
    python scripts/check-anthropic-rss.py
    python scripts/check-anthropic-rss.py --create-issue
    python scripts/check-anthropic-rss.py --rss-url https://custom-feed.xml
"""

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional
from xml.etree import ElementTree as ET

try:
    import requests
except ImportError:
    print("⚠️  requests library not found. Install with: pip install requests")
    sys.exit(1)


class AnthropicRSSChecker:
    """Check Anthropic blog RSS feed for new posts."""

    DEFAULT_RSS_URL = "https://www.anthropic.com/rss.xml"
    CACHE_FILE = Path(".cache/anthropic-rss.json")
    SOURCES_FILE = Path("SOURCES.md")

    def __init__(self, rss_url: Optional[str] = None):
        self.rss_url = rss_url or self.DEFAULT_RSS_URL
        self.cache = self._load_cache()
        self.sources_urls = self._load_sources_urls()

    def _load_cache(self) -> Dict:
        """Load cached RSS entries."""
        if not self.CACHE_FILE.exists():
            return {"entries": [], "last_check": None}

        try:
            with open(self.CACHE_FILE, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️  Error loading cache: {e}")
            return {"entries": [], "last_check": None}

    def _save_cache(self, entries: List[Dict]):
        """Save RSS entries to cache."""
        self.CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)

        cache_data = {
            "entries": entries,
            "last_check": datetime.now().isoformat(),
        }

        with open(self.CACHE_FILE, 'w') as f:
            json.dump(cache_data, f, indent=2)

    def _load_sources_urls(self) -> set:
        """Extract all URLs from SOURCES.md."""
        if not self.SOURCES_FILE.exists():
            print(f"⚠️  {self.SOURCES_FILE} not found")
            return set()

        content = self.SOURCES_FILE.read_text()

        # Extract URLs (markdown links and plain URLs)
        url_pattern = re.compile(r'https?://[^\s\)]+')
        urls = set(url_pattern.findall(content))

        print(f"📚 Loaded {len(urls)} URLs from {self.SOURCES_FILE}")
        return urls

    def fetch_rss_feed(self) -> List[Dict]:
        """Fetch and parse RSS feed."""
        print(f"🌐 Fetching RSS feed from {self.rss_url}...")

        try:
            response = requests.get(self.rss_url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"❌ Error fetching RSS feed: {e}")
            return []

        # Parse XML
        try:
            root = ET.fromstring(response.content)
        except ET.ParseError as e:
            print(f"❌ Error parsing RSS XML: {e}")
            return []

        # Extract entries
        entries = []
        for item in root.findall(".//item"):
            entry = {
                "title": item.findtext("title", "Untitled"),
                "link": item.findtext("link", ""),
                "pubDate": item.findtext("pubDate", ""),
                "description": item.findtext("description", "")[:200],  # First 200 chars
                "guid": item.findtext("guid", ""),
            }

            # Generate hash for deduplication
            entry_hash = hashlib.md5(entry["link"].encode()).hexdigest()
            entry["hash"] = entry_hash

            entries.append(entry)

        print(f"   Found {len(entries)} entries in RSS feed")
        return entries

    def detect_new_posts(self, current_entries: List[Dict]) -> List[Dict]:
        """Compare current entries with cached entries and SOURCES.md."""
        cached_hashes = set(e["hash"] for e in self.cache.get("entries", []))

        new_posts = []
        for entry in current_entries:
            # Check if URL already in SOURCES.md
            if entry["link"] in self.sources_urls:
                continue  # Already documented

            # Check if in cache (seen before but not in SOURCES.md yet)
            if entry["hash"] in cached_hashes:
                continue  # Already detected, waiting for human review

            # This is a new post!
            new_posts.append(entry)

        return new_posts

    def run(self) -> Dict:
        """Run RSS check and return results."""
        current_entries = self.fetch_rss_feed()

        if not current_entries:
            return {
                "new_posts": [],
                "error": "Failed to fetch RSS feed",
            }

        new_posts = self.detect_new_posts(current_entries)

        # Update cache
        self._save_cache(current_entries)

        return {
            "new_posts": new_posts,
            "total_entries": len(current_entries),
            "check_date": datetime.now().isoformat(),
        }


def generate_issue_body(results: Dict) -> str:
    """Generate GitHub issue body for new blog posts."""
    body = []
    body.append("## New Anthropic Blog Posts Detected\n\n")
    body.append(f"**Check Date**: {results['check_date']}\n")
    body.append(f"**Total Entries**: {results['total_entries']}\n\n")

    new_posts = results["new_posts"]

    if not new_posts:
        body.append("✅ No new posts detected. All blog posts are documented in SOURCES.md.\n\n")
        return "".join(body)

    body.append(f"### 🆕 New Posts ({len(new_posts)})\n\n")

    for i, post in enumerate(new_posts, 1):
        body.append(f"#### {i}. {post['title']}\n\n")
        body.append(f"**URL**: {post['link']}\n")
        body.append(f"**Published**: {post['pubDate']}\n")
        body.append(f"**Description**: {post['description']}...\n\n")

        body.append("**Action Required**:\n")
        body.append("1. Review blog post content\n")
        body.append("2. Run `scripts/analyze-blog-post.py` to extract Claude Code patterns\n")
        body.append("3. Update affected pattern files\n")
        body.append("4. Add URL to SOURCES.md with evidence tier\n\n")

        body.append("**AI Analysis** (run this command):\n")
        body.append(f"```bash\n")
        body.append(f"python scripts/analyze-blog-post.py --url '{post['link']}'\n")
        body.append(f"```\n\n")

        body.append("---\n\n")

    body.append("**Next Steps**:\n")
    body.append("1. Assign this issue to a team member\n")
    body.append("2. Analyze each new post for Claude Code relevance\n")
    body.append("3. Update patterns if new recommendations found\n")
    body.append("4. Close issue when all posts processed\n\n")

    body.append("---\n\n")
    body.append("**Generated by**: `scripts/check-anthropic-rss.py`\n")
    body.append(f"**Timestamp**: {datetime.now().isoformat()}\n")

    return "".join(body)


def main():
    parser = argparse.ArgumentParser(description="Check Anthropic blog RSS for new posts")
    parser.add_argument("--rss-url", help="Custom RSS feed URL")
    parser.add_argument("--create-issue", action="store_true", help="Create GitHub issue for new posts")
    args = parser.parse_args()

    # Run RSS check
    checker = AnthropicRSSChecker(rss_url=args.rss_url)
    results = checker.run()

    # Print summary
    new_posts_count = len(results.get("new_posts", []))

    print(f"\n📊 Summary:")
    print(f"   Total entries: {results.get('total_entries', 0)}")
    print(f"   🆕 New posts: {new_posts_count}")

    if new_posts_count > 0:
        print(f"\n🆕 NEW POSTS DETECTED:")
        for post in results["new_posts"]:
            print(f"   - {post['title']}")
            print(f"     {post['link']}")

    # Generate issue body
    issue_body = generate_issue_body(results)

    if args.create_issue:
        # Write issue body to file
        issue_file = Path("anthropic-rss-issue.md")
        issue_file.write_text(issue_body)
        print(f"\n✅ Issue body written to {issue_file}")
        print("   GitHub Actions will create issue from this file")
    else:
        print("\n📝 Issue Body Preview:")
        print("=" * 60)
        print(issue_body)
        print("=" * 60)
        print("\n💡 Run with --create-issue to generate issue file")

    # Exit with success code (new posts are informational, not errors)
    if new_posts_count > 0:
        print(f"\n✅ {new_posts_count} new post(s) detected (exit code 0)")
    else:
        print("\n✅ No new posts (exit code 0)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
