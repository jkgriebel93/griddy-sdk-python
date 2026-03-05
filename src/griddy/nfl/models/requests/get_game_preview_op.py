from __future__ import annotations

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata


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
