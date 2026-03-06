"""Models for the PFR Player Birthplaces pages.

Landing page (``/friv/birthplaces.htm``):
    Summary table listing countries/states with player counts and notable players.

Filtered page (``/friv/birthplaces.cgi?country=...&state=...``):
    Individual players born in the selected location with career statistics.
"""

from __future__ import annotations

from typing import List, Optional

from ..base import PFRBaseModel

# ── Landing page ─────────────────────────────────────────────────────────


class BirthplaceLocation(PFRBaseModel):
    """A country/state row from the birthplaces landing page."""

    rank: int
    birth_country: str
    birth_country_href: Optional[str] = None
    birth_state: Optional[str] = None
    players: Optional[int] = None
    players_active: Optional[int] = None
    hofers: Optional[int] = None
    g: Optional[int] = None
    td: Optional[int] = None
    player_most_td: Optional[str] = None
    player_most_td_href: Optional[str] = None
    player_most_td_id: Optional[str] = None
    most_td: Optional[int] = None
    player_most_g: Optional[str] = None
    player_most_g_href: Optional[str] = None
    player_most_g_id: Optional[str] = None
    most_g: Optional[int] = None


class BirthplaceLanding(PFRBaseModel):
    """Top-level result for the birthplaces landing page."""

    title: str
    locations: List[BirthplaceLocation]


# ── Filtered page ────────────────────────────────────────────────────────


class BirthplacePlayer(PFRBaseModel):
    """A player born in the filtered location with career statistics."""

    rank: int
    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    pos: Optional[str] = None
    birth_city: Optional[str] = None
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


class BirthplaceFiltered(PFRBaseModel):
    """Top-level result for a filtered birthplaces page."""

    title: str
    country: str
    state: str
    players: List[BirthplacePlayer]
