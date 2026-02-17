"""NGS Game Center Overview entity models."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.types import BaseModel


class NgsPassingZoneTypedDict(TypedDict):
    """Passing zone statistics."""

    type: NotRequired[str]
    line_of_scrimmage_distance: NotRequired[str]
    section: NotRequired[str]
    attempts: NotRequired[int]
    completions: NotRequired[int]
    completion_pct: NotRequired[float]
    interceptions: NotRequired[int]
    touchdowns: NotRequired[int]
    yards: NotRequired[int]
    qb_rating: NotRequired[float]
    qb_rating_success_level: NotRequired[str]


class NgsPassingZone(BaseModel):
    """Passing zone statistics."""

    type: Optional[str] = None
    line_of_scrimmage_distance: Annotated[
        Optional[str], pydantic.Field(alias="lineOfScrimmageDistance")
    ] = None
    section: Optional[str] = None
    attempts: Optional[int] = None
    completions: Optional[int] = None
    completion_pct: Annotated[
        Optional[float], pydantic.Field(alias="completionPct")
    ] = None
    interceptions: Optional[int] = None
    touchdowns: Optional[int] = None
    yards: Optional[int] = None
    qb_rating: Annotated[Optional[float], pydantic.Field(alias="qbRating")] = None
    qb_rating_success_level: Annotated[
        Optional[str], pydantic.Field(alias="qbRatingSuccessLevel")
    ] = None


class NgsPasserInfoTypedDict(TypedDict):
    """Passer information in game overview."""

    game_id: NotRequired[int]
    esb_id: NotRequired[str]
    team_id: NotRequired[str]
    team_abbr: NotRequired[str]
    short_name: NotRequired[str]
    position: NotRequired[str]
    jersey_number: NotRequired[int]
    player_name: NotRequired[str]
    pass_yards: NotRequired[int]
    touchdowns: NotRequired[int]
    interceptions: NotRequired[int]
    attempts: NotRequired[int]
    completions: NotRequired[int]
    headshot: NotRequired[str]
    zones: NotRequired[List[NgsPassingZoneTypedDict]]


class NgsPasserInfo(BaseModel):
    """Passer information in game overview."""

    game_id: Annotated[Optional[int], pydantic.Field(alias="gameId")] = None
    esb_id: Annotated[Optional[str], pydantic.Field(alias="esbId")] = None
    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    team_abbr: Annotated[Optional[str], pydantic.Field(alias="teamAbbr")] = None
    short_name: Annotated[Optional[str], pydantic.Field(alias="shortName")] = None
    position: Optional[str] = None
    jersey_number: Annotated[Optional[int], pydantic.Field(alias="jerseyNumber")] = None
    player_name: Annotated[Optional[str], pydantic.Field(alias="playerName")] = None
    pass_yards: Annotated[Optional[int], pydantic.Field(alias="passYards")] = None
    touchdowns: Optional[int] = None
    interceptions: Optional[int] = None
    attempts: Optional[int] = None
    completions: Optional[int] = None
    headshot: Optional[str] = None
    zones: Optional[List[NgsPassingZone]] = None


class NgsPassersOverviewTypedDict(TypedDict):
    """Passers overview for home and visitor teams."""

    home: NotRequired[NgsPasserInfoTypedDict]
    visitor: NotRequired[NgsPasserInfoTypedDict]


class NgsPassersOverview(BaseModel):
    """Passers overview for home and visitor teams."""

    home: Optional[NgsPasserInfo] = None
    visitor: Optional[NgsPasserInfo] = None


class NgsRushLocationStatsTypedDict(TypedDict):
    """Rush location statistics."""

    yards: NotRequired[int]
    attempts: NotRequired[int]
    touchdowns: NotRequired[int]
    distance: NotRequired[float]
    avg_yards: NotRequired[float]
    avg_distance: NotRequired[float]
    avg_time_to_los: NotRequired[float]


class NgsRushLocationStats(BaseModel):
    """Rush location statistics."""

    yards: Optional[int] = None
    attempts: Optional[int] = None
    touchdowns: Optional[int] = None
    distance: Optional[float] = None
    avg_yards: Annotated[Optional[float], pydantic.Field(alias="avgYards")] = None
    avg_distance: Annotated[Optional[float], pydantic.Field(alias="avgDistance")] = None
    avg_time_to_los: Annotated[
        Optional[float], pydantic.Field(alias="avgTimeToLos")
    ] = None


class NgsRushInfoTypedDict(TypedDict):
    """Rush info for a rusher."""

    yards: NotRequired[int]
    attempts: NotRequired[int]
    touchdowns: NotRequired[int]
    distance: NotRequired[float]
    avg_yards: NotRequired[float]
    avg_distance: NotRequired[float]
    avg_time_to_los: NotRequired[float]
    rush_location_map: NotRequired[Dict[str, NgsRushLocationStatsTypedDict]]
    pre_snap_rush_location_map: NotRequired[Dict[str, NgsRushLocationStatsTypedDict]]


class NgsRushInfo(BaseModel):
    """Rush info for a rusher."""

    yards: Optional[int] = None
    attempts: Optional[int] = None
    touchdowns: Optional[int] = None
    distance: Optional[float] = None
    avg_yards: Annotated[Optional[float], pydantic.Field(alias="avgYards")] = None
    avg_distance: Annotated[Optional[float], pydantic.Field(alias="avgDistance")] = None
    avg_time_to_los: Annotated[
        Optional[float], pydantic.Field(alias="avgTimeToLos")
    ] = None
    rush_location_map: Annotated[
        Optional[Dict[str, NgsRushLocationStats]],
        pydantic.Field(alias="rushLocationMap"),
    ] = None
    pre_snap_rush_location_map: Annotated[
        Optional[Dict[str, NgsRushLocationStats]],
        pydantic.Field(alias="preSnapRushLocationMap"),
    ] = None


class NgsRusherInfoTypedDict(TypedDict):
    """Rusher information in game overview."""

    esb_id: NotRequired[str]
    jersey_number: NotRequired[int]
    player_name: NotRequired[str]
    position: NotRequired[str]
    rush_yards: NotRequired[int]
    short_name: NotRequired[str]
    team_id: NotRequired[str]
    yards: NotRequired[int]
    attempts: NotRequired[int]
    touchdowns: NotRequired[int]
    headshot: NotRequired[str]
    rush_info: NotRequired[NgsRushInfoTypedDict]


class NgsRusherInfo(BaseModel):
    """Rusher information in game overview."""

    esb_id: Annotated[Optional[str], pydantic.Field(alias="esbId")] = None
    jersey_number: Annotated[Optional[int], pydantic.Field(alias="jerseyNumber")] = None
    player_name: Annotated[Optional[str], pydantic.Field(alias="playerName")] = None
    position: Optional[str] = None
    rush_yards: Annotated[Optional[int], pydantic.Field(alias="rushYards")] = None
    short_name: Annotated[Optional[str], pydantic.Field(alias="shortName")] = None
    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    yards: Optional[int] = None
    attempts: Optional[int] = None
    touchdowns: Optional[int] = None
    headshot: Optional[str] = None
    rush_info: Annotated[Optional[NgsRushInfo], pydantic.Field(alias="rushInfo")] = None


class NgsRushersOverviewTypedDict(TypedDict):
    """Rushers overview for home and visitor teams."""

    home: NotRequired[List[NgsRusherInfoTypedDict]]
    visitor: NotRequired[List[NgsRusherInfoTypedDict]]


class NgsRushersOverview(BaseModel):
    """Rushers overview for home and visitor teams."""

    home: Optional[List[NgsRusherInfo]] = None
    visitor: Optional[List[NgsRusherInfo]] = None


class NgsReceptionInfoTypedDict(TypedDict):
    """Reception info for a receiver."""

    avg_air_yards: NotRequired[float]
    avg_cushion: NotRequired[float]
    avg_separation: NotRequired[float]
    targets: NotRequired[int]
    receptions: NotRequired[int]
    touchdowns: NotRequired[int]


class NgsReceptionInfo(BaseModel):
    """Reception info for a receiver."""

    avg_air_yards: Annotated[Optional[float], pydantic.Field(alias="avgAirYards")] = (
        None
    )
    avg_cushion: Annotated[Optional[float], pydantic.Field(alias="avgCushion")] = None
    avg_separation: Annotated[
        Optional[float], pydantic.Field(alias="avgSeparation")
    ] = None
    targets: Optional[int] = None
    receptions: Optional[int] = None
    touchdowns: Optional[int] = None


class NgsReceiverInfoTypedDict(TypedDict):
    """Receiver information in game overview."""

    esb_id: NotRequired[str]
    jersey_number: NotRequired[int]
    player_name: NotRequired[str]
    position: NotRequired[str]
    rec_yards: NotRequired[int]
    short_name: NotRequired[str]
    team_id: NotRequired[str]
    targets: NotRequired[int]
    receptions: NotRequired[int]
    touchdowns: NotRequired[int]
    headshot: NotRequired[str]
    reception_info: NotRequired[NgsReceptionInfoTypedDict]


class NgsReceiverInfo(BaseModel):
    """Receiver information in game overview."""

    esb_id: Annotated[Optional[str], pydantic.Field(alias="esbId")] = None
    jersey_number: Annotated[Optional[int], pydantic.Field(alias="jerseyNumber")] = None
    player_name: Annotated[Optional[str], pydantic.Field(alias="playerName")] = None
    position: Optional[str] = None
    rec_yards: Annotated[Optional[int], pydantic.Field(alias="recYards")] = None
    short_name: Annotated[Optional[str], pydantic.Field(alias="shortName")] = None
    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    targets: Optional[int] = None
    receptions: Optional[int] = None
    touchdowns: Optional[int] = None
    headshot: Optional[str] = None
    reception_info: Annotated[
        Optional[NgsReceptionInfo], pydantic.Field(alias="receptionInfo")
    ] = None


class NgsLeagueAverageTypedDict(TypedDict):
    """League average value."""

    avg: NotRequired[float]


class NgsLeagueAverage(BaseModel):
    """League average value."""

    avg: Optional[float] = None


class NgsReceiversOverviewTypedDict(TypedDict):
    """Receivers overview for home and visitor teams."""

    league_average_receiver_separation: NotRequired[NgsLeagueAverageTypedDict]
    home: NotRequired[List[NgsReceiverInfoTypedDict]]
    visitor: NotRequired[List[NgsReceiverInfoTypedDict]]


class NgsReceiversOverview(BaseModel):
    """Receivers overview for home and visitor teams."""

    league_average_receiver_separation: Annotated[
        Optional[NgsLeagueAverage],
        pydantic.Field(alias="leagueAverageReceiverSeparation"),
    ] = None
    home: Optional[List[NgsReceiverInfo]] = None
    visitor: Optional[List[NgsReceiverInfo]] = None


class NgsPassRusherInfoTypedDict(TypedDict):
    """Pass rusher information in game overview."""

    esb_id: NotRequired[str]
    gsis_id: NotRequired[str]
    team_id: NotRequired[str]
    player_name: NotRequired[str]
    short_name: NotRequired[str]
    jersey_number: NotRequired[int]
    position: NotRequired[str]
    blitz_count: NotRequired[int]
    avg_separation_to_qb: NotRequired[float]
    headshot: NotRequired[str]
    tackles: NotRequired[int]
    assists: NotRequired[int]
    sacks: NotRequired[float]
    forced_fumbles: NotRequired[int]


class NgsPassRusherInfo(BaseModel):
    """Pass rusher information in game overview."""

    esb_id: Annotated[Optional[str], pydantic.Field(alias="esbId")] = None
    gsis_id: Annotated[Optional[str], pydantic.Field(alias="gsisId")] = None
    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    player_name: Annotated[Optional[str], pydantic.Field(alias="playerName")] = None
    short_name: Annotated[Optional[str], pydantic.Field(alias="shortName")] = None
    jersey_number: Annotated[Optional[int], pydantic.Field(alias="jerseyNumber")] = None
    position: Optional[str] = None
    blitz_count: Annotated[Optional[int], pydantic.Field(alias="blitzCount")] = None
    avg_separation_to_qb: Annotated[
        Optional[float], pydantic.Field(alias="avgSeparationToQb")
    ] = None
    headshot: Optional[str] = None
    tackles: Optional[int] = None
    assists: Optional[int] = None
    sacks: Optional[float] = None
    forced_fumbles: Annotated[Optional[int], pydantic.Field(alias="forcedFumbles")] = (
        None
    )


class NgsPassRushersOverviewTypedDict(TypedDict):
    """Pass rushers overview for home and visitor teams."""

    league_average_separation_to_qb: NotRequired[NgsLeagueAverageTypedDict]
    home: NotRequired[List[NgsPassRusherInfoTypedDict]]
    visitor: NotRequired[List[NgsPassRusherInfoTypedDict]]


class NgsPassRushersOverview(BaseModel):
    """Pass rushers overview for home and visitor teams."""

    league_average_separation_to_qb: Annotated[
        Optional[NgsLeagueAverage], pydantic.Field(alias="leagueAverageSeparationToQb")
    ] = None
    home: Optional[List[NgsPassRusherInfo]] = None
    visitor: Optional[List[NgsPassRusherInfo]] = None


class NgsGameSpeedLeaderTypedDict(TypedDict):
    """Speed leader for a game."""

    gsis_play_id: NotRequired[int]
    esb_id: NotRequired[str]
    jersey_number: NotRequired[int]
    player_name: NotRequired[str]
    position: NotRequired[str]
    short_name: NotRequired[str]
    team_id: NotRequired[str]
    max_speed: NotRequired[float]
    headshot: NotRequired[str]


class NgsGameSpeedLeader(BaseModel):
    """Speed leader for a game."""

    gsis_play_id: Annotated[Optional[int], pydantic.Field(alias="gsisPlayId")] = None
    esb_id: Annotated[Optional[str], pydantic.Field(alias="esbId")] = None
    jersey_number: Annotated[Optional[int], pydantic.Field(alias="jerseyNumber")] = None
    player_name: Annotated[Optional[str], pydantic.Field(alias="playerName")] = None
    position: Optional[str] = None
    short_name: Annotated[Optional[str], pydantic.Field(alias="shortName")] = None
    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    max_speed: Annotated[Optional[float], pydantic.Field(alias="maxSpeed")] = None
    headshot: Optional[str] = None


class NgsTackleInfoTypedDict(TypedDict):
    """Tackle info with time to tackle."""

    time_to_tackle: NotRequired[float]


class NgsTackleInfo(BaseModel):
    """Tackle info with time to tackle."""

    time_to_tackle: Annotated[Optional[float], pydantic.Field(alias="timeToTackle")] = (
        None
    )


class NgsGameSackLeaderTypedDict(TypedDict):
    """Sack leader for a game."""

    gsis_play_id: NotRequired[int]
    esb_id: NotRequired[str]
    jersey_number: NotRequired[int]
    player_name: NotRequired[str]
    position: NotRequired[str]
    short_name: NotRequired[str]
    team_id: NotRequired[str]
    headshot: NotRequired[str]
    tackle_info: NotRequired[NgsTackleInfoTypedDict]


class NgsGameSackLeader(BaseModel):
    """Sack leader for a game."""

    gsis_play_id: Annotated[Optional[int], pydantic.Field(alias="gsisPlayId")] = None
    esb_id: Annotated[Optional[str], pydantic.Field(alias="esbId")] = None
    jersey_number: Annotated[Optional[int], pydantic.Field(alias="jerseyNumber")] = None
    player_name: Annotated[Optional[str], pydantic.Field(alias="playerName")] = None
    position: Optional[str] = None
    short_name: Annotated[Optional[str], pydantic.Field(alias="shortName")] = None
    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    headshot: Optional[str] = None
    tackle_info: Annotated[
        Optional[NgsTackleInfo], pydantic.Field(alias="tackleInfo")
    ] = None


class NgsPassInfoTypedDict(TypedDict):
    """Pass info with air distance."""

    air_distance: NotRequired[float]


class NgsPassInfo(BaseModel):
    """Pass info with air distance."""

    air_distance: Annotated[Optional[float], pydantic.Field(alias="airDistance")] = None


class NgsGamePassDistanceLeaderTypedDict(TypedDict):
    """Pass distance leader for a game."""

    gsis_play_id: NotRequired[int]
    esb_id: NotRequired[str]
    jersey_number: NotRequired[int]
    player_name: NotRequired[str]
    position: NotRequired[str]
    short_name: NotRequired[str]
    team_id: NotRequired[str]
    headshot: NotRequired[str]
    pass_info: NotRequired[NgsPassInfoTypedDict]


class NgsGamePassDistanceLeader(BaseModel):
    """Pass distance leader for a game."""

    gsis_play_id: Annotated[Optional[int], pydantic.Field(alias="gsisPlayId")] = None
    esb_id: Annotated[Optional[str], pydantic.Field(alias="esbId")] = None
    jersey_number: Annotated[Optional[int], pydantic.Field(alias="jerseyNumber")] = None
    player_name: Annotated[Optional[str], pydantic.Field(alias="playerName")] = None
    position: Optional[str] = None
    short_name: Annotated[Optional[str], pydantic.Field(alias="shortName")] = None
    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    headshot: Optional[str] = None
    pass_info: Annotated[Optional[NgsPassInfo], pydantic.Field(alias="passInfo")] = None


class NgsSpeedLeadersMapTypedDict(TypedDict):
    """Speed leaders for home and visitor."""

    home: NotRequired[NgsGameSpeedLeaderTypedDict]
    visitor: NotRequired[NgsGameSpeedLeaderTypedDict]


class NgsSpeedLeadersMap(BaseModel):
    """Speed leaders for home and visitor."""

    home: Optional[NgsGameSpeedLeader] = None
    visitor: Optional[NgsGameSpeedLeader] = None


class NgsSackLeadersMapTypedDict(TypedDict):
    """Sack leaders for home and visitor."""

    home: NotRequired[NgsGameSackLeaderTypedDict]
    visitor: NotRequired[NgsGameSackLeaderTypedDict]


class NgsSackLeadersMap(BaseModel):
    """Sack leaders for home and visitor."""

    home: Optional[NgsGameSackLeader] = None
    visitor: Optional[NgsGameSackLeader] = None


class NgsPassDistanceLeadersMapTypedDict(TypedDict):
    """Pass distance leaders for home and visitor."""

    home: NotRequired[NgsGamePassDistanceLeaderTypedDict]
    visitor: NotRequired[NgsGamePassDistanceLeaderTypedDict]


class NgsPassDistanceLeadersMap(BaseModel):
    """Pass distance leaders for home and visitor."""

    home: Optional[NgsGamePassDistanceLeader] = None
    visitor: Optional[NgsGamePassDistanceLeader] = None


class NgsGameLeadersTypedDict(TypedDict):
    """Game leaders for speed, sacks, and pass distance."""

    speed_leaders: NotRequired[NgsSpeedLeadersMapTypedDict]
    time_to_sack_leaders: NotRequired[NgsSackLeadersMapTypedDict]
    pass_distance_leaders: NotRequired[NgsPassDistanceLeadersMapTypedDict]


class NgsGameLeaders(BaseModel):
    """Game leaders for speed, sacks, and pass distance."""

    speed_leaders: Annotated[
        Optional[NgsSpeedLeadersMap], pydantic.Field(alias="speedLeaders")
    ] = None
    time_to_sack_leaders: Annotated[
        Optional[NgsSackLeadersMap], pydantic.Field(alias="timeToSackLeaders")
    ] = None
    pass_distance_leaders: Annotated[
        Optional[NgsPassDistanceLeadersMap], pydantic.Field(alias="passDistanceLeaders")
    ] = None


class NgsGameScheduleInfoTypedDict(TypedDict):
    """Game schedule information in overview."""

    game_key: NotRequired[int]
    game_date: NotRequired[str]
    game_id: NotRequired[int]
    game_time_eastern: NotRequired[str]
    home_team_abbr: NotRequired[str]
    home_team_id: NotRequired[str]
    season: NotRequired[int]
    season_type: NotRequired[str]
    visitor_team_abbr: NotRequired[str]
    visitor_team_id: NotRequired[str]
    week: NotRequired[int]


class NgsGameScheduleInfo(BaseModel):
    """Game schedule information in overview."""

    game_key: Annotated[Optional[int], pydantic.Field(alias="gameKey")] = None
    game_date: Annotated[Optional[str], pydantic.Field(alias="gameDate")] = None
    game_id: Annotated[Optional[int], pydantic.Field(alias="gameId")] = None
    game_time_eastern: Annotated[
        Optional[str], pydantic.Field(alias="gameTimeEastern")
    ] = None
    home_team_abbr: Annotated[Optional[str], pydantic.Field(alias="homeTeamAbbr")] = (
        None
    )
    home_team_id: Annotated[Optional[str], pydantic.Field(alias="homeTeamId")] = None
    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    visitor_team_abbr: Annotated[
        Optional[str], pydantic.Field(alias="visitorTeamAbbr")
    ] = None
    visitor_team_id: Annotated[Optional[str], pydantic.Field(alias="visitorTeamId")] = (
        None
    )
    week: Optional[int] = None
