from __future__ import annotations

from typing import Literal, Optional

import pydantic
from pydantic import model_serializer
from typing_extensions import Annotated

from ...types import UNSET, UNSET_SENTINEL, BaseModel, Nullable, OptionalNullable
from .conference import Conference
from .division import Division

ProTeamConferenceAbbr = Literal[
    "AFC",
    "NFC",
]
r"""Conference abbreviation"""


ProTeamTeamType = Literal[
    "TEAM",
    "PRO",
]
r"""Type of team (regular or Pro Bowl)"""


class ProTeam(BaseModel):
    abbr: Optional[str] = None
    r"""Three-letter team abbreviation"""

    alt_color: Annotated[Optional[str], pydantic.Field(alias="altColor")] = None
    r"""Alternate team color in hex format"""

    city: Optional[str] = None
    r"""Team city/location"""

    city_state: Annotated[Optional[str], pydantic.Field(alias="cityState")] = None
    r"""Team city and state"""

    conference: Optional[Conference] = None

    conference_abbr: Annotated[
        Optional[ProTeamConferenceAbbr], pydantic.Field(alias="conferenceAbbr")
    ] = None
    r"""Conference abbreviation"""

    dark_color: Annotated[Optional[str], pydantic.Field(alias="darkColor")] = None
    r"""Dark team color in hex format"""

    division: Optional[Division] = None

    domain: Optional[str] = None
    r"""Team website domain prefix"""

    full_name: Annotated[Optional[str], pydantic.Field(alias="fullName")] = None
    r"""Full team name"""

    is_pro_bowl: Annotated[Optional[bool], pydantic.Field(alias="isProBowl")] = False
    r"""Whether this is a Pro Bowl team"""

    logo: Optional[str] = None
    r"""URL to team logo (may contain formatInstructions placeholder)"""

    name: Optional[str] = None
    r"""Team name"""

    nick: Optional[str] = None
    r"""Team nickname (short form)"""

    nickname: Optional[str] = None
    r"""Team nickname"""

    primary_color: Annotated[Optional[str], pydantic.Field(alias="primaryColor")] = None
    r"""Primary team color in hex format"""

    season: Optional[int] = None
    r"""Current season year"""

    secondary_color: Annotated[
        Optional[str], pydantic.Field(alias="secondaryColor")
    ] = None
    r"""Secondary team color in hex format"""

    slug: Optional[str] = None
    r"""URL-friendly team identifier"""

    smart_id: Annotated[Optional[str], pydantic.Field(alias="smartId")] = None
    r"""Unique smart identifier for the team"""

    stadium_name: Annotated[Optional[str], pydantic.Field(alias="stadiumName")] = None
    r"""Name of the team's home stadium"""

    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    r"""Team identifier (4-digit string)"""

    team_site_ticket_url: Annotated[
        OptionalNullable[str], pydantic.Field(alias="teamSiteTicketUrl")
    ] = UNSET
    r"""URL to team's ticket purchase page"""

    team_site_url: Annotated[
        OptionalNullable[str], pydantic.Field(alias="teamSiteUrl")
    ] = UNSET
    r"""Team's official website URL"""

    team_type: Annotated[
        Optional[ProTeamTeamType], pydantic.Field(alias="teamType")
    ] = None
    r"""Type of team (regular or Pro Bowl)"""

    tertiary_color: Annotated[Optional[str], pydantic.Field(alias="tertiaryColor")] = (
        None
    )
    r"""Tertiary team color in hex format"""

    ticket_phone_number: Annotated[
        OptionalNullable[str], pydantic.Field(alias="ticketPhoneNumber")
    ] = UNSET
    r"""Phone number for ticket purchases"""

    year_found: Annotated[Optional[int], pydantic.Field(alias="yearFound")] = None
    r"""Year the team was founded"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "abbr",
            "altColor",
            "city",
            "cityState",
            "conference",
            "conferenceAbbr",
            "darkColor",
            "division",
            "domain",
            "fullName",
            "isProBowl",
            "logo",
            "name",
            "nick",
            "nickname",
            "primaryColor",
            "season",
            "secondaryColor",
            "slug",
            "smartId",
            "stadiumName",
            "teamId",
            "teamSiteTicketUrl",
            "teamSiteUrl",
            "teamType",
            "tertiaryColor",
            "ticketPhoneNumber",
            "yearFound",
        ]
        nullable_fields = ["teamSiteTicketUrl", "teamSiteUrl", "ticketPhoneNumber"]
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
