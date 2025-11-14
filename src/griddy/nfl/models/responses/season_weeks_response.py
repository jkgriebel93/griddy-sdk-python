from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from griddy.nfl.models.pagination import Pagination, PaginationTypedDict
from griddy.nfl.models.week import Week, WeekTypedDict
from griddy.nfl.types import BaseModel


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
