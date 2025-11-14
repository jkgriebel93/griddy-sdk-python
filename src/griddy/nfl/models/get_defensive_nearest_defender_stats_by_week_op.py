from __future__ import annotations

from typing import Literal, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.models.enums.down_enum import DownEnum
from griddy.nfl.models.enums.game_location_enum import GameLocationEnum
from griddy.nfl.models.enums.position_enums import DefenseNGSPositionGroupEnum
from griddy.nfl.models.enums.quarter_enum import QuarterEnum
from griddy.nfl.models.enums.yards_to_go_enum import YardsToGoEnum

from ..types import BaseModel
from ..utils import FieldMetadata, QueryParamMetadata
from .enums.defensive_splits_enum import DefenseNGSSplitEnum
from .season_type_enum import SeasonTypeEnum
from .sort_order_enum import SortOrderEnum
from .week_slug_enum import WeekSlugEnum

GetDefensiveNearestDefenderStatsByWeekSortKey = Literal[
    "cov"
    # TODO: Add the rest of these
]


class GetDefensiveNearestDefenderStatsByWeekRequestTypedDict(TypedDict):
    season: int
    r"""Season year"""
    season_type: SeasonTypeEnum
    r"""Type of season"""
    week: WeekSlugEnum
    r"""Week of the Season"""
    limit: NotRequired[int]
    r"""Maximum number of players to return"""
    offset: NotRequired[int]
    r"""Number of players to skip"""
    page: NotRequired[int]
    r"""Page number for pagination"""
    sort_key: NotRequired[GetDefensiveNearestDefenderStatsByWeekSortKey]
    r"""Field to sort by"""
    sort_value: NotRequired[SortOrderEnum]
    r"""Sort direction"""
    qualified_defender: NotRequired[bool]
    r"""Filter to only qualified defenders (minimum snap threshold)"""


class GetDefensiveNearestDefenderStatsByWeekRequest(BaseModel):
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
    r"""Week of the Season"""

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
        Optional[GetDefensiveNearestDefenderStatsByWeekSortKey],
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
