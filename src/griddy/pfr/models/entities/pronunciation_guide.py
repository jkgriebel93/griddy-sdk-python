"""Models for the PFR 'Pronunciation Guide' page.

Represents players with difficult-to-pronounce names and their phonetic
pronunciation guides, sourced from NFL and team media guides.
"""

from __future__ import annotations

from typing import List, Optional

from ..base import PFRBaseModel


class PronunciationEntry(PFRBaseModel):
    """A single player name with its phonetic pronunciation."""

    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    pronunciation: str


class PronunciationGuide(PFRBaseModel):
    """Parsed result of the PFR 'Pronunciation Guide' page."""

    title: str
    entries: List[PronunciationEntry]
