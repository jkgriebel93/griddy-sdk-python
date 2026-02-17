from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.models.entities.defensive_player_overview_stats import (
    DefensivePlayerOverviewStats,
    DefensivePlayerOverviewStatsTypedDict,
)
from griddy_nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy_nfl.models.enums.sort_order_enum import SortOrderEnum
from griddy_nfl.types import BaseModel


class DefensiveOverviewStatsResponseTypedDict(TypedDict):
    defenders: List[DefensivePlayerOverviewStatsTypedDict]
    limit: int
    r"""Maximum number of results returned"""
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
    r"""Total number of players matching the criteria"""
    qualified_defender: NotRequired[bool]
    r"""Whether results are filtered to qualified defenders only"""
    team_defense: NotRequired[str]
    r"""Team filter applied (if any)"""


class DefensiveOverviewStatsResponse(BaseModel):
    defenders: List[DefensivePlayerOverviewStats]

    limit: int
    r"""Maximum number of results returned"""

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
    r"""Total number of players matching the criteria"""

    qualified_defender: Annotated[
        Optional[bool], pydantic.Field(alias="qualifiedDefender")
    ] = None
    r"""Whether results are filtered to qualified defenders only"""

    team_defense: Annotated[Optional[str], pydantic.Field(alias="teamDefense")] = None
    r"""Team filter applied (if any)"""
