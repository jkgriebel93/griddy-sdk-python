"""Response model for NGS live scores endpoint."""

from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.types import BaseModel


class NgsTeamScore(BaseModel):
    """Score breakdown by quarter for a team."""

    point_total: Annotated[Optional[int], pydantic.Field(alias="pointTotal")] = None
    point_q1: Annotated[Optional[int], pydantic.Field(alias="pointQ1")] = None
    point_q2: Annotated[Optional[int], pydantic.Field(alias="pointQ2")] = None
    point_q3: Annotated[Optional[int], pydantic.Field(alias="pointQ3")] = None
    point_q4: Annotated[Optional[int], pydantic.Field(alias="pointQ4")] = None
    point_ot: Annotated[Optional[int], pydantic.Field(alias="pointOT")] = None
    timeouts_remaining: Annotated[
        Optional[int], pydantic.Field(alias="timeoutsRemaining")
    ] = None


class NgsGameScoreDetail(BaseModel):
    """Detailed score information for a game."""

    time: Optional[str] = None
    phase: Optional[str | int] = None
    visitor_team_score: Annotated[
        Optional[NgsTeamScore], pydantic.Field(alias="visitorTeamScore")
    ] = None
    home_team_score: Annotated[
        Optional[NgsTeamScore], pydantic.Field(alias="homeTeamScore")
    ] = None


class NgsTeamInfo(BaseModel):
    """Team information in NGS responses."""

    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    smart_id: Annotated[Optional[str], pydantic.Field(alias="smartId")] = None
    logo: Optional[str] = None
    abbr: Optional[str] = None
    city_state: Annotated[Optional[str], pydantic.Field(alias="cityState")] = None
    full_name: Annotated[Optional[str], pydantic.Field(alias="fullName")] = None
    nick: Optional[str] = None
    team_type: Annotated[Optional[str], pydantic.Field(alias="teamType")] = None
    conference_abbr: Annotated[
        Optional[str], pydantic.Field(alias="conferenceAbbr")
    ] = None
    division_abbr: Annotated[Optional[str], pydantic.Field(alias="divisionAbbr")] = None


class NgsLiveGameScore(BaseModel):
    """A single game score entry in the live scores response."""

    game_id: Annotated[Optional[int], pydantic.Field(alias="gameId")] = None
    game_key: Annotated[Optional[int], pydantic.Field(alias="gameKey")] = None
    game_smart_id: Annotated[Optional[str], pydantic.Field(alias="gameSmartId")] = None
    home_team_id: Annotated[Optional[str], pydantic.Field(alias="homeTeamId")] = None
    home_team_abbr: Annotated[Optional[str], pydantic.Field(alias="homeTeamAbbr")] = (
        None
    )
    home_score: Annotated[Optional[int], pydantic.Field(alias="homeScore")] = None
    away_team_id: Annotated[Optional[str], pydantic.Field(alias="awayTeamId")] = None
    away_team_abbr: Annotated[Optional[str], pydantic.Field(alias="awayTeamAbbr")] = (
        None
    )
    away_score: Annotated[Optional[int], pydantic.Field(alias="awayScore")] = None
    game_clock: Annotated[Optional[str], pydantic.Field(alias="gameClock")] = None
    game_status: Annotated[Optional[str], pydantic.Field(alias="gameStatus")] = None
    game_date: Annotated[Optional[str], pydantic.Field(alias="gameDate")] = None
    game_time_eastern: Annotated[
        Optional[str], pydantic.Field(alias="gameTimeEastern")
    ] = None
    game_time: Annotated[Optional[str], pydantic.Field(alias="gameTime")] = None
    score: Optional[NgsGameScoreDetail] = None
    visitor_team: Annotated[
        Optional[NgsTeamInfo], pydantic.Field(alias="visitorTeam")
    ] = None
    home_team: Annotated[Optional[NgsTeamInfo], pydantic.Field(alias="homeTeam")] = None


class NgsLiveScoresResponse(BaseModel):
    """Response from the NGS live scores endpoint."""

    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    week: Optional[int] = None
    scores: Optional[List[NgsLiveGameScore]] = None
