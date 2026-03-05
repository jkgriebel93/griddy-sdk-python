from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import UNSET, BaseModel, Nullable, OptionalNullable


class PlayWinProbability(BaseModel):
    down: int
    r"""Down number (0 for kickoffs and special plays, 1-4 for regular plays)"""

    home_score: Annotated[int, pydantic.Field(alias="homeScore")]
    r"""Home team score after the play"""

    home_timeouts_left: Annotated[
        OptionalNullable[int], pydantic.Field(alias="homeTimeoutsLeft")
    ] = None
    r"""Number of timeouts remaining for home team"""

    play_description: Annotated[str, pydantic.Field(alias="playDescription")]
    r"""Detailed description of the play or game event"""

    play_id: Annotated[int, pydantic.Field(alias="playId")]
    r"""Unique play identifier"""

    possession_team_id: Annotated[str, pydantic.Field(alias="possessionTeamId")]
    r"""Team ID with possession (4-digit string)"""

    pre_snap_home_score: Annotated[int, pydantic.Field(alias="preSnapHomeScore")]
    r"""Home team score before the play"""

    pre_snap_visitor_score: Annotated[int, pydantic.Field(alias="preSnapVisitorScore")]
    r"""Visitor team score before the play"""

    quarter: int
    r"""Quarter number (1-4, or 5 for overtime)"""

    sequence: float
    r"""Play sequence number (can be decimal for special plays)"""

    visitor_score: Annotated[int, pydantic.Field(alias="visitorScore")]
    r"""Visitor team score after the play"""

    visitor_timeouts_left: Annotated[
        OptionalNullable[int], pydantic.Field(alias="visitorTimeoutsLeft")
    ] = None
    r"""Number of timeouts remaining for visitor team"""

    yards_to_go: Annotated[int, pydantic.Field(alias="yardsToGo")]
    r"""Yards needed for first down"""

    home_team_win_probability_added: Annotated[
        OptionalNullable[float], pydantic.Field(alias="homeTeamWinProbabilityAdded")
    ] = UNSET
    r"""Win Probability Added (WPA) for home team on this play"""

    post_play_home_team_win_probability: Annotated[
        OptionalNullable[float], pydantic.Field(alias="postPlayHomeTeamWinProbability")
    ] = UNSET
    r"""Home team win probability after the play (0-1)"""

    post_play_visitor_team_win_probability: Annotated[
        OptionalNullable[float],
        pydantic.Field(alias="postPlayVisitorTeamWinProbability"),
    ] = UNSET
    r"""Visiting team win probability after the play (0-1)"""

    pre_snap_home_team_win_probability: Annotated[
        OptionalNullable[float], pydantic.Field(alias="preSnapHomeTeamWinProbability")
    ] = UNSET
    r"""Home team win probability before the play (0-1, null for game start)"""

    pre_snap_visitor_team_win_probability: Annotated[
        OptionalNullable[float],
        pydantic.Field(alias="preSnapVisitorTeamWinProbability"),
    ] = UNSET
    r"""Visitor team win probability before the play (0-1, null for game start)"""

    visitor_team_win_probability_added: Annotated[
        OptionalNullable[float], pydantic.Field(alias="visitorTeamWinProbabilityAdded")
    ] = UNSET
    r"""Win Probability Added (WPA) for visitor team on this play (negative of home WPA)"""

    yardline: Optional[str] = None
    r"""Field position description (e.g., \"NE 27\" or empty for special plays)"""

    yardline_number: Annotated[
        OptionalNullable[int], pydantic.Field(alias="yardlineNumber")
    ] = UNSET
    r"""Yard line number (null for special plays)"""

    yardline_side: Annotated[
        OptionalNullable[str], pydantic.Field(alias="yardlineSide")
    ] = UNSET
    r"""Side of field (team abbreviation or null for midfield/special plays)"""
