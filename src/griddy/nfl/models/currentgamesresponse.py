from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel
from .currentgame import CurrentGame, CurrentGameTypedDict
from .seasontypeenum import SeasonTypeEnum


class CurrentGamesResponseTypedDict(TypedDict):
    games: NotRequired[List[CurrentGameTypedDict]]
    games_played_smart_ids: NotRequired[List[str]]
    r"""Smart IDs of games already played"""
    number_of_games: NotRequired[int]
    r"""Total number of games in the week"""
    number_of_games_played: NotRequired[int]
    r"""Number of games already played"""
    season: NotRequired[int]
    r"""Current season year"""
    season_type: NotRequired[SeasonTypeEnum]
    r"""Type of NFL season"""
    week: NotRequired[int]
    r"""Current week number"""


class CurrentGamesResponse(BaseModel):
    games: Optional[List[CurrentGame]] = None

    games_played_smart_ids: Annotated[
        Optional[List[str]], pydantic.Field(alias="gamesPlayedSmartIds")
    ] = None
    r"""Smart IDs of games already played"""

    number_of_games: Annotated[Optional[int], pydantic.Field(alias="numberOfGames")] = (
        None
    )
    r"""Total number of games in the week"""

    number_of_games_played: Annotated[
        Optional[int], pydantic.Field(alias="numberOfGamesPlayed")
    ] = None
    r"""Number of games already played"""

    season: Optional[int] = None
    r"""Current season year"""

    season_type: Annotated[
        Optional[SeasonTypeEnum], pydantic.Field(alias="seasonType")
    ] = None
    r"""Type of NFL season"""

    week: Optional[int] = None
    r"""Current week number"""
