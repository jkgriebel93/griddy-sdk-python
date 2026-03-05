from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.player import Player
from griddy.nfl.models.entities.team import Team
from griddy.nfl.types import BaseModel


class PlayerStatsResponsePagination(BaseModel):
    limit: Optional[int] = None

    offset: Optional[int] = None

    total: Optional[int] = None


class PlayerStatsResponseStats(BaseModel):
    r"""Statistics object varies by category"""


class PlayerStatsResponsePlayer(BaseModel):
    player: Optional[Player] = None

    stats: Optional[PlayerStatsResponseStats] = None
    r"""Statistics object varies by category"""

    team: Optional[Team] = None


class PlayerStatsResponse(BaseModel):
    pagination: Optional[PlayerStatsResponsePagination] = None

    players: Optional[List[PlayerStatsResponsePlayer]] = None

    season: Optional[int] = None

    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None

    stat_category: Annotated[Optional[str], pydantic.Field(alias="statCategory")] = None
