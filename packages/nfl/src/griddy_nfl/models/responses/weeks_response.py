from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from griddy_nfl.models.entities.pagination import Pagination, PaginationTypedDict
from griddy_nfl.models.entities.pro_week import ProWeek, ProWeekTypedDict
from griddy_nfl.types import BaseModel


class WeeksResponseTypedDict(TypedDict):
    pagination: NotRequired[PaginationTypedDict]
    weeks: NotRequired[List[ProWeekTypedDict]]


class WeeksResponse(BaseModel):
    pagination: Optional[Pagination] = None

    weeks: Optional[List[ProWeek]] = None
