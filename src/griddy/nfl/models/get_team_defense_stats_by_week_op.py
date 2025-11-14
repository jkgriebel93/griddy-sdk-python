from __future__ import annotations

from typing import List, Literal, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy.nfl.models.enums.sort_order_enum import SortOrderEnum
from griddy.nfl.models.enums.week_slug_enum import WeekSlugEnum

from ..types import BaseModel
from ..utils import FieldMetadata, QueryParamMetadata

# TODO: Move this to an enum module
GetTeamDefenseStatsByWeekSortKey = Literal[
    "total",
    "pass",
    "run",
    "yds",
    "passPct",
    "ypp",
    "td",
    "passTd",
    "rushTd",
    "epa",
    "epaPP",
    "passYds",
    "passYpp",
    "epaPass",
    "epaPassPP",
    "rushYds",
    "rushYpp",
    "epaRush",
    "epaRushPP",
    "ttt",
    "qbp",
    "qbpPct",
    "sackedYds",
    "ryoe",
    "interception",
    "forcedFumble",
    "fumbleRecovered",
    "defensiveTouchdown",
    "totalTakeaways",
    "ppg",
    "ypg",
    "passYpg",
    "rushYpg",
    "sackedYpg",
]
r"""Field to sort by"""

# TODO: Move this to an enum module
GetTeamDefenseStatsByWeekSplit = Literal[
    "TEAM_DEFENSE_BASE",
    "TEAM_DEFENSE_NICKEL",
    "TEAM_DEFENSE_DIME",
    "TEAM_DEFENSE_WHEN_LEADING",
    "TEAM_DEFENSE_WHEN_TRAILING",
    "TEAM_DEFENSE_WHEN_TIED",
    "TEAM_DEFENSE_RED_ZONE",
    "TEAM_DEFENSE_GOAL_TO_GO",
    "TEAM_DEFENSE_SHOTGUN",
    "TEAM_DEFENSE_UNDER_CENTER",
    "TEAM_DEFENSE_PISTOL",
    "TEAM_DEFENSE_MOTION",
]


class GetTeamDefenseStatsByWeekRequestTypedDict(TypedDict):
    season: int
    r"""Season year"""
    season_type: SeasonTypeEnum
    r"""Type of season"""
    week: WeekSlugEnum
    r"""Week number"""
    limit: NotRequired[int]
    r"""Maximum number of teams to return"""
    offset: NotRequired[int]
    r"""Number of records to skip for pagination"""
    page: NotRequired[int]
    r"""Page number for pagination"""
    sort_key: NotRequired[GetTeamDefenseStatsByWeekSortKey]
    r"""Field to sort by"""
    sort_value: NotRequired[SortOrderEnum]
    r"""Sort direction"""
    split: NotRequired[List[GetTeamDefenseStatsByWeekSplit]]
    r"""Defensive situation splits to filter by (supports multiple values)"""


class GetTeamDefenseStatsByWeekRequest(BaseModel):
    season: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Season year"""

    season_type: Annotated[
        SeasonTypeEnum,
        pydantic.Field(alias="seasonType"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Type of season"""
    week: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Week number"""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 35
    r"""Maximum number of teams to return"""

    offset: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 0
    r"""Number of records to skip for pagination"""

    page: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 1
    r"""Page number for pagination"""

    sort_key: Annotated[
        Optional[GetTeamDefenseStatsByWeekSortKey],
        pydantic.Field(alias="sortKey"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "ypg"
    r"""Field to sort by"""

    sort_value: Annotated[
        Optional[SortOrderEnum],
        pydantic.Field(alias="sortValue"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Sort direction"""

    split: Annotated[
        Optional[List[GetTeamDefenseStatsByWeekSplit]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Defensive situation splits to filter by (supports multiple values)"""
