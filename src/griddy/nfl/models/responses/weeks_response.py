from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from griddy.nfl.models.pagination import Pagination, PaginationTypedDict
from griddy.nfl.models.pro_week import ProWeek, ProWeekTypedDict
from griddy.nfl.types import BaseModel


class WeeksResponseTypedDict(TypedDict):
    pagination: NotRequired[PaginationTypedDict]
    weeks: NotRequired[List[ProWeekTypedDict]]


class WeeksResponse(BaseModel):
    pagination: Optional[Pagination] = None

    weeks: Optional[List[ProWeek]] = None
