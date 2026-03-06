"""Pydantic models for PFR Awards, Hall of Fame, and Pro Bowl pages.

Covers three page types:
- ``/awards/{award}.htm`` — award history (table ``#awards``)
- ``/hof/`` — Hall of Fame inductees (table ``#hof_players``)
- ``/years/{year}/probowl.htm`` — Pro Bowl roster (table ``#pro_bowl``)
"""

from __future__ import annotations

from typing import List, Optional

from ..base import PFRBaseModel

# ---------------------------------------------------------------------------
# Award Winner (one row in /awards/{award}.htm)
# ---------------------------------------------------------------------------


class AwardWinner(PFRBaseModel):
    """A single award winner row from an award history page."""

    year: Optional[int] = None
    year_href: Optional[str] = None
    league: Optional[str] = None
    pos: Optional[str] = None
    player: Optional[str] = None
    player_id: Optional[str] = None
    player_href: Optional[str] = None
    team: Optional[str] = None
    team_href: Optional[str] = None
    voting_href: Optional[str] = None


# ---------------------------------------------------------------------------
# Award History (top-level for /awards/{award}.htm)
# ---------------------------------------------------------------------------


class AwardHistory(PFRBaseModel):
    """Top-level result for a PFR award history page."""

    award: Optional[str] = None
    winners: List[AwardWinner] = []


# ---------------------------------------------------------------------------
# HOF Player (one row in /hof/)
# ---------------------------------------------------------------------------


class HofPlayer(PFRBaseModel):
    """A single Hall of Fame inductee with career statistics."""

    rank: Optional[int] = None
    player: Optional[str] = None
    player_id: Optional[str] = None
    player_href: Optional[str] = None
    pos: Optional[str] = None
    year_induction: Optional[int] = None
    year_induction_href: Optional[str] = None
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
    all_purpose_yds: Optional[int] = None
    all_td: Optional[int] = None
    tackles_combined: Optional[int] = None
    sacks: Optional[float] = None
    def_int: Optional[int] = None


# ---------------------------------------------------------------------------
# Hall of Fame (top-level for /hof/)
# ---------------------------------------------------------------------------


class HallOfFame(PFRBaseModel):
    """Top-level result for the PFR Hall of Fame page."""

    players: List[HofPlayer] = []


# ---------------------------------------------------------------------------
# Pro Bowl Player (one row in /years/{year}/probowl.htm)
# ---------------------------------------------------------------------------


class ProBowlPlayer(PFRBaseModel):
    """A single Pro Bowl roster entry with season statistics."""

    pos: Optional[str] = None
    player: Optional[str] = None
    player_id: Optional[str] = None
    player_href: Optional[str] = None
    is_starter: Optional[bool] = None
    did_not_play: Optional[bool] = None
    is_replacement: Optional[bool] = None
    conference: Optional[str] = None
    team: Optional[str] = None
    team_href: Optional[str] = None
    age: Optional[int] = None
    experience: Optional[int] = None
    g: Optional[int] = None
    gs: Optional[int] = None
    pass_cmp: Optional[int] = None
    pass_att: Optional[int] = None
    pass_yds: Optional[int] = None
    pass_td: Optional[int] = None
    pass_int: Optional[int] = None
    rush_att: Optional[int] = None
    rush_yds: Optional[int] = None
    rush_td: Optional[int] = None
    rec: Optional[int] = None
    rec_yds: Optional[int] = None
    rec_td: Optional[int] = None
    tackles_solo: Optional[int] = None
    sacks: Optional[float] = None
    def_int: Optional[int] = None
    all_pro_string: Optional[str] = None


# ---------------------------------------------------------------------------
# Pro Bowl Roster (top-level for /years/{year}/probowl.htm)
# ---------------------------------------------------------------------------


class ProBowlRoster(PFRBaseModel):
    """Top-level result for a PFR Pro Bowl roster page."""

    year: Optional[int] = None
    players: List[ProBowlPlayer] = []
