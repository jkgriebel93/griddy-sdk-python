
from __future__ import annotations
from .boxscorescore import BoxscoreScore, BoxscoreScoreTypedDict
from .boxscoresite import BoxscoreSite, BoxscoreSiteTypedDict
from .boxscoreteam import BoxscoreTeam, BoxscoreTeamTypedDict
from .seasontypeenum import SeasonTypeEnum
from datetime import datetime
from ..types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class BoxscoreScheduleTypedDict(TypedDict):
    game_date: NotRequired[str]
    game_id: NotRequired[str]
    game_key: NotRequired[int]
    game_time: NotRequired[datetime]
    game_time_eastern: NotRequired[str]
    game_type: NotRequired[SeasonTypeEnum]
    r"""Type of NFL season"""
    home_display_name: NotRequired[str]
    home_nickname: NotRequired[str]
    home_team: NotRequired[BoxscoreTeamTypedDict]
    home_team_abbr: NotRequired[str]
    home_team_id: NotRequired[str]
    iso_time: NotRequired[int]
    r"""Unix timestamp in milliseconds"""
    network_channel: NotRequired[str]
    ngs_game: NotRequired[bool]
    r"""Whether Next Gen Stats are available"""
    score: NotRequired[BoxscoreScoreTypedDict]
    season: NotRequired[int]
    season_type: NotRequired[SeasonTypeEnum]
    r"""Type of NFL season"""
    site: NotRequired[BoxscoreSiteTypedDict]
    smart_id: NotRequired[str]
    visitor_display_name: NotRequired[str]
    visitor_nickname: NotRequired[str]
    visitor_team: NotRequired[BoxscoreTeamTypedDict]
    visitor_team_abbr: NotRequired[str]
    visitor_team_id: NotRequired[str]
    week: NotRequired[int]
    week_name_abbr: NotRequired[str]


class BoxscoreSchedule(BaseModel):
    game_date: Annotated[Optional[str], pydantic.Field(alias="gameDate")] = None

    game_id: Annotated[Optional[str], pydantic.Field(alias="gameId")] = None

    game_key: Annotated[Optional[int], pydantic.Field(alias="gameKey")] = None

    game_time: Annotated[Optional[datetime], pydantic.Field(alias="gameTime")] = None

    game_time_eastern: Annotated[
        Optional[str], pydantic.Field(alias="gameTimeEastern")
    ] = None

    game_type: Annotated[Optional[SeasonTypeEnum], pydantic.Field(alias="gameType")] = (
        None
    )
    r"""Type of NFL season"""

    home_display_name: Annotated[
        Optional[str], pydantic.Field(alias="homeDisplayName")
    ] = None

    home_nickname: Annotated[Optional[str], pydantic.Field(alias="homeNickname")] = None

    home_team: Annotated[Optional[BoxscoreTeam], pydantic.Field(alias="homeTeam")] = (
        None
    )

    home_team_abbr: Annotated[Optional[str], pydantic.Field(alias="homeTeamAbbr")] = (
        None
    )

    home_team_id: Annotated[Optional[str], pydantic.Field(alias="homeTeamId")] = None

    iso_time: Annotated[Optional[int], pydantic.Field(alias="isoTime")] = None
    r"""Unix timestamp in milliseconds"""

    network_channel: Annotated[
        Optional[str], pydantic.Field(alias="networkChannel")
    ] = None

    ngs_game: Annotated[Optional[bool], pydantic.Field(alias="ngsGame")] = None
    r"""Whether Next Gen Stats are available"""

    score: Optional[BoxscoreScore] = None

    season: Optional[int] = None

    season_type: Annotated[
        Optional[SeasonTypeEnum], pydantic.Field(alias="seasonType")
    ] = None
    r"""Type of NFL season"""

    site: Optional[BoxscoreSite] = None

    smart_id: Annotated[Optional[str], pydantic.Field(alias="smartId")] = None

    visitor_display_name: Annotated[
        Optional[str], pydantic.Field(alias="visitorDisplayName")
    ] = None

    visitor_nickname: Annotated[
        Optional[str], pydantic.Field(alias="visitorNickname")
    ] = None

    visitor_team: Annotated[
        Optional[BoxscoreTeam], pydantic.Field(alias="visitorTeam")
    ] = None

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
