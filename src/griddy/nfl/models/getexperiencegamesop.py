from __future__ import annotations

import pydantic
from typing_extensions import Annotated, TypedDict

from ..types import BaseModel
from ..utils import FieldMetadata, QueryParamMetadata
from .seasontypeenum import SeasonTypeEnum


class GetExperienceGamesRequestTypedDict(TypedDict):
    season: int
    r"""Season year (e.g., 2025)"""
    season_type: SeasonTypeEnum
    r"""Type of season"""
    week: int
    r"""Week number within the season"""


class GetExperienceGamesRequest(BaseModel):
    season: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Season year (e.g., 2025)"""

    season_type: Annotated[
        SeasonTypeEnum,
        pydantic.Field(alias="seasonType"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Type of season"""

    week: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Week number within the season"""
