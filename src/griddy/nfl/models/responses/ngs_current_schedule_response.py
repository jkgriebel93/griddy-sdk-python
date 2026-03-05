"""Response model for NGS current schedule endpoint."""

from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.game_schedule import GameSchedule
from griddy.nfl.types import BaseModel


class NgsCurrentScheduleResponse(BaseModel):
    """Response from the NGS current schedule endpoint."""

    season: Optional[int] = None
    r"""Season year"""

    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    r"""Season type (REG, PRE, POST)"""

    week: Optional[int] = None
    r"""Current week number"""

    games: Optional[List[GameSchedule]] = None
    r"""List of games in the current week"""
