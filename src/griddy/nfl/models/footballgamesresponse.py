from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from griddy.nfl.models.weeklygamedetail import (
    WeeklyGameDetail,
    WeeklyGameDetailTypedDict,
)

from ..types import BaseModel
from .pagination import Pagination, PaginationTypedDict


class FootballGamesResponseTypedDict(TypedDict):
    games: NotRequired[List[WeeklyGameDetailTypedDict]]
    pagination: NotRequired[PaginationTypedDict]


class FootballGamesResponse(BaseModel):
    games: Optional[List[WeeklyGameDetail]] = None

    pagination: Optional[Pagination] = None
