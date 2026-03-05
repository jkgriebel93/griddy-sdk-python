"""Models for the PFR 'Cups of Coffee' page.

Represents players who played only a single game in the NFL, with their
career statistics from that one game.
"""

from __future__ import annotations

from typing import List, Optional

from ...types import BaseModel


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


class CupsOfCoffee(BaseModel):
    """Parsed result of the PFR 'Cups of Coffee' page."""

    title: str
    entries: List[CoffeeEntry]
