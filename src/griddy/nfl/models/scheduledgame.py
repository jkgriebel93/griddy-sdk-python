from __future__ import annotations
from .gamescore import GameScore, GameScoreTypedDict
from .gamesite import GameSite, GameSiteTypedDict
from .scheduleteam import ScheduleTeam, ScheduleTeamTypedDict
from .seasontypeenum import SeasonTypeEnum
from datetime import date, datetime
from ..types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ScheduledGameTypedDict(TypedDict):
    game_date: NotRequired[Nullable[date]]
    r"""Game date (YYYY-MM-DD format)"""
    game_id: NotRequired[int]
    r"""Game identifier (format is YYYYMMDDNN)"""
    game_key: NotRequired[int]
    r"""Unique game key"""
    game_time: NotRequired[Nullable[datetime]]
    r"""Game time in UTC"""
    game_time_eastern: NotRequired[Nullable[str]]
    r"""Game time in Eastern timezone (HH:MM:SS)"""
    game_type: NotRequired[SeasonTypeEnum]
    r"""Type of NFL season"""
    home_display_name: NotRequired[str]
    r"""Home team display name"""
    home_nickname: NotRequired[str]
    r"""Home team nickname"""
    home_team: NotRequired[ScheduleTeamTypedDict]
    home_team_abbr: NotRequired[str]
    r"""Home team abbreviation"""
    home_team_id: NotRequired[str]
    r"""Home team identifier"""
    iso_time: NotRequired[Nullable[int]]
    r"""Unix timestamp in milliseconds"""
    network_channel: NotRequired[Nullable[str]]
    r"""Broadcast network"""
    ngs_game: NotRequired[bool]
    r"""Whether Next Gen Stats are available"""
    released_to_clubs: NotRequired[bool]
    r"""Whether game info is released to clubs"""
    score: NotRequired[GameScoreTypedDict]
    season: NotRequired[int]
    r"""Season year"""
    season_type: NotRequired[SeasonTypeEnum]
    r"""Type of NFL season"""
    site: NotRequired[GameSiteTypedDict]
    smart_id: NotRequired[str]
    r"""Smart identifier for the game"""
    validated: NotRequired[bool]
    r"""Whether game info is validated"""
    visitor_display_name: NotRequired[str]
    r"""Visitor team display name"""
    visitor_nickname: NotRequired[str]
    r"""Visitor team nickname"""
    visitor_team: NotRequired[ScheduleTeamTypedDict]
    visitor_team_abbr: NotRequired[str]
    r"""Visitor team abbreviation"""
    visitor_team_id: NotRequired[str]
    r"""Visitor team identifier"""
    week: NotRequired[int]
    r"""Week number"""
    week_name_abbr: NotRequired[str]
    r"""Week name abbreviation"""


class ScheduledGame(BaseModel):
    game_date: Annotated[OptionalNullable[date], pydantic.Field(alias="gameDate")] = (
        UNSET
    )
    r"""Game date (YYYY-MM-DD format)"""

    game_id: Annotated[Optional[int], pydantic.Field(alias="gameId")] = None
    r"""Game identifier (format is YYYYMMDDNN)"""

    game_key: Annotated[Optional[int], pydantic.Field(alias="gameKey")] = None
    r"""Unique game key"""

    game_time: Annotated[
        OptionalNullable[datetime], pydantic.Field(alias="gameTime")
    ] = UNSET
    r"""Game time in UTC"""

    game_time_eastern: Annotated[
        OptionalNullable[str], pydantic.Field(alias="gameTimeEastern")
    ] = UNSET
    r"""Game time in Eastern timezone (HH:MM:SS)"""

    game_type: Annotated[Optional[SeasonTypeEnum], pydantic.Field(alias="gameType")] = (
        None
    )
    r"""Type of NFL season"""

    home_display_name: Annotated[
        Optional[str], pydantic.Field(alias="homeDisplayName")
    ] = None
    r"""Home team display name"""

    home_nickname: Annotated[Optional[str], pydantic.Field(alias="homeNickname")] = None
    r"""Home team nickname"""

    home_team: Annotated[Optional[ScheduleTeam], pydantic.Field(alias="homeTeam")] = (
        None
    )

    home_team_abbr: Annotated[Optional[str], pydantic.Field(alias="homeTeamAbbr")] = (
        None
    )
    r"""Home team abbreviation"""

    home_team_id: Annotated[Optional[str], pydantic.Field(alias="homeTeamId")] = None
    r"""Home team identifier"""

    iso_time: Annotated[OptionalNullable[int], pydantic.Field(alias="isoTime")] = UNSET
    r"""Unix timestamp in milliseconds"""

    network_channel: Annotated[
        OptionalNullable[str], pydantic.Field(alias="networkChannel")
    ] = UNSET
    r"""Broadcast network"""

    ngs_game: Annotated[Optional[bool], pydantic.Field(alias="ngsGame")] = None
    r"""Whether Next Gen Stats are available"""

    released_to_clubs: Annotated[
        Optional[bool], pydantic.Field(alias="releasedToClubs")
    ] = None
    r"""Whether game info is released to clubs"""

    score: Optional[GameScore] = None

    season: Optional[int] = None
    r"""Season year"""

    season_type: Annotated[
        Optional[SeasonTypeEnum], pydantic.Field(alias="seasonType")
    ] = None
    r"""Type of NFL season"""

    site: Optional[GameSite] = None

    smart_id: Annotated[Optional[str], pydantic.Field(alias="smartId")] = None
    r"""Smart identifier for the game"""

    validated: Optional[bool] = None
    r"""Whether game info is validated"""

    visitor_display_name: Annotated[
        Optional[str], pydantic.Field(alias="visitorDisplayName")
    ] = None
    r"""Visitor team display name"""

    visitor_nickname: Annotated[
        Optional[str], pydantic.Field(alias="visitorNickname")
    ] = None
    r"""Visitor team nickname"""

    visitor_team: Annotated[
        Optional[ScheduleTeam], pydantic.Field(alias="visitorTeam")
    ] = None

    visitor_team_abbr: Annotated[
        Optional[str], pydantic.Field(alias="visitorTeamAbbr")
    ] = None
    r"""Visitor team abbreviation"""

    visitor_team_id: Annotated[Optional[str], pydantic.Field(alias="visitorTeamId")] = (
        None
    )
    r"""Visitor team identifier"""

    week: Optional[int] = None
    r"""Week number"""

    week_name_abbr: Annotated[Optional[str], pydantic.Field(alias="weekNameAbbr")] = (
        None
    )
    r"""Week name abbreviation"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "gameDate",
            "gameId",
            "gameKey",
            "gameTime",
            "gameTimeEastern",
            "gameType",
            "homeDisplayName",
            "homeNickname",
            "homeTeam",
            "homeTeamAbbr",
            "homeTeamId",
            "isoTime",
            "networkChannel",
            "ngsGame",
            "releasedToClubs",
            "score",
            "season",
            "seasonType",
            "site",
            "smartId",
            "validated",
            "visitorDisplayName",
            "visitorNickname",
            "visitorTeam",
            "visitorTeamAbbr",
            "visitorTeamId",
            "week",
            "weekNameAbbr",
        ]
        nullable_fields = [
            "gameDate",
            "gameTime",
            "gameTimeEastern",
            "isoTime",
            "networkChannel",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
