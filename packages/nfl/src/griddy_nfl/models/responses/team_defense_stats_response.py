from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.models.entities.team_defense_stats import (
    TeamDefenseStats,
    TeamDefenseStatsTypedDict,
)
from griddy_nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy_nfl.models.enums.sort_order_enum import SortOrderEnum
from griddy_nfl.types import BaseModel


class TeamDefenseStatsResponseTypedDict(TypedDict):
    defense: List[TeamDefenseStatsTypedDict]
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
    r"""Total number of teams matching the criteria"""
    split: NotRequired[List[str]]
    r"""Applied defensive situation splits"""


class TeamDefenseStatsResponse(BaseModel):
    defense: List[TeamDefenseStats]

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
    r"""Total number of teams matching the criteria"""

    split: Optional[List[str]] = None
    r"""Applied defensive situation splits"""
