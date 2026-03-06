from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata


class GetPlayByPlayRequest(BaseModel):
    """Request parameters for fetching play-by-play data."""

    game_id: Annotated[
        str,
        pydantic.Field(alias="gameId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Game identifier (UUID)"""

    include_penalties: Annotated[
        Optional[bool],
        pydantic.Field(alias="includePenalties"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = True
    r"""Include penalty details"""

    include_formations: Annotated[
        Optional[bool],
        pydantic.Field(alias="includeFormations"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Include offensive/defensive formations"""
