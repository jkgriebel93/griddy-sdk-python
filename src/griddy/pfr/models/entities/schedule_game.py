"""Pydantic model for a single game row in a PFR season schedule.

Used by the ``/years/{year}/games.htm`` schedule page parser.
"""

from __future__ import annotations

from typing import Optional

from ..base import PFRBaseModel


class ScheduleGame(PFRBaseModel):
    """A single game entry from the PFR season schedule table."""

    week_num: str
    game_day_of_week: str
    game_date: str
    gametime: Optional[str] = None
    winner: str
    game_location: str
    loser: str
    boxscore_word: Optional[str] = None
    pts_win: Optional[int] = None
    pts_lose: Optional[int] = None
    yards_win: Optional[int] = None
    to_win: Optional[int] = None
    yards_lose: Optional[int] = None
    to_lose: Optional[int] = None
    winner_href: Optional[str] = None
    loser_href: Optional[str] = None
    boxscore_word_href: Optional[str] = None
