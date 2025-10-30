
from __future__ import annotations
from ..types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DivisionTypedDict(TypedDict):
    abbr: NotRequired[str]
    r"""Division abbreviation"""
    full_name: NotRequired[str]
    r"""Full division name"""
    id: NotRequired[str]
    r"""Division identifier"""


class Division(BaseModel):
    abbr: Optional[str] = None
    r"""Division abbreviation"""

    full_name: Annotated[Optional[str], pydantic.Field(alias="fullName")] = None
    r"""Full division name"""

    id: Optional[str] = None
    r"""Division identifier"""
