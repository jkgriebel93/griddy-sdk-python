from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


class Division(BaseModel):
    abbr: Optional[str] = None
    r"""Division abbreviation"""

    full_name: Annotated[Optional[str], pydantic.Field(alias="fullName")] = None
    r"""Full division name"""

    id: Optional[str] = None
    r"""Division identifier"""
