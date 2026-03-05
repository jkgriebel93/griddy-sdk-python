from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata


class GetFootballGamesRequest(BaseModel):
    season: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Season year"""

    season_type: Annotated[
        SeasonTypeEnum,
        pydantic.Field(alias="seasonType"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Type of season"""

    week: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Week number"""

    with_external_ids: Annotated[
        Optional[bool],
        pydantic.Field(alias="withExternalIds"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Include external IDs in response"""
