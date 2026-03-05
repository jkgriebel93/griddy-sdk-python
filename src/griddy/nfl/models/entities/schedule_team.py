from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.enums.conference_enum import ConferenceEnum
from griddy.nfl.models.enums.team_type_enum import TeamTypeEnum

from ...types import BaseModel


class ScheduleTeam(BaseModel):
    abbr: Optional[str] = None

    city_state: Annotated[Optional[str], pydantic.Field(alias="cityState")] = None

    conference_abbr: Annotated[
        Optional[ConferenceEnum], pydantic.Field(alias="conferenceAbbr")
    ] = None
    r"""NFL conference"""

    division_abbr: Annotated[Optional[str], pydantic.Field(alias="divisionAbbr")] = None

    full_name: Annotated[Optional[str], pydantic.Field(alias="fullName")] = None

    logo: Optional[str] = None

    nick: Optional[str] = None

    smart_id: Annotated[Optional[str], pydantic.Field(alias="smartId")] = None

    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None

    team_type: Annotated[Optional[TeamTypeEnum], pydantic.Field(alias="teamType")] = (
        None
    )
    r"""Team type classification"""
