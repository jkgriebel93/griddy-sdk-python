from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel
from .seasontypeenum import SeasonTypeEnum
from .sortorderenum import SortOrderEnum
from .teamoffenserushstats import TeamOffenseRushStats, TeamOffenseRushStatsTypedDict


class TeamOffenseRushStatsResponseTypedDict(TypedDict):
    limit: int
    r"""Maximum number of results returned"""
    offset: int
    r"""Number of records skipped"""
    season: int
    r"""Season year"""
    season_type: SeasonTypeEnum
    r"""Type of season"""
    # TODO: Need to add enum for this
    sort_key: str
    r"""Field used to sort results"""
    sort_value: SortOrderEnum
    r"""Sort direction for results"""
    total: int
    r"""Number of records matching criteria"""
    offense: List[TeamOffenseRushStatsTypedDict]


class TeamOffenseRushStatsResponse(BaseModel):
    limit: int
    r"""Maximum number of results returned"""
    offset: int
    r"""Number of records skipped"""
    season: int
    r"""Season year"""
    season_type: Annotated[SeasonTypeEnum, pydantic.Field(alias="seasonType")]
    r"""Type of season"""
    # TODO: Need to add enum for this
    sort_key: Annotated[str, pydantic.Field(alias="sortKey")]
    r"""Field used to sort results"""
    sort_value: Annotated[SortOrderEnum, pydantic.Field(alias="sortValue")]
    r"""Sort direction for results"""
    total: int
    r"""Number of records matching criteria"""
    offense: List[TeamOffenseRushStatsTypedDict]
