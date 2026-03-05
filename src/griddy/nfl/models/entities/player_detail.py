from datetime import date
from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from ...types import UNSET, BaseModel, OptionalNullable
from .award import Award
from .career_stats import CareerStats
from .contract_info import ContractInfo
from .season_stats import SeasonStats


class PlayerDetail(BaseModel):
    birth_date: Annotated[Optional[date], pydantic.Field(alias="birthDate")] = None
    r"""Player's birth date"""

    college_conference: Annotated[
        Optional[str], pydantic.Field(alias="collegeConference")
    ] = None
    r"""Player's college conference"""

    college_name: Annotated[Optional[str], pydantic.Field(alias="collegeName")] = None
    r"""Player's college"""

    current_team_id: Annotated[Optional[str], pydantic.Field(alias="currentTeamId")] = (
        None
    )
    r"""Current team identifier"""

    display_name: Annotated[Optional[str], pydantic.Field(alias="displayName")] = None
    r"""Player's display name"""

    draft_club: Annotated[OptionalNullable[str], pydantic.Field(alias="draftClub")] = (
        UNSET
    )
    r"""Team that drafted the player"""

    draft_number: Annotated[
        OptionalNullable[int], pydantic.Field(alias="draftNumber")
    ] = UNSET
    r"""Overall draft pick number"""

    draftround: OptionalNullable[int] = UNSET
    r"""Draft round"""

    entry_year: Annotated[Optional[int], pydantic.Field(alias="entryYear")] = None
    r"""Year player entered the league"""

    esb_id: Annotated[Optional[str], pydantic.Field(alias="esbId")] = None
    r"""ESB identifier"""

    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None
    r"""Player's first name"""

    football_name: Annotated[Optional[str], pydantic.Field(alias="footballName")] = None
    r"""Player's football name (nickname)"""

    gsis_id: Annotated[Optional[str], pydantic.Field(alias="gsisId")] = None
    r"""GSIS identifier"""

    gsis_it_id: Annotated[Optional[int], pydantic.Field(alias="gsisItId")] = None
    r"""GSIS IT identifier"""

    headshot: Optional[str] = None
    r"""URL to player headshot image"""

    height: Optional[str] = None
    r"""Player height (format is feet-inches)"""

    jersey_number: Annotated[Optional[int], pydantic.Field(alias="jerseyNumber")] = None
    r"""Player's jersey number"""

    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None
    r"""Player's last name"""

    nfl_id: Annotated[Optional[int], pydantic.Field(alias="nflId")] = None
    r"""NFL player identifier"""

    ngs_position: Annotated[
        OptionalNullable[str], pydantic.Field(alias="ngsPosition")
    ] = UNSET
    r"""Next Gen Stats position"""

    ngs_position_group: Annotated[
        OptionalNullable[str], pydantic.Field(alias="ngsPositionGroup")
    ] = UNSET
    r"""Next Gen Stats position group"""

    position: Optional[str] = None
    r"""Player's position"""

    position_group: Annotated[Optional[str], pydantic.Field(alias="positionGroup")] = (
        None
    )
    r"""Player's position group"""

    rookie_year: Annotated[Optional[int], pydantic.Field(alias="rookieYear")] = None
    r"""Player's rookie year"""

    season: Optional[int] = None
    r"""Current season"""

    short_name: Annotated[Optional[str], pydantic.Field(alias="shortName")] = None
    r"""Shortened player name"""

    smart_id: Annotated[Optional[str], pydantic.Field(alias="smartId")] = None
    r"""Smart identifier for the player"""

    status: Optional[str] = None
    r"""Player status code"""

    status_description_abbr: Annotated[
        Optional[str], pydantic.Field(alias="statusDescriptionAbbr")
    ] = None
    r"""Abbreviated status description"""

    status_short_description: Annotated[
        Optional[str], pydantic.Field(alias="statusShortDescription")
    ] = None
    r"""Short status description"""

    team_abbr: Annotated[Optional[str], pydantic.Field(alias="teamAbbr")] = None
    r"""Current team abbreviation"""

    uniform_number: Annotated[Optional[str], pydantic.Field(alias="uniformNumber")] = (
        None
    )
    r"""Player's uniform number (formatted)"""

    weight: Optional[int] = None
    r"""Player weight in pounds"""

    years_of_experience: Annotated[
        Optional[int], pydantic.Field(alias="yearsOfExperience")
    ] = None
    r"""Years of NFL experience"""

    awards: Optional[List[Award]] = None

    biography: Optional[str] = None
    r"""Player biography"""

    career_stats: Annotated[
        Optional[CareerStats], pydantic.Field(alias="careerStats")
    ] = None

    contract_info: Annotated[
        Optional[ContractInfo], pydantic.Field(alias="contractInfo")
    ] = None

    current_season_stats: Annotated[
        Optional[SeasonStats], pydantic.Field(alias="currentSeasonStats")
    ] = None
