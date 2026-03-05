"""Models for the PFR Active Players Born Before a Date page.

Page (``/friv/age.cgi?month=...&day=...&year=...``):
    Active players born on or before the specified date with career statistics.
"""

from __future__ import annotations

from typing import List, Optional

from ..base import PFRBaseModel


class PlayerBornBefore(PFRBaseModel):
    rank: int
    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    birth_date: Optional[str] = None
    age: Optional[int] = None
    pos: Optional[str] = None
    year_min: Optional[int] = None
    year_max: Optional[int] = None
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


class PlayersBornBefore(PFRBaseModel):
    title: str
    month: int
    day: int
    year: int
    players: List[PlayerBornBefore]
