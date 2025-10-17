# griddy-sdk
This document covers the NFL.com portion of the griddy SDK. That is - the NFL's Regular and Pro API for accessing game schedules, team information, standings, statistics, and venue data. This API provides comprehensive access to NFL data including real-time game information, team rosters, seasonal statistics, and historical data. The NFL Pro API is for accessing advanced statistics, film room content, player data, and fantasy information. This API provides comprehensive access to NFL Pro features including Next Gen Stats, Film Room analysis, player projections, and game insights.



## Getting Started

### Usage

```python

import os
from griddy import nfl
from griddy.nfl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = nfl.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: NFLAuth
configuration = nfl.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with nfl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nfl.AuthenticationController(api_client)
    token_request = {"clientKey":"4cFUW6DmwJpzT9L7LrG3qRAcABG5s04g","clientSecret":"CZuvCL49d9OwfGsR","deviceId":"3cfdef35-c7fe-4f2d-8630-1ec72f52b44d","deviceInfo":"eyJtb2RlbCI6ImRlc2t0b3AiLCJ2ZXJzaW9uIjoiQ2hyb21lIiwib3NOYW1lIjoiV2luZG93cyIsIm9zVmVyc2lvbiI6IjEwIn0=","networkType":"other"} # TokenRequest | 

    try:
        # Generate Initial Access Token
        api_response = api_instance.generate_token(token_request)
        print("The response of AuthenticationController->generate_token:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationController->generate_token: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationController* | [**generate_token**](docs/AuthenticationController.md#generate_token) | **POST** /identity/v3/token | Generate Initial Access Token
*AuthenticationController* | [**refresh_token**](docs/AuthenticationController.md#refresh_token) | **POST** /identity/v3/token/refresh | Refresh Access Token
*BettingController* | [**get_weekly_betting_odds**](docs/BettingController.md#get_weekly_betting_odds) | **GET** /api/schedules/week/odds | Get Weekly Betting Odds
*ContentController* | [**get_game_insights**](docs/ContentController.md#get_game_insights) | **GET** /api/content/insights/game | Get Game-Specific Insights
*ContentController* | [**get_game_preview**](docs/ContentController.md#get_game_preview) | **GET** /api/content/game/preview | Get Game Preview Content
*ContentController* | [**get_home_film_cards**](docs/ContentController.md#get_home_film_cards) | **GET** /api/content/home-film-cards | Get Home Film Cards
*ContentInsightsController* | [**get_season_content_insights**](docs/ContentInsightsController.md#get_season_content_insights) | **GET** /api/content/insights/season | Get Season Content Insights
*DefensivePassRushStatisticsController* | [**get_defensive_pass_rush_stats_by_season**](docs/DefensivePassRushStatisticsController.md#get_defensive_pass_rush_stats_by_season) | **GET** /api/secured/stats/defense/passRush/season | Get Defensive Pass Rush Statistics by Season
*DefensivePlayerOverviewController* | [**get_defensive_overview_stats_by_season**](docs/DefensivePlayerOverviewController.md#get_defensive_overview_stats_by_season) | **GET** /api/secured/stats/defense/overview/season | Get Defensive Player Overview Statistics by Season
*DefensiveStatisticsController* | [**get_defensive_stats_by_season**](docs/DefensiveStatisticsController.md#get_defensive_stats_by_season) | **GET** /api/secured/stats/defense/nearest/season | Get Defensive Player Statistics by Season
*ExperienceController* | [**get_experience_games**](docs/ExperienceController.md#get_experience_games) | **GET** /experience/v1/games | Get Games by Season and Week
*ExperienceController* | [**get_experience_teams**](docs/ExperienceController.md#get_experience_teams) | **GET** /experience/v1/teams | Get All Teams
*FantasyStatisticsController* | [**get_fantasy_stats_by_season**](docs/FantasyStatisticsController.md#get_fantasy_stats_by_season) | **GET** /api/secured/stats/fantasy/season | Get Fantasy Football Statistics by Season
*FilmroomController* | [**get_filmroom_plays**](docs/FilmroomController.md#get_filmroom_plays) | **GET** /api/secured/videos/filmroom/plays | Get Filmroom Plays with Advanced Filtering
*FootballController* | [**get_draft_info**](docs/FootballController.md#get_draft_info) | **GET** /football/v2/draft/{year} | Get Draft Information
*FootballController* | [**get_football_box_score**](docs/FootballController.md#get_football_box_score) | **GET** /football/v2/games/{gameId}/boxscore | Get Game Box Score (Football API)
*FootballController* | [**get_football_games**](docs/FootballController.md#get_football_games) | **GET** /football/v2/games/season/{season}/seasonType/{seasonType}/week/{week} | Get Games by Season, Type, and Week
*FootballController* | [**get_injury_reports**](docs/FootballController.md#get_injury_reports) | **GET** /football/v2/injuries | Get Injury Reports
*FootballController* | [**get_live_game_stats**](docs/FootballController.md#get_live_game_stats) | **GET** /football/v2/stats/live/game-summaries | Get Live Game Statistics
*FootballController* | [**get_play_by_play**](docs/FootballController.md#get_play_by_play) | **GET** /football/v2/games/{gameId}/playbyplay | Get Play-by-Play Data
*FootballController* | [**get_player_details**](docs/FootballController.md#get_player_details) | **GET** /football/v2/players/{playerId} | Get Player Details
*FootballController* | [**get_players_team_roster**](docs/FootballController.md#get_players_team_roster) | **GET** /football/v2/players/teams/{teamId}/roster | Get Team Roster
*FootballController* | [**get_season_player_stats**](docs/FootballController.md#get_season_player_stats) | **GET** /football/v2/stats/players/season | Get Season Player Statistics
*FootballController* | [**get_season_weeks**](docs/FootballController.md#get_season_weeks) | **GET** /football/v2/weeks/season/{season} | Get Season Weeks
*FootballController* | [**get_standings**](docs/FootballController.md#get_standings) | **GET** /football/v2/standings | Get Standings
*FootballController* | [**get_transactions**](docs/FootballController.md#get_transactions) | **GET** /football/v2/transactions | Get Transactions
*FootballController* | [**get_venues**](docs/FootballController.md#get_venues) | **GET** /football/v2/venues | Get NFL Venues
*FootballController* | [**get_weekly_game_details**](docs/FootballController.md#get_weekly_game_details) | **GET** /football/v2/experience/weekly-game-details | Get Weekly Game Details with Standings
*PlayerPassingStatisticsController* | [**get_player_passing_stats_by_week**](docs/PlayerPassingStatisticsController.md#get_player_passing_stats_by_week) | **GET** /api/secured/stats/players-offense/passing/week | Get Player Passing Statistics by Week
*PlayerReceivingStatisticsController* | [**get_player_receiving_stats_by_season**](docs/PlayerReceivingStatisticsController.md#get_player_receiving_stats_by_season) | **GET** /api/secured/stats/players-offense/receiving/season | Get Player Receiving Statistics by Season
*PlayerReceivingStatisticsController* | [**get_player_receiving_stats_by_week**](docs/PlayerReceivingStatisticsController.md#get_player_receiving_stats_by_week) | **GET** /api/secured/stats/players-offense/receiving/week | Get Player Receiving Statistics by Week
*PlayerRushingStatisticsController* | [**get_player_rushing_stats_by_season**](docs/PlayerRushingStatisticsController.md#get_player_rushing_stats_by_season) | **GET** /api/secured/stats/players-offense/rushing/season | Get Player Rushing Statistics by Season
*PlayerRushingStatisticsController* | [**get_player_rushing_stats_by_week**](docs/PlayerRushingStatisticsController.md#get_player_rushing_stats_by_week) | **GET** /api/secured/stats/players-offense/rushing/week | Get Player Rushing Statistics by Week
*PlayerStatisticsController* | [**get_player_passing_stats_by_season**](docs/PlayerStatisticsController.md#get_player_passing_stats_by_season) | **GET** /api/secured/stats/players-offense/passing/season | Get Player Passing Statistics by Season
*PlayersController* | [**get_player**](docs/PlayersController.md#get_player) | **GET** /api/players/player | Get Player Details
*PlayersController* | [**get_projected_stats**](docs/PlayersController.md#get_projected_stats) | **GET** /api/players/projectedStats | Get Projected Player Statistics
*PlayersController* | [**search_players**](docs/PlayersController.md#search_players) | **GET** /api/players/search | Search Players
*PlaysController* | [**get_summary_play**](docs/PlaysController.md#get_summary_play) | **GET** /api/plays/summaryPlay | Get Play Summary
*SchedulesController* | [**get_game_matchup_rankings**](docs/SchedulesController.md#get_game_matchup_rankings) | **GET** /api/schedules/game/matchup/rankings | Get Game Matchup Rankings
*SchedulesController* | [**get_scheduled_game**](docs/SchedulesController.md#get_scheduled_game) | **GET** /api/schedules/game | Get Single Game Details
*SchedulesController* | [**get_scheduled_games**](docs/SchedulesController.md#get_scheduled_games) | **GET** /api/schedules/games | Get Games by Week
*SchedulesController* | [**get_team_injuries**](docs/SchedulesController.md#get_team_injuries) | **GET** /api/schedules/game/team/injuries | Get Team Injuries for Game Week
*SchedulesExtendedController* | [**get_current_week_games**](docs/SchedulesExtendedController.md#get_current_week_games) | **GET** /api/schedules/current | Get Current Week Games
*SchedulesExtendedController* | [**get_future_betting_odds**](docs/SchedulesExtendedController.md#get_future_betting_odds) | **GET** /api/schedules/genius/future/odds | Get Future Betting Odds
*SchedulesExtendedController* | [**get_team_standings**](docs/SchedulesExtendedController.md#get_team_standings) | **GET** /api/schedules/standings | Get Team Standings
*ScoresController* | [**get_live_game_scores**](docs/ScoresController.md#get_live_game_scores) | **GET** /api/scores/live/games | Get Live Game Scores
*SeasonScheduleController* | [**get_schedule_season_weeks**](docs/SeasonScheduleController.md#get_schedule_season_weeks) | **GET** /api/schedules/weeks | Get Season Weeks
*SecuredVideosController* | [**get_coaches_film_videos**](docs/SecuredVideosController.md#get_coaches_film_videos) | **GET** /api/secured/videos/coaches | Get Coaches Film Videos
*StatsController* | [**get_game_team_rankings**](docs/StatsController.md#get_game_team_rankings) | **GET** /api/stats/game/team-rankings | Get Team Rankings for Game
*StatsController* | [**get_gamecenter**](docs/StatsController.md#get_gamecenter) | **GET** /api/stats/gamecenter | Get Gamecenter Statistics
*StatsController* | [**get_multiple_rankings_all_teams**](docs/StatsController.md#get_multiple_rankings_all_teams) | **GET** /api/stats/multiple-rankings/all-teams | Get Multiple Rankings for All Teams
*StatsController* | [**get_stats_boxscore**](docs/StatsController.md#get_stats_boxscore) | **GET** /api/stats/boxscore | Get Game Boxscore (Stats API)
*TeamDefensePassStatisticsController* | [**get_team_defense_pass_stats_by_season**](docs/TeamDefensePassStatisticsController.md#get_team_defense_pass_stats_by_season) | **GET** /api/secured/stats/team-defense/pass/season | Get Team Defense Pass Statistics by Season
*TeamDefenseRushStatisticsController* | [**get_team_defense_rush_stats_by_season**](docs/TeamDefenseRushStatisticsController.md#get_team_defense_rush_stats_by_season) | **GET** /api/secured/stats/team-defense/rush/season | Get Team Defense Rush Statistics by Season
*TeamDefenseStatisticsController* | [**get_team_defense_stats_by_season**](docs/TeamDefenseStatisticsController.md#get_team_defense_stats_by_season) | **GET** /api/secured/stats/team-defense/overview/season | Get Team Defense Statistics by Season
*TeamOffenseOverviewStatisticsController* | [**get_team_offense_overview_stats_by_season**](docs/TeamOffenseOverviewStatisticsController.md#get_team_offense_overview_stats_by_season) | **GET** /api/secured/stats/team-offense/overview/season | Get Team Offense Overview Statistics by Season
*TeamOffensePassStatisticsController* | [**get_team_offense_pass_stats_by_season**](docs/TeamOffensePassStatisticsController.md#get_team_offense_pass_stats_by_season) | **GET** /api/secured/stats/team-offense/pass/season | Get Team Offense Pass Statistics by Season
*TeamsController* | [**get_all_teams**](docs/TeamsController.md#get_all_teams) | **GET** /api/teams/all | Get All Teams
*TeamsController* | [**get_team_roster**](docs/TeamsController.md#get_team_roster) | **GET** /api/teams/roster | Get Team Roster
*TeamsController* | [**get_team_schedule**](docs/TeamsController.md#get_team_schedule) | **GET** /api/teams/schedule | Get Team Schedule
*TeamsController* | [**get_weekly_team_roster**](docs/TeamsController.md#get_weekly_team_roster) | **GET** /api/teams/rosterWeek | Get Weekly Team Roster
*WinProbabilityController* | [**get_plays_win_probability**](docs/WinProbabilityController.md#get_plays_win_probability) | **GET** /api/secured/plays/winProbability | Get Game Win Probability by Plays
*WinProbabilityController* | [**get_win_probability_min**](docs/WinProbabilityController.md#get_win_probability_min) | **GET** /api/secured/plays/winProbabilityMin | Get Minimal Win Probability Data


## Documentation For Models

 - [AirYardTypeEnum](docs/AirYardTypeEnum.md)
 - [Award](docs/Award.md)
 - [BettingOddsFormat](docs/BettingOddsFormat.md)
 - [BettingOddsFormatAmericanOdds](docs/BettingOddsFormatAmericanOdds.md)
 - [BettingOddsFormatAmericanOddsExamplesInner](docs/BettingOddsFormatAmericanOddsExamplesInner.md)
 - [BettingOddsFormatDecimalOdds](docs/BettingOddsFormatDecimalOdds.md)
 - [BettingOddsFormatFractionalOdds](docs/BettingOddsFormatFractionalOdds.md)
 - [BinaryFlagEnum](docs/BinaryFlagEnum.md)
 - [BoxScorePlayerExtraPointsStatistic](docs/BoxScorePlayerExtraPointsStatistic.md)
 - [BoxScorePlayerFieldGoalsStatistic](docs/BoxScorePlayerFieldGoalsStatistic.md)
 - [BoxScorePlayerFumblesStatistic](docs/BoxScorePlayerFumblesStatistic.md)
 - [BoxScorePlayerKickReturnStatistic](docs/BoxScorePlayerKickReturnStatistic.md)
 - [BoxScorePlayerKickingStatistic](docs/BoxScorePlayerKickingStatistic.md)
 - [BoxScorePlayerPassingStatistic](docs/BoxScorePlayerPassingStatistic.md)
 - [BoxScorePlayerPuntReturnStatistic](docs/BoxScorePlayerPuntReturnStatistic.md)
 - [BoxScorePlayerPuntingStatistic](docs/BoxScorePlayerPuntingStatistic.md)
 - [BoxScorePlayerReceivingStatistic](docs/BoxScorePlayerReceivingStatistic.md)
 - [BoxScorePlayerRushingStatistic](docs/BoxScorePlayerRushingStatistic.md)
 - [BoxScorePlayerTacklesStatistic](docs/BoxScorePlayerTacklesStatistic.md)
 - [BoxScoreResponse](docs/BoxScoreResponse.md)
 - [BoxScoreResponsePlayerStats](docs/BoxScoreResponsePlayerStats.md)
 - [BoxScoreResponsePlayerStatsAway](docs/BoxScoreResponsePlayerStatsAway.md)
 - [BoxScoreResponseTeamStats](docs/BoxScoreResponseTeamStats.md)
 - [BoxscoreSchedule](docs/BoxscoreSchedule.md)
 - [BoxscoreScore](docs/BoxscoreScore.md)
 - [BoxscoreTeam](docs/BoxscoreTeam.md)
 - [BroadcastInfo](docs/BroadcastInfo.md)
 - [BroadcastInfoInternationalWatchOptionsInner](docs/BroadcastInfoInternationalWatchOptionsInner.md)
 - [BroadcastInfoStreamingNetworksInner](docs/BroadcastInfoStreamingNetworksInner.md)
 - [CalculationMethodEnum](docs/CalculationMethodEnum.md)
 - [CameraSourceEnum](docs/CameraSourceEnum.md)
 - [CareerStats](docs/CareerStats.md)
 - [Clinched](docs/Clinched.md)
 - [CoachesFileVideoSubTypeEnum](docs/CoachesFileVideoSubTypeEnum.md)
 - [CoachesFilmResponse](docs/CoachesFilmResponse.md)
 - [CoachesFilmVideo](docs/CoachesFilmVideo.md)
 - [Conference](docs/Conference.md)
 - [ConferenceEnum](docs/ConferenceEnum.md)
 - [ContentTagEnum](docs/ContentTagEnum.md)
 - [ContractInfo](docs/ContractInfo.md)
 - [CoverageMetrics](docs/CoverageMetrics.md)
 - [CoverageMetricsCompletionRateOverExpected](docs/CoverageMetricsCompletionRateOverExpected.md)
 - [CoverageMetricsCoverageSnaps](docs/CoverageMetricsCoverageSnaps.md)
 - [CoverageMetricsReceiverSeparation](docs/CoverageMetricsReceiverSeparation.md)
 - [CoverageMetricsTargetsAllowed](docs/CoverageMetricsTargetsAllowed.md)
 - [CurrentGame](docs/CurrentGame.md)
 - [CurrentGamesResponse](docs/CurrentGamesResponse.md)
 - [DataTypeEnum](docs/DataTypeEnum.md)
 - [DefenseFieldPositionEnum](docs/DefenseFieldPositionEnum.md)
 - [DefenseGameSituationEnum](docs/DefenseGameSituationEnum.md)
 - [DefensiveMetricsExplanation](docs/DefensiveMetricsExplanation.md)
 - [DefensiveMetricsExplanationEpa](docs/DefensiveMetricsExplanationEpa.md)
 - [DefensiveMetricsExplanationQbpPct](docs/DefensiveMetricsExplanationQbpPct.md)
 - [DefensiveMetricsExplanationRyoe](docs/DefensiveMetricsExplanationRyoe.md)
 - [DefensiveOverviewMetricsExplanation](docs/DefensiveOverviewMetricsExplanation.md)
 - [DefensiveOverviewMetricsExplanationHardStops](docs/DefensiveOverviewMetricsExplanationHardStops.md)
 - [DefensiveOverviewMetricsExplanationPressureRate](docs/DefensiveOverviewMetricsExplanationPressureRate.md)
 - [DefensiveOverviewMetricsExplanationTackleStops](docs/DefensiveOverviewMetricsExplanationTackleStops.md)
 - [DefensiveOverviewStatsResponse](docs/DefensiveOverviewStatsResponse.md)
 - [DefensivePassMetricsExplanation](docs/DefensivePassMetricsExplanation.md)
 - [DefensivePassMetricsExplanationEpaPass](docs/DefensivePassMetricsExplanationEpaPass.md)
 - [DefensivePassMetricsExplanationReceiverSeparation](docs/DefensivePassMetricsExplanationReceiverSeparation.md)
 - [DefensivePassMetricsExplanationYacoe](docs/DefensivePassMetricsExplanationYacoe.md)
 - [DefensivePassRushStats](docs/DefensivePassRushStats.md)
 - [DefensivePlayerOverviewStats](docs/DefensivePlayerOverviewStats.md)
 - [DefensivePlayerStats](docs/DefensivePlayerStats.md)
 - [DefensivePositionEnum](docs/DefensivePositionEnum.md)
 - [DefensivePositionGroupEnum](docs/DefensivePositionGroupEnum.md)
 - [DefensiveRushMetricsExplanation](docs/DefensiveRushMetricsExplanation.md)
 - [DefensiveRushMetricsExplanationBoxCount](docs/DefensiveRushMetricsExplanationBoxCount.md)
 - [DefensiveRushMetricsExplanationRyoe](docs/DefensiveRushMetricsExplanationRyoe.md)
 - [DefensiveRushMetricsExplanationStuffRate](docs/DefensiveRushMetricsExplanationStuffRate.md)
 - [DefensiveRushMetricsExplanationYardsBeforeContact](docs/DefensiveRushMetricsExplanationYardsBeforeContact.md)
 - [DefensiveSituationTypeEnum](docs/DefensiveSituationTypeEnum.md)
 - [DefensiveSplitCategory](docs/DefensiveSplitCategory.md)
 - [DefensiveStatCategory](docs/DefensiveStatCategory.md)
 - [DefensiveStats](docs/DefensiveStats.md)
 - [DefensiveStatsResponse](docs/DefensiveStatsResponse.md)
 - [DeviceInfo](docs/DeviceInfo.md)
 - [Division](docs/Division.md)
 - [DraftInfo](docs/DraftInfo.md)
 - [DraftPick](docs/DraftPick.md)
 - [DraftResponse](docs/DraftResponse.md)
 - [DraftResponseRoundsInner](docs/DraftResponseRoundsInner.md)
 - [Drive](docs/Drive.md)
 - [DriveResultEnum](docs/DriveResultEnum.md)
 - [ExperienceGamesResponse](docs/ExperienceGamesResponse.md)
 - [ExperienceTeamsResponse](docs/ExperienceTeamsResponse.md)
 - [ExternalId](docs/ExternalId.md)
 - [FantasyPlayerPositionEnum](docs/FantasyPlayerPositionEnum.md)
 - [FantasyPlayerStats](docs/FantasyPlayerStats.md)
 - [FantasyPositionGroupEnum](docs/FantasyPositionGroupEnum.md)
 - [FantasyStatsResponse](docs/FantasyStatsResponse.md)
 - [FantayScoringExplanation](docs/FantayScoringExplanation.md)
 - [FantayScoringExplanationHalfPprScoring](docs/FantayScoringExplanationHalfPprScoring.md)
 - [FantayScoringExplanationPprScoring](docs/FantayScoringExplanationPprScoring.md)
 - [FantayScoringExplanationStandardScoring](docs/FantayScoringExplanationStandardScoring.md)
 - [FilmCard](docs/FilmCard.md)
 - [FilmCardLinkParams](docs/FilmCardLinkParams.md)
 - [FilmroomPlay](docs/FilmroomPlay.md)
 - [FilmroomPlaysResponse](docs/FilmroomPlaysResponse.md)
 - [FootballGamesResponse](docs/FootballGamesResponse.md)
 - [FormationEnum](docs/FormationEnum.md)
 - [FuturesMarket](docs/FuturesMarket.md)
 - [FuturesOddsResponse](docs/FuturesOddsResponse.md)
 - [FuturesOddsResponseData](docs/FuturesOddsResponseData.md)
 - [Game](docs/Game.md)
 - [GameDetail](docs/GameDetail.md)
 - [GameInsight](docs/GameInsight.md)
 - [GameOdds](docs/GameOdds.md)
 - [GamePhaseEnum](docs/GamePhaseEnum.md)
 - [GamePreviewResponse](docs/GamePreviewResponse.md)
 - [GameQuarterEnum](docs/GameQuarterEnum.md)
 - [GameResultEnum](docs/GameResultEnum.md)
 - [GameSchedule](docs/GameSchedule.md)
 - [GameScore](docs/GameScore.md)
 - [GameSituation](docs/GameSituation.md)
 - [GameStatsResponse](docs/GameStatsResponse.md)
 - [GameStatusEnum](docs/GameStatusEnum.md)
 - [GameSummaryTeam](docs/GameSummaryTeam.md)
 - [GameSummaryTeamScore](docs/GameSummaryTeamScore.md)
 - [GameSummaryTeamTimeouts](docs/GameSummaryTeamTimeouts.md)
 - [GameTeam](docs/GameTeam.md)
 - [GameTeamScore](docs/GameTeamScore.md)
 - [GamecenterResponse](docs/GamecenterResponse.md)
 - [GamecenterResponseLeaders](docs/GamecenterResponseLeaders.md)
 - [GamecenterResponseLeadersPassDistanceLeaders](docs/GamecenterResponseLeadersPassDistanceLeaders.md)
 - [GamecenterResponseLeadersSpeedLeaders](docs/GamecenterResponseLeadersSpeedLeaders.md)
 - [GamecenterResponseLeadersTimeToSackLeaders](docs/GamecenterResponseLeadersTimeToSackLeaders.md)
 - [GamecenterResponsePassRushers](docs/GamecenterResponsePassRushers.md)
 - [GamecenterResponsePassRushersLeagueAverageSeparationToQb](docs/GamecenterResponsePassRushersLeagueAverageSeparationToQb.md)
 - [GamecenterResponsePassers](docs/GamecenterResponsePassers.md)
 - [GamecenterResponseReceivers](docs/GamecenterResponseReceivers.md)
 - [GamecenterResponseReceiversLeagueAverageReceiverSeparation](docs/GamecenterResponseReceiversLeagueAverageReceiverSeparation.md)
 - [GamecenterResponseRushers](docs/GamecenterResponseRushers.md)
 - [GamecenterSchedule](docs/GamecenterSchedule.md)
 - [GamesResponse](docs/GamesResponse.md)
 - [GetPlaysWinProbability200Response](docs/GetPlaysWinProbability200Response.md)
 - [GetPlaysWinProbabilityGameIdParameter](docs/GetPlaysWinProbabilityGameIdParameter.md)
 - [HomeFilmCardsResponse](docs/HomeFilmCardsResponse.md)
 - [InjuredPlayerGameStatusEnum](docs/InjuredPlayerGameStatusEnum.md)
 - [InjuryEntry](docs/InjuryEntry.md)
 - [InjuryEntryPracticeStatus](docs/InjuryEntryPracticeStatus.md)
 - [InjuryReportResponse](docs/InjuryReportResponse.md)
 - [Insight](docs/Insight.md)
 - [InsightContentExplanation](docs/InsightContentExplanation.md)
 - [InsightContentExplanationEvergreenContent](docs/InsightContentExplanationEvergreenContent.md)
 - [InsightContentExplanationFantasyInsights](docs/InsightContentExplanationFantasyInsights.md)
 - [InsightContentExplanationPostgameInsights](docs/InsightContentExplanationPostgameInsights.md)
 - [InsightContentExplanationPregameInsights](docs/InsightContentExplanationPregameInsights.md)
 - [KickingStats](docs/KickingStats.md)
 - [LeaderEntryBaseSchema](docs/LeaderEntryBaseSchema.md)
 - [LineOfScrimmageDistanceEnum](docs/LineOfScrimmageDistanceEnum.md)
 - [LiveGame](docs/LiveGame.md)
 - [LiveGameAwayTeam](docs/LiveGameAwayTeam.md)
 - [LiveGameSummaryData](docs/LiveGameSummaryData.md)
 - [LiveScoresResponse](docs/LiveScoresResponse.md)
 - [MatchupRankingsResponse](docs/MatchupRankingsResponse.md)
 - [MeridiemEnum](docs/MeridiemEnum.md)
 - [MoneyLine](docs/MoneyLine.md)
 - [MultipleRankingsCategory](docs/MultipleRankingsCategory.md)
 - [MultipleRankingsCategoryPagination](docs/MultipleRankingsCategoryPagination.md)
 - [NetworkTypeEnum](docs/NetworkTypeEnum.md)
 - [NextGenStatsPositionEnum](docs/NextGenStatsPositionEnum.md)
 - [NextGenStatsPositionGroupEnum](docs/NextGenStatsPositionGroupEnum.md)
 - [OddsSelection](docs/OddsSelection.md)
 - [OffenseFieldPositionEnum](docs/OffenseFieldPositionEnum.md)
 - [OffenseGameSituationEnum](docs/OffenseGameSituationEnum.md)
 - [OffensiveFormationEnum](docs/OffensiveFormationEnum.md)
 - [OffensiveMetricsExplanation](docs/OffensiveMetricsExplanation.md)
 - [OffensiveMetricsExplanationEpa](docs/OffensiveMetricsExplanationEpa.md)
 - [OffensiveMetricsExplanationRedZoneEfficiency](docs/OffensiveMetricsExplanationRedZoneEfficiency.md)
 - [OffensiveMetricsExplanationThirdDownConversion](docs/OffensiveMetricsExplanationThirdDownConversion.md)
 - [OffensivePlayerPositionEnum](docs/OffensivePlayerPositionEnum.md)
 - [OffensiveSituationTypeEnum](docs/OffensiveSituationTypeEnum.md)
 - [OffensiveSkillPositionEnum](docs/OffensiveSkillPositionEnum.md)
 - [OffensiveSplitCategory](docs/OffensiveSplitCategory.md)
 - [OverallRecord](docs/OverallRecord.md)
 - [OverallRecordAllOfStreak](docs/OverallRecordAllOfStreak.md)
 - [Pagination](docs/Pagination.md)
 - [ParticipantPlayerInfo](docs/ParticipantPlayerInfo.md)
 - [PassDistanceLeaderEntry](docs/PassDistanceLeaderEntry.md)
 - [PassRushMetricsExplanation](docs/PassRushMetricsExplanation.md)
 - [PassRushMetricsExplanationPassRushRating](docs/PassRushMetricsExplanationPassRushRating.md)
 - [PassRushMetricsExplanationTimeToSack](docs/PassRushMetricsExplanationTimeToSack.md)
 - [PassRushStatsResponse](docs/PassRushStatsResponse.md)
 - [PassRusherStats](docs/PassRusherStats.md)
 - [PasserStats](docs/PasserStats.md)
 - [PassingSectionEnum](docs/PassingSectionEnum.md)
 - [PassingStats](docs/PassingStats.md)
 - [PassingStatsCategoryEnum](docs/PassingStatsCategoryEnum.md)
 - [PassingStatsResponse](docs/PassingStatsResponse.md)
 - [PassingZone](docs/PassingZone.md)
 - [PassingZoneStats](docs/PassingZoneStats.md)
 - [Penalty](docs/Penalty.md)
 - [PersonnelEnum](docs/PersonnelEnum.md)
 - [PersonnelPackageEnum](docs/PersonnelPackageEnum.md)
 - [Play](docs/Play.md)
 - [PlayByPlayResponse](docs/PlayByPlayResponse.md)
 - [PlayDetail](docs/PlayDetail.md)
 - [PlayDirectionEnum](docs/PlayDirectionEnum.md)
 - [PlayParticipant](docs/PlayParticipant.md)
 - [PlayParticipantRoleEnum](docs/PlayParticipantRoleEnum.md)
 - [PlayStat](docs/PlayStat.md)
 - [PlayStateEnum](docs/PlayStateEnum.md)
 - [PlaySummaryResponse](docs/PlaySummaryResponse.md)
 - [PlayTypeEnum](docs/PlayTypeEnum.md)
 - [PlayWinProbability](docs/PlayWinProbability.md)
 - [Player](docs/Player.md)
 - [PlayerDetail](docs/PlayerDetail.md)
 - [PlayerGameStats](docs/PlayerGameStats.md)
 - [PlayerPassingStats](docs/PlayerPassingStats.md)
 - [PlayerProjection](docs/PlayerProjection.md)
 - [PlayerProjectionRelationships](docs/PlayerProjectionRelationships.md)
 - [PlayerProjectionRelationshipsWeekPointsInner](docs/PlayerProjectionRelationshipsWeekPointsInner.md)
 - [PlayerProjectionRelationshipsWeekStatsInner](docs/PlayerProjectionRelationshipsWeekStatsInner.md)
 - [PlayerReceivingStats](docs/PlayerReceivingStats.md)
 - [PlayerRushingStats](docs/PlayerRushingStats.md)
 - [PlayerSearchResponse](docs/PlayerSearchResponse.md)
 - [PlayerSearchResult](docs/PlayerSearchResult.md)
 - [PlayerStatisticBaseSchema](docs/PlayerStatisticBaseSchema.md)
 - [PlayerStatsResponse](docs/PlayerStatsResponse.md)
 - [PlayerStatsResponsePagination](docs/PlayerStatsResponsePagination.md)
 - [PlayerStatsResponsePlayersInner](docs/PlayerStatsResponsePlayersInner.md)
 - [PlayerWeekProjectedPoints](docs/PlayerWeekProjectedPoints.md)
 - [PlayerWeekProjectedPointsAttributes](docs/PlayerWeekProjectedPointsAttributes.md)
 - [PlayerWeekProjectedStats](docs/PlayerWeekProjectedStats.md)
 - [PlayerWeekProjectedStatsAttributes](docs/PlayerWeekProjectedStatsAttributes.md)
 - [PointSpread](docs/PointSpread.md)
 - [PointsRecord](docs/PointsRecord.md)
 - [PointsRecordAllOfPoints](docs/PointsRecordAllOfPoints.md)
 - [PositionGroupEnum](docs/PositionGroupEnum.md)
 - [PracticeStatusEnum](docs/PracticeStatusEnum.md)
 - [PrimetimeGameCategoryEnum](docs/PrimetimeGameCategoryEnum.md)
 - [ProInjuryReportResponse](docs/ProInjuryReportResponse.md)
 - [ProInjuryReportResponsePagination](docs/ProInjuryReportResponsePagination.md)
 - [ProTeam](docs/ProTeam.md)
 - [ProjectedStatsResponse](docs/ProjectedStatsResponse.md)
 - [ProjectedStatsResponseIncludedInner](docs/ProjectedStatsResponseIncludedInner.md)
 - [ProjectedStatsResponseMeta](docs/ProjectedStatsResponseMeta.md)
 - [ProjectedStatsResponseMetaPage](docs/ProjectedStatsResponseMetaPage.md)
 - [ProjectedStatsResponsePagination](docs/ProjectedStatsResponsePagination.md)
 - [QBAlignmentEnum](docs/QBAlignmentEnum.md)
 - [QualifiedDefenderCriteria](docs/QualifiedDefenderCriteria.md)
 - [QualifiedPasserCriteria](docs/QualifiedPasserCriteria.md)
 - [ReceiverStats](docs/ReceiverStats.md)
 - [ReceiverStatsAllOfReceptionInfo](docs/ReceiverStatsAllOfReceptionInfo.md)
 - [ReceivingMetricsExplanation](docs/ReceivingMetricsExplanation.md)
 - [ReceivingMetricsExplanationCatchRateOverExpected](docs/ReceivingMetricsExplanationCatchRateOverExpected.md)
 - [ReceivingMetricsExplanationReceiverSeparation](docs/ReceivingMetricsExplanationReceiverSeparation.md)
 - [ReceivingMetricsExplanationYardsAfterCatchOverExpected](docs/ReceivingMetricsExplanationYardsAfterCatchOverExpected.md)
 - [ReceivingStats](docs/ReceivingStats.md)
 - [ReceivingStatsCategoryEnum](docs/ReceivingStatsCategoryEnum.md)
 - [ReceivingStatsResponse](docs/ReceivingStatsResponse.md)
 - [Record](docs/Record.md)
 - [RefreshTokenRequest](docs/RefreshTokenRequest.md)
 - [Replay](docs/Replay.md)
 - [ReplayIds](docs/ReplayIds.md)
 - [ReplayTagsInner](docs/ReplayTagsInner.md)
 - [ReplayThumbnail](docs/ReplayThumbnail.md)
 - [ResponseMetadata](docs/ResponseMetadata.md)
 - [RoofTypeEnum](docs/RoofTypeEnum.md)
 - [RosterResponse](docs/RosterResponse.md)
 - [RosterResponseRoster](docs/RosterResponseRoster.md)
 - [RushLocationMapEntry](docs/RushLocationMapEntry.md)
 - [RusherStats](docs/RusherStats.md)
 - [RushingInfo](docs/RushingInfo.md)
 - [RushingMap](docs/RushingMap.md)
 - [RushingStats](docs/RushingStats.md)
 - [RushingStatsResponse](docs/RushingStatsResponse.md)
 - [ScheduledGame](docs/ScheduledGame.md)
 - [ScoreTypeEnum](docs/ScoreTypeEnum.md)
 - [ScoringPlay](docs/ScoringPlay.md)
 - [SeasonStats](docs/SeasonStats.md)
 - [SeasonTypeEnum](docs/SeasonTypeEnum.md)
 - [SeasonWeeksResponse](docs/SeasonWeeksResponse.md)
 - [Site](docs/Site.md)
 - [SocialMedia](docs/SocialMedia.md)
 - [SortOrderEnum](docs/SortOrderEnum.md)
 - [SpeedLeaderEntry](docs/SpeedLeaderEntry.md)
 - [Standings](docs/Standings.md)
 - [StandingsRecord](docs/StandingsRecord.md)
 - [StandingsRecordAllOfPoints](docs/StandingsRecordAllOfPoints.md)
 - [StandingsResponse](docs/StandingsResponse.md)
 - [StandingsResponseWeeksInner](docs/StandingsResponseWeeksInner.md)
 - [StandingsTeam](docs/StandingsTeam.md)
 - [StatisticRanking](docs/StatisticRanking.md)
 - [StatisticRankingStatistic](docs/StatisticRankingStatistic.md)
 - [StatisticalCategory](docs/StatisticalCategory.md)
 - [StatsQueryMetadata](docs/StatsQueryMetadata.md)
 - [SuccessLevelEnum](docs/SuccessLevelEnum.md)
 - [Summary](docs/Summary.md)
 - [TargetLocationEnum](docs/TargetLocationEnum.md)
 - [Team](docs/Team.md)
 - [TeamBoxScore](docs/TeamBoxScore.md)
 - [TeamBoxscore](docs/TeamBoxscore.md)
 - [TeamDefensePassStats](docs/TeamDefensePassStats.md)
 - [TeamDefensePassStatsResponse](docs/TeamDefensePassStatsResponse.md)
 - [TeamDefenseRushStats](docs/TeamDefenseRushStats.md)
 - [TeamDefenseRushStatsResponse](docs/TeamDefenseRushStatsResponse.md)
 - [TeamDefenseStats](docs/TeamDefenseStats.md)
 - [TeamDefenseStatsResponse](docs/TeamDefenseStatsResponse.md)
 - [TeamGameStats](docs/TeamGameStats.md)
 - [TeamInfo](docs/TeamInfo.md)
 - [TeamInjuryReport](docs/TeamInjuryReport.md)
 - [TeamMatchupRankings](docs/TeamMatchupRankings.md)
 - [TeamOffenseOverviewStats](docs/TeamOffenseOverviewStats.md)
 - [TeamOffenseOverviewStatsResponse](docs/TeamOffenseOverviewStatsResponse.md)
 - [TeamOffensePassStats](docs/TeamOffensePassStats.md)
 - [TeamOffensePassStatsResponse](docs/TeamOffensePassStatsResponse.md)
 - [TeamRankingEntry](docs/TeamRankingEntry.md)
 - [TeamRankings](docs/TeamRankings.md)
 - [TeamRankingsResponse](docs/TeamRankingsResponse.md)
 - [TeamRosterResponse](docs/TeamRosterResponse.md)
 - [TeamScore](docs/TeamScore.md)
 - [TeamTypeEnum](docs/TeamTypeEnum.md)
 - [TicketVendor](docs/TicketVendor.md)
 - [TimeToSackLeaderEntry](docs/TimeToSackLeaderEntry.md)
 - [TokenRequest](docs/TokenRequest.md)
 - [TokenResponse](docs/TokenResponse.md)
 - [Totals](docs/Totals.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionTypeEnum](docs/TransactionTypeEnum.md)
 - [TransactionsResponse](docs/TransactionsResponse.md)
 - [Venue](docs/Venue.md)
 - [VenueInfo](docs/VenueInfo.md)
 - [VenuesResponse](docs/VenuesResponse.md)
 - [VideoAuthorizations](docs/VideoAuthorizations.md)
 - [VideoAuthorizationsNflPlusPlusInner](docs/VideoAuthorizationsNflPlusPlusInner.md)
 - [VideoAuthorizationsNflPlusPlusInnerNFLPLUSCOACHESFILM](docs/VideoAuthorizationsNflPlusPlusInnerNFLPLUSCOACHESFILM.md)
 - [VideoAuthorizationsNflPlusPlusInnerNFLPLUSCOACHESFILMRequirements](docs/VideoAuthorizationsNflPlusPlusInnerNFLPLUSCOACHESFILMRequirements.md)
 - [VideoGamePlayIds](docs/VideoGamePlayIds.md)
 - [VideoTag](docs/VideoTag.md)
 - [VideoThumbnail](docs/VideoThumbnail.md)
 - [Week](docs/Week.md)
 - [WeekSlugEnum](docs/WeekSlugEnum.md)
 - [WeekTypeEnum](docs/WeekTypeEnum.md)
 - [WeeklyGameDetail](docs/WeeklyGameDetail.md)
 - [WeeklyGameDetailSummaryScore](docs/WeeklyGameDetailSummaryScore.md)
 - [WeeklyGameDetailSummaryTeam](docs/WeeklyGameDetailSummaryTeam.md)
 - [WeeklyGameDetailSummaryTimeouts](docs/WeeklyGameDetailSummaryTimeouts.md)
 - [WeeklyOddsResponse](docs/WeeklyOddsResponse.md)
 - [WeeklyPassingStatsResponse](docs/WeeklyPassingStatsResponse.md)
 - [WeeklyPlayer](docs/WeeklyPlayer.md)
 - [WeeklyPlayerPassingStats](docs/WeeklyPlayerPassingStats.md)
 - [WeeklyPlayerRushingStats](docs/WeeklyPlayerRushingStats.md)
 - [WeeklyRosterResponse](docs/WeeklyRosterResponse.md)
 - [WeeklyRushingStatsResponse](docs/WeeklyRushingStatsResponse.md)
 - [WeeksResponse](docs/WeeksResponse.md)
 - [WinProbabilityMetadata](docs/WinProbabilityMetadata.md)
 - [WinProbabilityMetrics](docs/WinProbabilityMetrics.md)
 - [WinProbabilityResponse](docs/WinProbabilityResponse.md)
 - [WinProbabilityTrend](docs/WinProbabilityTrend.md)
 - [WinProbabilityTrendBiggestSwing](docs/WinProbabilityTrendBiggestSwing.md)
 - [WinProbabilityTrendFinalProbability](docs/WinProbabilityTrendFinalProbability.md)
 - [YardsToGoTypeEnum](docs/YardsToGoTypeEnum.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="NFLAuth"></a>
### NFLAuth

- **Type**: Bearer authentication


## Author

john@thistlegrow.software


