from __future__ import annotations

from typing import Literal, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy.nfl.models.enums.sort_order_enum import SortOrderEnum
from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata

GetDefensiveNearestDefenderStatsBySeasonSortKey = Literal[
    "cov" "snap",
    "snapPct",
    # Run snaps
    "rd",
    # Tackles
    "tck",
    "tStop",
    # Hustle stops
    "h",
    # Pass rushes
    "pr",
    "sack",
    "qbp",
    # QB pressure rate
    "qbpR",
    "tgt",
    "recNd",
    "recYdsNd",
    "recTdNd",
    "int",
    "passRatingNd",
]


class GetDefensiveNearestDefenderStatsBySeasonRequest(BaseModel):
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
    r"""Number of players to skip"""

    page: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 1
    r"""Page number for pagination"""

    sort_key: Annotated[
        Optional[GetDefensiveNearestDefenderStatsBySeasonSortKey],
        pydantic.Field(alias="sortKey"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "cov"
    r"""Field to sort by"""

    sort_value: Annotated[
        Optional[SortOrderEnum],
        pydantic.Field(alias="sortValue"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Sort direction"""

    qualified_defender: Annotated[
        Optional[bool],
        pydantic.Field(alias="qualifiedDefender"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Filter to only qualified defenders (minimum snap threshold)"""

    # game_location: Annotated[
    #     GameLocationEnum,
    #     pydantic.Field(alias="gameLocation"),
    #     FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    # ]
    # r"""Where the game was played"""
    #
    # quarter: Annotated[
    #     Optional[QuarterEnum],
    #     FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    # ] = None
    # r"""Period of the game"""
    #
    # down: Annotated[
    #     Optional[DownEnum],
    #     FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    # ] = None
    # r"""Down of the snap"""
    #
    # yards_to_go: Annotated[
    #     Optional[YardsToGoEnum],
    #     pydantic.Field(alias="yardsToGo"),
    #     FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    # ] = None
    # r"""Yards required to gain first down"""
    #
    # position_group: Annotated[
    #     Optional[DefenseNGSPositionGroupEnum],
    #     pydantic.Field(alias="positionGroup"),
    #     FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    # ] = None
    # r"""Restrict to a specific position group"""
    #
    # team_defense: Annotated[
    #     Optional[int],
    #     pydantic.Field(alias="teamDefense"),
    #     FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    # ] = None
    # r"""Integer team ID"""
    #
    # team_offense: Annotated[
    #     Optional[int],
    #     pydantic.Field(alias="teamOffense"),
    #     FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    # ] = None
    # r"""Integer team ID of defender's opponent"""
    #
    # split: Annotated[
    #     Optional[DefenseNGSSplitEnum],
    #     FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    # ] = None
    # r"""Various situational/alignment splits offered by the NFL"""
