from __future__ import annotations

from typing import List, Literal, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy.nfl.models.enums.sort_order_enum import SortOrderEnum
from griddy.nfl.models.enums.week_slug_enum import WeekSlugEnum
from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata

GetTeamOffenseStatsByWeekSortKey = Literal[
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
    "to",
    "ppg",
    "ypg",
    "passYpg",
    "rushYpg",
    "redZonePct",
    "thirdDownPct",
]
r"""Field to sort by"""


GetTeamOffenseStatsByWeekSplit = Literal[
    "TEAM_SHOTGUN",
    "TEAM_UNDER_CENTER",
    "TEAM_PISTOL",
    "TEAM_WHEN_LEADING",
    "TEAM_WHEN_TRAILING",
    "TEAM_WHEN_TIED",
    "TEAM_RED_ZONE",
    "TEAM_GOAL_TO_GO",
]


class GetTeamOffenseStatsByWeekRequestTypedDict(TypedDict):
    season: int
    r"""Season year"""
    season_type: SeasonTypeEnum
    r"""Type of season"""
    week: WeekSlugEnum
    r"""Week identifier"""
    limit: NotRequired[int]
    r"""Maximum number of teams to return"""
    offset: NotRequired[int]
    r"""Number of records to skip for pagination"""
    page: NotRequired[int]
    r"""Page number for pagination"""
    sort_key: NotRequired[GetTeamOffenseStatsByWeekSortKey]
    r"""Field to sort by"""
    sort_value: NotRequired[SortOrderEnum]
    r"""Sort direction"""
    team_defense: NotRequired[str]
    r"""Filter by specific team identifier"""
    split: NotRequired[List[GetTeamOffenseStatsByWeekSplit]]
    r"""Offensive situation splits to filter by (supports multiple values)"""


class GetTeamOffenseStatsByWeekRequest(BaseModel):
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
        WeekSlugEnum,
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Week identifier"""

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
        Optional[GetTeamOffenseStatsByWeekSortKey],
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

    team_defense: Annotated[
        Optional[str],
        pydantic.Field(alias="teamDefense"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by specific team identifier"""

    split: Annotated[
        Optional[List[GetTeamOffenseStatsByWeekSplit]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Offensive situation splits to filter by (supports multiple values)"""
