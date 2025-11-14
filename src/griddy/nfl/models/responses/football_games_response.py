from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from griddy.nfl.models.entities.pagination import Pagination, PaginationTypedDict
from griddy.nfl.models.entities.weekly_game_detail import (
    WeeklyGameDetail,
    WeeklyGameDetailTypedDict,
)
from griddy.nfl.types import BaseModel


class FootballGamesResponseTypedDict(TypedDict):
    games: NotRequired[List[WeeklyGameDetailTypedDict]]
    pagination: NotRequired[PaginationTypedDict]


class FootballGamesResponse(BaseModel):
    games: Optional[List[WeeklyGameDetail]] = None

    pagination: Optional[Pagination] = None
