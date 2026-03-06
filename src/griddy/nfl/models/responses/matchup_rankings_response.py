from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.team_matchup_rankings import TeamMatchupRankings
from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy.nfl.types import BaseModel


class MatchupRankingsResponse(BaseModel):
    """Response containing matchup rankings."""

    game_id: Annotated[Optional[int], pydantic.Field(alias="gameId")] = None

    game_key: Annotated[Optional[int], pydantic.Field(alias="gameKey")] = None

    home_team_matchup_rankings: Annotated[
        Optional[TeamMatchupRankings], pydantic.Field(alias="homeTeamMatchupRankings")
    ] = None
    r"""Comprehensive team rankings across multiple statistical categories"""

    season: Optional[int] = None

    season_type: Annotated[
        Optional[SeasonTypeEnum], pydantic.Field(alias="seasonType")
    ] = None
    r"""Type of NFL season"""

    visitor_team_matchup_rankings: Annotated[
        Optional[TeamMatchupRankings],
        pydantic.Field(alias="visitorTeamMatchupRankings"),
    ] = None
    r"""Comprehensive team rankings across multiple statistical categories"""

    week: Optional[int] = None
