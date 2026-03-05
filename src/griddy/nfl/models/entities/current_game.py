from __future__ import annotations

from datetime import date, datetime
from typing import List, Literal, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.enums.game_status_enum import GameStatusEnum
from griddy.nfl.models.enums.meridiem_enum import MeridiemEnum
from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum

from ...types import UNSET, BaseModel, Nullable, OptionalNullable
from .broadcast_info import BroadcastInfo
from .external_id import ExternalID
from .game_team import GameTeam
from .ticket_vendor import TicketVendor
from .venue import Venue

CurrentGameCategory = Literal["MNF", "SNF", "TNF", "OTHER"]
r"""Prime time game designation"""


class CurrentGameExtension(BaseModel):
    pass


class CurrentGame(BaseModel):
    away_team: Annotated[Optional[GameTeam], pydantic.Field(alias="awayTeam")] = None

    broadcast_info: Annotated[
        Optional[BroadcastInfo], pydantic.Field(alias="broadcastInfo")
    ] = None

    category: OptionalNullable[CurrentGameCategory] = UNSET

    date_: Annotated[Optional[date], pydantic.Field(alias="date")] = None
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

    extensions: Optional[List[CurrentGameExtension]] = None

    external_ids: Annotated[
        Optional[List[ExternalID]], pydantic.Field(alias="externalIds")
    ] = None

    game_type: Annotated[Optional[str], pydantic.Field(alias="gameType")] = None
    r"""Type of game"""

    home_team: Annotated[Optional[GameTeam], pydantic.Field(alias="homeTeam")] = None

    id: Optional[str] = None
    r"""Unique game identifier"""

    international: Optional[bool] = None
    r"""Whether game is played internationally"""

    neutral_site: Annotated[Optional[bool], pydantic.Field(alias="neutralSite")] = None
    r"""Whether game is at neutral venue"""

    phase: Optional[str | int] = None
    r"""Game phase (e.g., PREGAME, FINAL)"""

    season: Optional[int] = None

    season_type: Annotated[
        Optional[SeasonTypeEnum], pydantic.Field(alias="seasonType")
    ] = None
    r"""Type of NFL season"""

    status: Optional[GameStatusEnum] = None
    r"""Game status"""

    ticket_url: Annotated[OptionalNullable[str], pydantic.Field(alias="ticketUrl")] = (
        UNSET
    )

    ticket_vendors: Annotated[
        Optional[List[TicketVendor]], pydantic.Field(alias="ticketVendors")
    ] = None

    time: Optional[datetime] = None
    r"""Game time in UTC"""

    venue: Optional[Venue] = None

    version: Optional[int] = None

    week: Optional[int] = None

    week_type: Annotated[Optional[str], pydantic.Field(alias="weekType")] = None
