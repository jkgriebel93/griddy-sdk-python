"""Models for the PFR 'Pronunciation Guide' page.

Represents players with difficult-to-pronounce names and their phonetic
pronunciation guides, sourced from NFL and team media guides.
"""

from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from ...types import BaseModel


class PronunciationEntryTypedDict(TypedDict):
    """TypedDict for a single pronunciation guide entry."""

    player: str
    player_href: NotRequired[Optional[str]]
    player_id: NotRequired[Optional[str]]
    pronunciation: str


class PronunciationEntry(BaseModel):
    """A single player name with its phonetic pronunciation."""

    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    pronunciation: str


class PronunciationGuideTypedDict(TypedDict):
    """TypedDict for the full pronunciation guide page."""

    title: str
    entries: List[PronunciationEntryTypedDict]


class PronunciationGuide(BaseModel):
    """Parsed result of the PFR 'Pronunciation Guide' page."""

    title: str
    entries: List[PronunciationEntry]
