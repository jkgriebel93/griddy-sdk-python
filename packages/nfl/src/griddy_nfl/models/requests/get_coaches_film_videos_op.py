from __future__ import annotations

from typing import List

import pydantic
from typing_extensions import Annotated, TypedDict

from griddy_nfl.types import BaseModel
from griddy_nfl.utils import FieldMetadata, QueryParamMetadata


class GetCoachesFilmVideosRequestTypedDict(TypedDict):
    game_id: List[str]
    r"""Game identifiers (UUID format, supports multiple games)"""
    play_id: List[str]
    r"""Play identifiers for specific plays within the games"""


class GetCoachesFilmVideosRequest(BaseModel):
    game_id: Annotated[
        List[str],
        pydantic.Field(alias="gameId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Game identifiers (UUID format, supports multiple games)"""

    play_id: Annotated[
        List[str],
        pydantic.Field(alias="playId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Play identifiers for specific plays within the games"""
