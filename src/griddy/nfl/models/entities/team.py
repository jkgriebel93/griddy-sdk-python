from __future__ import annotations

from typing import List, Literal, Optional

import pydantic
from typing_extensions import Annotated

from ...types import UNSET, BaseModel, OptionalNullable
from .social_media import SocialMedia
from .team_venue import TeamVenue

TeamConferenceAbbr = Literal[
    "AFC",
    "NFC",
]
r"""Conference abbreviation"""


TeamTeamType = Literal[
    "TEAM",
    "PRO",
]
r"""Type of team (regular or Pro Bowl)"""


class Team(BaseModel):
    abbreviation: Optional[str] = None
    r"""Three-letter team abbreviation"""

    conference_abbr: Annotated[
        Optional[TeamConferenceAbbr], pydantic.Field(alias="conferenceAbbr")
    ] = None
    r"""Conference abbreviation"""

    conference_full_name: Annotated[
        Optional[str], pydantic.Field(alias="conferenceFullName")
    ] = None
    r"""Full conference name"""

    current_logo: Annotated[Optional[str], pydantic.Field(alias="currentLogo")] = None
    r"""URL to team logo (may contain {formatInstructions} placeholder)"""

    division_full_name: Annotated[
        Optional[str], pydantic.Field(alias="divisionFullName")
    ] = None
    r"""Full division name"""

    full_name: Annotated[Optional[str], pydantic.Field(alias="fullName")] = None
    r"""Full team name"""

    id: Optional[str] = None
    r"""Unique team identifier"""

    league: Optional[str] = None
    r"""League name"""

    location: Optional[str] = None
    r"""Team location/city"""

    nfl_shop_url: Annotated[
        OptionalNullable[str], pydantic.Field(alias="nflShopUrl")
    ] = UNSET
    r"""URL to team's NFL shop"""

    nick_name: Annotated[Optional[str], pydantic.Field(alias="nickName")] = None
    r"""Team nickname"""

    official_website_url: Annotated[
        OptionalNullable[str], pydantic.Field(alias="officialWebsiteUrl")
    ] = UNSET
    r"""Team's official website"""

    owners: OptionalNullable[str] = UNSET
    r"""Team ownership information"""

    primary_color: Annotated[Optional[str], pydantic.Field(alias="primaryColor")] = None
    r"""Primary team color (hex)"""

    season: Optional[str] = None
    r"""Current season"""

    secondary_color: Annotated[
        Optional[str], pydantic.Field(alias="secondaryColor")
    ] = None
    r"""Secondary team color (hex)"""

    socials: Optional[List[SocialMedia]] = None

    team_type: Annotated[Optional[TeamTeamType], pydantic.Field(alias="teamType")] = (
        None
    )
    r"""Type of team (regular or Pro Bowl)"""

    venues: Optional[List[TeamVenue]] = None

    year_established: Annotated[
        Optional[int], pydantic.Field(alias="yearEstablished")
    ] = None
    r"""Year team was established"""
