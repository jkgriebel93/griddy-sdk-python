from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.types import BaseModel
from griddy_nfl.utils import FieldMetadata, QueryParamMetadata


class GetGameInsightsRequestTypedDict(TypedDict):
    season: int
    r"""Season year"""
    fapi_game_id: str
    r"""FAPI Game identifier (UUID)"""
    away_team_id: str
    r"""Away team identifier"""
    home_team_id: str
    r"""Home team identifier"""
    limit: NotRequired[int]
    r"""Maximum number of insights to return"""
    tags: NotRequired[str]
    r"""Comma-separated list of tags to filter by"""
    exclude_tags: NotRequired[str]
    r"""Comma-separated list of tags to exclude"""


class GetGameInsightsRequest(BaseModel):
    season: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Season year"""

    fapi_game_id: Annotated[
        str,
        pydantic.Field(alias="fapiGameId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""FAPI Game identifier (UUID)"""

    away_team_id: Annotated[
        str,
        pydantic.Field(alias="awayTeamId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Away team identifier"""

    home_team_id: Annotated[
        str,
        pydantic.Field(alias="homeTeamId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Home team identifier"""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 20
    r"""Maximum number of insights to return"""

    tags: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Comma-separated list of tags to filter by"""

    exclude_tags: Annotated[
        Optional[str],
        pydantic.Field(alias="excludeTags"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Comma-separated list of tags to exclude"""
