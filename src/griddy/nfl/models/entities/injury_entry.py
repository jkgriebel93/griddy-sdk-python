from __future__ import annotations

from typing import Literal, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.enums.practice_status_enum import PracticeStatusEnum

from ...types import BaseModel
from .player import Player

InjuryEntryGameStatus = Literal[
    "QUESTIONABLE",
    "DOUBTFUL",
    "OUT",
    "IR",
]
r"""Game status designation"""


class PracticeStatus(BaseModel):
    friday: Optional[PracticeStatusEnum] = None
    r"""Player practice participation status"""

    thursday: Optional[PracticeStatusEnum] = None
    r"""Player practice participation status"""

    wednesday: Optional[PracticeStatusEnum] = None
    r"""Player practice participation status"""


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
