"""Pydantic models for PFR NFL Draft pages.

Covers three page types:
- ``/years/{year}/draft.htm`` — annual draft results
- ``/draft/{year}-combine.htm`` — NFL Combine measurements
- ``/teams/{team}/draft.htm`` — team-specific draft history
"""

from __future__ import annotations

from typing import List, Optional

from ..base import PFRBaseModel

# ---------------------------------------------------------------------------
# Year Draft Pick (one row in /years/{year}/draft.htm)
# ---------------------------------------------------------------------------


class DraftPick(PFRBaseModel):
    draft_round: Optional[int] = None
    draft_pick: Optional[int] = None
    team: Optional[str] = None
    team_href: Optional[str] = None
    player: Optional[str] = None
    player_id: Optional[str] = None
    player_href: Optional[str] = None
    pos: Optional[str] = None
    age: Optional[int] = None
    year_max: Optional[int] = None
    all_pros_first_team: Optional[int] = None
    pro_bowls: Optional[int] = None
    years_as_primary_starter: Optional[int] = None
    career_av: Optional[int] = None
    draft_av: Optional[int] = None
    g: Optional[int] = None
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
    def_int: Optional[int] = None
    sacks: Optional[float] = None
    college: Optional[str] = None
    college_href: Optional[str] = None
    college_stats_href: Optional[str] = None


# ---------------------------------------------------------------------------
# Year Draft (top-level for /years/{year}/draft.htm)
# ---------------------------------------------------------------------------


class YearDraft(PFRBaseModel):
    year: Optional[int] = None
    picks: List[DraftPick] = []


# ---------------------------------------------------------------------------
# Combine Entry (one row in /draft/{year}-combine.htm)
# ---------------------------------------------------------------------------


class CombineEntry(PFRBaseModel):
    player: Optional[str] = None
    player_id: Optional[str] = None
    player_href: Optional[str] = None
    pos: Optional[str] = None
    school: Optional[str] = None
    school_href: Optional[str] = None
    college_stats_href: Optional[str] = None
    height: Optional[str] = None
    weight: Optional[int] = None
    forty_yd: Optional[float] = None
    vertical: Optional[float] = None
    bench_reps: Optional[int] = None
    broad_jump: Optional[int] = None
    cone: Optional[float] = None
    shuttle: Optional[float] = None
    draft_info: Optional[str] = None
    drafted_team: Optional[str] = None
    drafted_round: Optional[str] = None
    drafted_pick: Optional[str] = None
    drafted_year: Optional[int] = None


# ---------------------------------------------------------------------------
# Combine Results (top-level for /draft/{year}-combine.htm)
# ---------------------------------------------------------------------------


class CombineResults(PFRBaseModel):
    year: Optional[int] = None
    entries: List[CombineEntry] = []


# ---------------------------------------------------------------------------
# Team Draft Pick (one row in /teams/{team}/draft.htm)
# ---------------------------------------------------------------------------


class TeamDraftPick(PFRBaseModel):
    year: Optional[int] = None
    year_href: Optional[str] = None
    draft_round: Optional[int] = None
    player: Optional[str] = None
    player_id: Optional[str] = None
    player_href: Optional[str] = None
    draft_pick: Optional[int] = None
    pos: Optional[str] = None
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
    pass_int: Optional[int] = None
    rush_att: Optional[int] = None
    rush_yds: Optional[int] = None
    rush_td: Optional[int] = None
    rec: Optional[int] = None
    rec_yds: Optional[int] = None
    rec_td: Optional[int] = None
    def_int: Optional[int] = None
    sacks: Optional[float] = None
    college: Optional[str] = None
    college_href: Optional[str] = None


# ---------------------------------------------------------------------------
# Team Draft (top-level for /teams/{team}/draft.htm)
# ---------------------------------------------------------------------------


class TeamDraft(PFRBaseModel):
    team: Optional[str] = None
    picks: List[TeamDraftPick] = []
