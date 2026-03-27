"""Source registry resource."""

from pathlib import Path
from typing import Optional

from ..parsers.sources_parser import SourcesParser, SourceEntry


class SourceRegistry:
    """Registry of all sources from SOURCES.md."""

    def __init__(self, sources_file: Path):
        self.sources_file = sources_file
        self.parser = SourcesParser(sources_file)
        self._sources: list[SourceEntry] = []
        self._loaded = False

    async def refresh(self) -> None:
        """Reload sources from disk."""
        self._sources = self.parser.parse()
        self._loaded = True

    def get_all(self) -> list[SourceEntry]:
        """Get all sources."""
        if not self._loaded:
            self._sources = self.parser.parse()
            self._loaded = True
        return self._sources

    def get_by_id(self, source_id: str) -> Optional[SourceEntry]:
        """Get source by ID."""
        sources = self.get_all()
        for source in sources:
            if source.id == source_id:
                return source
        return None

    def get_by_tier(self, tier: str) -> list[SourceEntry]:
        """Get sources by tier."""
        return [s for s in self.get_all() if s.tier == tier.upper()]

    def get_by_url(self, url: str) -> Optional[SourceEntry]:
        """Get source by URL."""
        for source in self.get_all():
            if source.url == url:
                return source
        return None

    def get_sources_for_pattern(self, pattern_id: str) -> list[SourceEntry]:
        """Get sources that reference a pattern."""
        return [s for s in self.get_all() if pattern_id in s.pattern_refs]

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "total_sources": len(self.get_all()),
            "sources": [s.to_dict() for s in self.get_all()],
            "by_tier": {
                tier: len(self.get_by_tier(tier))
                for tier in ["A", "B", "C", "D"]
            },
            "by_type": self._count_by_type()
        }

    def _count_by_type(self) -> dict[str, int]:
        """Count sources by type."""
        counts: dict[str, int] = {}
        for source in self.get_all():
            source_type = source.source_type or "unknown"
            counts[source_type] = counts.get(source_type, 0) + 1
        return counts
