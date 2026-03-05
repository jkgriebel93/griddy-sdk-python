from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.enums.conference_enum import ConferenceEnum
from griddy.nfl.models.enums.team_type_enum import TeamTypeEnum

from ...types import UNSET, BaseModel, OptionalNullable
from .conference import Conference
from .division import Division


class TeamInfo(BaseModel):
    r"""Basic team information included in roster responses"""

    abbr: Optional[str] = None

    city_state: Annotated[Optional[str], pydantic.Field(alias="cityState")] = None

    conference: Optional[Conference] = None

    conference_abbr: Annotated[
        Optional[ConferenceEnum], pydantic.Field(alias="conferenceAbbr")
    ] = None
    r"""NFL conference"""

    division: Optional[Division] = None

    full_name: Annotated[Optional[str], pydantic.Field(alias="fullName")] = None

    logo: Optional[str] = None

    nick: Optional[str] = None

    season: Optional[int] = None

    smart_id: Annotated[Optional[str], pydantic.Field(alias="smartId")] = None

    stadium_name: Annotated[Optional[str], pydantic.Field(alias="stadiumName")] = None

    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None

    team_site_ticket_url: Annotated[
        OptionalNullable[str], pydantic.Field(alias="teamSiteTicketUrl")
    ] = UNSET

    team_site_url: Annotated[
        OptionalNullable[str], pydantic.Field(alias="teamSiteUrl")
    ] = UNSET

    team_type: Annotated[Optional[TeamTypeEnum], pydantic.Field(alias="teamType")] = (
        None
    )
    r"""Team type classification"""

    ticket_phone_number: Annotated[
        OptionalNullable[str], pydantic.Field(alias="ticketPhoneNumber")
    ] = UNSET

    year_found: Annotated[Optional[int], pydantic.Field(alias="yearFound")] = None
