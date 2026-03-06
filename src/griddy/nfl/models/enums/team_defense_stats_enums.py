from __future__ import annotations

from typing import Literal

TeamDefenseStatsSortKeyEnum = Literal[
    "total",
    "pass",
    "run",
    "yds",
    "passPct",
    "ypp",
    "td",
    "passTd",
    "rushTd",
    "epa",
    "epaPP",
    "passYds",
    "passYpp",
    "epaPass",
    "epaPassPP",
    "rushYds",
    "rushYpp",
    "epaRush",
    "epaRushPP",
    "ttt",
    "qbp",
    "qbpPct",
    "sackedYds",
    "ryoe",
    "interception",
    "forcedFumble",
    "fumbleRecovered",
    "defensiveTouchdown",
    "totalTakeaways",
    "ppg",
    "ypg",
    "passYpg",
    "rushYpg",
    "sackedYpg",
]
r"""Field to sort team defense stats by"""

TeamDefenseStatsSplitEnum = Literal[
    "TEAM_DEFENSE_BASE",
    "TEAM_DEFENSE_NICKEL",
    "TEAM_DEFENSE_DIME",
    "TEAM_DEFENSE_WHEN_LEADING",
    "TEAM_DEFENSE_WHEN_TRAILING",
    "TEAM_DEFENSE_WHEN_TIED",
    "TEAM_DEFENSE_RED_ZONE",
    "TEAM_DEFENSE_GOAL_TO_GO",
    "TEAM_DEFENSE_SHOTGUN",
    "TEAM_DEFENSE_UNDER_CENTER",
    "TEAM_DEFENSE_PISTOL",
    "TEAM_DEFENSE_MOTION",
]
r"""Defensive situation splits"""
