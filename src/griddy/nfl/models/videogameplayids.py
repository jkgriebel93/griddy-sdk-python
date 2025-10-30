
from __future__ import annotations
from ..types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class VideoGamePlayIdsTypedDict(TypedDict):
    away_team_id: str
    r"""Away team UUID"""
    game_id: str
    r"""Game UUID"""
    home_team_id: str
    r"""Home team UUID"""
    play_id: str
    r"""Play identifier"""


class VideoGamePlayIds(BaseModel):
    away_team_id: Annotated[str, pydantic.Field(alias="awayTeamId")]
    r"""Away team UUID"""

    game_id: Annotated[str, pydantic.Field(alias="gameId")]
    r"""Game UUID"""

    home_team_id: Annotated[str, pydantic.Field(alias="homeTeamId")]
    r"""Home team UUID"""

    play_id: Annotated[str, pydantic.Field(alias="playId")]
    r"""Play identifier"""
