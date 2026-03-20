from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class StyleProfile:
    risk_preference: str = "平衡"
    horizon: str = "中期"
    focus_sectors: list[str] = field(default_factory=list)
    preferred_factors: list[str] = field(default_factory=list)
    reasoning_patterns: list[str] = field(default_factory=list)
    watch_signals: list[str] = field(default_factory=list)
    learned_samples: int = 0
    updated_at: str = ""

    def touch(self) -> None:
        self.updated_at = datetime.now().isoformat(timespec="seconds")

    def merge(self, data: dict[str, Any]) -> None:
        self.risk_preference = data.get("risk_preference", self.risk_preference)
        self.horizon = data.get("horizon", self.horizon)
        self.focus_sectors = _merge_unique(self.focus_sectors, data.get("focus_sectors", []))
        self.preferred_factors = _merge_unique(self.preferred_factors, data.get("preferred_factors", []))
        self.reasoning_patterns = _merge_unique(self.reasoning_patterns, data.get("reasoning_patterns", []))
        self.watch_signals = _merge_unique(self.watch_signals, data.get("watch_signals", []))
        self.learned_samples += 1
        self.touch()

    def to_dict(self) -> dict[str, Any]:
        return {
            "risk_preference": self.risk_preference,
            "horizon": self.horizon,
            "focus_sectors": self.focus_sectors,
            "preferred_factors": self.preferred_factors,
            "reasoning_patterns": self.reasoning_patterns,
            "watch_signals": self.watch_signals,
            "learned_samples": self.learned_samples,
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any] | None) -> "StyleProfile":
        if not data:
            profile = cls()
            profile.touch()
            return profile
        return cls(
            risk_preference=data.get("risk_preference", "平衡"),
            horizon=data.get("horizon", "中期"),
            focus_sectors=data.get("focus_sectors", []),
            preferred_factors=data.get("preferred_factors", []),
            reasoning_patterns=data.get("reasoning_patterns", []),
            watch_signals=data.get("watch_signals", []),
            learned_samples=int(data.get("learned_samples", 0)),
            updated_at=data.get("updated_at", ""),
        )


def _merge_unique(base: list[str], incoming: list[str]) -> list[str]:
    seen = set()
    merged: list[str] = []
    for item in [*base, *incoming]:
        normalized = item.strip()
        if not normalized:
            continue
        if normalized not in seen:
            seen.add(normalized)
            merged.append(normalized)
    return merged
