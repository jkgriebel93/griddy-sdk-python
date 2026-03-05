from __future__ import annotations

from typing import Optional

from ...types import BaseModel


class TeamVenue(BaseModel):
    city: Optional[str] = None
    r"""Venue city"""

    country: Optional[str] = None
    r"""Venue country"""

    id: Optional[str] = None
    r"""Venue identifier"""

    name: Optional[str] = None
    r"""Venue name"""
