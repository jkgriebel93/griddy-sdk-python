from __future__ import annotations

import pydantic
from typing_extensions import Annotated

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, PathParamMetadata


class GetLiveTeamStatisticsRequest(BaseModel):
    """Request parameters for fetching live team statistics."""

    game_id: Annotated[
        str,
        pydantic.Field(alias="gameId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Game identifier (UUID)"""
