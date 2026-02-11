"""Response model for NGS live scores endpoint."""

from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.types import BaseModel


class NgsTeamScoreTypedDict(TypedDict):
    """Score breakdown by quarter for a team."""

    point_total: NotRequired[int]
    point_q1: NotRequired[int]
    point_q2: NotRequired[int]
    point_q3: NotRequired[int]
    point_q4: NotRequired[int]
    point_ot: NotRequired[int]
    timeouts_remaining: NotRequired[int]


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


class NgsGameScoreDetailTypedDict(TypedDict):
    """Detailed score information for a game."""

    time: NotRequired[str]
    phase: NotRequired[str | int]
    visitor_team_score: NotRequired[NgsTeamScoreTypedDict]
    home_team_score: NotRequired[NgsTeamScoreTypedDict]


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


class NgsTeamInfoTypedDict(TypedDict):
    """Team information in NGS responses."""

    team_id: NotRequired[str]
    smart_id: NotRequired[str]
    logo: NotRequired[str]
    abbr: NotRequired[str]
    city_state: NotRequired[str]
    full_name: NotRequired[str]
    nick: NotRequired[str]
    team_type: NotRequired[str]
    conference_abbr: NotRequired[str]
    division_abbr: NotRequired[str]


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


class NgsLiveGameScoreTypedDict(TypedDict):
    """A single game score entry in the live scores response."""

    game_id: NotRequired[int]
    game_key: NotRequired[int]
    game_smart_id: NotRequired[str]
    home_team_id: NotRequired[str]
    home_team_abbr: NotRequired[str]
    home_score: NotRequired[int]
    away_team_id: NotRequired[str]
    away_team_abbr: NotRequired[str]
    away_score: NotRequired[int]
    game_clock: NotRequired[str]
    game_status: NotRequired[str]
    game_date: NotRequired[str]
    game_time_eastern: NotRequired[str]
    game_time: NotRequired[str]
    score: NotRequired[NgsGameScoreDetailTypedDict]
    visitor_team: NotRequired[NgsTeamInfoTypedDict]
    home_team: NotRequired[NgsTeamInfoTypedDict]


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


class NgsLiveScoresResponseTypedDict(TypedDict):
    """Response from the NGS live scores endpoint."""

    season: NotRequired[int]
    season_type: NotRequired[str]
    week: NotRequired[int]
    scores: NotRequired[List[NgsLiveGameScoreTypedDict]]


class NgsLiveScoresResponse(BaseModel):
    """Response from the NGS live scores endpoint."""

    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    week: Optional[int] = None
    scores: Optional[List[NgsLiveGameScore]] = None
