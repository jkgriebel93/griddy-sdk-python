from __future__ import annotations
from ..types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class LinkParamsTypedDict(TypedDict):
    r"""Parameters for constructing film room link"""

    dropback: NotRequired[int]
    r"""Dropback indicator (1 for yes)"""
    nfl_id: NotRequired[str]
    r"""NFL player identifier"""
    passer_id: NotRequired[str]
    r"""Passer ID for QB film"""
    rusher_id: NotRequired[str]
    r"""Rusher ID for RB film"""
    season: NotRequired[str]
    r"""Season year"""
    target_id: NotRequired[str]
    r"""Target ID for receiver film"""
    week_slug: NotRequired[str]
    r"""Week identifier"""


class LinkParams(BaseModel):
    r"""Parameters for constructing film room link"""

    dropback: Optional[int] = None
    r"""Dropback indicator (1 for yes)"""

    nfl_id: Annotated[Optional[str], pydantic.Field(alias="nflId")] = None
    r"""NFL player identifier"""

    passer_id: Annotated[Optional[str], pydantic.Field(alias="passerId")] = None
    r"""Passer ID for QB film"""

    rusher_id: Annotated[Optional[str], pydantic.Field(alias="rusherId")] = None
    r"""Rusher ID for RB film"""

    season: Optional[str] = None
    r"""Season year"""

    target_id: Annotated[Optional[str], pydantic.Field(alias="targetId")] = None
    r"""Target ID for receiver film"""

    week_slug: Annotated[Optional[str], pydantic.Field(alias="weekSlug")] = None
    r"""Week identifier"""


class FilmCardTypedDict(TypedDict):
    link_params: LinkParamsTypedDict
    r"""Parameters for constructing film room link"""
    team_id: str
    r"""Team identifier"""
    title: str
    r"""Title of the film content"""


class FilmCard(BaseModel):
    link_params: Annotated[LinkParams, pydantic.Field(alias="linkParams")]
    r"""Parameters for constructing film room link"""

    team_id: Annotated[str, pydantic.Field(alias="teamId")]
    r"""Team identifier"""

    title: str
    r"""Title of the film content"""
