"""Pydantic models for a PFR player profile page.

Covers ``/players/{letter}/{player_id}.htm`` pages on Pro Football Reference,
including biographical info, jersey numbers, career statistics, and transactions.
"""

from __future__ import annotations

from datetime import date, datetime  # noqa: F401 — date used in Transaction annotation
from typing import Any, Dict, List, Optional, Union

from ..base import PFRBaseModel

# --- Player Names ---


class PlayerNames(PFRBaseModel):
    """Parsed player name components (first, middle, last, suffix, nicknames)."""

    first_name: str
    middle_name: str
    last_name: str
    suffix: str
    nicknames: List[str]
    pretty_name: str


# --- Birth Place ---


class BirthPlace(PFRBaseModel):
    """City and state of a player's birth."""

    city: str
    state: str


# --- Draft Info ---


class RoundAndOverall(PFRBaseModel):
    """Draft round and overall pick number."""

    round: int
    overall: int


class DraftInfo(PFRBaseModel):
    """Draft selection details (team, round/overall, and year)."""

    team: str
    rd_and_ovr: RoundAndOverall
    year: int


# --- Player Bio ---


class PlayerBio(PFRBaseModel):
    """Biographical information from the player profile meta panel."""

    photo_url: str
    names: PlayerNames
    position: str
    height: int
    weight: str
    birth_date: datetime
    birth_place: BirthPlace
    college: str
    high_school: str
    draft: Optional[DraftInfo] = None
    throws: Optional[str] = None


# --- Jersey Number ---


class JerseyNumber(PFRBaseModel):
    """A jersey number worn by the player for a team and year range."""

    number: str
    team: str
    start_year: int
    end_year: int


# --- Transaction ---


class Transaction(PFRBaseModel):
    """A roster transaction (signing, trade, release, etc.) with date."""

    date: date
    description: str


# --- Player Statistics ---


class PlayerStatistics(PFRBaseModel):
    """Regular-season and post-season stat tables keyed by category."""

    regular_season: Dict[str, List[Dict[str, Any]]] = {}
    post_season: Dict[str, List[Dict[str, Any]]] = {}


# --- Player Profile (top-level) ---


class PlayerProfile(PFRBaseModel):
    """Top-level model for a full PFR player profile page."""

    bio: PlayerBio
    jersey_numbers: List[JerseyNumber]
    summary_stats: Dict[str, Union[int, float, str]]
    statistics: PlayerStatistics
    transactions: List[Transaction]
    links: Dict[str, Dict[str, str]]
    leader_boards: Dict[str, List[str]]
