from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ...types import BaseModel


class PlayPlayerTypedDict(TypedDict):
    first_name: str
    gsis_id: str
    r"""GSIS player ID"""
    last_name: str
    nfl_id: int
    r"""NFL player ID"""
    player_name: str
    r"""Full player name"""
    position: str
    r"""Player position"""
    position_group: str
    r"""Position group"""
    team_id: str
    r"""Team ID"""
    uniform_number: NotRequired[str]
    r"""Jersey number"""


class PlayPlayer(BaseModel):
    first_name: Annotated[str, pydantic.Field(alias="firstName")]

    gsis_id: Annotated[str, pydantic.Field(alias="gsisId")]
    r"""GSIS player ID"""

    last_name: Annotated[str, pydantic.Field(alias="lastName")]

    nfl_id: Annotated[int, pydantic.Field(alias="nflId")]
    r"""NFL player ID"""

    player_name: Annotated[str, pydantic.Field(alias="playerName")]
    r"""Full player name"""

    position: str
    r"""Player position"""

    position_group: Annotated[str, pydantic.Field(alias="positionGroup")]
    r"""Position group"""

    team_id: Annotated[str, pydantic.Field(alias="teamId")]
    r"""Team ID"""

    uniform_number: Annotated[Optional[str], pydantic.Field(alias="uniformNumber")] = (
        None
    )
    r"""Jersey number"""
