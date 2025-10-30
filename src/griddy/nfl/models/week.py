
from __future__ import annotations
from .proteam import ProTeam, ProTeamTypedDict
from .seasontypeenum import SeasonTypeEnum
from datetime import date
from ..types import BaseModel
import pydantic
from typing import List, Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


WeekWeekType = Literal[
    "HOF",
    "PRE",
    "REG",
]
r"""Type of week"""


class WeekTypedDict(TypedDict):
    bye_teams: NotRequired[List[ProTeamTypedDict]]
    r"""Teams on bye this week (empty array if no bye teams)"""
    date_begin: NotRequired[date]
    r"""First day of the week"""
    date_end: NotRequired[date]
    r"""Last day of the week"""
    season: NotRequired[int]
    r"""Season year"""
    season_type: NotRequired[SeasonTypeEnum]
    r"""Type of NFL season"""
    season_type_week: NotRequired[str]
    r"""Combined season type and week identifier"""
    text: NotRequired[str]
    r"""Human-readable week description"""
    week: NotRequired[int]
    r"""Week number (0 for Hall of Fame game)"""
    week_slug: NotRequired[str]
    r"""Week identifier slug"""
    week_type: NotRequired[WeekWeekType]
    r"""Type of week"""


class Week(BaseModel):
    bye_teams: Annotated[Optional[List[ProTeam]], pydantic.Field(alias="byeTeams")] = (
        None
    )
    r"""Teams on bye this week (empty array if no bye teams)"""

    date_begin: Annotated[Optional[date], pydantic.Field(alias="dateBegin")] = None
    r"""First day of the week"""

    date_end: Annotated[Optional[date], pydantic.Field(alias="dateEnd")] = None
    r"""Last day of the week"""

    season: Optional[int] = None
    r"""Season year"""

    season_type: Annotated[
        Optional[SeasonTypeEnum], pydantic.Field(alias="seasonType")
    ] = None
    r"""Type of NFL season"""

    season_type_week: Annotated[
        Optional[str], pydantic.Field(alias="seasonTypeWeek")
    ] = None
    r"""Combined season type and week identifier"""

    text: Optional[str] = None
    r"""Human-readable week description"""

    week: Optional[int] = None
    r"""Week number (0 for Hall of Fame game)"""

    week_slug: Annotated[Optional[str], pydantic.Field(alias="weekSlug")] = None
    r"""Week identifier slug"""

    week_type: Annotated[Optional[WeekWeekType], pydantic.Field(alias="weekType")] = (
        None
    )
    r"""Type of week"""
