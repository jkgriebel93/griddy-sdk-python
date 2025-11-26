from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ...types import BaseModel


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
