from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy.nfl.models.enums.sort_order_enum import SortOrderEnum

from ..types import BaseModel
from .fantasy_player_stats import FantasyPlayerStats, FantasyPlayerStatsTypedDict


class FantasyStatsResponseTypedDict(TypedDict):
    limit: int
    r"""Maximum number of results returned"""
    offset: int
    r"""Number of records skipped"""
    players: List[FantasyPlayerStatsTypedDict]
    season: int
    r"""Season year"""
    season_type: SeasonTypeEnum
    r"""Type of NFL season"""
    sort_key: str
    r"""Field used for sorting"""
    sort_value: SortOrderEnum
    r"""Sort direction for ordered results"""
    total: int
    r"""Total number of players matching the criteria"""
    last_n_weeks: NotRequired[int]
    r"""Number of recent weeks analyzed (if applied)"""
    min_offensive_snaps: NotRequired[int]
    r"""Minimum offensive snaps filter applied"""
    position_group: NotRequired[List[str]]
    r"""Position groups included in results"""
    team_offense: NotRequired[str]
    r"""Offensive team filter applied (if any)"""
    week: NotRequired[List[str]]
    r"""Specific weeks included in analysis"""


class FantasyStatsResponse(BaseModel):
    limit: int
    r"""Maximum number of results returned"""

    offset: int
    r"""Number of records skipped"""

    players: List[FantasyPlayerStats]

    season: int
    r"""Season year"""

    season_type: Annotated[SeasonTypeEnum, pydantic.Field(alias="seasonType")]
    r"""Type of NFL season"""

    sort_key: Annotated[str, pydantic.Field(alias="sortKey")]
    r"""Field used for sorting"""

    sort_value: Annotated[SortOrderEnum, pydantic.Field(alias="sortValue")]
    r"""Sort direction for ordered results"""

    total: int
    r"""Total number of players matching the criteria"""

    last_n_weeks: Annotated[Optional[int], pydantic.Field(alias="lastNWeeks")] = None
    r"""Number of recent weeks analyzed (if applied)"""

    min_offensive_snaps: Annotated[
        Optional[int], pydantic.Field(alias="minOffensiveSnaps")
    ] = None
    r"""Minimum offensive snaps filter applied"""

    position_group: Annotated[
        Optional[List[str]], pydantic.Field(alias="positionGroup")
    ] = None
    r"""Position groups included in results"""

    team_offense: Annotated[Optional[str], pydantic.Field(alias="teamOffense")] = None
    r"""Offensive team filter applied (if any)"""

    week: Optional[List[str]] = None
    r"""Specific weeks included in analysis"""
