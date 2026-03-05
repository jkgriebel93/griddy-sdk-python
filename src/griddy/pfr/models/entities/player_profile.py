from __future__ import annotations

from datetime import date, datetime
from typing import Any, Dict, List, Optional, Union

from pydantic import field_validator

from ...types import BaseModel

# --- Player Names ---


class PlayerNames(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    suffix: str
    nicknames: List[str]
    pretty_name: str


# --- Birth Place ---


class BirthPlace(BaseModel):
    city: str
    state: str


# --- Draft Info ---


class RoundAndOverall(BaseModel):
    round: int
    overall: int


class DraftInfo(BaseModel):
    team: str
    rd_and_ovr: RoundAndOverall
    year: int


# --- Player Bio ---


class PlayerBio(BaseModel):
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

    @field_validator("draft", mode="before")
    @classmethod
    def _empty_dict_to_none(cls, v: Any) -> Any:
        if isinstance(v, dict) and not v:
            return None
        return v


# --- Jersey Number ---


class JerseyNumber(BaseModel):
    number: str
    team: str
    start_year: int
    end_year: int


# --- Transaction ---


class Transaction(BaseModel):
    date: date
    description: str


# --- Player Statistics ---


class PlayerStatistics(BaseModel):
    regular_season: Dict[str, List[Dict[str, Any]]] = {}
    post_season: Dict[str, List[Dict[str, Any]]] = {}


# --- Player Profile (top-level) ---


class PlayerProfile(BaseModel):
    bio: PlayerBio
    jersey_numbers: List[JerseyNumber]
    summary_stats: Dict[str, Union[int, float, str]]
    statistics: PlayerStatistics
    transactions: List[Transaction]
    links: Dict[str, Dict[str, str]]
    leader_boards: Dict[str, List[str]]
