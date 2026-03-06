from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


class OddsSelection(BaseModel):
    """Individual betting odds selection option."""

    decimal: Optional[float] = None
    r"""Decimal odds for this selection"""

    is_available: Annotated[Optional[bool], pydantic.Field(alias="isAvailable")] = None
    r"""Whether this selection is currently available for betting"""

    name: Optional[str] = None
    r"""Team name (e.g., \"KC Chiefs\", \"BUF Bills\")"""
