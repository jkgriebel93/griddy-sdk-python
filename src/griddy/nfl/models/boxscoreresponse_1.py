
from __future__ import annotations
from .boxscoreschedule import BoxscoreSchedule, BoxscoreScheduleTypedDict
from .teamboxscore import TeamBoxscore, TeamBoxscoreTypedDict
from ..types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class BoxscoreResponse1TypedDict(TypedDict):
    away: NotRequired[TeamBoxscoreTypedDict]
    game_id: NotRequired[str]
    r"""Game identifier"""
    home: NotRequired[TeamBoxscoreTypedDict]
    schedule: NotRequired[BoxscoreScheduleTypedDict]


class BoxscoreResponse1(BaseModel):
    away: Optional[TeamBoxscore] = None

    game_id: Annotated[Optional[str], pydantic.Field(alias="gameId")] = None
    r"""Game identifier"""

    home: Optional[TeamBoxscore] = None

    schedule: Optional[BoxscoreSchedule] = None
