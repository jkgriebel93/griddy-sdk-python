from __future__ import annotations
from .gameodds import GameOdds, GameOddsTypedDict
from .seasontypeenum import SeasonTypeEnum
from ..types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


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
