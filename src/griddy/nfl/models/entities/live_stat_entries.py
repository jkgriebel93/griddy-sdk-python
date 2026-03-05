from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel

# ---------------------------------------------------------------------------
# Live Team Statistics Entry
# ---------------------------------------------------------------------------


class LiveTeamStatEntry(BaseModel):
    r"""A single team's statistics from a live team-statistics response."""

    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None

    # Defense
    defensive_fumbles_forced: Annotated[
        Optional[int], pydantic.Field(alias="defensiveFumblesForced")
    ] = None

    defensive_fumbles_recovered: Annotated[
        Optional[int], pydantic.Field(alias="defensiveFumblesRecovered")
    ] = None

    defensive_interceptions: Annotated[
        Optional[int], pydantic.Field(alias="defensiveInterceptions")
    ] = None

    defensive_passes_defended: Annotated[
        Optional[int], pydantic.Field(alias="defensivePassesDefended")
    ] = None

    defensive_quarterback_hits: Annotated[
        Optional[int], pydantic.Field(alias="defensiveQuarterbackHits")
    ] = None

    defensive_sacks: Annotated[
        Optional[int], pydantic.Field(alias="defensiveSacks")
    ] = None

    defensive_safeties: Annotated[
        Optional[int], pydantic.Field(alias="defensiveSafeties")
    ] = None

    defensive_tackles_combined: Annotated[
        Optional[float], pydantic.Field(alias="defensiveTacklesCombined")
    ] = None

    defensive_tackles_for_loss: Annotated[
        Optional[float], pydantic.Field(alias="defensiveTacklesForLoss")
    ] = None

    defensive_touchdowns: Annotated[
        Optional[int], pydantic.Field(alias="defensiveTouchdowns")
    ] = None

    # Extra points
    extra_point_kick_attempts: Annotated[
        Optional[int], pydantic.Field(alias="extraPointKickAttempts")
    ] = None

    extra_point_kick_blocked: Annotated[
        Optional[int], pydantic.Field(alias="extraPointKickBlocked")
    ] = None

    extra_point_kick_made: Annotated[
        Optional[int], pydantic.Field(alias="extraPointKickMade")
    ] = None

    # Field goals
    field_goals_attempts: Annotated[
        Optional[int], pydantic.Field(alias="fieldGoalsAttempts")
    ] = None

    field_goals_blocked: Annotated[
        Optional[int], pydantic.Field(alias="fieldGoalsBlocked")
    ] = None

    field_goals_longest_made: Annotated[
        Optional[int], pydantic.Field(alias="fieldGoalsLongestMade")
    ] = None

    field_goals_made: Annotated[
        Optional[int], pydantic.Field(alias="fieldGoalsMade")
    ] = None

    # First downs
    first_downs_passing: Annotated[
        Optional[int], pydantic.Field(alias="firstDownsPassing")
    ] = None

    first_downs_penalty: Annotated[
        Optional[int], pydantic.Field(alias="firstDownsPenalty")
    ] = None

    first_downs_rushing: Annotated[
        Optional[int], pydantic.Field(alias="firstDownsRushing")
    ] = None

    first_downs_total: Annotated[
        Optional[int], pydantic.Field(alias="firstDownsTotal")
    ] = None

    # Fourth down
    fourth_down_attempts: Annotated[
        Optional[int], pydantic.Field(alias="fourthDownAttempts")
    ] = None

    fourth_down_conversions: Annotated[
        Optional[int], pydantic.Field(alias="fourthDownConversions")
    ] = None

    # Fumbles
    fumbles_lost: Annotated[Optional[int], pydantic.Field(alias="fumblesLost")] = None

    fumbles_made: Annotated[Optional[int], pydantic.Field(alias="fumblesMade")] = None

    fumbles_own_recoveries: Annotated[
        Optional[int], pydantic.Field(alias="fumblesOwnRecoveries")
    ] = None

    fumbles_returned_touchdowns: Annotated[
        Optional[int], pydantic.Field(alias="fumblesReturnedTouchdowns")
    ] = None

    # Goal to go
    goal_to_go_attempts: Annotated[
        Optional[int], pydantic.Field(alias="goalToGoAttempts")
    ] = None

    goal_to_go_successes: Annotated[
        Optional[int], pydantic.Field(alias="goalToGoSuccesses")
    ] = None

    # Interceptions
    interceptions_longest_touchdown: Annotated[
        Optional[int], pydantic.Field(alias="interceptionsLongestTouchdown")
    ] = None

    interceptions_made: Annotated[
        Optional[int], pydantic.Field(alias="interceptionsMade")
    ] = None

    interceptions_returned: Annotated[
        Optional[int], pydantic.Field(alias="interceptionsReturned")
    ] = None

    interceptions_returned_touchdowns: Annotated[
        Optional[int], pydantic.Field(alias="interceptionsReturnedTouchdowns")
    ] = None

    interceptions_returned_yards: Annotated[
        Optional[int], pydantic.Field(alias="interceptionsReturnedYards")
    ] = None

    # Kick returns
    kick_returns_longest: Annotated[
        Optional[int], pydantic.Field(alias="kickReturnsLongest")
    ] = None

    kick_returns_yards_average: Annotated[
        Optional[float], pydantic.Field(alias="kickReturnsYardsAverage")
    ] = None

    # Kickoffs
    kickoffs_in_end_zone: Annotated[
        Optional[int], pydantic.Field(alias="kickoffsInEndZone")
    ] = None

    kickoffs_made: Annotated[Optional[int], pydantic.Field(alias="kickoffsMade")] = None

    kickoffs_returned: Annotated[
        Optional[int], pydantic.Field(alias="kickoffsReturned")
    ] = None

    kickoffs_returned_touchdowns: Annotated[
        Optional[int], pydantic.Field(alias="kickoffsReturnedTouchdowns")
    ] = None

    kickoffs_returned_yards: Annotated[
        Optional[int], pydantic.Field(alias="kickoffsReturnedYards")
    ] = None

    kickoffs_touchbacks: Annotated[
        Optional[int], pydantic.Field(alias="kickoffsTouchbacks")
    ] = None

    # Passing
    passing_attempts: Annotated[
        Optional[int], pydantic.Field(alias="passingAttempts")
    ] = None

    passing_completion_percent: Annotated[
        Optional[float], pydantic.Field(alias="passingCompletionPercent")
    ] = None

    passing_completions: Annotated[
        Optional[int], pydantic.Field(alias="passingCompletions")
    ] = None

    passing_interceptions: Annotated[
        Optional[int], pydantic.Field(alias="passingInterceptions")
    ] = None

    passing_rating: Annotated[
        Optional[float], pydantic.Field(alias="passingRating")
    ] = None

    passing_sack_yards_lost: Annotated[
        Optional[float], pydantic.Field(alias="passingSackYardsLost")
    ] = None

    passing_sacks: Annotated[Optional[int], pydantic.Field(alias="passingSacks")] = None

    passing_touchdowns: Annotated[
        Optional[int], pydantic.Field(alias="passingTouchdowns")
    ] = None

    passing_yards: Annotated[Optional[int], pydantic.Field(alias="passingYards")] = None

    passing_yards_average: Annotated[
        Optional[float], pydantic.Field(alias="passingYardsAverage")
    ] = None

    passing_yards_per_attempt: Annotated[
        Optional[float], pydantic.Field(alias="passingYardsPerAttempt")
    ] = None

    # Penalties
    penalties_made: Annotated[Optional[int], pydantic.Field(alias="penaltiesMade")] = (
        None
    )

    penalties_yards: Annotated[
        Optional[int], pydantic.Field(alias="penaltiesYards")
    ] = None

    # Punt returns
    punt_returns_longest: Annotated[
        Optional[int], pydantic.Field(alias="puntReturnsLongest")
    ] = None

    punt_returns_yards_average: Annotated[
        Optional[float], pydantic.Field(alias="puntReturnsYardsAverage")
    ] = None

    # Punts
    punts_attempts: Annotated[Optional[int], pydantic.Field(alias="puntsAttempts")] = (
        None
    )

    punts_blocked: Annotated[Optional[int], pydantic.Field(alias="puntsBlocked")] = None

    punts_inside20: Annotated[Optional[int], pydantic.Field(alias="puntsInside20")] = (
        None
    )

    punts_longest: Annotated[Optional[int], pydantic.Field(alias="puntsLongest")] = None

    punts_returned: Annotated[Optional[int], pydantic.Field(alias="puntsReturned")] = (
        None
    )

    punts_returned_touchdowns: Annotated[
        Optional[int], pydantic.Field(alias="puntsReturnedTouchdowns")
    ] = None

    punts_returned_yards: Annotated[
        Optional[int], pydantic.Field(alias="puntsReturnedYards")
    ] = None

    punts_touchbacks: Annotated[
        Optional[int], pydantic.Field(alias="puntsTouchbacks")
    ] = None

    punts_yards: Annotated[Optional[int], pydantic.Field(alias="puntsYards")] = None

    punts_yards_average_gross: Annotated[
        Optional[float], pydantic.Field(alias="puntsYardsAverageGross")
    ] = None

    punts_yards_average_net: Annotated[
        Optional[float], pydantic.Field(alias="puntsYardsAverageNet")
    ] = None

    # Receiving
    receptions: Optional[int] = None

    receptions_long: Annotated[
        Optional[int], pydantic.Field(alias="receptionsLong")
    ] = None

    receptions_pass_target: Annotated[
        Optional[int], pydantic.Field(alias="receptionsPassTarget")
    ] = None

    receptions_touchdowns: Annotated[
        Optional[int], pydantic.Field(alias="receptionsTouchdowns")
    ] = None

    receptions_yards: Annotated[
        Optional[int], pydantic.Field(alias="receptionsYards")
    ] = None

    receptions_yards_after_catch: Annotated[
        Optional[int], pydantic.Field(alias="receptionsYardsAfterCatch")
    ] = None

    # Red zone
    red_zone_attempts: Annotated[
        Optional[int], pydantic.Field(alias="redZoneAttempts")
    ] = None

    red_zone_successes: Annotated[
        Optional[int], pydantic.Field(alias="redZoneSuccesses")
    ] = None

    # Rushing
    rushing_long: Annotated[Optional[int], pydantic.Field(alias="rushingLong")] = None

    rushing_plays: Annotated[Optional[int], pydantic.Field(alias="rushingPlays")] = None

    rushing_tackles_for_loss: Annotated[
        Optional[int], pydantic.Field(alias="rushingTacklesForLoss")
    ] = None

    rushing_tackles_for_loss_yards: Annotated[
        Optional[int], pydantic.Field(alias="rushingTacklesForLossYards")
    ] = None

    rushing_touchdowns: Annotated[
        Optional[int], pydantic.Field(alias="rushingTouchdowns")
    ] = None

    rushing_yards: Annotated[Optional[int], pydantic.Field(alias="rushingYards")] = None

    rushing_yards_average: Annotated[
        Optional[float], pydantic.Field(alias="rushingYardsAverage")
    ] = None

    # Safeties
    safeties_one_point: Annotated[
        Optional[int], pydantic.Field(alias="safetiesOnePoint")
    ] = None

    safeties_two_point: Annotated[
        Optional[int], pydantic.Field(alias="safetiesTwoPoint")
    ] = None

    # Score
    score_ot: Annotated[Optional[int], pydantic.Field(alias="scoreOT")] = None

    score_q1: Annotated[Optional[int], pydantic.Field(alias="scoreQ1")] = None

    score_q2: Annotated[Optional[int], pydantic.Field(alias="scoreQ2")] = None

    score_q3: Annotated[Optional[int], pydantic.Field(alias="scoreQ3")] = None

    score_q4: Annotated[Optional[int], pydantic.Field(alias="scoreQ4")] = None

    score_total: Annotated[Optional[int], pydantic.Field(alias="scoreTotal")] = None

    # Third down
    third_down_attempts: Annotated[
        Optional[int], pydantic.Field(alias="thirdDownAttempts")
    ] = None

    third_down_conversions: Annotated[
        Optional[int], pydantic.Field(alias="thirdDownConversions")
    ] = None

    # Time
    time_of_possession: Annotated[
        Optional[str], pydantic.Field(alias="timeOfPossession")
    ] = None

    timeouts_remaining: Annotated[
        Optional[int], pydantic.Field(alias="timeoutsRemaining")
    ] = None

    timeouts_used: Annotated[Optional[int], pydantic.Field(alias="timeoutsUsed")] = None

    # Totals
    total_plays: Annotated[Optional[int], pydantic.Field(alias="totalPlays")] = None

    total_yards: Annotated[Optional[int], pydantic.Field(alias="totalYards")] = None

    touchdowns_all_other: Annotated[
        Optional[int], pydantic.Field(alias="touchdownsAllOther")
    ] = None

    turnovers: Optional[int] = None

    # Two-point conversions
    two_point_conversions_defensive_returns: Annotated[
        Optional[int],
        pydantic.Field(alias="twoPointConversionsDefensiveReturns"),
    ] = None

    two_point_conversions_passing_attempts: Annotated[
        Optional[int],
        pydantic.Field(alias="twoPointConversionsPassingAttempts"),
    ] = None

    two_point_conversions_passing_successes: Annotated[
        Optional[int],
        pydantic.Field(alias="twoPointConversionsPassingSuccesses"),
    ] = None

    two_point_conversions_rushing_attempts: Annotated[
        Optional[int],
        pydantic.Field(alias="twoPointConversionsRushingAttempts"),
    ] = None

    two_point_conversions_rushing_successes: Annotated[
        Optional[int],
        pydantic.Field(alias="twoPointConversionsRushingSuccesses"),
    ] = None


# ---------------------------------------------------------------------------
# Live Player Statistics Entry
# ---------------------------------------------------------------------------


class LivePlayerStatEntry(BaseModel):
    r"""A single player's statistics from a live player-statistics response."""

    # Identity
    person_id: Annotated[Optional[str], pydantic.Field(alias="personId")] = None

    gsis_player_id: Annotated[Optional[str], pydantic.Field(alias="gsisPlayerId")] = (
        None
    )

    gsis_player_name: Annotated[
        Optional[str], pydantic.Field(alias="gsisPlayerName")
    ] = None

    gsis_player_jersey_number: Annotated[
        Optional[str], pydantic.Field(alias="gsisPlayerJerseyNumber")
    ] = None

    # Defense
    defensive_fumbles_forced: Annotated[
        Optional[int], pydantic.Field(alias="defensiveFumblesForced")
    ] = None

    defensive_fumbles_recovered: Annotated[
        Optional[int], pydantic.Field(alias="defensiveFumblesRecovered")
    ] = None

    defensive_interceptions: Annotated[
        Optional[int], pydantic.Field(alias="defensiveInterceptions")
    ] = None

    defensive_miscellaneous_fumbles_forced: Annotated[
        Optional[int],
        pydantic.Field(alias="defensiveMiscellaneousFumblesForced"),
    ] = None

    defensive_miscellaneous_fumbles_recovered: Annotated[
        Optional[int],
        pydantic.Field(alias="defensiveMiscellaneousFumblesRecovered"),
    ] = None

    defensive_miscellaneous_tackles: Annotated[
        Optional[float],
        pydantic.Field(alias="defensiveMiscellaneousTackles"),
    ] = None

    defensive_miscellaneous_tackles_assists: Annotated[
        Optional[int],
        pydantic.Field(alias="defensiveMiscellaneousTacklesAssists"),
    ] = None

    defensive_passes_defended: Annotated[
        Optional[int], pydantic.Field(alias="defensivePassesDefended")
    ] = None

    defensive_quarterback_hits: Annotated[
        Optional[int], pydantic.Field(alias="defensiveQuarterbackHits")
    ] = None

    defensive_sack_yards: Annotated[
        Optional[float], pydantic.Field(alias="defensiveSackYards")
    ] = None

    defensive_sacks: Annotated[
        Optional[float], pydantic.Field(alias="defensiveSacks")
    ] = None

    defensive_safeties: Annotated[
        Optional[int], pydantic.Field(alias="defensiveSafeties")
    ] = None

    defensive_special_teams_blocks: Annotated[
        Optional[int], pydantic.Field(alias="defensiveSpecialTeamsBlocks")
    ] = None

    defensive_special_teams_fumbles_forced: Annotated[
        Optional[int],
        pydantic.Field(alias="defensiveSpecialTeamsFumblesForced"),
    ] = None

    defensive_special_teams_fumbles_recovered: Annotated[
        Optional[int],
        pydantic.Field(alias="defensiveSpecialTeamsFumblesRecovered"),
    ] = None

    defensive_special_teams_tackles: Annotated[
        Optional[float],
        pydantic.Field(alias="defensiveSpecialTeamsTackles"),
    ] = None

    defensive_special_teams_tackles_assists: Annotated[
        Optional[int],
        pydantic.Field(alias="defensiveSpecialTeamsTacklesAssists"),
    ] = None

    defensive_tackles: Annotated[
        Optional[float], pydantic.Field(alias="defensiveTackles")
    ] = None

    defensive_tackles_assists: Annotated[
        Optional[int], pydantic.Field(alias="defensiveTacklesAssists")
    ] = None

    defensive_tackles_combined: Annotated[
        Optional[float], pydantic.Field(alias="defensiveTacklesCombined")
    ] = None

    defensive_tackles_for_loss: Annotated[
        Optional[float], pydantic.Field(alias="defensiveTacklesForLoss")
    ] = None

    defensive_tackles_for_loss_yards: Annotated[
        Optional[float], pydantic.Field(alias="defensiveTacklesForLossYards")
    ] = None

    # Extra points
    extra_points_attempted: Annotated[
        Optional[int], pydantic.Field(alias="extraPointsAttempted")
    ] = None

    extra_points_blocked: Annotated[
        Optional[int], pydantic.Field(alias="extraPointsBlocked")
    ] = None

    extra_points_made: Annotated[
        Optional[int], pydantic.Field(alias="extraPointsMade")
    ] = None

    extra_points_missed: Annotated[
        Optional[int], pydantic.Field(alias="extraPointsMissed")
    ] = None

    # Field goals
    field_goals_attempted: Annotated[
        Optional[int], pydantic.Field(alias="fieldGoalsAttempted")
    ] = None

    field_goals_average_length: Annotated[
        Optional[float], pydantic.Field(alias="fieldGoalsAverageLength")
    ] = None

    field_goals_blocked: Annotated[
        Optional[int], pydantic.Field(alias="fieldGoalsBlocked")
    ] = None

    field_goals_longest_made: Annotated[
        Optional[int], pydantic.Field(alias="fieldGoalsLongestMade")
    ] = None

    field_goals_made: Annotated[
        Optional[int], pydantic.Field(alias="fieldGoalsMade")
    ] = None

    field_goals_missed: Annotated[
        Optional[int], pydantic.Field(alias="fieldGoalsMissed")
    ] = None

    field_goals_total_yards: Annotated[
        Optional[int], pydantic.Field(alias="fieldGoalsTotalYards")
    ] = None

    # Fumbles
    fumbles: Optional[int] = None

    fumbles_forced: Annotated[Optional[int], pydantic.Field(alias="fumblesForced")] = (
        None
    )

    fumbles_lost: Annotated[Optional[int], pydantic.Field(alias="fumblesLost")] = None

    fumbles_opponent_recoveries: Annotated[
        Optional[int], pydantic.Field(alias="fumblesOpponentRecoveries")
    ] = None

    fumbles_opponent_recovery_touchdowns: Annotated[
        Optional[int],
        pydantic.Field(alias="fumblesOpponentRecoveryTouchdowns"),
    ] = None

    fumbles_opponent_recovery_yards: Annotated[
        Optional[int], pydantic.Field(alias="fumblesOpponentRecoveryYards")
    ] = None

    fumbles_out_of_bounds: Annotated[
        Optional[int], pydantic.Field(alias="fumblesOutOfBounds")
    ] = None

    fumbles_own_recoveries: Annotated[
        Optional[int], pydantic.Field(alias="fumblesOwnRecoveries")
    ] = None

    fumbles_own_recovery_touchdowns: Annotated[
        Optional[int], pydantic.Field(alias="fumblesOwnRecoveryTouchdowns")
    ] = None

    fumbles_own_recovery_yards: Annotated[
        Optional[int], pydantic.Field(alias="fumblesOwnRecoveryYards")
    ] = None

    fumbles_recovered_in_end_zone_for_touchdown: Annotated[
        Optional[int],
        pydantic.Field(alias="fumblesRecoveredInEndZoneForTouchdown"),
    ] = None

    # Interceptions
    interceptions: Optional[int] = None

    interceptions_long: Annotated[
        Optional[int], pydantic.Field(alias="interceptionsLong")
    ] = None

    interceptions_longest_touchdown: Annotated[
        Optional[int], pydantic.Field(alias="interceptionsLongestTouchdown")
    ] = None

    interceptions_touchdowns: Annotated[
        Optional[int], pydantic.Field(alias="interceptionsTouchdowns")
    ] = None

    interceptions_yards: Annotated[
        Optional[int], pydantic.Field(alias="interceptionsYards")
    ] = None

    # Kick returns
    kick_returns: Annotated[Optional[int], pydantic.Field(alias="kickReturns")] = None

    kick_returns_fair_catches: Annotated[
        Optional[int], pydantic.Field(alias="kickReturnsFairCatches")
    ] = None

    kick_returns_longest: Annotated[
        Optional[int], pydantic.Field(alias="kickReturnsLongest")
    ] = None

    kick_returns_longest_touchdown: Annotated[
        Optional[int], pydantic.Field(alias="kickReturnsLongestTouchdown")
    ] = None

    kick_returns_touchdowns: Annotated[
        Optional[int], pydantic.Field(alias="kickReturnsTouchdowns")
    ] = None

    kick_returns_yards: Annotated[
        Optional[int], pydantic.Field(alias="kickReturnsYards")
    ] = None

    kick_returns_yards_average: Annotated[
        Optional[float], pydantic.Field(alias="kickReturnsYardsAverage")
    ] = None

    # Kickoffs
    kickoffs: Optional[int] = None

    kickoffs_inside20: Annotated[
        Optional[int], pydantic.Field(alias="kickoffsInside20")
    ] = None

    kickoffs_out_of_bounds: Annotated[
        Optional[int], pydantic.Field(alias="kickoffsOutOfBounds")
    ] = None

    kickoffs_return_yards: Annotated[
        Optional[int], pydantic.Field(alias="kickoffsReturnYards")
    ] = None

    kickoffs_to_end_zone: Annotated[
        Optional[int], pydantic.Field(alias="kickoffsToEndZone")
    ] = None

    kickoffs_touchbacks: Annotated[
        Optional[int], pydantic.Field(alias="kickoffsTouchbacks")
    ] = None

    kickoffs_yards: Annotated[Optional[int], pydantic.Field(alias="kickoffsYards")] = (
        None
    )

    # Passing
    passing_attempts: Annotated[
        Optional[int], pydantic.Field(alias="passingAttempts")
    ] = None

    passing_completion_percent: Annotated[
        Optional[float], pydantic.Field(alias="passingCompletionPercent")
    ] = None

    passing_completions: Annotated[
        Optional[int], pydantic.Field(alias="passingCompletions")
    ] = None

    passing_interceptions: Annotated[
        Optional[int], pydantic.Field(alias="passingInterceptions")
    ] = None

    passing_long: Annotated[Optional[int], pydantic.Field(alias="passingLong")] = None

    passing_longest_touchdown_pass: Annotated[
        Optional[int], pydantic.Field(alias="passingLongestTouchdownPass")
    ] = None

    passing_rating: Annotated[
        Optional[float], pydantic.Field(alias="passingRating")
    ] = None

    passing_sack_yards_lost: Annotated[
        Optional[float], pydantic.Field(alias="passingSackYardsLost")
    ] = None

    passing_times_sacked: Annotated[
        Optional[int], pydantic.Field(alias="passingTimesSacked")
    ] = None

    passing_touchdowns: Annotated[
        Optional[int], pydantic.Field(alias="passingTouchdowns")
    ] = None

    passing_yards: Annotated[Optional[int], pydantic.Field(alias="passingYards")] = None

    passing_yards_average: Annotated[
        Optional[float], pydantic.Field(alias="passingYardsAverage")
    ] = None

    passing_yards_per_attempt: Annotated[
        Optional[float], pydantic.Field(alias="passingYardsPerAttempt")
    ] = None

    # Punt returns
    punt_returns: Annotated[Optional[int], pydantic.Field(alias="puntReturns")] = None

    punt_returns_fair_catches: Annotated[
        Optional[int], pydantic.Field(alias="puntReturnsFairCatches")
    ] = None

    punt_returns_longest: Annotated[
        Optional[int], pydantic.Field(alias="puntReturnsLongest")
    ] = None

    punt_returns_longest_touchdown: Annotated[
        Optional[int], pydantic.Field(alias="puntReturnsLongestTouchdown")
    ] = None

    punt_returns_touchdowns: Annotated[
        Optional[int], pydantic.Field(alias="puntReturnsTouchdowns")
    ] = None

    punt_returns_yards: Annotated[
        Optional[int], pydantic.Field(alias="puntReturnsYards")
    ] = None

    punt_returns_yards_average: Annotated[
        Optional[float], pydantic.Field(alias="puntReturnsYardsAverage")
    ] = None

    # Punts
    punts: Optional[int] = None

    punts_blocked: Annotated[Optional[int], pydantic.Field(alias="puntsBlocked")] = None

    punts_inside20: Annotated[Optional[int], pydantic.Field(alias="puntsInside20")] = (
        None
    )

    punts_longest: Annotated[Optional[int], pydantic.Field(alias="puntsLongest")] = None

    punts_return_yards: Annotated[
        Optional[int], pydantic.Field(alias="puntsReturnYards")
    ] = None

    punts_touchbacks: Annotated[
        Optional[int], pydantic.Field(alias="puntsTouchbacks")
    ] = None

    punts_yards: Annotated[Optional[int], pydantic.Field(alias="puntsYards")] = None

    punts_yards_average_gross: Annotated[
        Optional[float], pydantic.Field(alias="puntsYardsAverageGross")
    ] = None

    punts_yards_average_net: Annotated[
        Optional[float], pydantic.Field(alias="puntsYardsAverageNet")
    ] = None

    # Receiving
    receptions: Optional[int] = None

    receptions_average: Annotated[
        Optional[float], pydantic.Field(alias="receptionsAverage")
    ] = None

    receptions_long: Annotated[
        Optional[int], pydantic.Field(alias="receptionsLong")
    ] = None

    receptions_longest_touchdown: Annotated[
        Optional[int], pydantic.Field(alias="receptionsLongestTouchdown")
    ] = None

    receptions_pass_target: Annotated[
        Optional[int], pydantic.Field(alias="receptionsPassTarget")
    ] = None

    receptions_touchdowns: Annotated[
        Optional[int], pydantic.Field(alias="receptionsTouchdowns")
    ] = None

    receptions_yards: Annotated[
        Optional[int], pydantic.Field(alias="receptionsYards")
    ] = None

    receptions_yards_after_catch: Annotated[
        Optional[int], pydantic.Field(alias="receptionsYardsAfterCatch")
    ] = None

    # Rushing
    rushing_attempts: Annotated[
        Optional[int], pydantic.Field(alias="rushingAttempts")
    ] = None

    rushing_average: Annotated[
        Optional[float], pydantic.Field(alias="rushingAverage")
    ] = None

    rushing_long: Annotated[Optional[int], pydantic.Field(alias="rushingLong")] = None

    rushing_longest_touchdown: Annotated[
        Optional[int], pydantic.Field(alias="rushingLongestTouchdown")
    ] = None

    rushing_touchdowns: Annotated[
        Optional[int], pydantic.Field(alias="rushingTouchdowns")
    ] = None

    rushing_yards: Annotated[Optional[int], pydantic.Field(alias="rushingYards")] = None

    # Two-point conversions
    two_point_defensive_attempts: Annotated[
        Optional[int], pydantic.Field(alias="twoPointDefensiveAttempts")
    ] = None

    two_point_defensive_successes: Annotated[
        Optional[int], pydantic.Field(alias="twoPointDefensiveSuccesses")
    ] = None

    two_point_passing_attempts: Annotated[
        Optional[int], pydantic.Field(alias="twoPointPassingAttempts")
    ] = None

    two_point_passing_successes: Annotated[
        Optional[int], pydantic.Field(alias="twoPointPassingSuccesses")
    ] = None

    two_point_reception_attempts: Annotated[
        Optional[int], pydantic.Field(alias="twoPointReceptionAttempts")
    ] = None

    two_point_reception_successes: Annotated[
        Optional[int], pydantic.Field(alias="twoPointReceptionSuccesses")
    ] = None

    two_point_rushing_attempts: Annotated[
        Optional[int], pydantic.Field(alias="twoPointRushingAttempts")
    ] = None

    two_point_rushing_successes: Annotated[
        Optional[int], pydantic.Field(alias="twoPointRushingSuccesses")
    ] = None


# ---------------------------------------------------------------------------
# Live Player Team Entry (wrapper for awayTeam / homeTeam in player stats)
# ---------------------------------------------------------------------------


class LivePlayerTeamEntry(BaseModel):
    r"""A team wrapper in a live player-statistics response (teamId + players array)."""

    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None

    players: Optional[List[LivePlayerStatEntry]] = None
