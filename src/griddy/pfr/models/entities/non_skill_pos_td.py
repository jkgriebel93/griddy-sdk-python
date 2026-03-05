"""Models for the PFR 'Non-Skill Position TD Scorers' page.

Represents game-level instances of non-skill position players scoring
an offensive touchdown, with rushing and receiving stats for that game.
"""

from __future__ import annotations

from typing import List, Optional

from ...types import BaseModel


class NonSkillPosTdEntry(BaseModel):
    """A single game instance of a non-skill position player scoring a TD."""

    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    pos: str
    week_num: Optional[int] = None
    game_day_of_week: Optional[str] = None
    game_date: Optional[str] = None
    boxscore_href: Optional[str] = None
    game_outcome: Optional[str] = None
    team: Optional[str] = None
    team_href: Optional[str] = None
    game_location: Optional[str] = None
    opp: Optional[str] = None
    opp_href: Optional[str] = None
    pts_off: Optional[int] = None
    pts_def: Optional[int] = None
    rush_att: Optional[int] = None
    rush_yds: Optional[int] = None
    rush_long: Optional[int] = None
    rush_yds_per_att: Optional[float] = None
    rush_td: Optional[int] = None
    rec: Optional[int] = None
    rec_yds: Optional[int] = None
    rec_long: Optional[int] = None
    rec_yds_per_rec: Optional[float] = None
    rec_td: Optional[int] = None


class NonSkillPosTdScorers(BaseModel):
    """Parsed result of the PFR non-skill position TD scorers page."""

    title: str
    entries: List[NonSkillPosTdEntry]
