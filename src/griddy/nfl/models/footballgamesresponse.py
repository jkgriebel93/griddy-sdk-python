
from __future__ import annotations
from .pagination import Pagination, PaginationTypedDict
from .progame import ProGame, ProGameTypedDict
from ..types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class FootballGamesResponseTypedDict(TypedDict):
    games: NotRequired[List[ProGameTypedDict]]
    pagination: NotRequired[PaginationTypedDict]


class FootballGamesResponse(BaseModel):
    games: Optional[List[ProGame]] = None

    pagination: Optional[Pagination] = None
