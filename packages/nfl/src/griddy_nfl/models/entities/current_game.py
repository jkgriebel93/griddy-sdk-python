from __future__ import annotations

from datetime import date, datetime
from typing import List, Literal, Optional

import pydantic
from pydantic import model_serializer
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.models.enums.game_status_enum import GameStatusEnum
from griddy_nfl.models.enums.meridiem_enum import MeridiemEnum
from griddy_nfl.models.enums.season_type_enum import SeasonTypeEnum

from ...types import UNSET, UNSET_SENTINEL, BaseModel, Nullable, OptionalNullable
from .broadcast_info import BroadcastInfo, BroadcastInfoTypedDict
from .external_id import ExternalID, ExternalIDTypedDict
from .game_team import GameTeam, GameTeamTypedDict
from .ticket_vendor import TicketVendor, TicketVendorTypedDict
from .venue import Venue, VenueTypedDict

CurrentGameCategory = Literal["MNF", "SNF", "TNF", "OTHER"]
r"""Prime time game designation"""


class CurrentGameExtensionTypedDict(TypedDict):
    pass


class CurrentGameExtension(BaseModel):
    pass


class CurrentGameTypedDict(TypedDict):
    away_team: NotRequired[GameTeamTypedDict]
    broadcast_info: NotRequired[BroadcastInfoTypedDict]
    category: NotRequired[Nullable[CurrentGameCategory]]
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
    extensions: NotRequired[List[CurrentGameExtensionTypedDict]]
    external_ids: NotRequired[List[ExternalIDTypedDict]]
    game_type: NotRequired[str]
    r"""Type of game"""
    home_team: NotRequired[GameTeamTypedDict]
    id: NotRequired[str]
    r"""Unique game identifier"""
    international: NotRequired[bool]
    r"""Whether game is played internationally"""
    neutral_site: NotRequired[bool]
    r"""Whether game is at neutral venue"""
    phase: NotRequired[str | int]
    r"""Game phase (e.g., PREGAME, FINAL)"""
    season: NotRequired[int]
    season_type: NotRequired[SeasonTypeEnum]
    r"""Type of NFL season"""
    status: NotRequired[GameStatusEnum]
    r"""Game status"""
    ticket_url: NotRequired[Nullable[str]]
    ticket_vendors: NotRequired[List[TicketVendorTypedDict]]
    time: NotRequired[datetime]
    r"""Game time in UTC"""
    venue: NotRequired[VenueTypedDict]
    version: NotRequired[int]
    week: NotRequired[int]
    week_type: NotRequired[str]


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
