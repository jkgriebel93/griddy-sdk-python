from __future__ import annotations

from datetime import datetime
from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum

from ..types import BaseModel
from .game_score import GameScore, GameScoreTypedDict
from .team_info import TeamInfo, TeamInfoTypedDict
from .venue_info import VenueInfo, VenueInfoTypedDict


class GameScheduleTypedDict(TypedDict):
    game_date: NotRequired[str]
    r"""Game date MM/DD/YYYY"""
    game_id: NotRequired[int]
    game_key: NotRequired[int]
    game_time: NotRequired[datetime]
    game_time_eastern: NotRequired[str]
    r"""Eastern time"""
    game_type: NotRequired[SeasonTypeEnum]
    r"""Type of NFL season"""
    home_display_name: NotRequired[str]
    home_nickname: NotRequired[str]
    home_team: NotRequired[TeamInfoTypedDict]
    r"""Basic team information included in roster responses"""
    home_team_abbr: NotRequired[str]
    home_team_id: NotRequired[str]
    iso_time: NotRequired[int]
    r"""ISO timestamp in milliseconds"""
    network_channel: NotRequired[str]
    r"""Broadcast network"""
    ngs_game: NotRequired[bool]
    r"""Next Gen Stats available"""
    released_to_clubs: NotRequired[bool]
    score: NotRequired[GameScoreTypedDict]
    season: NotRequired[int]
    season_type: NotRequired[SeasonTypeEnum]
    r"""Type of NFL season"""
    site: NotRequired[VenueInfoTypedDict]
    smart_id: NotRequired[str]
    validated: NotRequired[bool]
    visitor_display_name: NotRequired[str]
    visitor_nickname: NotRequired[str]
    visitor_team: NotRequired[TeamInfoTypedDict]
    r"""Basic team information included in roster responses"""
    visitor_team_abbr: NotRequired[str]
    visitor_team_id: NotRequired[str]
    week: NotRequired[int]
    week_name_abbr: NotRequired[str]


class GameSchedule(BaseModel):
    game_date: Annotated[Optional[str], pydantic.Field(alias="gameDate")] = None
    r"""Game date MM/DD/YYYY"""

    game_id: Annotated[Optional[int], pydantic.Field(alias="gameId")] = None

    game_key: Annotated[Optional[int], pydantic.Field(alias="gameKey")] = None

    game_time: Annotated[Optional[datetime], pydantic.Field(alias="gameTime")] = None

    game_time_eastern: Annotated[
        Optional[str], pydantic.Field(alias="gameTimeEastern")
    ] = None
    r"""Eastern time"""

    game_type: Annotated[Optional[SeasonTypeEnum], pydantic.Field(alias="gameType")] = (
        None
    )
    r"""Type of NFL season"""

    home_display_name: Annotated[
        Optional[str], pydantic.Field(alias="homeDisplayName")
    ] = None

    home_nickname: Annotated[Optional[str], pydantic.Field(alias="homeNickname")] = None

    home_team: Annotated[Optional[TeamInfo], pydantic.Field(alias="homeTeam")] = None
    r"""Basic team information included in roster responses"""

    home_team_abbr: Annotated[Optional[str], pydantic.Field(alias="homeTeamAbbr")] = (
        None
    )

    home_team_id: Annotated[Optional[str], pydantic.Field(alias="homeTeamId")] = None

    iso_time: Annotated[Optional[int], pydantic.Field(alias="isoTime")] = None
    r"""ISO timestamp in milliseconds"""

    network_channel: Annotated[
        Optional[str], pydantic.Field(alias="networkChannel")
    ] = None
    r"""Broadcast network"""

    ngs_game: Annotated[Optional[bool], pydantic.Field(alias="ngsGame")] = None
    r"""Next Gen Stats available"""

    released_to_clubs: Annotated[
        Optional[bool], pydantic.Field(alias="releasedToClubs")
    ] = None

    score: Optional[GameScore] = None

    season: Optional[int] = None

    season_type: Annotated[
        Optional[SeasonTypeEnum], pydantic.Field(alias="seasonType")
    ] = None
    r"""Type of NFL season"""

    site: Optional[VenueInfo] = None

    smart_id: Annotated[Optional[str], pydantic.Field(alias="smartId")] = None

    validated: Optional[bool] = None

    visitor_display_name: Annotated[
        Optional[str], pydantic.Field(alias="visitorDisplayName")
    ] = None

    visitor_nickname: Annotated[
        Optional[str], pydantic.Field(alias="visitorNickname")
    ] = None

    visitor_team: Annotated[Optional[TeamInfo], pydantic.Field(alias="visitorTeam")] = (
        None
    )
    r"""Basic team information included in roster responses"""

    visitor_team_abbr: Annotated[
        Optional[str], pydantic.Field(alias="visitorTeamAbbr")
    ] = None

    visitor_team_id: Annotated[Optional[str], pydantic.Field(alias="visitorTeamId")] = (
        None
    )

    week: Optional[int] = None

    week_name_abbr: Annotated[Optional[str], pydantic.Field(alias="weekNameAbbr")] = (
        None
    )
