from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata


class GetStandingsRequest(BaseModel):
    """Request parameters for fetching standings."""

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

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 20
    r"""Maximum number of results to return"""
