from __future__ import annotations

from datetime import date, datetime
from typing import List, Literal, Optional

import pydantic
from pydantic import model_serializer
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.models.enums.meridiem_enum import MeridiemEnum
from griddy_nfl.models.enums.season_type_enum import SeasonTypeEnum

from ...types import UNSET, UNSET_SENTINEL, BaseModel, Nullable, OptionalNullable
from .broadcast_info import BroadcastInfo, BroadcastInfoTypedDict
from .external_id import ExternalID, ExternalIDTypedDict
from .standings import Standings, StandingsTypedDict
from .team import Team, TeamTypedDict
from .ticket_vendor import TicketVendor, TicketVendorTypedDict
from .venue import Venue, VenueTypedDict

WeeklyGameDetailCategory = Literal["MNF", "SNF", "TNF", "OTHER"]
r"""Prime time game designation"""


class WeeklyGameDetailExtensionTypedDict(TypedDict):
    pass


class WeeklyGameDetailExtension(BaseModel):
    pass


WeeklyGameDetailStatus = Literal[
    "SCHEDULED", "IN_PROGRESS", "FINAL", "POSTPONED", "CANCELLED", "FINAL_OVERTIME"
]
r"""Game status"""


class DriveChartPlayStatTypedDict(TypedDict):
    play_stat_id: NotRequired[str]
    gsis_player_id: NotRequired[Optional[str]]
    gsis_player_name: NotRequired[Optional[str]]
    gsis_player_jersey_number: NotRequired[Optional[str]]
    person_id: NotRequired[Optional[str]]
    stat_type: NotRequired[int]
    team_id: NotRequired[str]
    yards: NotRequired[Optional[int]]


class DriveChartPlayStat(BaseModel):
    play_stat_id: Annotated[Optional[str], pydantic.Field(alias="playStatId")] = None
    gsis_player_id: Annotated[Optional[str], pydantic.Field(alias="gsisPlayerId")] = (
        None
    )
    gsis_player_name: Annotated[
        Optional[str], pydantic.Field(alias="gsisPlayerName")
    ] = None
    gsis_player_jersey_number: Annotated[
        Optional[str], pydantic.Field(alias="gsisPlayerJerseyNumber")
    ] = None
    person_id: Annotated[Optional[str], pydantic.Field(alias="personId")] = None
    stat_type: Annotated[Optional[int], pydantic.Field(alias="statType")] = None
    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    yards: Optional[int] = None


class DriveChartPlayTypedDict(TypedDict):
    play_id: NotRequired[int]
    clock_time: NotRequired[Optional[str]]
    down: NotRequired[int]
    drive_net_yards: NotRequired[int]
    drive_play_count: NotRequired[int]
    drive_sequence: NotRequired[int]
    drive_time_of_possession: NotRequired[Optional[str]]
    next_play_type: NotRequired[str]
    next_play_is_goal_to_go: NotRequired[bool]
    pre_play_by_play: NotRequired[Optional[str]]
    play_deleted: NotRequired[bool]
    play_description: NotRequired[Optional[str]]
    play_description_with_jersey_numbers: NotRequired[Optional[str]]
    play_end_time: NotRequired[Optional[str]]
    play_is_end_of_quarter: NotRequired[bool]
    play_is_goal_to_go: NotRequired[bool]
    play_scored: NotRequired[bool]
    play_sequence_number: NotRequired[float]
    play_start_time: NotRequired[Optional[str]]
    play_type: NotRequired[str]
    quarter: NotRequired[int]
    scoring_play_type: NotRequired[str]
    scoring_team_id: NotRequired[Optional[str]]
    special_teams_play_type: NotRequired[str]
    yard_line: NotRequired[Optional[str]]
    yards_gained: NotRequired[int]
    yards_remaining: NotRequired[int]
    stats: NotRequired[List[DriveChartPlayStatTypedDict]]


class DriveChartPlay(BaseModel):
    play_id: Annotated[Optional[int], pydantic.Field(alias="playId")] = None
    clock_time: Annotated[Optional[str], pydantic.Field(alias="clockTime")] = None
    down: Optional[int] = None
    drive_net_yards: Annotated[Optional[int], pydantic.Field(alias="driveNetYards")] = (
        None
    )
    drive_play_count: Annotated[
        Optional[int], pydantic.Field(alias="drivePlayCount")
    ] = None
    drive_sequence: Annotated[Optional[int], pydantic.Field(alias="driveSequence")] = (
        None
    )
    drive_time_of_possession: Annotated[
        Optional[str], pydantic.Field(alias="driveTimeOfPossession")
    ] = None
    next_play_type: Annotated[Optional[str], pydantic.Field(alias="nextPlayType")] = (
        None
    )
    next_play_is_goal_to_go: Annotated[
        Optional[bool], pydantic.Field(alias="nextPlayIsGoalToGo")
    ] = None
    pre_play_by_play: Annotated[
        Optional[str], pydantic.Field(alias="prePlayByPlay")
    ] = None
    play_deleted: Annotated[Optional[bool], pydantic.Field(alias="playDeleted")] = None
    play_description: Annotated[
        Optional[str], pydantic.Field(alias="playDescription")
    ] = None
    play_description_with_jersey_numbers: Annotated[
        Optional[str], pydantic.Field(alias="playDescriptionWithJerseyNumbers")
    ] = None
    play_end_time: Annotated[Optional[str], pydantic.Field(alias="playEndTime")] = None
    play_is_end_of_quarter: Annotated[
        Optional[bool], pydantic.Field(alias="playIsEndOfQuarter")
    ] = None
    play_is_goal_to_go: Annotated[
        Optional[bool], pydantic.Field(alias="playIsGoalToGo")
    ] = None
    play_scored: Annotated[Optional[bool], pydantic.Field(alias="playScored")] = None
    play_sequence_number: Annotated[
        Optional[float], pydantic.Field(alias="playSequenceNumber")
    ] = None
    play_start_time: Annotated[Optional[str], pydantic.Field(alias="playStartTime")] = (
        None
    )
    play_type: Annotated[Optional[str], pydantic.Field(alias="playType")] = None
    quarter: Optional[int] = None
    scoring_play_type: Annotated[
        Optional[str], pydantic.Field(alias="scoringPlayType")
    ] = None
    scoring_team_id: Annotated[Optional[str], pydantic.Field(alias="scoringTeamId")] = (
        None
    )
    special_teams_play_type: Annotated[
        Optional[str], pydantic.Field(alias="specialTeamsPlayType")
    ] = None
    yard_line: Annotated[Optional[str], pydantic.Field(alias="yardLine")] = None
    yards_gained: Annotated[Optional[int], pydantic.Field(alias="yardsGained")] = None
    yards_remaining: Annotated[
        Optional[int], pydantic.Field(alias="yardsRemaining")
    ] = None
    stats: Optional[List[DriveChartPlayStat]] = None


class DriveTypedDict(TypedDict):
    sequence: NotRequired[int]
    team_id: NotRequired[str]
    started_clock: NotRequired[str]
    started_description: NotRequired[str]
    started_play_id: NotRequired[int]
    started_play_sequence_number: NotRequired[float]
    started_quarter: NotRequired[int]
    started_time: NotRequired[str]
    started_yard_line: NotRequired[str]
    ended_clock: NotRequired[str]
    ended_description: NotRequired[str]
    ended_play_id: NotRequired[int]
    ended_play_sequence_number: NotRequired[float]
    ended_quarter: NotRequired[int]
    ended_time: NotRequired[Optional[str]]
    ended_with_score: NotRequired[bool]
    ended_yard_line: NotRequired[str]
    first_downs: NotRequired[int]
    inside_20: NotRequired[bool]
    plays: NotRequired[int]
    time_of_possession: NotRequired[str]
    total_ended_with_score: NotRequired[bool]
    yards_gained: NotRequired[int]
    yards_gained_by_penalty: NotRequired[int]
    yards_gained_net: NotRequired[int]


class Drive(BaseModel):
    sequence: Optional[int] = None
    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    started_clock: Annotated[Optional[str], pydantic.Field(alias="startedClock")] = None
    started_description: Annotated[
        Optional[str], pydantic.Field(alias="startedDescription")
    ] = None
    started_play_id: Annotated[Optional[int], pydantic.Field(alias="startedPlayId")] = (
        None
    )
    started_play_sequence_number: Annotated[
        Optional[float], pydantic.Field(alias="startedPlaySequenceNumber")
    ] = None
    started_quarter: Annotated[
        Optional[int], pydantic.Field(alias="startedQuarter")
    ] = None
    started_time: Annotated[Optional[str], pydantic.Field(alias="startedTime")] = None
    started_yard_line: Annotated[
        Optional[str], pydantic.Field(alias="startedYardLine")
    ] = None
    ended_clock: Annotated[Optional[str], pydantic.Field(alias="endedClock")] = None
    ended_description: Annotated[
        Optional[str], pydantic.Field(alias="endedDescription")
    ] = None
    ended_play_id: Annotated[Optional[int], pydantic.Field(alias="endedPlayId")] = None
    ended_play_sequence_number: Annotated[
        Optional[float], pydantic.Field(alias="endedPlaySequenceNumber")
    ] = None
    ended_quarter: Annotated[Optional[int], pydantic.Field(alias="endedQuarter")] = None
    ended_time: Annotated[Optional[str], pydantic.Field(alias="endedTime")] = None
    ended_with_score: Annotated[
        Optional[bool], pydantic.Field(alias="endedWithScore")
    ] = None
    ended_yard_line: Annotated[Optional[str], pydantic.Field(alias="endedYardLine")] = (
        None
    )
    first_downs: Annotated[Optional[int], pydantic.Field(alias="firstDowns")] = None
    inside_20: Annotated[Optional[bool], pydantic.Field(alias="inside20")] = None
    plays: Optional[int] = None
    time_of_possession: Annotated[
        Optional[str], pydantic.Field(alias="timeOfPossession")
    ] = None
    total_ended_with_score: Annotated[
        Optional[bool], pydantic.Field(alias="totalEndedWithScore")
    ] = None
    yards_gained: Annotated[Optional[int], pydantic.Field(alias="yardsGained")] = None
    yards_gained_by_penalty: Annotated[
        Optional[int], pydantic.Field(alias="yardsGainedByPenalty")
    ] = None
    yards_gained_net: Annotated[
        Optional[int], pydantic.Field(alias="yardsGainedNet")
    ] = None


class DriveChartTypedDict(TypedDict):
    r"""Drive-by-drive data"""

    game_id: NotRequired[str]
    offset: NotRequired[int]
    drives: NotRequired[List[DriveTypedDict]]
    plays: NotRequired[List[DriveChartPlayTypedDict]]


class DriveChart(BaseModel):
    r"""Drive-by-drive data"""

    game_id: Annotated[Optional[str], pydantic.Field(alias="gameId")] = None
    offset: Optional[int] = None
    drives: Optional[List[Drive]] = None
    plays: Optional[List[DriveChartPlay]] = None


class ReplayTypedDict(TypedDict):
    pass


class Replay(BaseModel):
    type_: Annotated[Optional[str], pydantic.Field(alias="type")] = None
    authorizations: Optional[dict] = None
    description: Optional[str] = None
    duration: Optional[int] = None
    external_id: Annotated[Optional[str], pydantic.Field(alias="externalId")] = None
    ids: Optional[dict] = None
    images: Optional[list] = None
    mcp_playback_id: Annotated[Optional[str], pydantic.Field(alias="mcpPlaybackId")] = (
        None
    )
    play_ids: Annotated[Optional[list], pydantic.Field(alias="playIds")] = None
    publish_date: Annotated[Optional[str], pydantic.Field(alias="publishDate")] = None
    sub_type: Annotated[Optional[str], pydantic.Field(alias="subType")] = None
    tags: Optional[list] = None
    thumbnail: Optional[dict] = None
    title: Optional[str] = None
    videos: Optional[list] = None


class SummaryTypedDict(TypedDict):
    r"""Game summary information"""


class Summary(BaseModel):
    r"""Game summary information"""


class TaggedVideosTypedDict(TypedDict):
    r"""Tagged video content"""


class TaggedVideos(BaseModel):
    r"""Tagged video content"""


class WeeklyGameDetailTypedDict(TypedDict):
    away_team: NotRequired[TeamTypedDict]
    broadcast_info: NotRequired[BroadcastInfoTypedDict]
    category: NotRequired[Nullable[WeeklyGameDetailCategory]]
    date_: NotRequired[date]
    r"""Game date (YYYY-MM-DD)"""
    date_am_pm: NotRequired[MeridiemEnum]
    r"""Time of day indicator"""
    date_day: NotRequired[str]
    r"""Day of week (full)"""
    date_day_month: NotRequired[str]
    r"""Date in M/D format"""
    date_day_short: NotRequired[str]
    r"""Day of week (abbreviated)"""
    date_time: NotRequired[str]
    r"""Time without AM/PM"""
    date_time_am_pm: NotRequired[str]
    r"""Time with AM/PM"""
    extensions: NotRequired[List[WeeklyGameDetailExtensionTypedDict]]
    r"""Additional game data extensions"""
    external_ids: NotRequired[List[ExternalIDTypedDict]]
    game_type: NotRequired[str]
    r"""Type of game"""
    home_team: NotRequired[TeamTypedDict]
    id: NotRequired[str]
    r"""Unique game identifier"""
    international: NotRequired[bool]
    r"""Whether game is played internationally"""
    neutral_site: NotRequired[bool]
    r"""Whether game is at neutral venue"""
    phase: NotRequired[str | int]
    r"""Game phase"""
    season: NotRequired[int]
    r"""Season year"""
    season_type: NotRequired[SeasonTypeEnum]
    r"""Type of NFL season"""
    status: NotRequired[WeeklyGameDetailStatus]
    r"""Game status"""
    ticket_url: NotRequired[Nullable[str]]
    r"""Primary ticket purchase URL"""
    ticket_vendors: NotRequired[List[TicketVendorTypedDict]]
    time: NotRequired[datetime]
    r"""Game time in UTC"""
    venue: NotRequired[VenueTypedDict]
    version: NotRequired[int]
    r"""Data version number"""
    week: NotRequired[int]
    r"""Week number"""
    week_type: NotRequired[str]
    r"""Week type (e.g., REG, HOF)"""
    away_team_standings: NotRequired[StandingsTypedDict]
    drive_chart: NotRequired[Nullable[DriveChartTypedDict]]
    r"""Drive-by-drive data"""
    home_team_standings: NotRequired[StandingsTypedDict]
    replays: NotRequired[List[ReplayTypedDict]]
    r"""Replay video links"""
    summary: NotRequired[Nullable[SummaryTypedDict]]
    r"""Game summary information"""
    tagged_videos: NotRequired[Nullable[List[TaggedVideosTypedDict]]]
    r"""Tagged video content"""


class WeeklyGameDetail(BaseModel):
    away_team: Annotated[Optional[Team], pydantic.Field(alias="awayTeam")] = None

    broadcast_info: Annotated[
        Optional[BroadcastInfo], pydantic.Field(alias="broadcastInfo")
    ] = None

    category: Optional[WeeklyGameDetailCategory] = None

    date_: Annotated[Optional[str], pydantic.Field(alias="date")] = None
    r"""Game date (YYYY-MM-DD)"""

    date_am_pm: Annotated[Optional[MeridiemEnum], pydantic.Field(alias="dateAmPm")] = (
        None
    )
    r"""Time of day indicator"""

    date_day: Annotated[Optional[str], pydantic.Field(alias="dateDay")] = None
    r"""Day of week (full)"""

    date_day_month: Annotated[Optional[str], pydantic.Field(alias="dateDayMonth")] = (
        None
    )
    r"""Date in M/D format"""

    date_day_short: Annotated[Optional[str], pydantic.Field(alias="dateDayShort")] = (
        None
    )
    r"""Day of week (abbreviated)"""

    date_time: Annotated[Optional[str], pydantic.Field(alias="dateTime")] = None
    r"""Time without AM/PM"""

    date_time_am_pm: Annotated[Optional[str], pydantic.Field(alias="dateTimeAmPm")] = (
        None
    )
    r"""Time with AM/PM"""

    extensions: Optional[List[WeeklyGameDetailExtension]] = None
    r"""Additional game data extensions"""

    external_ids: Annotated[
        Optional[List[ExternalID]], pydantic.Field(alias="externalIds")
    ] = None

    game_type: Annotated[Optional[str], pydantic.Field(alias="gameType")] = None
    r"""Type of game"""

    home_team: Annotated[Optional[Team], pydantic.Field(alias="homeTeam")] = None

    id: Optional[str] = None
    r"""Unique game identifier"""

    international: Optional[bool] = None
    r"""Whether game is played internationally"""

    neutral_site: Annotated[Optional[bool], pydantic.Field(alias="neutralSite")] = None
    r"""Whether game is at neutral venue"""

    phase: Optional[str | int] = None
    r"""Game phase"""

    season: Optional[int] = None
    r"""Season year"""

    season_type: Annotated[
        Optional[SeasonTypeEnum], pydantic.Field(alias="seasonType")
    ] = None
    r"""Type of NFL season"""

    status: Optional[WeeklyGameDetailStatus] = None
    r"""Game status"""

    ticket_url: Annotated[Optional[str], pydantic.Field(alias="ticketUrl")] = None
    r"""Primary ticket purchase URL"""

    ticket_vendors: Annotated[
        Optional[List[TicketVendor]], pydantic.Field(alias="ticketVendors")
    ] = None

    time: Optional[str] = None
    r"""Game time in UTC"""

    venue: Optional[Venue] = None

    version: Optional[int] = None
    r"""Data version number"""

    week: Optional[int] = None
    r"""Week number"""

    week_type: Annotated[Optional[str], pydantic.Field(alias="weekType")] = None
    r"""Week type (e.g., REG, HOF)"""

    away_team_standings: Annotated[
        Optional[Standings], pydantic.Field(alias="awayTeamStandings")
    ] = None

    drive_chart: Annotated[Optional[DriveChart], pydantic.Field(alias="driveChart")] = (
        None
    )
    r"""Drive-by-drive data"""

    home_team_standings: Annotated[
        Optional[Standings], pydantic.Field(alias="homeTeamStandings")
    ] = None

    replays: Optional[List[Replay]] = None
    r"""Replay video links"""

    summary: Optional[Summary] = None
    r"""Game summary information"""

    tagged_videos: Annotated[
        Optional[List[TaggedVideos]], pydantic.Field(alias="taggedVideos")
    ] = None
