from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.models.entities.team_offense_pass_stats import (
    TeamOffensePassStats,
    TeamOffensePassStatsTypedDict,
)
from griddy_nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy_nfl.models.enums.sort_order_enum import SortOrderEnum
from griddy_nfl.types import BaseModel


class TeamOffensePassStatsResponseTypedDict(TypedDict):
    limit: int
    r"""Maximum number of results returned"""
    offense: List[TeamOffensePassStatsTypedDict]
    offset: int
    r"""Number of records skipped"""
    season: int
    r"""Season year"""
    season_type: SeasonTypeEnum
    r"""Type of NFL season"""
    sort_key: NotRequired[str]
    r"""Field used for sorting"""
    sort_value: NotRequired[SortOrderEnum]
    r"""Sort direction for ordered results"""
    total: int
    r"""Total number of teams matching the criteria"""
    team_defense: NotRequired[str]
    r"""Applied team filter (if any)"""


class TeamOffensePassStatsResponse(BaseModel):
    limit: int
    r"""Maximum number of results returned"""

    offense: List[TeamOffensePassStats]

    offset: int
    r"""Number of records skipped"""

    season: int
    r"""Season year"""

    season_type: Annotated[SeasonTypeEnum, pydantic.Field(alias="seasonType")]
    r"""Type of NFL season"""

    sort_key: Annotated[Optional[str], pydantic.Field(alias="sortKey")] = None
    r"""Field used for sorting"""

    sort_value: Annotated[
        Optional[SortOrderEnum], pydantic.Field(alias="sortValue")
    ] = None
    r"""Sort direction for ordered results"""

    total: int
    r"""Total number of teams matching the criteria"""

    team_defense: Annotated[Optional[str], pydantic.Field(alias="teamDefense")] = None
    r"""Applied team filter (if any)"""
