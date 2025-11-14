from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from griddy.nfl.models.pagination import Pagination, PaginationTypedDict
from griddy.nfl.models.pro_game import ProGame, ProGameTypedDict
from griddy.nfl.types import BaseModel


class ExperienceGamesResponseTypedDict(TypedDict):
    games: NotRequired[List[ProGameTypedDict]]
    pagination: NotRequired[PaginationTypedDict]


class ExperienceGamesResponse(BaseModel):
    games: Optional[List[ProGame]] = None

    pagination: Optional[Pagination] = None
