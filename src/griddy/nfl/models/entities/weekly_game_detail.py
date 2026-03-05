from __future__ import annotations

from datetime import date, datetime
from typing import List, Literal, Optional

import pydantic
from pydantic import model_serializer
from typing_extensions import Annotated

from griddy.nfl.models.enums.meridiem_enum import MeridiemEnum
from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum

from ...types import UNSET, UNSET_SENTINEL, BaseModel, Nullable, OptionalNullable
from .broadcast_info import BroadcastInfo
from .external_id import ExternalID
from .standings import Standings
from .team import Team
from .ticket_vendor import TicketVendor
from .venue import Venue

WeeklyGameDetailCategory = Literal["MNF", "SNF", "TNF", "OTHER"]
r"""Prime time game designation"""


class WeeklyGameDetailExtension(BaseModel):
    pass


WeeklyGameDetailStatus = Literal[
    "SCHEDULED", "IN_PROGRESS", "FINAL", "POSTPONED", "CANCELLED", "FINAL_OVERTIME"
]
r"""Game status"""


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


class DriveChart(BaseModel):
    r"""Drive-by-drive data"""

    game_id: Annotated[Optional[str], pydantic.Field(alias="gameId")] = None
    offset: Optional[int] = None
    drives: Optional[List[Drive]] = None
    plays: Optional[List[DriveChartPlay]] = None


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


class Summary(BaseModel):
    r"""Game summary information"""


class TaggedVideos(BaseModel):
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
