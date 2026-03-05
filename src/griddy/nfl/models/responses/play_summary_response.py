from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.game_schedule import GameSchedule
from griddy.nfl.models.entities.play_detail import PlayDetail
from griddy.nfl.models.entities.play_player import PlayPlayer
from griddy.nfl.types import BaseModel


class PlaySummaryResponse(BaseModel):
    game_id: Annotated[int, pydantic.Field(alias="gameId")]
    r"""Game identifier in integer format"""

    play: PlayDetail

    play_id: Annotated[int, pydantic.Field(alias="playId")]
    r"""Play identifier"""

    schedule: GameSchedule

    away: Optional[List[PlayPlayer]] = None
    r"""Away team players involved in the play"""

    game_key: Annotated[Optional[int], pydantic.Field(alias="gameKey")] = None
    r"""Unique game key"""

    gsis_play_id: Annotated[Optional[int], pydantic.Field(alias="gsisPlayId")] = None
    r"""GSIS play identifier"""

    home: Optional[List[PlayPlayer]] = None
    r"""Home team players involved in the play"""

    home_is_offense: Annotated[
        Optional[bool], pydantic.Field(alias="homeIsOffense")
    ] = None
    r"""Whether home team has offensive possession"""
