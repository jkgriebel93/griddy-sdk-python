from __future__ import annotations

from typing import List, Optional

from ...types import BaseModel


class UniformNumberPlayer(BaseModel):
    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    year_min: Optional[int] = None
    year_max: Optional[int] = None
    av: Optional[int] = None


class UniformNumbers(BaseModel):
    title: str
    number: int
    team: Optional[str] = None
    players: List[UniformNumberPlayer]
