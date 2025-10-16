from __future__ import annotations

from typing import List

import pydantic
from typing_extensions import Annotated, TypedDict

from ..types import BaseModel
from .livegame import LiveGame, LiveGameTypedDict
from .seasontypeenum import SeasonTypeEnum


class LiveScoresResponseTypedDict(TypedDict):
    games: List[LiveGameTypedDict]
    r"""Array of live game data (empty when no games are active)"""
    season: str
    r"""Season year"""
    season_type: SeasonTypeEnum
    r"""Type of NFL season"""
    week: str
    r"""Week number"""


class LiveScoresResponse(BaseModel):
    games: List[LiveGame]
    r"""Array of live game data (empty when no games are active)"""

    season: str
    r"""Season year"""

    season_type: Annotated[SeasonTypeEnum, pydantic.Field(alias="seasonType")]
    r"""Type of NFL season"""

    week: str
    r"""Week number"""
