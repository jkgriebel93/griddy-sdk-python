
from __future__ import annotations
from .player import Player, PlayerTypedDict
from .team import Team, TeamTypedDict
from ..types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PenaltyTypedDict(TypedDict):
    accepted: NotRequired[bool]
    no_play: NotRequired[bool]
    player: NotRequired[PlayerTypedDict]
    team: NotRequired[TeamTypedDict]
    type: NotRequired[str]
    yards: NotRequired[int]


class Penalty(BaseModel):
    accepted: Optional[bool] = None

    no_play: Annotated[Optional[bool], pydantic.Field(alias="noPlay")] = None

    player: Optional[Player] = None

    team: Optional[Team] = None

    type: Optional[str] = None

    yards: Optional[int] = None
