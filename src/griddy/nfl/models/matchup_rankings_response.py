from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum

from ..types import BaseModel
from .team_matchup_rankings import TeamMatchupRankings, TeamMatchupRankingsTypedDict


class MatchupRankingsResponseTypedDict(TypedDict):
    game_id: NotRequired[int]
    game_key: NotRequired[int]
    home_team_matchup_rankings: NotRequired[TeamMatchupRankingsTypedDict]
    r"""Comprehensive team rankings across multiple statistical categories"""
    season: NotRequired[int]
    season_type: NotRequired[SeasonTypeEnum]
    r"""Type of NFL season"""
    visitor_team_matchup_rankings: NotRequired[TeamMatchupRankingsTypedDict]
    r"""Comprehensive team rankings across multiple statistical categories"""
    week: NotRequired[int]


class MatchupRankingsResponse(BaseModel):
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
