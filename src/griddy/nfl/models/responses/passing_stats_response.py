from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.models.entities.player_passing_stats import (
    PlayerPassingStats,
    PlayerPassingStatsTypedDict,
)
from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy.nfl.models.enums.sort_order_enum import SortOrderEnum
from griddy.nfl.types import BaseModel


class PassingStatsResponseTypedDict(TypedDict):
    limit: int
    r"""Maximum number of results returned"""
    offset: int
    r"""Number of records skipped"""
    passers: List[PlayerPassingStatsTypedDict]
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
    qualified_passer: NotRequired[bool]
    r"""Whether results are filtered to qualified passers only"""


class PassingStatsResponse(BaseModel):
    limit: int
    r"""Maximum number of results returned"""

    offset: int
    r"""Number of records skipped"""

    passers: List[PlayerPassingStats]

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

    qualified_passer: Annotated[
        Optional[bool], pydantic.Field(alias="qualifiedPasser")
    ] = None
    r"""Whether results are filtered to qualified passers only"""
