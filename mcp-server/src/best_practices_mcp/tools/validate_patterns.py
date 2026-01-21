"""Pattern validation tool."""

import asyncio
import re
from pathlib import Path
from typing import Any, Optional

import httpx

from ..resources.pattern_registry import PatternRegistry
from ..resources.source_registry import SourceRegistry


async def validate_patterns(
    action: str,
    pattern_id: Optional[str],
    validation_type: str,
    pattern_registry: PatternRegistry,
    source_registry: SourceRegistry,
    repo_root: Path,
) -> dict[str, Any]:
    """Validate patterns for structure, links, evidence, and cross-references."""

    if action == "validate_single":
        if not pattern_id:
            return {"error": "pattern_id required for validate_single action"}
        pattern = pattern_registry.get_by_id(pattern_id)
        if not pattern:
            return {"error": f"Pattern not found: {pattern_id}"}
        results = [await _validate_pattern(pattern, validation_type, source_registry, repo_root)]

    elif action == "validate_all":
        patterns = pattern_registry.get_all()
        results = await asyncio.gather(*[
            _validate_pattern(p, validation_type, source_registry, repo_root)
            for p in patterns
        ])

    elif action == "check_links":
        patterns = pattern_registry.get_all()
        results = await asyncio.gather(*[
            _validate_pattern(p, "links", source_registry, repo_root)
            for p in patterns
        ])

    elif action == "check_evidence":
        patterns = pattern_registry.get_all()
        results = await asyncio.gather(*[
            _validate_pattern(p, "evidence", source_registry, repo_root)
            for p in patterns
        ])

    else:
        return {"error": f"Unknown action: {action}"}

    # Summarize results
    valid = sum(1 for r in results if r["status"] == "valid")
    needs_update = sum(1 for r in results if r["status"] == "needs-update")
    broken = sum(1 for r in results if r["status"] == "broken")

    return {
        "action": action,
        "patterns_checked": len(results),
        "results": results,
        "summary": {
            "valid": valid,
            "needs_update": needs_update,
            "broken": broken
        }
    }


async def _validate_pattern(
    pattern,
    validation_type: str,
    source_registry: SourceRegistry,
    repo_root: Path,
) -> dict[str, Any]:
    """Validate a single pattern."""
    issues: list[dict] = []

    if validation_type in ("structure", "full"):
        issues.extend(_check_structure(pattern))

    if validation_type in ("links", "full"):
        link_issues = await _check_links(pattern, repo_root)
        issues.extend(link_issues)

    if validation_type in ("evidence", "full"):
        issues.extend(_check_evidence(pattern, source_registry))

    if validation_type in ("cross-refs", "full"):
        issues.extend(_check_cross_refs(pattern, repo_root))

    # Determine status
    has_errors = any(i["severity"] == "error" for i in issues)
    has_warnings = any(i["severity"] == "warning" for i in issues)

    if has_errors:
        status = "broken"
    elif has_warnings:
        status = "needs-update"
    else:
        status = "valid"

    return {
        "pattern_id": pattern.id,
        "status": status,
        "issues": issues,
        "evidence_status": {
            "tier_claimed": pattern.evidence_tier,
            "sources_count": len(pattern.sources),
        }
    }


def _check_structure(pattern) -> list[dict]:
    """Check pattern has required structure."""
    issues = []

    # Required: Title (name)
    if not pattern.name:
        issues.append({
            "type": "missing_title",
            "description": "Pattern missing title (H1 header)",
            "severity": "error"
        })

    # Required: Evidence tier
    if not pattern.evidence_tier:
        issues.append({
            "type": "missing_evidence_tier",
            "description": "Pattern missing evidence tier declaration",
            "severity": "warning"
        })

    # Required: At least one source
    if not pattern.sources:
        issues.append({
            "type": "missing_sources",
            "description": "Pattern has no source references",
            "severity": "warning"
        })

    # Recommended: SDD phase
    if not pattern.sdd_phase:
        issues.append({
            "type": "missing_sdd_phase",
            "description": "Pattern missing SDD phase declaration",
            "severity": "info"
        })

    # Recommended sections
    recommended_sections = ["Implementation", "Example", "Related"]
    for section in recommended_sections:
        if not any(section.lower() in s.lower() for s in pattern.sections):
            issues.append({
                "type": "missing_section",
                "description": f"Pattern missing recommended section: {section}",
                "severity": "info"
            })

    return issues


async def _check_links(pattern, repo_root: Path) -> list[dict]:
    """Check internal and external links are valid."""
    issues = []

    # Check internal links
    for link in pattern.internal_links:
        # Resolve relative to pattern file
        pattern_dir = repo_root / Path(pattern.file_path).parent
        link_path = (pattern_dir / link).resolve()

        # Also try from repo root
        if not link_path.exists():
            link_path = (repo_root / link).resolve()

        if not link_path.exists():
            issues.append({
                "type": "broken_internal_link",
                "description": f"Internal link not found: {link}",
                "severity": "error"
            })

    # Check external links (sample a few to avoid rate limiting)
    external_sample = pattern.external_links[:3]  # Check max 3 external links
    async with httpx.AsyncClient(timeout=10.0, follow_redirects=True) as client:
        for url in external_sample:
            try:
                response = await client.head(url)
                # 403/429 are often false positives (rate limiting, bot blocking)
                # 404/410 are genuine broken links
                if response.status_code in (404, 410):
                    issues.append({
                        "type": "broken_external_link",
                        "description": f"External link returned {response.status_code}: {url}",
                        "severity": "warning"
                    })
                elif response.status_code >= 500:
                    issues.append({
                        "type": "external_link_server_error",
                        "description": f"External link server error {response.status_code}: {url}",
                        "severity": "info"
                    })
            except httpx.RequestError:
                # Connection errors are often transient or due to bot blocking
                pass  # Don't flag as issue

    return issues


def _check_evidence(pattern, source_registry: SourceRegistry) -> list[dict]:
    """Check evidence tier is properly supported."""
    issues = []

    if not pattern.evidence_tier:
        return issues

    tier = pattern.evidence_tier.upper()

    # Tier A requires primary sources (at least one documented source)
    if tier == "A":
        if not pattern.sources:
            issues.append({
                "type": "tier_mismatch",
                "description": "Tier A pattern has no documented sources",
                "severity": "warning"
            })

    # Tier B requires peer-reviewed or expert sources
    if tier == "B":
        if len(pattern.sources) < 1:
            issues.append({
                "type": "insufficient_sources",
                "description": "Tier B pattern should have expert or peer-reviewed sources",
                "severity": "warning"
            })

    # Check if sources exist in SOURCES.md
    for source in pattern.sources:
        url = source.get("url")
        if url and not source_registry.get_by_url(url):
            issues.append({
                "type": "undocumented_source",
                "description": f"Source not in SOURCES.md: {url}",
                "severity": "info"
            })

    return issues


def _check_cross_refs(pattern, repo_root: Path) -> list[dict]:
    """Check cross-references between patterns."""
    issues = []

    # Check related patterns exist
    patterns_dir = repo_root / "patterns"
    for related_id in pattern.related_patterns:
        related_path = patterns_dir / f"{related_id}.md"
        if not related_path.exists():
            issues.append({
                "type": "broken_pattern_ref",
                "description": f"Related pattern not found: {related_id}",
                "severity": "error"
            })

    return issues
