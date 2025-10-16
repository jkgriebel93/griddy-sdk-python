from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from ..types import BaseModel
from .pagination import Pagination, PaginationTypedDict
from .week import Week, WeekTypedDict


class SeasonWeeksResponseTypedDict(TypedDict):
    pagination: NotRequired[PaginationTypedDict]
    season: NotRequired[str]
    r"""Season year"""
    weeks: NotRequired[List[WeekTypedDict]]


class SeasonWeeksResponse(BaseModel):
    pagination: Optional[Pagination] = None

    season: Optional[str] = None
    r"""Season year"""

    weeks: Optional[List[Week]] = None
