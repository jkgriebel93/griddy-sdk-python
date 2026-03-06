from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.current_game import CurrentGame
from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy.nfl.types import BaseModel


class CurrentGamesResponse(BaseModel):
    """Response containing currently active games."""

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
