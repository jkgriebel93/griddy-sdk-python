from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from ...types import BaseModel


class UniformNumberPlayerTypedDict(TypedDict):
    player: str
    player_href: NotRequired[Optional[str]]
    player_id: NotRequired[Optional[str]]
    year_min: NotRequired[Optional[int]]
    year_max: NotRequired[Optional[int]]
    av: NotRequired[Optional[int]]


class UniformNumberPlayer(BaseModel):
    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    year_min: Optional[int] = None
    year_max: Optional[int] = None
    av: Optional[int] = None


class UniformNumbersTypedDict(TypedDict):
    title: str
    number: int
    team: NotRequired[Optional[str]]
    players: List[UniformNumberPlayerTypedDict]


class UniformNumbers(BaseModel):
    title: str
    number: int
    team: Optional[str] = None
    players: List[UniformNumberPlayer]
