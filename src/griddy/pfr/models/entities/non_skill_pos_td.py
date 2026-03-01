"""Models for the PFR 'Non-Skill Position TD Scorers' page.

Represents game-level instances of non-skill position players scoring
an offensive touchdown, with rushing and receiving stats for that game.
"""

from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from ...types import BaseModel


class NonSkillPosTdEntryTypedDict(TypedDict):
    """TypedDict for a single non-skill position TD scoring instance."""

    player: str
    player_href: NotRequired[Optional[str]]
    player_id: NotRequired[Optional[str]]
    pos: str
    week_num: NotRequired[Optional[int]]
    game_day_of_week: NotRequired[Optional[str]]
    game_date: NotRequired[Optional[str]]
    boxscore_href: NotRequired[Optional[str]]
    game_outcome: NotRequired[Optional[str]]
    team: NotRequired[Optional[str]]
    team_href: NotRequired[Optional[str]]
    game_location: NotRequired[Optional[str]]
    opp: NotRequired[Optional[str]]
    opp_href: NotRequired[Optional[str]]
    pts_off: NotRequired[Optional[int]]
    pts_def: NotRequired[Optional[int]]
    rush_att: NotRequired[Optional[int]]
    rush_yds: NotRequired[Optional[int]]
    rush_long: NotRequired[Optional[int]]
    rush_yds_per_att: NotRequired[Optional[float]]
    rush_td: NotRequired[Optional[int]]
    rec: NotRequired[Optional[int]]
    rec_yds: NotRequired[Optional[int]]
    rec_long: NotRequired[Optional[int]]
    rec_yds_per_rec: NotRequired[Optional[float]]
    rec_td: NotRequired[Optional[int]]


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


class NonSkillPosTdScorersTypedDict(TypedDict):
    """TypedDict for the full non-skill position TD scorers page."""

    title: str
    entries: List[NonSkillPosTdEntryTypedDict]


class NonSkillPosTdScorers(BaseModel):
    """Parsed result of the PFR non-skill position TD scorers page."""

    title: str
    entries: List[NonSkillPosTdEntry]
