"""Pattern registry resource."""

from pathlib import Path
from typing import Optional

from ..parsers.markdown_parser import MarkdownParser, PatternMetadata


class PatternRegistry:
    """Registry of all documented patterns."""

    def __init__(self, patterns_dir: Path):
        self.patterns_dir = patterns_dir
        self.parser = MarkdownParser(patterns_dir)
        self._patterns: list[PatternMetadata] = []
        self._loaded = False

    async def refresh(self) -> None:
        """Reload patterns from disk."""
        self._patterns = self.parser.parse_all()
        self._loaded = True

    def get_all(self) -> list[PatternMetadata]:
        """Get all patterns."""
        if not self._loaded:
            self._patterns = self.parser.parse_all()
            self._loaded = True
        return self._patterns

    def get_by_id(self, pattern_id: str) -> Optional[PatternMetadata]:
        """Get pattern by ID."""
        patterns = self.get_all()
        for pattern in patterns:
            if pattern.id == pattern_id:
                return pattern
        return None

    def get_by_tier(self, tier: str) -> list[PatternMetadata]:
        """Get patterns by evidence tier."""
        return [p for p in self.get_all() if p.evidence_tier == tier.upper()]

    def get_by_phase(self, phase: str) -> list[PatternMetadata]:
        """Get patterns by SDD phase."""
        return [p for p in self.get_all() if p.sdd_phase == phase.lower()]

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "total_patterns": len(self.get_all()),
            "patterns": [p.to_dict() for p in self.get_all()],
            "by_tier": {
                tier: len(self.get_by_tier(tier))
                for tier in ["A", "B", "C", "D"]
            },
            "by_phase": {
                phase: len(self.get_by_phase(phase))
                for phase in ["foundational", "specify", "plan", "tasks", "implement", "cross-phase"]
            }
        }
