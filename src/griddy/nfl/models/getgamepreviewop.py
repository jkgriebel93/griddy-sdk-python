from __future__ import annotations
from .seasontypeenum import SeasonTypeEnum
from ..types import BaseModel
from ..utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing_extensions import Annotated, TypedDict


class GetGamePreviewRequestTypedDict(TypedDict):
    season: int
    r"""Season year"""
    season_type: SeasonTypeEnum
    r"""Type of season"""
    week: int
    r"""Week number"""
    visitor_display_name: str
    r"""Visiting team display name"""
    home_display_name: str
    r"""Home team display name"""


class GetGamePreviewRequest(BaseModel):
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
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Week number"""

    visitor_display_name: Annotated[
        str,
        pydantic.Field(alias="visitorDisplayName"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Visiting team display name"""

    home_display_name: Annotated[
        str,
        pydantic.Field(alias="homeDisplayName"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Home team display name"""
