from __future__ import annotations

from datetime import date, datetime
from typing import List, Literal, Optional

import pydantic
from pydantic import model_serializer
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import UNSET, UNSET_SENTINEL, BaseModel, Nullable, OptionalNullable
from .broadcast_info import BroadcastInfo, BroadcastInfoTypedDict
from .external_id import ExternalID, ExternalIDTypedDict
from .meridiem_enum import MeridiemEnum
from .season_type_enum import SeasonTypeEnum
from .team import Team, TeamTypedDict
from .ticket_vendor import TicketVendor, TicketVendorTypedDict
from .venue import Venue, VenueTypedDict

ProGameCategory = Literal[
    "MNF",
    "SNF",
    "TNF",
]
r"""Prime time game designation"""


class ProGameExtensionTypedDict(TypedDict):
    pass


class ProGameExtension(BaseModel):
    pass


ProGameStatus = Literal[
    "SCHEDULED",
    "IN_PROGRESS",
    "FINAL",
    "POSTPONED",
    "CANCELLED",
]
r"""Game status"""


class ProGameTypedDict(TypedDict):
    away_team: NotRequired[TeamTypedDict]
    broadcast_info: NotRequired[BroadcastInfoTypedDict]
    category: NotRequired[Nullable[ProGameCategory]]
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
    extensions: NotRequired[List[ProGameExtensionTypedDict]]
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
    phase: NotRequired[str]
    r"""Game phase"""
    season: NotRequired[int]
    r"""Season year"""
    season_type: NotRequired[SeasonTypeEnum]
    r"""Type of NFL season"""
    status: NotRequired[ProGameStatus]
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


class ProGame(BaseModel):
    away_team: Annotated[Optional[Team], pydantic.Field(alias="awayTeam")] = None

    broadcast_info: Annotated[
        Optional[BroadcastInfo], pydantic.Field(alias="broadcastInfo")
    ] = None

    category: OptionalNullable[ProGameCategory] = UNSET

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

    extensions: Optional[List[ProGameExtension]] = None
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

    phase: Optional[str] = None
    r"""Game phase"""

    season: Optional[int] = None
    r"""Season year"""

    season_type: Annotated[
        Optional[SeasonTypeEnum], pydantic.Field(alias="seasonType")
    ] = None
    r"""Type of NFL season"""

    status: Optional[ProGameStatus] = None
    r"""Game status"""

    ticket_url: Annotated[OptionalNullable[str], pydantic.Field(alias="ticketUrl")] = (
        UNSET
    )
    r"""Primary ticket purchase URL"""

    ticket_vendors: Annotated[
        Optional[List[TicketVendor]], pydantic.Field(alias="ticketVendors")
    ] = None

    time: Optional[datetime] = None
    r"""Game time in UTC"""

    venue: Optional[Venue] = None

    version: Optional[int] = None
    r"""Data version number"""

    week: Optional[int] = None
    r"""Week number"""

    week_type: Annotated[Optional[str], pydantic.Field(alias="weekType")] = None
    r"""Week type (e.g., REG, HOF)"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "awayTeam",
            "broadcastInfo",
            "category",
            "date",
            "dateAmPm",
            "dateDay",
            "dateDayMonth",
            "dateDayShort",
            "dateTime",
            "dateTimeAmPm",
            "extensions",
            "externalIds",
            "gameType",
            "homeTeam",
            "id",
            "international",
            "neutralSite",
            "phase",
            "season",
            "seasonType",
            "status",
            "ticketUrl",
            "ticketVendors",
            "time",
            "venue",
            "version",
            "week",
            "weekType",
        ]
        nullable_fields = ["category", "ticketUrl"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(n)  # FIX: Use field name, not alias
            serialized.pop(n, None)

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
