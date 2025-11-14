from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel
from .conference_enum import ConferenceEnum


class ConferenceTypedDict(TypedDict):
    abbr: NotRequired[ConferenceEnum]
    r"""NFL conference"""
    full_name: NotRequired[str]
    r"""Full conference name"""
    id: NotRequired[str]
    r"""Conference identifier"""


class Conference(BaseModel):
    abbr: Optional[ConferenceEnum] = None
    r"""NFL conference"""

    full_name: Annotated[Optional[str], pydantic.Field(alias="fullName")] = None
    r"""Full conference name"""

    id: Optional[str] = None
    r"""Conference identifier"""
