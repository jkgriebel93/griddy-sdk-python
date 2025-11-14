from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel
from .boxscore_schedule import BoxscoreSchedule, BoxscoreScheduleTypedDict
from .team_boxscore import TeamBoxscore, TeamBoxscoreTypedDict


class BoxscoreResponseTypedDict(TypedDict):
    away: NotRequired[TeamBoxscoreTypedDict]
    game_id: NotRequired[str]
    r"""Game identifier"""
    home: NotRequired[TeamBoxscoreTypedDict]
    schedule: NotRequired[BoxscoreScheduleTypedDict]


class BoxscoreResponse(BaseModel):
    away: Optional[TeamBoxscore] = None

    game_id: Annotated[Optional[str], pydantic.Field(alias="gameId")] = None
    r"""Game identifier"""

    home: Optional[TeamBoxscore] = None

    schedule: Optional[BoxscoreSchedule] = None
