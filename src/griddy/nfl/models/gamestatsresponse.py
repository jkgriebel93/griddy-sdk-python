from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from ..types import BaseModel
from .pagination import Pagination, PaginationTypedDict


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
