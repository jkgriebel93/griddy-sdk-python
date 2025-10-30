from __future__ import annotations

from datetime import datetime
from typing import Literal, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel
from .player import Player, PlayerTypedDict
from .team import Team, TeamTypedDict

TransactionType = Literal[
    "TRADE",
    "SIGNED",
    "RELEASED",
    "WAIVED",
    "PRACTICE_SQUAD",
    "IR",
    "SUSPENDED",
    "ACTIVATED",
]


class TransactionTypedDict(TypedDict):
    compensation_details: NotRequired[str]
    r"""Trade compensation or contract details"""
    date_: NotRequired[datetime]
    details: NotRequired[str]
    r"""Transaction details"""
    id: NotRequired[str]
    player: NotRequired[PlayerTypedDict]
    related_team: NotRequired[TeamTypedDict]
    team: NotRequired[TeamTypedDict]
    type: NotRequired[TransactionType]


class Transaction(BaseModel):
    compensation_details: Annotated[
        Optional[str], pydantic.Field(alias="compensationDetails")
    ] = None
    r"""Trade compensation or contract details"""

    date_: Annotated[Optional[datetime], pydantic.Field(alias="date")] = None

    details: Optional[str] = None
    r"""Transaction details"""

    id: Optional[str] = None

    player: Optional[Player] = None

    related_team: Annotated[Optional[Team], pydantic.Field(alias="relatedTeam")] = None

    team: Optional[Team] = None

    type: Optional[TransactionType] = None
