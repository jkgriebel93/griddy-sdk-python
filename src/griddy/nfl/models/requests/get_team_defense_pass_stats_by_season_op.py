from __future__ import annotations

from typing import Literal, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy.nfl.models.enums.sort_order_enum import SortOrderEnum
from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata

GetTeamDefensePassStatsBySeasonSortKey = Literal[
    "total",
    "pass",
    "passPct",
    "passTd",
    "passYds",
    "passYpp",
    "epaPass",
    "epaPassPP",
    "ttt",
    "qbp",
    "qbpPct",
    "sackedYds",
    "sack",
    "sackPct",
    "ttp",
    "blitzPct",
    "yac",
    "yacoe",
    "sep",
    "go",
    "passYpg",
    "sackedYpg",
]
r"""Field to sort by"""


class GetTeamDefensePassStatsBySeasonRequest(BaseModel):
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
        Optional[GetTeamDefensePassStatsBySeasonSortKey],
        pydantic.Field(alias="sortKey"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "passYpg"
    r"""Field to sort by"""

    sort_value: Annotated[
        Optional[SortOrderEnum],
        pydantic.Field(alias="sortValue"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Sort direction"""
