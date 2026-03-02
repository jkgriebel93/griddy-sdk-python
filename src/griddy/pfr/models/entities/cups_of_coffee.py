"""Models for the PFR 'Cups of Coffee' page.

Represents players who played only a single game in the NFL, with their
career statistics from that one game.
"""

from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from ...types import BaseModel


class CoffeeEntryTypedDict(TypedDict):
    """TypedDict for a single 'cup of coffee' player."""

    player: str
    player_href: NotRequired[Optional[str]]
    player_id: NotRequired[Optional[str]]
    pos: NotRequired[Optional[str]]
    year_id: NotRequired[Optional[str]]
    all_pros_first_team: NotRequired[Optional[int]]
    pro_bowls: NotRequired[Optional[int]]
    years_as_primary_starter: NotRequired[Optional[int]]
    career_av: NotRequired[Optional[int]]
    g: NotRequired[Optional[int]]
    pass_cmp: NotRequired[Optional[int]]
    pass_att: NotRequired[Optional[int]]
    pass_yds: NotRequired[Optional[int]]
    pass_td: NotRequired[Optional[int]]
    pass_long: NotRequired[Optional[int]]
    pass_int: NotRequired[Optional[int]]
    pass_sacked: NotRequired[Optional[int]]
    pass_sacked_yds: NotRequired[Optional[int]]
    rush_att: NotRequired[Optional[int]]
    rush_yds: NotRequired[Optional[int]]
    rush_td: NotRequired[Optional[int]]
    rush_long: NotRequired[Optional[int]]
    rec: NotRequired[Optional[int]]
    rec_yds: NotRequired[Optional[int]]
    rec_td: NotRequired[Optional[int]]
    rec_long: NotRequired[Optional[int]]


class CoffeeEntry(BaseModel):
    """A single player who played only one NFL game."""

    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    pos: Optional[str] = None
    year_id: Optional[str] = None
    all_pros_first_team: Optional[int] = None
    pro_bowls: Optional[int] = None
    years_as_primary_starter: Optional[int] = None
    career_av: Optional[int] = None
    g: Optional[int] = None
    pass_cmp: Optional[int] = None
    pass_att: Optional[int] = None
    pass_yds: Optional[int] = None
    pass_td: Optional[int] = None
    pass_long: Optional[int] = None
    pass_int: Optional[int] = None
    pass_sacked: Optional[int] = None
    pass_sacked_yds: Optional[int] = None
    rush_att: Optional[int] = None
    rush_yds: Optional[int] = None
    rush_td: Optional[int] = None
    rush_long: Optional[int] = None
    rec: Optional[int] = None
    rec_yds: Optional[int] = None
    rec_td: Optional[int] = None
    rec_long: Optional[int] = None


class CupsOfCoffeeTypedDict(TypedDict):
    """TypedDict for the full cups of coffee page."""

    title: str
    entries: List[CoffeeEntryTypedDict]


class CupsOfCoffee(BaseModel):
    """Parsed result of the PFR 'Cups of Coffee' page."""

    title: str
    entries: List[CoffeeEntry]
