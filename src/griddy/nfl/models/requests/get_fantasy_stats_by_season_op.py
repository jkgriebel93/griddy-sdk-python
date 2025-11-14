from __future__ import annotations

from typing import List, Literal, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy.nfl.models.enums.sort_order_enum import SortOrderEnum
from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata

GetFantasyStatsBySeasonSortKey = Literal[
    "fpStd",
    "fpPpr",
    "fpHalfPpr",
    "passYds",
    "passTd",
    "passInt",
    "rushYds",
    "rushTd",
    "recYds",
    "recTd",
    "rec",
    "tgt",
    "snapPct",
    "targetShare",
    "redZoneTargets",
]
r"""Field to sort by"""


GetFantasyStatsBySeasonPositionGroup = Literal[
    "QB",
    "RB",
    "WR",
    "TE",
    "SPEC",
]


class GetFantasyStatsBySeasonRequestTypedDict(TypedDict):
    season: int
    r"""Season year"""
    season_type: SeasonTypeEnum
    r"""Type of season"""
    limit: NotRequired[int]
    r"""Maximum number of players to return"""
    offset: NotRequired[int]
    r"""Number of records to skip for pagination"""
    page: NotRequired[int]
    r"""Page number for pagination"""
    sort_key: NotRequired[GetFantasyStatsBySeasonSortKey]
    r"""Field to sort by"""
    sort_value: NotRequired[SortOrderEnum]
    r"""Sort direction"""
    position_group: NotRequired[List[GetFantasyStatsBySeasonPositionGroup]]
    r"""Filter by position groups (supports multiple positions)"""
    team_offense: NotRequired[str]
    r"""Filter by specific offensive team ID"""
    team_defense: NotRequired[str]
    r"""Filter by specific defensive team ID (opponent analysis)"""
    min_offensive_snaps: NotRequired[int]
    r"""Minimum offensive snaps threshold for inclusion"""
    last_n_weeks: NotRequired[int]
    r"""Number of recent weeks to analyze (rolling window)"""


class GetFantasyStatsBySeasonRequest(BaseModel):
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

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 35
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
        Optional[GetFantasyStatsBySeasonSortKey],
        pydantic.Field(alias="sortKey"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "fpStd"
    r"""Field to sort by"""

    sort_value: Annotated[
        Optional[SortOrderEnum],
        pydantic.Field(alias="sortValue"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Sort direction"""

    position_group: Annotated[
        Optional[List[GetFantasyStatsBySeasonPositionGroup]],
        pydantic.Field(alias="positionGroup"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by position groups (supports multiple positions)"""

    team_offense: Annotated[
        Optional[str],
        pydantic.Field(alias="teamOffense"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by specific offensive team ID"""

    team_defense: Annotated[
        Optional[str],
        pydantic.Field(alias="teamDefense"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by specific defensive team ID (opponent analysis)"""

    min_offensive_snaps: Annotated[
        Optional[int],
        pydantic.Field(alias="minOffensiveSnaps"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 0
    r"""Minimum offensive snaps threshold for inclusion"""

    last_n_weeks: Annotated[
        Optional[int],
        pydantic.Field(alias="lastNWeeks"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Number of recent weeks to analyze (rolling window)"""
