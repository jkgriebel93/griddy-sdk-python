from __future__ import annotations

import pydantic
from typing_extensions import Annotated, TypedDict

from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata


class GetGameTeamRankingsRequestTypedDict(TypedDict):
    season: int
    r"""Season year"""
    season_type: SeasonTypeEnum
    r"""Type of season"""
    away_team_id: str
    r"""Away team UUID"""
    home_team_id: str
    r"""Home team UUID"""
    week: int
    r"""Week number"""


class GetGameTeamRankingsRequest(BaseModel):
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

    away_team_id: Annotated[
        str,
        pydantic.Field(alias="awayTeamId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Away team UUID"""

    home_team_id: Annotated[
        str,
        pydantic.Field(alias="homeTeamId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Home team UUID"""

    week: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Week number"""
