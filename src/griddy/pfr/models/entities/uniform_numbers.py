"""Pydantic models for PFR Uniform Numbers pages.

Covers ``/players/uniform.cgi?number=...&team=...`` pages on Pro Football
Reference, listing players who wore a given number.
"""

from __future__ import annotations

from typing import List, Optional

from ..base import PFRBaseModel


class UniformNumberPlayer(PFRBaseModel):
    """A player who wore the queried uniform number."""

    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    year_min: Optional[int] = None
    year_max: Optional[int] = None
    av: Optional[int] = None


class UniformNumbers(PFRBaseModel):
    """Top-level result for a PFR uniform numbers page."""

    title: str
    number: int
    team: Optional[str] = None
    players: List[UniformNumberPlayer]
