from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ...types import BaseModel
from .season_stats import SeasonStats, SeasonStatsTypedDict


class CareerStatsTypedDict(TypedDict):
    season_stats: NotRequired[List[SeasonStatsTypedDict]]
    total_games: NotRequired[int]
    total_starts: NotRequired[int]


class CareerStats(BaseModel):
    season_stats: Annotated[
        Optional[List[SeasonStats]], pydantic.Field(alias="seasonStats")
    ] = None

    total_games: Annotated[Optional[int], pydantic.Field(alias="totalGames")] = None

    total_starts: Annotated[Optional[int], pydantic.Field(alias="totalStarts")] = None
