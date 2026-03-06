from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata


class GetPlayerDetailsRequest(BaseModel):
    """Request parameters for fetching player details."""

    player_id: Annotated[
        str,
        pydantic.Field(alias="playerId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Player identifier"""

    season: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Season for statistics (defaults to current)"""
