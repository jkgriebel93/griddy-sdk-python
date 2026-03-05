"""Pydantic models for PFR executive profile pages.

Covers the ``/executives/{ExecutiveId}.htm`` pages on Pro Football Reference,
including career team results and per-team summary totals.
"""

from __future__ import annotations

from typing import List, Optional

from ..base import PFRBaseModel

# --- Executive Bio (from #meta div) ---


class ExecutiveBio(PFRBaseModel):
    name: str


# --- Executive Result (from exec_results table body) ---


class ExecutiveResult(PFRBaseModel):
    year: Optional[str] = None
    year_href: Optional[str] = None
    team: Optional[str] = None
    team_href: Optional[str] = None
    league: Optional[str] = None
    job_title: Optional[str] = None
    wins: Optional[int] = None
    losses: Optional[int] = None
    ties: Optional[int] = None
    win_loss_pct: Optional[str] = None
    playoff_wins: Optional[int] = None
    playoff_losses: Optional[int] = None
    playoff_result: Optional[str] = None
    playoff_result_href: Optional[str] = None


# --- Executive Results Total (from exec_results table footer) ---


class ExecutiveResultsTotal(PFRBaseModel):
    label: Optional[str] = None
    tenure: Optional[str] = None
    wins: Optional[int] = None
    losses: Optional[int] = None
    ties: Optional[int] = None
    playoff_wins: Optional[int] = None
    playoff_losses: Optional[int] = None


# --- Executive Profile (top-level model) ---


class ExecutiveProfile(PFRBaseModel):
    bio: ExecutiveBio
    exec_results: List[ExecutiveResult]
    exec_results_totals: List[ExecutiveResultsTotal]
