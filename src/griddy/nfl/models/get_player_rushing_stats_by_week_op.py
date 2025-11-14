from __future__ import annotations

from typing import List, Literal, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy.nfl.models.enums.sort_order_enum import SortOrderEnum
from griddy.nfl.models.enums.week_slug_enum import WeekSlugEnum

from ..types import BaseModel
from ..utils import FieldMetadata, QueryParamMetadata

GetPlayerRushingStatsByWeekSortKey = Literal[
    "att",
    "yds",
    "td",
    "ypc",
    "epa",
    "epaAtt",
    "xRy",
    "xYpc",
    "ryoe",
    "ryoeAtt",
    "yaco",
    "yacoAtt",
    "ybco",
    "success",
    "fum",
    "lost",
    "rush10PYds",
    "rush15PMph",
    "rush20PMph",
    "eff",
    "inTPct",
    "stBoxPct",
    "underPct",
]
r"""Field to sort by"""


class GetPlayerRushingStatsByWeekRequestTypedDict(TypedDict):
    season: int
    r"""Season year"""
    season_type: SeasonTypeEnum
    r"""Type of season"""
    week: WeekSlugEnum
    r"""Week identifier"""
    limit: NotRequired[int]
    r"""Maximum number of players to return"""
    offset: NotRequired[int]
    r"""Number of records to skip for pagination"""
    page: NotRequired[int]
    r"""Page number for pagination"""
    sort_key: NotRequired[GetPlayerRushingStatsByWeekSortKey]
    r"""Field to sort by"""
    sort_value: NotRequired[SortOrderEnum]
    r"""Sort direction"""
    qualified_rusher: NotRequired[bool]
    r"""Filter to only qualified rushers (minimum attempts threshold)"""
    team_offense: NotRequired[List[str]]
    r"""Filter by specific team IDs (supports multiple teams)"""


class GetPlayerRushingStatsByWeekRequest(BaseModel):
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
    ] = 50
    r"""Maximum number of players to return"""

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
        Optional[GetPlayerRushingStatsByWeekSortKey],
        pydantic.Field(alias="sortKey"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "yds"
    r"""Field to sort by"""

    sort_value: Annotated[
        Optional[SortOrderEnum],
        pydantic.Field(alias="sortValue"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Sort direction"""

    qualified_rusher: Annotated[
        Optional[bool],
        pydantic.Field(alias="qualifiedRusher"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Filter to only qualified rushers (minimum attempts threshold)"""

    team_offense: Annotated[
        Optional[List[str]],
        pydantic.Field(alias="teamOffense"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by specific team IDs (supports multiple teams)"""
