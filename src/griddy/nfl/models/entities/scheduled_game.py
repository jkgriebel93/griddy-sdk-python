from __future__ import annotations

from datetime import date, datetime
from typing import Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum

from ...types import UNSET, BaseModel, OptionalNullable
from .game_score import GameScore
from .game_site import GameSite
from .schedule_team import ScheduleTeam


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
