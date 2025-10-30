
from __future__ import annotations
from .pagination import Pagination, PaginationTypedDict
from .seasontypeenum import SeasonTypeEnum
from .standings import Standings, StandingsTypedDict
from ..types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class StandingsResponseWeekTypedDict(TypedDict):
    standings: NotRequired[List[StandingsTypedDict]]
    week: NotRequired[int]


class StandingsResponseWeek(BaseModel):
    standings: Optional[List[Standings]] = None

    week: Optional[int] = None


class StandingsResponseTypedDict(TypedDict):
    pagination: NotRequired[PaginationTypedDict]
    season: NotRequired[int]
    season_type: NotRequired[SeasonTypeEnum]
    r"""Type of NFL season"""
    week: NotRequired[int]
    r"""Current week for standings"""
    weeks: NotRequired[List[StandingsResponseWeekTypedDict]]


class StandingsResponse(BaseModel):
    pagination: Optional[Pagination] = None

    season: Optional[int] = None

    season_type: Annotated[
        Optional[SeasonTypeEnum], pydantic.Field(alias="seasonType")
    ] = None
    r"""Type of NFL season"""

    week: Optional[int] = None
    r"""Current week for standings"""

    weeks: Optional[List[StandingsResponseWeek]] = None
