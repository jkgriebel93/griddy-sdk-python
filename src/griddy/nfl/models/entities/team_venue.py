from __future__ import annotations

from typing import Optional

from typing_extensions import NotRequired, TypedDict

from ...types import BaseModel


class TeamVenueTypedDict(TypedDict):
    city: NotRequired[str]
    r"""Venue city"""
    country: NotRequired[str]
    r"""Venue country"""
    id: NotRequired[str]
    r"""Venue identifier"""
    name: NotRequired[str]
    r"""Venue name"""


class TeamVenue(BaseModel):
    city: Optional[str] = None
    r"""Venue city"""

    country: Optional[str] = None
    r"""Venue country"""

    id: Optional[str] = None
    r"""Venue identifier"""

    name: Optional[str] = None
    r"""Venue name"""
