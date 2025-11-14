from __future__ import annotations

from typing import List

import pydantic
from typing_extensions import Annotated, TypedDict

from ..types import BaseModel
from .play_win_probability import PlayWinProbability, PlayWinProbabilityTypedDict


class WinProbabilityResponseTypedDict(TypedDict):
    game_id: int
    r"""Game identifier (10-digit format YYYYMMDDNN)"""
    game_key: int
    r"""Unique game key identifier"""
    plays: List[PlayWinProbabilityTypedDict]
    r"""Chronological list of all plays with win probability data"""
    pregame_away_team_win_probability: float
    r"""Away team's win probability before the game started"""
    pregame_home_team_win_probability: float
    r"""Home team's win probability before the game started"""


class WinProbabilityResponse(BaseModel):
    game_id: Annotated[int, pydantic.Field(alias="gameId")]
    r"""Game identifier (10-digit format YYYYMMDDNN)"""

    game_key: Annotated[int, pydantic.Field(alias="gameKey")]
    r"""Unique game key identifier"""

    plays: List[PlayWinProbability]
    r"""Chronological list of all plays with win probability data"""

    pregame_away_team_win_probability: Annotated[
        float, pydantic.Field(alias="pregameAwayTeamWinProbability")
    ]
    r"""Away team's win probability before the game started"""

    pregame_home_team_win_probability: Annotated[
        float, pydantic.Field(alias="pregameHomeTeamWinProbability")
    ]
    r"""Home team's win probability before the game started"""
