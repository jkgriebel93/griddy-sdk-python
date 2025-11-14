from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from ..types import BaseModel
from .pagination import Pagination, PaginationTypedDict
from .pro_game import ProGame, ProGameTypedDict


class ExperienceGamesResponseTypedDict(TypedDict):
    games: NotRequired[List[ProGameTypedDict]]
    pagination: NotRequired[PaginationTypedDict]


class ExperienceGamesResponse(BaseModel):
    games: Optional[List[ProGame]] = None

    pagination: Optional[Pagination] = None
