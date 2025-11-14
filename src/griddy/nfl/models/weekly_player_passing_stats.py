from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel
from .game_result_enum import GameResultEnum


class WeeklyPlayerPassingStatsTypedDict(TypedDict):
    att: int
    r"""Attempts"""
    cmp: int
    r"""Completions"""
    display_name: str
    r"""Player's full name"""
    gp: int
    r"""Games played"""
    gs: int
    r"""Games started"""
    int_: int
    r"""Interceptions"""
    nfl_id: str
    r"""NFL player identifier"""
    position: str
    r"""Player position"""
    td: int
    r"""Touchdown passes"""
    team_id: str
    r"""Team identifier"""
    yds: int
    r"""Passing yards"""
    att_pg: NotRequired[float]
    r"""Attempts per game"""
    avg_sep: NotRequired[float]
    r"""Average receiver separation at target (yards)"""
    avg_ttp: NotRequired[float]
    r"""Average time to pass (seconds)"""
    avg_tts: NotRequired[float]
    r"""Average time to sack (seconds)"""
    avg_ttt: NotRequired[float]
    r"""Average time to throw (seconds)"""
    ay: NotRequired[float]
    r"""Air yards"""
    ay_att: NotRequired[float]
    r"""Air yards per attempt"""
    blitz_r: NotRequired[float]
    r"""Blitz rate faced (0-1)"""
    cmp_pg: NotRequired[float]
    r"""Completions per game"""
    cmp_pct: NotRequired[float]
    r"""Completion percentage (0-1)"""
    cpoe: NotRequired[float]
    r"""Completion percentage over expected"""
    db: NotRequired[int]
    r"""Dropbacks"""
    db_pg: NotRequired[float]
    r"""Dropbacks per game"""
    deep_att_pct: NotRequired[float]
    r"""Deep attempt percentage (20+ air yards) (0-1)"""
    drop: NotRequired[int]
    r"""Dropped passes by receivers"""
    drop_pg: NotRequired[float]
    r"""Drops per game"""
    drop_r: NotRequired[float]
    r"""Drop rate (0-1)"""
    epa: NotRequired[float]
    r"""Expected Points Added"""
    epa_db: NotRequired[float]
    r"""EPA per dropback"""
    epa_pg: NotRequired[float]
    r"""EPA per game"""
    fapi_game_id: NotRequired[str]
    r"""Football API game identifier"""
    final_score: NotRequired[str]
    r"""Final score of the game"""
    game_id: NotRequired[int]
    r"""Game identifier (10-digit format YYYYMMDDNN)"""
    game_result: NotRequired[GameResultEnum]
    r"""Game result (Win/Loss/Tie)"""
    headshot: NotRequired[str]
    r"""URL to player headshot image (contains formatInstructions placeholder)"""
    int_pg: NotRequired[float]
    r"""Interceptions per game"""
    is_home: NotRequired[bool]
    r"""Whether player's team was at home"""
    jersey_number: NotRequired[int]
    r"""Player's jersey number"""
    ngs_position: NotRequired[str]
    r"""Next Gen Stats position"""
    ngs_position_group: NotRequired[str]
    r"""Next Gen Stats position group"""
    opponent_team_id: NotRequired[str]
    r"""Opponent team identifier"""
    pa_db_pct: NotRequired[float]
    r"""Play action dropback percentage (0-1)"""
    position_group: NotRequired[str]
    r"""Position group"""
    qbp: NotRequired[int]
    r"""Times under QB pressure"""
    qbp_pg: NotRequired[float]
    r"""QB pressure per game"""
    qbp_r: NotRequired[float]
    r"""QB pressure rate (0-1)"""
    qp: NotRequired[bool]
    r"""Qualified passer status"""
    rating: NotRequired[float]
    r"""Passer rating"""
    sack: NotRequired[int]
    r"""Times sacked"""
    sack_pg: NotRequired[float]
    r"""Sacks per game"""
    short_name: NotRequired[str]
    r"""Abbreviated player name"""
    td_pg: NotRequired[float]
    r"""Touchdowns per game"""
    tg: NotRequired[int]
    r"""Team games for player"""
    total_tg: NotRequired[int]
    r"""Total team games in period"""
    tw_att_pg: NotRequired[float]
    r"""Two-minute attempts per game"""
    tw_att_pct: NotRequired[float]
    r"""Two-minute drill attempt percentage (0-1)"""
    week_slug: NotRequired[str]
    r"""Week identifier slug"""
    x_cmp: NotRequired[float]
    r"""Expected completion percentage (0-1)"""
    x_yac: NotRequired[float]
    r"""Expected yards after catch"""
    yac: NotRequired[float]
    r"""Yards after catch"""
    yac_pct: NotRequired[float]
    r"""YAC percentage of total yards (0-1)"""
    yds_pg: NotRequired[float]
    r"""Yards per game"""
    ypa: NotRequired[float]
    r"""Yards per attempt"""


class WeeklyPlayerPassingStats(BaseModel):
    att: int
    r"""Attempts"""

    cmp: int
    r"""Completions"""

    display_name: Annotated[str, pydantic.Field(alias="displayName")]
    r"""Player's full name"""

    gp: int
    r"""Games played"""

    gs: int
    r"""Games started"""

    int_: Annotated[int, pydantic.Field(alias="int")]
    r"""Interceptions"""

    nfl_id: Annotated[str, pydantic.Field(alias="nflId")]
    r"""NFL player identifier"""

    position: str
    r"""Player position"""

    td: int
    r"""Touchdown passes"""

    team_id: Annotated[str, pydantic.Field(alias="teamId")]
    r"""Team identifier"""

    yds: int
    r"""Passing yards"""

    att_pg: Annotated[Optional[float], pydantic.Field(alias="attPG")] = None
    r"""Attempts per game"""

    avg_sep: Annotated[Optional[float], pydantic.Field(alias="avgSep")] = None
    r"""Average receiver separation at target (yards)"""

    avg_ttp: Annotated[Optional[float], pydantic.Field(alias="avgTTP")] = None
    r"""Average time to pass (seconds)"""

    avg_tts: Annotated[Optional[float], pydantic.Field(alias="avgTTS")] = None
    r"""Average time to sack (seconds)"""

    avg_ttt: Annotated[Optional[float], pydantic.Field(alias="avgTTT")] = None
    r"""Average time to throw (seconds)"""

    ay: Optional[float] = None
    r"""Air yards"""

    ay_att: Annotated[Optional[float], pydantic.Field(alias="ayAtt")] = None
    r"""Air yards per attempt"""

    blitz_r: Annotated[Optional[float], pydantic.Field(alias="blitzR")] = None
    r"""Blitz rate faced (0-1)"""

    cmp_pg: Annotated[Optional[float], pydantic.Field(alias="cmpPG")] = None
    r"""Completions per game"""

    cmp_pct: Annotated[Optional[float], pydantic.Field(alias="cmpPct")] = None
    r"""Completion percentage (0-1)"""

    cpoe: Optional[float] = None
    r"""Completion percentage over expected"""

    db: Optional[int] = None
    r"""Dropbacks"""

    db_pg: Annotated[Optional[float], pydantic.Field(alias="dbPG")] = None
    r"""Dropbacks per game"""

    deep_att_pct: Annotated[Optional[float], pydantic.Field(alias="deepAttPct")] = None
    r"""Deep attempt percentage (20+ air yards) (0-1)"""

    drop: Optional[int] = None
    r"""Dropped passes by receivers"""

    drop_pg: Annotated[Optional[float], pydantic.Field(alias="dropPG")] = None
    r"""Drops per game"""

    drop_r: Annotated[Optional[float], pydantic.Field(alias="dropR")] = None
    r"""Drop rate (0-1)"""

    epa: Optional[float] = None
    r"""Expected Points Added"""

    epa_db: Annotated[Optional[float], pydantic.Field(alias="epaDb")] = None
    r"""EPA per dropback"""

    epa_pg: Annotated[Optional[float], pydantic.Field(alias="epaPG")] = None
    r"""EPA per game"""

    fapi_game_id: Annotated[Optional[str], pydantic.Field(alias="fapiGameId")] = None
    r"""Football API game identifier"""

    final_score: Annotated[Optional[str], pydantic.Field(alias="finalScore")] = None
    r"""Final score of the game"""

    game_id: Annotated[Optional[int], pydantic.Field(alias="gameId")] = None
    r"""Game identifier (10-digit format YYYYMMDDNN)"""

    game_result: Annotated[
        Optional[GameResultEnum], pydantic.Field(alias="gameResult")
    ] = None
    r"""Game result (Win/Loss/Tie)"""

    headshot: Optional[str] = None
    r"""URL to player headshot image (contains formatInstructions placeholder)"""

    int_pg: Annotated[Optional[float], pydantic.Field(alias="intPG")] = None
    r"""Interceptions per game"""

    is_home: Annotated[Optional[bool], pydantic.Field(alias="isHome")] = None
    r"""Whether player's team was at home"""

    jersey_number: Annotated[Optional[int], pydantic.Field(alias="jerseyNumber")] = None
    r"""Player's jersey number"""

    ngs_position: Annotated[Optional[str], pydantic.Field(alias="ngsPosition")] = None
    r"""Next Gen Stats position"""

    ngs_position_group: Annotated[
        Optional[str], pydantic.Field(alias="ngsPositionGroup")
    ] = None
    r"""Next Gen Stats position group"""

    opponent_team_id: Annotated[
        Optional[str], pydantic.Field(alias="opponentTeamId")
    ] = None
    r"""Opponent team identifier"""

    pa_db_pct: Annotated[Optional[float], pydantic.Field(alias="paDbPct")] = None
    r"""Play action dropback percentage (0-1)"""

    position_group: Annotated[Optional[str], pydantic.Field(alias="positionGroup")] = (
        None
    )
    r"""Position group"""

    qbp: Optional[int] = None
    r"""Times under QB pressure"""

    qbp_pg: Annotated[Optional[float], pydantic.Field(alias="qbpPG")] = None
    r"""QB pressure per game"""

    qbp_r: Annotated[Optional[float], pydantic.Field(alias="qbpR")] = None
    r"""QB pressure rate (0-1)"""

    qp: Optional[bool] = None
    r"""Qualified passer status"""

    rating: Optional[float] = None
    r"""Passer rating"""

    sack: Optional[int] = None
    r"""Times sacked"""

    sack_pg: Annotated[Optional[float], pydantic.Field(alias="sackPG")] = None
    r"""Sacks per game"""

    short_name: Annotated[Optional[str], pydantic.Field(alias="shortName")] = None
    r"""Abbreviated player name"""

    td_pg: Annotated[Optional[float], pydantic.Field(alias="tdPG")] = None
    r"""Touchdowns per game"""

    tg: Optional[int] = None
    r"""Team games for player"""

    total_tg: Annotated[Optional[int], pydantic.Field(alias="totalTg")] = None
    r"""Total team games in period"""

    tw_att_pg: Annotated[Optional[float], pydantic.Field(alias="twAttPG")] = None
    r"""Two-minute attempts per game"""

    tw_att_pct: Annotated[Optional[float], pydantic.Field(alias="twAttPct")] = None
    r"""Two-minute drill attempt percentage (0-1)"""

    week_slug: Annotated[Optional[str], pydantic.Field(alias="weekSlug")] = None
    r"""Week identifier slug"""

    x_cmp: Annotated[Optional[float], pydantic.Field(alias="xCmp")] = None
    r"""Expected completion percentage (0-1)"""

    x_yac: Annotated[Optional[float], pydantic.Field(alias="xYac")] = None
    r"""Expected yards after catch"""

    yac: Optional[float] = None
    r"""Yards after catch"""

    yac_pct: Annotated[Optional[float], pydantic.Field(alias="yacPct")] = None
    r"""YAC percentage of total yards (0-1)"""

    yds_pg: Annotated[Optional[float], pydantic.Field(alias="ydsPG")] = None
    r"""Yards per game"""

    ypa: Optional[float] = None
    r"""Yards per attempt"""
