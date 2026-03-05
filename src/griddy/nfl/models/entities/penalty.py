from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel
from .player import Player
from .team import Team


class Penalty(BaseModel):
    accepted: Optional[bool] = None

    no_play: Annotated[Optional[bool], pydantic.Field(alias="noPlay")] = None

    player: Optional[Player] = None

    team: Optional[Team] = None

    type: Optional[str] = None

    yards: Optional[int] = None
