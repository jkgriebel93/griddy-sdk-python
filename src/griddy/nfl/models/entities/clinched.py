from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


class Clinched(BaseModel):
    """Playoff clinching status for a team."""

    bye: Optional[bool] = None
    r"""Clinched first-round bye"""

    division: Optional[bool] = None
    r"""Clinched division title"""

    eliminated: Optional[bool] = None
    r"""Eliminated from playoff contention"""

    home_field: Annotated[Optional[bool], pydantic.Field(alias="homeField")] = None
    r"""Clinched home field advantage"""

    playoff: Optional[bool] = None
    r"""Clinched playoff berth"""

    wild_card: Annotated[Optional[bool], pydantic.Field(alias="wildCard")] = None
    r"""Clinched wild card berth"""
