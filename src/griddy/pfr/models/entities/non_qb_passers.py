"""Models for the PFR 'Non-Quarterback Passing' page.

Represents players whose primary position was not QB who have thrown
a pass in the NFL (post-1960), along with their passing statistics.
"""

from __future__ import annotations

from typing import List, Optional

from ...types import BaseModel


class NonQBPasserEntry(BaseModel):
    """A single non-QB passer entry with passing statistics."""

    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    pos: str
    year_min: Optional[int] = None
    year_max: Optional[int] = None
    pass_cmp: Optional[int] = None
    pass_att: Optional[int] = None
    pass_cmp_perc: Optional[float] = None
    pass_yds: Optional[int] = None
    pass_td: Optional[int] = None
    pass_td_perc: Optional[float] = None
    pass_int: Optional[int] = None
    pass_int_perc: Optional[float] = None
    pass_long: Optional[int] = None
    pass_yds_per_att: Optional[float] = None
    pass_adj_yds_per_att: Optional[float] = None
    pass_yds_per_cmp: Optional[float] = None
    pass_yds_per_g: Optional[float] = None
    pass_rating: Optional[float] = None
    qbr: Optional[float] = None
    pass_sacked: Optional[int] = None
    pass_sacked_yds: Optional[int] = None
    pass_sacked_perc: Optional[float] = None
    pass_net_yds_per_att: Optional[float] = None
    pass_adj_net_yds_per_att: Optional[float] = None


class NonQBPassers(BaseModel):
    """Parsed result of the PFR non-QB passers page."""

    title: str
    entries: List[NonQBPasserEntry]
