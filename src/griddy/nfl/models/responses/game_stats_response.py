from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from griddy.nfl.models.pagination import Pagination, PaginationTypedDict
from griddy.nfl.types import BaseModel


class GameStatsResponseDataTypedDict(TypedDict):
    r"""Game statistics data"""


class GameStatsResponseData(BaseModel):
    r"""Game statistics data"""


class GameStatsResponseTypedDict(TypedDict):
    data: NotRequired[List[GameStatsResponseDataTypedDict]]
    pagination: NotRequired[PaginationTypedDict]


class GameStatsResponse(BaseModel):
    data: Optional[List[GameStatsResponseData]] = None

    pagination: Optional[Pagination] = None
