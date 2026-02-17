from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.models.entities.team_offense_rush_stats import (
    TeamOffenseRushStats,
    TeamOffenseRushStatsTypedDict,
)
from griddy_nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy_nfl.models.enums.sort_order_enum import SortOrderEnum
from griddy_nfl.types import BaseModel


class TeamOffenseRushStatsResponseTypedDict(TypedDict):
    limit: int
    r"""Maximum number of results returned"""
    offset: int
    r"""Number of records skipped"""
    season: int
    r"""Season year"""
    season_type: SeasonTypeEnum
    r"""Type of season"""
    sort_key: NotRequired[str]
    r"""Field used to sort results"""
    sort_value: NotRequired[SortOrderEnum]
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

    sort_key: Annotated[Optional[str], pydantic.Field(alias="sortKey")] = None
    r"""Field used to sort results"""

    sort_value: Annotated[
        Optional[SortOrderEnum], pydantic.Field(alias="sortValue")
    ] = None
    r"""Sort direction for results"""

    total: int
    r"""Number of records matching criteria"""

    offense: List[TeamOffenseRushStats]
