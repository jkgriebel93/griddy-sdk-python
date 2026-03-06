from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.game_odds import GameOdds
from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy.nfl.types import BaseModel


class WeeklyOddsResponse(BaseModel):
    """Response containing weekly betting odds."""

    games: Optional[List[GameOdds]] = None

    season: Optional[str] = None
    r"""Season year"""

    season_type: Annotated[
        Optional[SeasonTypeEnum], pydantic.Field(alias="seasonType")
    ] = None
    r"""Type of NFL season"""

    week: Optional[str] = None
    r"""Week number"""
