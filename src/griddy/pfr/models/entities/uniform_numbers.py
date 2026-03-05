from __future__ import annotations

from typing import List, Optional

from ..base import PFRBaseModel


class UniformNumberPlayer(PFRBaseModel):
    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    year_min: Optional[int] = None
    year_max: Optional[int] = None
    av: Optional[int] = None


class UniformNumbers(PFRBaseModel):
    title: str
    number: int
    team: Optional[str] = None
    players: List[UniformNumberPlayer]
