from __future__ import annotations

from typing import Literal, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata

GetSeasonPlayerStatsPosition = Literal[
    "QB",
    "RB",
    "WR",
    "TE",
    "OL",
    "DL",
    "LB",
    "DB",
    "K",
    "P",
    "LS",
]
r"""Filter by position group"""


StatCategory = Literal[
    "passing",
    "rushing",
    "receiving",
    "defense",
    "kicking",
    "punting",
    "returning",
]
r"""Statistical category to retrieve"""


class GetSeasonPlayerStatsRequest(BaseModel):
    """Request parameters for fetching season player stats."""

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

    position: Annotated[
        Optional[GetSeasonPlayerStatsPosition],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by position group"""

    team_id: Annotated[
        Optional[str],
        pydantic.Field(alias="teamId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by team"""

    stat_category: Annotated[
        Optional[StatCategory],
        pydantic.Field(alias="statCategory"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Statistical category to retrieve"""

    sort: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Sort field and order"""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 50
    r"""Maximum number of results"""

    offset: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 0
    r"""Offset for pagination"""
