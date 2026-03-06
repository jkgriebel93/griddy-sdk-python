from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel
from .season_stats import SeasonStats


class CareerStats(BaseModel):
    """Aggregated career statistics for a player."""

    season_stats: Annotated[
        Optional[List[SeasonStats]], pydantic.Field(alias="seasonStats")
    ] = None

    total_games: Annotated[Optional[int], pydantic.Field(alias="totalGames")] = None

    total_starts: Annotated[Optional[int], pydantic.Field(alias="totalStarts")] = None
