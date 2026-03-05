"""Models for the PFR 'Multisport Athletes' page.

Represents athletes who played multiple sports professionally, including
their NFL career statistics and links to their profiles on other sports
reference sites.
"""

from __future__ import annotations

from typing import List, Optional

from ..base import PFRBaseModel


class OtherSportLink(PFRBaseModel):
    """A link to another sports reference site for a multi-sport athlete."""

    text: str
    href: str


class MultiSportPlayer(PFRBaseModel):
    """A single athlete who played multiple sports professionally."""

    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
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
    other_links: List[OtherSportLink] = []


class MultiSportPlayers(PFRBaseModel):
    """Parsed result of the PFR 'Multisport Athletes' page."""

    title: str
    entries: List[MultiSportPlayer]
