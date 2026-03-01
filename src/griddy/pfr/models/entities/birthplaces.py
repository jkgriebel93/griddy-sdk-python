"""Models for the PFR Player Birthplaces pages.

Landing page (``/friv/birthplaces.htm``):
    Summary table listing countries/states with player counts and notable players.

Filtered page (``/friv/birthplaces.cgi?country=...&state=...``):
    Individual players born in the selected location with career statistics.
"""

from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from ...types import BaseModel

# ── Landing page ─────────────────────────────────────────────────────────


class BirthplaceLocationTypedDict(TypedDict):
    rank: int
    birth_country: str
    birth_country_href: NotRequired[Optional[str]]
    birth_state: NotRequired[Optional[str]]
    players: NotRequired[Optional[int]]
    players_active: NotRequired[Optional[int]]
    hofers: NotRequired[Optional[int]]
    g: NotRequired[Optional[int]]
    td: NotRequired[Optional[int]]
    player_most_td: NotRequired[Optional[str]]
    player_most_td_href: NotRequired[Optional[str]]
    player_most_td_id: NotRequired[Optional[str]]
    most_td: NotRequired[Optional[int]]
    player_most_g: NotRequired[Optional[str]]
    player_most_g_href: NotRequired[Optional[str]]
    player_most_g_id: NotRequired[Optional[str]]
    most_g: NotRequired[Optional[int]]


class BirthplaceLocation(BaseModel):
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


class BirthplaceLandingTypedDict(TypedDict):
    title: str
    locations: List[BirthplaceLocationTypedDict]


class BirthplaceLanding(BaseModel):
    title: str
    locations: List[BirthplaceLocation]


# ── Filtered page ────────────────────────────────────────────────────────


class BirthplacePlayerTypedDict(TypedDict):
    rank: int
    player: str
    player_href: NotRequired[Optional[str]]
    player_id: NotRequired[Optional[str]]
    pos: NotRequired[Optional[str]]
    birth_city: NotRequired[Optional[str]]
    year_min: NotRequired[Optional[int]]
    year_max: NotRequired[Optional[int]]
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


class BirthplacePlayer(BaseModel):
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


class BirthplaceFilteredTypedDict(TypedDict):
    title: str
    country: str
    state: str
    players: List[BirthplacePlayerTypedDict]


class BirthplaceFiltered(BaseModel):
    title: str
    country: str
    state: str
    players: List[BirthplacePlayer]
