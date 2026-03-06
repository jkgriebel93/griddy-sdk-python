from __future__ import annotations

from datetime import datetime
from typing import Literal, Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel
from .player import Player
from .team import Team

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


class Transaction(BaseModel):
    """NFL player transaction such as a trade, signing, or release."""

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
