"""Response model for NGS current schedule endpoint."""

from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.models.entities.game_schedule import GameSchedule, GameScheduleTypedDict
from griddy_nfl.types import BaseModel


class NgsCurrentScheduleResponseTypedDict(TypedDict):
    """Response from the NGS current schedule endpoint."""

    season: NotRequired[int]
    r"""Season year"""
    season_type: NotRequired[str]
    r"""Season type (REG, PRE, POST)"""
    week: NotRequired[int]
    r"""Current week number"""
    games: NotRequired[List[GameScheduleTypedDict]]
    r"""List of games in the current week"""


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
