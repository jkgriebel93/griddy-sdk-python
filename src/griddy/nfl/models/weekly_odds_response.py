from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel
from .game_odds import GameOdds, GameOddsTypedDict
from .season_type_enum import SeasonTypeEnum


class WeeklyOddsResponseTypedDict(TypedDict):
    games: NotRequired[List[GameOddsTypedDict]]
    season: NotRequired[str]
    r"""Season year"""
    season_type: NotRequired[SeasonTypeEnum]
    r"""Type of NFL season"""
    week: NotRequired[str]
    r"""Week number"""


class WeeklyOddsResponse(BaseModel):
    games: Optional[List[GameOdds]] = None

    season: Optional[str] = None
    r"""Season year"""

    season_type: Annotated[
        Optional[SeasonTypeEnum], pydantic.Field(alias="seasonType")
    ] = None
    r"""Type of NFL season"""

    week: Optional[str] = None
    r"""Week number"""
