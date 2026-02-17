from __future__ import annotations

from typing import Literal, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.models.enums.practice_status_enum import PracticeStatusEnum

from ...types import BaseModel
from .player import Player, PlayerTypedDict

InjuryEntryGameStatus = Literal[
    "QUESTIONABLE",
    "DOUBTFUL",
    "OUT",
    "IR",
]
r"""Game status designation"""


class PracticeStatusTypedDict(TypedDict):
    friday: NotRequired[PracticeStatusEnum]
    r"""Player practice participation status"""
    thursday: NotRequired[PracticeStatusEnum]
    r"""Player practice participation status"""
    wednesday: NotRequired[PracticeStatusEnum]
    r"""Player practice participation status"""


class PracticeStatus(BaseModel):
    friday: Optional[PracticeStatusEnum] = None
    r"""Player practice participation status"""

    thursday: Optional[PracticeStatusEnum] = None
    r"""Player practice participation status"""

    wednesday: Optional[PracticeStatusEnum] = None
    r"""Player practice participation status"""


class InjuryEntryTypedDict(TypedDict):
    game_status: NotRequired[InjuryEntryGameStatus]
    r"""Game status designation"""
    injury: NotRequired[str]
    r"""Injury description"""
    player: NotRequired[PlayerTypedDict]
    practice_status: NotRequired[PracticeStatusTypedDict]


class InjuryEntry(BaseModel):
    game_status: Annotated[
        Optional[InjuryEntryGameStatus], pydantic.Field(alias="gameStatus")
    ] = None
    r"""Game status designation"""

    injury: Optional[str] = None
    r"""Injury description"""

    player: Optional[Player] = None

    practice_status: Annotated[
        Optional[PracticeStatus], pydantic.Field(alias="practiceStatus")
    ] = None
