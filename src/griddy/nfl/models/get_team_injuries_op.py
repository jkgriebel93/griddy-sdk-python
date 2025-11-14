from __future__ import annotations

import pydantic
from typing_extensions import Annotated, TypedDict

from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum

from ..types import BaseModel
from ..utils import FieldMetadata, QueryParamMetadata


class GetTeamInjuriesRequestTypedDict(TypedDict):
    season: int
    r"""Season year"""
    season_type: SeasonTypeEnum
    r"""Type of season"""
    team_id: str
    r"""Team identifier (UUID format)"""
    week: int
    r"""Week number within the season"""


class GetTeamInjuriesRequest(BaseModel):
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

    team_id: Annotated[
        str,
        pydantic.Field(alias="teamId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Team identifier (UUID format)"""

    week: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Week number within the season"""
