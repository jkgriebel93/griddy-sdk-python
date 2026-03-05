from __future__ import annotations

from datetime import date, datetime  # noqa: F401 — date used in Transaction annotation
from typing import Any, Dict, List, Optional, Union

from ..base import PFRBaseModel

# --- Player Names ---


class PlayerNames(PFRBaseModel):
    first_name: str
    middle_name: str
    last_name: str
    suffix: str
    nicknames: List[str]
    pretty_name: str


# --- Birth Place ---


class BirthPlace(PFRBaseModel):
    city: str
    state: str


# --- Draft Info ---


class RoundAndOverall(PFRBaseModel):
    round: int
    overall: int


class DraftInfo(PFRBaseModel):
    team: str
    rd_and_ovr: RoundAndOverall
    year: int


# --- Player Bio ---


class PlayerBio(PFRBaseModel):
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
    number: str
    team: str
    start_year: int
    end_year: int


# --- Transaction ---


class Transaction(PFRBaseModel):
    date: date
    description: str


# --- Player Statistics ---


class PlayerStatistics(PFRBaseModel):
    regular_season: Dict[str, List[Dict[str, Any]]] = {}
    post_season: Dict[str, List[Dict[str, Any]]] = {}


# --- Player Profile (top-level) ---


class PlayerProfile(PFRBaseModel):
    bio: PlayerBio
    jersey_numbers: List[JerseyNumber]
    summary_stats: Dict[str, Union[int, float, str]]
    statistics: PlayerStatistics
    transactions: List[Transaction]
    links: Dict[str, Dict[str, str]]
    leader_boards: Dict[str, List[str]]
