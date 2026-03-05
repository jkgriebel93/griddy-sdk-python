from __future__ import annotations

from datetime import date, datetime
from typing import List, Literal, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum

from ...types import UNSET, BaseModel, Nullable, OptionalNullable

InsightPosition = Literal[
    "QB",
    "RB",
    "WR",
    "TE",
    "OL",
    "DL",
    "LB",
    "DB",
    "K",
    "P",
]
r"""Player position"""


SecondTeamType = Literal[
    "offense",
    "defense",
]
r"""Context of the second team (typically \"defense\" for opponent)"""


class Insight(BaseModel):
    created_at: Annotated[datetime, pydantic.Field(alias="createdAt")]
    r"""Content creation timestamp"""

    created_by: Annotated[str, pydantic.Field(alias="createdBy")]
    r"""Content creator identifier"""

    date_: Annotated[date, pydantic.Field(alias="date")]
    r"""Content publication date"""

    id: str
    r"""Unique content identifier"""

    nfl_id: Annotated[Optional[int], pydantic.Field(alias="nflId")] = None
    r"""NFL player identifier"""

    player_name: Annotated[Optional[str], pydantic.Field(alias="playerName")] = None
    r"""Player's full name"""

    position: Optional[InsightPosition] = None
    r"""Player position"""

    season: int
    r"""Season year"""

    season_type: Annotated[SeasonTypeEnum, pydantic.Field(alias="seasonType")]
    r"""Type of NFL season"""

    tags: List[str]
    r"""Content classification tags"""

    team_abbr: Annotated[str, pydantic.Field(alias="teamAbbr")]
    r"""Player's team abbreviation"""

    team_id: Annotated[str, pydantic.Field(alias="teamId")]
    r"""Player's team identifier"""

    title: str
    r"""Main insight headline or title"""

    updated_at: Annotated[datetime, pydantic.Field(alias="updatedAt")]
    r"""Last update timestamp"""

    updated_by: Annotated[str, pydantic.Field(alias="updatedBy")]
    r"""Last editor identifier"""

    week: int
    r"""Week number (if applicable)"""

    esb_id: Annotated[Optional[str], pydantic.Field(alias="esbId")] = None
    r"""ESB player identifier"""

    evergreen: Optional[bool] = False
    r"""Whether content is evergreen (timeless) or time-sensitive"""

    game_id: Annotated[OptionalNullable[int], pydantic.Field(alias="gameId")] = UNSET
    r"""Game identifier (10-digit format YYYYMMDDNN)"""

    gsis_id: Annotated[Optional[str], pydantic.Field(alias="gsisId")] = None
    r"""GSIS player identifier"""

    headshot: Optional[str] = None
    r"""URL to player headshot image (contains formatInstructions placeholder)"""

    image_url: Annotated[OptionalNullable[str], pydantic.Field(alias="imageUrl")] = (
        UNSET
    )
    r"""Associated image or chart URL (optional)"""

    jersey_number: Annotated[Optional[int], pydantic.Field(alias="jerseyNumber")] = None
    r"""Player's jersey number"""

    second_team_abbr: Annotated[
        OptionalNullable[str], pydantic.Field(alias="secondTeamAbbr")
    ] = UNSET
    r"""Opponent or related team abbreviation"""

    second_team_id: Annotated[
        OptionalNullable[str], pydantic.Field(alias="secondTeamId")
    ] = UNSET
    r"""Opponent or related team identifier"""

    second_team_type: Annotated[
        OptionalNullable[SecondTeamType], pydantic.Field(alias="secondTeamType")
    ] = UNSET
    r"""Context of the second team (typically \"defense\" for opponent)"""

    smart_id: Annotated[Optional[str], pydantic.Field(alias="smartId")] = None
    r"""Smart player identifier"""

    sub_note1: Annotated[Optional[str], pydantic.Field(alias="subNote1")] = None
    r"""Detailed insight content and analysis"""
