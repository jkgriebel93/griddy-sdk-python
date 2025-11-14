from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from ..types import BaseModel
from .pagination import Pagination, PaginationTypedDict
from .pro_week import ProWeek, ProWeekTypedDict


class WeeksResponseTypedDict(TypedDict):
    pagination: NotRequired[PaginationTypedDict]
    weeks: NotRequired[List[ProWeekTypedDict]]


class WeeksResponse(BaseModel):
    pagination: Optional[Pagination] = None

    weeks: Optional[List[ProWeek]] = None
