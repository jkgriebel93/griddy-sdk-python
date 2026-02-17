from __future__ import annotations

import pydantic
from typing_extensions import Annotated, TypedDict

from griddy_nfl.types import BaseModel
from griddy_nfl.utils import FieldMetadata, PathParamMetadata


class GetHistoricalPlayerStatsRequestTypedDict(TypedDict):
    game_id: str
    r"""Game identifier (UUID)"""
    team_id: str
    r"""Team identifier (UUID)"""


class GetHistoricalPlayerStatsRequest(BaseModel):
    game_id: Annotated[
        str,
        pydantic.Field(alias="gameId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Game identifier (UUID)"""

    team_id: Annotated[
        str,
        pydantic.Field(alias="teamId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Team identifier (UUID)"""
