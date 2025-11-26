from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum

from ...types import BaseModel


class VideoTagTypedDict(TypedDict):
    r"""Video tag information"""

    game_id: NotRequired[str]
    r"""Game identifier (for game tags)"""
    person_id: NotRequired[str]
    r"""Person identifier (for player tags)"""
    season: NotRequired[str]
    r"""Season year (for game tags)"""
    season_type: NotRequired[SeasonTypeEnum]
    r"""Type of NFL season"""
    slug: NotRequired[str]
    r"""URL-friendly tag identifier"""
    team_id: NotRequired[str]
    r"""Team identifier (for team tags)"""
    title: NotRequired[str]
    r"""Tag title"""
    week: NotRequired[str]
    r"""Week number (for game tags)"""


class VideoTag(BaseModel):
    r"""Video tag information"""

    game_id: Annotated[Optional[str], pydantic.Field(alias="gameId")] = None
    r"""Game identifier (for game tags)"""

    person_id: Annotated[Optional[str], pydantic.Field(alias="personId")] = None
    r"""Person identifier (for player tags)"""

    season: Optional[str] = None
    r"""Season year (for game tags)"""

    season_type: Annotated[
        Optional[SeasonTypeEnum], pydantic.Field(alias="seasonType")
    ] = None
    r"""Type of NFL season"""

    slug: Optional[str] = None
    r"""URL-friendly tag identifier"""

    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    r"""Team identifier (for team tags)"""

    title: Optional[str] = None
    r"""Tag title"""

    week: Optional[str] = None
    r"""Week number (for game tags)"""
