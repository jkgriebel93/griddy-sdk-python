import builtins
from typing import TYPE_CHECKING

from griddy.core._import import dynamic_import

if TYPE_CHECKING:
    from griddy.nfl.models.entities.combine_events import (
        BenchPress,
        BroadJump,
        FortyYardDash,
        TenYardSplit,
        ThreeConeDrill,
        TwentyYardShuffle,
        VerticalJump,
    )
    from griddy.nfl.models.entities.combine_profile import (
        CombinePerson,
        CombineProfile,
    )
    from griddy.nfl.models.entities.draft_day import DraftDay
    from griddy.nfl.models.entities.football_roster import (
        FootballRoster,
    )
    from griddy.nfl.models.entities.ngs_content import (
        NgsChart,
        NgsChartPlayer,
        NgsHighlight,
    )
    from griddy.nfl.models.entities.ngs_game_overview import (
        NgsGameLeaders,
        NgsGamePassDistanceLeader,
        NgsGameSackLeader,
        NgsGameScheduleInfo,
        NgsGameSpeedLeader,
        NgsLeagueAverage,
        NgsPassDistanceLeadersMap,
        NgsPasserInfo,
        NgsPassersOverview,
        NgsPassInfo,
        NgsPassingZone,
        NgsPassRusherInfo,
        NgsPassRushersOverview,
        NgsReceiverInfo,
        NgsReceiversOverview,
        NgsReceptionInfo,
        NgsRusherInfo,
        NgsRushersOverview,
        NgsRushInfo,
        NgsRushLocationStats,
        NgsSackLeadersMap,
        NgsSpeedLeadersMap,
        NgsTackleInfo,
    )
    from griddy.nfl.models.entities.ngs_leaders import (
        NgsCompletionLeader,
        NgsCompletionLeaderEntry,
        NgsDistanceLeader,
        NgsDistanceLeaderEntry,
        NgsERYLeader,
        NgsERYLeaderEntry,
        NgsSackLeader,
        NgsSackLeaderEntry,
        NgsSpeedLeader,
        NgsSpeedLeaderEntry,
        NgsTackleLeader,
        NgsTackleLeaderEntry,
        NgsYACLeader,
        NgsYACLeaderEntry,
    )
    from griddy.nfl.models.entities.ngs_news import (
        NgsContentItem,
        NgsContentMetadata,
        NgsContentPagination,
        NgsContentTag,
        NgsThumbnail,
    )
    from griddy.nfl.models.entities.ngs_play import (
        NgsPlay,
        NgsPlayStat,
    )
    from griddy.nfl.models.entities.ngs_stats import (
        NgsPassingStat,
        NgsReceivingStat,
        NgsRushingStat,
    )
    from griddy.nfl.models.entities.person import Person
    from griddy.nfl.models.entities.team_offense_rush_stats import (
        TeamOffenseRushStats,
    )
    from griddy.nfl.models.enums.binary_flag_enum import BinaryFlagEnum
    from griddy.nfl.models.enums.combine_enums import (
        CollegeClassEnum,
        DesignationEnum,
        EventFilterEnum,
    )
    from griddy.nfl.models.enums.conference_enum import ConferenceEnum
    from griddy.nfl.models.enums.defensive_position_group_enum import (
        DefensivePositionGroupEnum,
    )
    from griddy.nfl.models.enums.game_phase_enum import GamePhaseEnum
    from griddy.nfl.models.enums.game_result_enum import GameResultEnum
    from griddy.nfl.models.enums.game_status_enum import GameStatusEnum
    from griddy.nfl.models.enums.meridiem_enum import MeridiemEnum
    from griddy.nfl.models.enums.offensive_player_position_enum import (
        OffensivePlayerPositionEnum,
    )
    from griddy.nfl.models.enums.offensive_skill_position_enum import (
        OffensiveSkillPositionEnum,
    )
    from griddy.nfl.models.enums.passing_stats_category_enum import (
        PassingStatsCategoryEnum,
    )
    from griddy.nfl.models.enums.play_type_enum import PlayTypeEnum
    from griddy.nfl.models.enums.practice_status_enum import PracticeStatusEnum
    from griddy.nfl.models.enums.receiving_stats_category_enum import (
        ReceivingStatsCategoryEnum,
    )
    from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum
    from griddy.nfl.models.enums.site_roof_type_enum import SiteRoofTypeEnum
    from griddy.nfl.models.enums.sort_order_enum import SortOrderEnum
    from griddy.nfl.models.enums.team_type_enum import TeamTypeEnum
    from griddy.nfl.models.enums.week_slug_enum import WeekSlugEnum
    from griddy.nfl.models.requests.get_coaches_film_videos_op import (
        GetCoachesFilmVideosRequest,
    )
    from griddy.nfl.models.requests.get_combine_profiles_op import (
        GetCombineProfilesRequest,
    )
    from griddy.nfl.models.requests.get_combine_rankings_op import (
        GetCombineRankingsRequest,
    )
    from griddy.nfl.models.requests.get_defensive_nearest_defender_stats_by_season_op import (
        GetDefensiveNearestDefenderStatsBySeasonRequest,
        GetDefensiveNearestDefenderStatsBySeasonSortKey,
    )
    from griddy.nfl.models.requests.get_defensive_nearest_defender_stats_by_week_op import (
        GetDefensiveNearestDefenderStatsByWeekRequest,
        GetDefensiveNearestDefenderStatsByWeekSortKey,
    )
    from griddy.nfl.models.requests.get_defensive_overview_stats_by_season_op import (
        GetDefensiveOverviewStatsBySeasonRequest,
        GetDefensiveOverviewStatsBySeasonSortKey,
    )
    from griddy.nfl.models.requests.get_defensive_overview_stats_by_week_op import (
        GetDefensiveOverviewStatsByWeekRequest,
        GetDefensiveOverviewStatsByWeekSortKey,
    )
    from griddy.nfl.models.requests.get_defensive_passrush_stats_by_season_op import (
        GetDefensivePassRushStatsBySeasonRequest,
        GetDefensivePassRushStatsBySeasonSortKey,
    )
    from griddy.nfl.models.requests.get_defensive_passrush_stats_by_week_op import (
        GetDefensivePassRushStatsByWeekRequest,
        GetDefensivePassRushStatsByWeekSortKey,
    )
    from griddy.nfl.models.requests.get_defensive_stats_by_season_op import (
        GetDefensiveStatsBySeasonRequest,
        GetDefensiveStatsBySeasonSortKey,
    )
    from griddy.nfl.models.requests.get_draft_info_op import (
        GetDraftInfoRequest,
    )
    from griddy.nfl.models.requests.get_draft_picks_report_op import (
        GetDraftPicksReportRequest,
    )
    from griddy.nfl.models.requests.get_fantasy_stats_by_season_op import (
        GetFantasyStatsBySeasonPositionGroup,
        GetFantasyStatsBySeasonRequest,
        GetFantasyStatsBySeasonSortKey,
    )
    from griddy.nfl.models.requests.get_film_room_plays_op import (
        AirYardType,
        DefCoverageType,
        DefendersInTheBoxType,
        DropbackTimeType,
        GetFilmroomPlaysRequest,
        Personnel,
        QbAlignment,
        ReceiverAlignment,
        RushDirection,
        SeparationType,
        TargetLocation,
        YardsToGoType,
    )
    from griddy.nfl.models.requests.get_football_boxscore_op import (
        GetFootballBoxScoreRequest,
    )
    from griddy.nfl.models.requests.get_football_games_op import (
        GetFootballGamesRequest,
    )
    from griddy.nfl.models.requests.get_football_rosters_op import (
        GetFootballRostersRequest,
    )
    from griddy.nfl.models.requests.get_football_teams_op import (
        GetFootballTeamsRequest,
    )
    from griddy.nfl.models.requests.get_game_center_op import (
        GetGamecenterRequest,
    )
    from griddy.nfl.models.requests.get_game_insights_op import (
        GetGameInsightsRequest,
    )
    from griddy.nfl.models.requests.get_game_matchup_rankings_op import (
        GetGameMatchupRankingsRequest,
    )
    from griddy.nfl.models.requests.get_game_preview_op import (
        GetGamePreviewRequest,
    )
    from griddy.nfl.models.requests.get_game_team_rankings_op import (
        GetGameTeamRankingsRequest,
    )
    from griddy.nfl.models.requests.get_injury_reports_op import (
        GetInjuryReportsRequest,
    )
    from griddy.nfl.models.requests.get_live_game_scores_op import (
        GetLiveGameScoresRequest,
    )
    from griddy.nfl.models.requests.get_live_game_stats_op import (
        GetLiveGameStatsRequest,
    )
    from griddy.nfl.models.requests.get_multiple_rankings_all_teams_op import (
        GetMultipleRankingsAllTeamsRequest,
    )
    from griddy.nfl.models.requests.get_ngs_content_op import (
        GetNgsChartsRequest,
        GetNgsHighlightsRequest,
    )
    from griddy.nfl.models.requests.get_ngs_current_schedule_op import (
        GetNgsCurrentScheduleRequest,
    )
    from griddy.nfl.models.requests.get_ngs_game_overview_op import (
        GetNgsGameOverviewRequest,
    )
    from griddy.nfl.models.requests.get_ngs_leaders_op import (
        GetNgsLeadersRequest,
        GetNgsSeasonLeadersRequest,
    )
    from griddy.nfl.models.requests.get_ngs_live_scores_op import (
        GetNgsLiveScoresRequest,
    )
    from griddy.nfl.models.requests.get_ngs_news_op import (
        GetNgsArticlesRequest,
        GetNgsMixedContentRequest,
        GetNgsVideoClipsRequest,
    )
    from griddy.nfl.models.requests.get_ngs_passing_stats_op import (
        GetNgsPassingStatsRequest,
    )
    from griddy.nfl.models.requests.get_ngs_receiving_stats_op import (
        GetNgsReceivingStatsRequest,
    )
    from griddy.nfl.models.requests.get_ngs_rushing_stats_op import (
        GetNgsRushingStatsRequest,
    )
    from griddy.nfl.models.requests.get_ngs_schedule_op import (
        GetNgsScheduleRequest,
    )
    from griddy.nfl.models.requests.get_ngs_teams_op import (
        GetNgsTeamsRequest,
    )
    from griddy.nfl.models.requests.get_play_by_play_op import (
        GetPlayByPlayRequest,
    )
    from griddy.nfl.models.requests.get_play_list import (
        GetPlayListRequest,
    )
    from griddy.nfl.models.requests.get_player_details_op import (
        GetPlayerDetailsRequest,
    )
    from griddy.nfl.models.requests.get_player_op import (
        GetPlayerRequest,
    )
    from griddy.nfl.models.requests.get_player_passing_stats_by_season_op import (
        GetPlayerPassingStatsBySeasonRequest,
    )
    from griddy.nfl.models.requests.get_player_passing_stats_by_week_op import (
        GetPlayerPassingStatsByWeekRequest,
    )
    from griddy.nfl.models.requests.get_player_receiving_stats_by_season_op import (
        GetPlayerReceivingStatsBySeasonRequest,
    )
    from griddy.nfl.models.requests.get_player_receiving_stats_by_week_op import (
        GetPlayerReceivingStatsByWeekRequest,
    )
    from griddy.nfl.models.requests.get_player_rushing_stats_by_season_op import (
        GetPlayerRushingStatsBySeasonRequest,
        GetPlayerRushingStatsBySeasonSortKey,
    )
    from griddy.nfl.models.requests.get_player_rushing_stats_by_week_op import (
        GetPlayerRushingStatsByWeekRequest,
        GetPlayerRushingStatsByWeekSortKey,
    )
    from griddy.nfl.models.requests.get_players_team_roster_op import (
        GetPlayersTeamRosterRequest,
    )
    from griddy.nfl.models.requests.get_plays_win_probability_op import (
        GameID,
        GetPlaysWinProbabilityRequest,
    )
    from griddy.nfl.models.requests.get_projected_stats_op import (
        GetProjectedStatsRequest,
    )
    from griddy.nfl.models.requests.get_schedule_season_weeks_op import (
        GetScheduleSeasonWeeksRequest,
    )
    from griddy.nfl.models.requests.get_scheduled_game_op import (
        GetScheduledGameRequest,
    )
    from griddy.nfl.models.requests.get_scheduled_games_op import (
        GetScheduledGamesRequest,
    )
    from griddy.nfl.models.requests.get_season_content_insights_op import (
        GetSeasonContentInsightsRequest,
        Tag,
    )
    from griddy.nfl.models.requests.get_season_player_stats_op import (
        GetSeasonPlayerStatsPosition,
        GetSeasonPlayerStatsRequest,
        StatCategory,
    )
    from griddy.nfl.models.requests.get_season_weeks_op import (
        GetSeasonWeeksRequest,
    )
    from griddy.nfl.models.requests.get_standings_op import (
        GetStandingsRequest,
    )
    from griddy.nfl.models.requests.get_stats_boxscore_op import (
        GetStatsBoxscoreRequest,
    )
    from griddy.nfl.models.requests.get_summary_play_op import (
        GetSummaryPlayRequest,
    )
    from griddy.nfl.models.requests.get_team_defense_pass_stats_by_season_op import (
        GetTeamDefensePassStatsBySeasonRequest,
        GetTeamDefensePassStatsBySeasonSortKey,
    )
    from griddy.nfl.models.requests.get_team_defense_pass_stats_by_week_op import (
        GetTeamDefensePassStatsByWeekRequest,
        GetTeamDefensePassStatsByWeekSortKey,
    )
    from griddy.nfl.models.requests.get_team_defense_rush_stats_by_season_op import (
        GetTeamDefenseRushStatsBySeasonRequest,
        GetTeamDefenseRushStatsBySeasonSortKey,
    )
    from griddy.nfl.models.requests.get_team_defense_rush_stats_by_week_op import (
        GetTeamDefenseRushStatsByWeekRequest,
        GetTeamDefenseRushStatsByWeekSortKey,
    )
    from griddy.nfl.models.requests.get_team_defense_stats_by_season_op import (
        GetTeamDefenseStatsBySeasonRequest,
        GetTeamDefenseStatsBySeasonSortKey,
        GetTeamDefenseStatsBySeasonSplit,
    )
    from griddy.nfl.models.requests.get_team_defense_stats_by_week_op import (
        GetTeamDefenseStatsByWeekRequest,
        GetTeamDefenseStatsByWeekSortKey,
        GetTeamDefenseStatsByWeekSplit,
    )
    from griddy.nfl.models.requests.get_team_injuries_op import (
        GetTeamInjuriesRequest,
    )
    from griddy.nfl.models.requests.get_team_needs_op import (
        GetTeamNeedsRequest,
    )
    from griddy.nfl.models.requests.get_team_offense_overview_stats_by_season_op import (
        GetTeamOffenseStatsBySeasonRequest,
        GetTeamOffenseStatsBySeasonSortKey,
        GetTeamOffenseStatsBySeasonSplit,
    )
    from griddy.nfl.models.requests.get_team_offense_overview_stats_by_week_op import (
        GetTeamOffenseStatsByWeekRequest,
        GetTeamOffenseStatsByWeekSortKey,
        GetTeamOffenseStatsByWeekSplit,
    )
    from griddy.nfl.models.requests.get_team_offense_pass_stats_by_season_op import (
        GetTeamOffensePassStatsBySeasonRequest,
        GetTeamOffensePassStatsBySeasonSortKey,
    )
    from griddy.nfl.models.requests.get_team_offense_pass_stats_by_week_op import (
        GetTeamOffensePassStatsByWeekRequest,
        GetTeamOffensePassStatsByWeekSortKey,
    )
    from griddy.nfl.models.requests.get_team_offense_rush_stats_by_season_op import (
        GetTeamOffenseRushStatsBySeasonRequest,
        GetTeamOffenseRushStatsBySeasonSortKey,
    )
    from griddy.nfl.models.requests.get_team_offense_rush_stats_by_week_op import (
        GetTeamOffenseRushStatsByWeekRequest,
        GetTeamOffenseRushStatsByWeekSortKey,
    )
    from griddy.nfl.models.requests.get_team_roster_op import (
        GetTeamRosterRequest,
    )
    from griddy.nfl.models.requests.get_team_schedule_op import (
        GetTeamScheduleRequest,
    )
    from griddy.nfl.models.requests.get_team_standings_op import (
        GetTeamStandingsRequest,
    )
    from griddy.nfl.models.requests.get_transactions_op import (
        GetTransactionsRequest,
        GetTransactionsTransactionType,
    )
    from griddy.nfl.models.requests.get_venues_op import (
        GetVenuesRequest,
    )
    from griddy.nfl.models.requests.get_week_of_date_op import (
        GetWeekOfDateRequest,
    )
    from griddy.nfl.models.requests.get_weekly_betting_odds_op import (
        GetWeeklyBettingOddsRequest,
    )
    from griddy.nfl.models.requests.get_weekly_game_details_op import (
        GetWeeklyGameDetailsRequest,
    )
    from griddy.nfl.models.requests.get_weekly_team_roster_op import (
        GetWeeklyTeamRosterRequest,
    )
    from griddy.nfl.models.requests.get_win_probability_min_op import (
        GetWinProbabilityMinRequest,
    )
    from griddy.nfl.models.requests.refresh_token_request import (
        RefreshTokenRequest,
        RefreshTokenRequestNetworkType,
    )
    from griddy.nfl.models.requests.token_request import (
        TokenRequest,
        TokenRequestNetworkType,
    )
    from griddy.nfl.models.responses.boxscore_response import (
        BoxscoreResponse,
    )
    from griddy.nfl.models.responses.boxscore_response_2 import (
        Away,
        BoxScoreResponse2,
        Home,
        PlayerStats,
        TeamStats,
    )
    from griddy.nfl.models.responses.coaches_film_response import (
        CoachesFilmResponse,
    )
    from griddy.nfl.models.responses.combine_profiles_response import (
        CombineProfilesResponse,
    )
    from griddy.nfl.models.responses.combine_rankings_response import (
        CombineRankingsResponse,
    )
    from griddy.nfl.models.responses.current_games_response import (
        CurrentGamesResponse,
    )
    from griddy.nfl.models.responses.defensive_overview_stats_response import (
        DefensiveOverviewStatsResponse,
    )
    from griddy.nfl.models.responses.draft_response import (
        DraftResponse,
    )
    from griddy.nfl.models.responses.fantasy_stats_response import (
        FantasyStatsResponse,
    )
    from griddy.nfl.models.responses.film_room_plays_response import (
        FilmroomPlaysResponse,
    )
    from griddy.nfl.models.responses.football_games_response import (
        FootballGamesResponse,
    )
    from griddy.nfl.models.responses.football_rosters_response import (
        FootballRostersResponse,
    )
    from griddy.nfl.models.responses.football_teams_response import (
        FootballTeamsResponse,
    )
    from griddy.nfl.models.responses.futures_odds_response import (
        FuturesOddsResponse,
        FuturesOddsResponseData,
    )
    from griddy.nfl.models.responses.game_center_response import (
        GamecenterResponse,
        Leaders,
        LeagueAverageReceiverSeparation,
        LeagueAverageSeparationToQb,
        PassDistanceLeaders,
        Passers,
        PassRushers,
        Receivers,
        Rushers,
        SpeedLeaders,
        TimeToSackLeaders,
    )
    from griddy.nfl.models.responses.game_preview_response import (
        GamePreviewResponse,
        Preview,
    )
    from griddy.nfl.models.responses.game_stats_response import (
        GameStatsResponse,
        GameStatsResponseData,
    )
    from griddy.nfl.models.responses.games_response import (
        GamesResponse,
    )
    from griddy.nfl.models.responses.home_filmcards_response import (
        HomeFilmCardsResponse,
    )
    from griddy.nfl.models.responses.injury_report_response import (
        InjuryReportResponse,
    )
    from griddy.nfl.models.responses.lives_cores_response import (
        LiveScoresResponse,
    )
    from griddy.nfl.models.responses.matchup_rankings_response import (
        MatchupRankingsResponse,
    )
    from griddy.nfl.models.responses.nearest_defender_stats_response import (
        NearestDefenderStatsResponse,
    )
    from griddy.nfl.models.responses.ngs_content_response import (
        NgsChartPlayersResponse,
        NgsChartsResponse,
        NgsHighlightsResponse,
    )
    from griddy.nfl.models.responses.ngs_current_schedule_response import (
        NgsCurrentScheduleResponse,
    )
    from griddy.nfl.models.responses.ngs_game_overview_response import (
        NgsGameCenterOverviewResponse,
    )
    from griddy.nfl.models.responses.ngs_leaders_response import (
        NgsCompletionLeadersResponse,
        NgsDistanceLeadersResponse,
        NgsERYLeadersResponse,
        NgsSackLeadersResponse,
        NgsSpeedLeadersResponse,
        NgsTackleLeadersResponse,
        NgsYACLeadersResponse,
    )
    from griddy.nfl.models.responses.ngs_live_scores_response import (
        NgsGameScoreDetail,
        NgsLiveGameScore,
        NgsLiveScoresResponse,
        NgsTeamInfo,
        NgsTeamScore,
    )
    from griddy.nfl.models.responses.ngs_news_response import (
        NgsArticlesResponse,
        NgsMixedContentResponse,
        NgsVideosResponse,
    )
    from griddy.nfl.models.responses.ngs_stats_response import (
        NgsPassingStatsResponse,
        NgsReceivingStatsResponse,
        NgsRushingStatsResponse,
    )
    from griddy.nfl.models.responses.pass_rush_stats_response import (
        PassRushStatsResponse,
    )
    from griddy.nfl.models.responses.passing_stats_response import (
        PassingStatsResponse,
    )
    from griddy.nfl.models.responses.play_by_play_response import (
        PlayByPlayResponse,
    )
    from griddy.nfl.models.responses.play_summary_response import (
        PlaySummaryResponse,
    )
    from griddy.nfl.models.responses.play_win_probability_response import (
        PlayWinProbabilityResponse,
    )
    from griddy.nfl.models.responses.player_search_response import (
        PlayerSearchResponse,
    )
    from griddy.nfl.models.responses.player_stats_response import (
        PlayerStatsResponse,
        PlayerStatsResponsePagination,
        PlayerStatsResponsePlayer,
        PlayerStatsResponseStats,
    )
    from griddy.nfl.models.responses.playlist_response import (
        PlaylistResponse,
    )
    from griddy.nfl.models.responses.projected_stats_response import (
        Included,
        Meta,
        Page,
        ProjectedStatsResponse,
        ProjectedStatsResponsePagination,
    )
    from griddy.nfl.models.responses.receiving_stats_response import (
        ReceivingStatsResponse,
    )
    from griddy.nfl.models.responses.roster_response import (
        Roster,
        RosterResponse,
    )
    from griddy.nfl.models.responses.rushing_stats_response import (
        RushingStatsResponse,
    )
    from griddy.nfl.models.responses.season_weeks_response import (
        SeasonWeeksResponse,
    )
    from griddy.nfl.models.responses.standings_response import (
        StandingsResponse,
        StandingsResponseWeek,
    )
    from griddy.nfl.models.responses.team_defense_pass_stats_response import (
        TeamDefensePassStatsResponse,
    )
    from griddy.nfl.models.responses.team_defense_rush_stats_response import (
        TeamDefenseRushStatsResponse,
    )
    from griddy.nfl.models.responses.team_defense_stats_response import (
        TeamDefenseStatsResponse,
    )
    from griddy.nfl.models.responses.team_needs_response import (
        TeamNeedsResponse,
    )
    from griddy.nfl.models.responses.team_offense_overview_stats_response import (
        TeamOffenseStatsResponse,
    )
    from griddy.nfl.models.responses.team_offense_pass_stats_response import (
        TeamOffensePassStatsResponse,
    )
    from griddy.nfl.models.responses.team_offense_rush_stats_response import (
        TeamOffenseRushStatsResponse,
    )
    from griddy.nfl.models.responses.team_rankings_response import (
        TeamRankingsResponse,
    )
    from griddy.nfl.models.responses.team_roster_response import (
        TeamRosterResponse,
    )
    from griddy.nfl.models.responses.token_response import (
        TokenResponse,
    )
    from griddy.nfl.models.responses.transactions_response import (
        TransactionsResponse,
    )
    from griddy.nfl.models.responses.venues_response import (
        VenuesResponse,
    )
    from griddy.nfl.models.responses.weekly_odds_response import (
        WeeklyOddsResponse,
    )
    from griddy.nfl.models.responses.weekly_passing_stats_response import (
        WeeklyPassingStatsResponse,
    )
    from griddy.nfl.models.responses.weekly_roster_response import (
        WeeklyRosterResponse,
    )
    from griddy.nfl.models.responses.weekly_rushing_stats_response import (
        WeeklyRushingStatsResponse,
    )
    from griddy.nfl.models.responses.weeks_response import (
        WeeksResponse,
    )
    from griddy.nfl.models.responses.win_probability_response import (
        WinProbabilityResponse,
    )

    from .entities.award import Award, AwardType
    from .entities.boxscore_schedule import BoxscoreSchedule
    from .entities.boxscore_score import BoxscoreScore
    from .entities.boxscore_site import BoxscoreSite
    from .entities.boxscore_team import BoxscoreTeam
    from .entities.broadcast_info import (
        BroadcastInfo,
        InternationalWatchOption,
        StreamingNetwork,
        Territory,
    )
    from .entities.career_stats import CareerStats
    from .entities.clinched import Clinched
    from .entities.coaches_film_video import (
        Background,
        CameraSource,
        CoachesFilmVideo,
        CoachesFilmVideoType,
        Cta,
        Image,
        PromoAsset,
        SubType,
        Video,
    )
    from .entities.conference import Conference
    from .entities.contract_info import ContractInfo
    from .entities.current_game import (
        CurrentGame,
        CurrentGameCategory,
        CurrentGameExtension,
    )
    from .entities.defensive_nearest_defender_stats import (
        DefensiveNearestDefenderStats,
    )
    from .entities.defensive_pass_rush_stats import (
        DefensivePassRushStats,
    )
    from .entities.defensive_player_overview_stats import (
        DefensivePlayerOverviewStats,
    )
    from .entities.defensive_stats import DefensiveStats
    from .entities.division import Division
    from .entities.draft_pick import DraftPick
    from .entities.drive import Drive, Result
    from .entities.external_id import ExternalID
    from .entities.fantasy_player_stats import (
        FantasyPlayerStats,
        FantasyPlayerStatsPosition,
        PositionGroup,
    )
    from .entities.film_card import (
        FilmCard,
        LinkParams,
    )
    from .entities.film_room_play import FilmroomPlay
    from .entities.futures_market import (
        Fixture,
        FuturesMarket,
    )
    from .entities.game import (
        Game,
        GameCategory,
        GameExtension,
        GameStatus,
    )
    from .entities.game_center_schedule import (
        GamecenterSchedule,
    )
    from .entities.game_detail import GameDetail
    from .entities.game_insight import (
        Content,
        GameInsight,
    )
    from .entities.game_odds import GameOdds
    from .entities.game_schedule import GameSchedule
    from .entities.game_score import GameScore
    from .entities.game_site import GameSite
    from .entities.game_team import GameTeam, Score
    from .entities.historical_stat_categories import (
        HistoricalStatCategories,
    )
    from .entities.injury_entry import (
        InjuryEntry,
        InjuryEntryGameStatus,
        PracticeStatus,
    )
    from .entities.insight import (
        Insight,
        InsightPosition,
        SecondTeamType,
    )
    from .entities.kicking_stats import KickingStats
    from .entities.live_game import (
        AwayTeam,
        HomeTeam,
        LiveGame,
    )
    from .entities.live_stat_entries import (
        LivePlayerStatEntry,
        LivePlayerTeamEntry,
        LiveTeamStatEntry,
    )
    from .entities.moneyline import MoneyLine
    from .entities.multiple_rankings_category import (
        MultipleRankingsCategory,
        MultipleRankingsCategoryPagination,
    )
    from .entities.nfl_auth import NFLAuth
    from .entities.odds_selection import OddsSelection
    from .entities.overall_record import (
        OverallRecord,
        OverallRecordPoints,
        OverallRecordType,
        Streak,
    )
    from .entities.pagination import Pagination
    from .entities.passer_stats import (
        PasserStats,
        Zone,
    )
    from .entities.passing_stats import PassingStats
    from .entities.penalty import Penalty
    from .entities.play import Play
    from .entities.play_detail import (
        PlayDetail,
        PlayDirection,
        PlayState,
    )
    from .entities.play_participant import (
        PlayParticipant,
        PlayParticipantStats,
        Role,
    )
    from .entities.play_player import PlayPlayer
    from .entities.play_stat import PlayStat
    from .entities.play_win_probability import (
        PlayWinProbability,
    )
    from .entities.player import Player
    from .entities.player_detail import PlayerDetail
    from .entities.player_game_stats import PlayerGameStats
    from .entities.player_passing_stats import (
        PlayerPassingStats,
    )
    from .entities.player_projection import (
        PlayerProjection,
        Relationships,
        RelationshipsTypePlayerWeekProjectedPoints,
        RelationshipsTypePlayerWeekProjectedStats,
        TypePlayer,
        WeekPoint,
        WeekStat,
    )
    from .entities.player_receiving_stats import (
        PlayerReceivingStats,
    )
    from .entities.player_rushing_stats import (
        PlayerRushingStats,
    )
    from .entities.player_search_result import (
        PlayerSearchResult,
    )
    from .entities.player_week_projected_points import (
        PlayerWeekProjectedPoints,
        PlayerWeekProjectedPointsAttributes,
        PlayerWeekProjectedPointsType,
    )
    from .entities.player_week_projected_stats import (
        PlayerWeekProjectedStats,
        PlayerWeekProjectedStatsAttributes,
        PlayerWeekProjectedStatsType,
    )
    from .entities.point_spread import PointSpread
    from .entities.points_record import (
        PointsRecord,
        PointsRecordPoints,
    )
    from .entities.pro_game import (
        ProGame,
        ProGameCategory,
        ProGameExtension,
        ProGameStatus,
    )
    from .entities.pro_play import ProPlay
    from .entities.pro_team import (
        ProTeam,
        ProTeamConferenceAbbr,
        ProTeamTeamType,
    )
    from .entities.pro_week import ProWeek, ProWeekWeekType
    from .entities.receiving_stats import ReceivingStats
    from .entities.record import Record
    from .entities.response_metadata import ResponseMetadata
    from .entities.rushing_stats import RushingStats
    from .entities.schedule_team import ScheduleTeam
    from .entities.scheduled_game import ScheduledGame
    from .entities.scoring_play import ScoreType, ScoringPlay
    from .entities.search_players_op import (
        SearchPlayersRequest,
    )
    from .entities.season_stats import SeasonStats
    from .entities.security import Security
    from .entities.site import Site
    from .entities.social_media import SocialMedia
    from .entities.standings import (
        Standings,
        StandingsTeam,
    )
    from .entities.standings_record import (
        StandingsRecord,
        StandingsRecordPoints,
    )
    from .entities.statistic_ranking import (
        Statistic,
        StatisticRanking,
    )
    from .entities.team import Team, TeamConferenceAbbr, TeamTeamType
    from .entities.team_boxscore import TeamBoxscore
    from .entities.team_defense_pass_stats import (
        TeamDefensePassStats,
    )
    from .entities.team_defense_rush_stats import (
        TeamDefenseRushStats,
    )
    from .entities.team_defense_stats import TeamDefenseStats
    from .entities.team_game_stats import TeamGameStats
    from .entities.team_info import TeamInfo
    from .entities.team_injury_report import TeamInjuryReport
    from .entities.team_matchup_rankings import (
        TeamMatchupRankings,
    )
    from .entities.team_offense_overview_stats import (
        TeamOffenseStats,
    )
    from .entities.team_offense_pass_stats import (
        TeamOffensePassStats,
    )
    from .entities.team_ranking_entry import TeamRankingEntry
    from .entities.team_rankings import TeamRankings
    from .entities.team_score import TeamScore
    from .entities.team_venue import TeamVenue
    from .entities.ticket_vendor import TicketVendor
    from .entities.totals import Totals
    from .entities.transaction import Transaction, TransactionType
    from .entities.venue import Venue
    from .entities.venue_info import VenueInfo
    from .entities.video_authorizations import (
        NFLPLUSPLUSNFLPLUSCOACHESFILM,
        NflPlusPlus,
        NflPlusPlusRequirements,
        NflPlusPremium,
        NFLPLUSPremiumNFLPLUSCOACHESFILM,
        NflPlusPremiumRequirements,
        ProPremium,
        ProPremiumNFLPLUSCOACHESFILM,
        ProPremiumRequirements,
        VideoAuthorizations,
    )
    from .entities.video_game_play_ids import (
        VideoGamePlayIds,
    )
    from .entities.video_tag import VideoTag
    from .entities.video_thumbnail import VideoThumbnail
    from .entities.week import Week, WeekWeekType
    from .entities.weekly_game_detail import (
        DriveChart,
        Replay,
        Summary,
        TaggedVideos,
        WeeklyGameDetail,
        WeeklyGameDetailCategory,
        WeeklyGameDetailExtension,
        WeeklyGameDetailStatus,
    )
    from .entities.weekly_player import WeeklyPlayer
    from .entities.weekly_player_passing_stats import (
        WeeklyPlayerPassingStats,
    )
    from .entities.weekly_player_rushing_stats import (
        WeeklyPlayerRushingStats,
    )
    from .enums.defensive_splits_enum import DefenseNGSSplitEnum
    from .enums.down_enum import DownEnum
    from .enums.game_location_enum import GameLocationEnum
    from .enums.position_enums import (
        DefenseNGSPositionEnum,
        DefenseNGSPositionGroupEnum,
        DefensePositionEnum,
        DefensePositionGroupEnum,
    )
    from .enums.quarter_enum import QuarterEnum
    from .enums.yards_to_go_enum import YardsToGoEnum
    from .requests.get_game_details_by_slug_op import (
        GetGameDetailsBySlugRequest,
    )
    from .requests.get_game_details_op import (
        GetGameDetailsRequest,
    )
    from .requests.get_historical_player_stats_op import (
        GetHistoricalPlayerStatsRequest,
    )
    from .requests.get_historical_team_stats_op import (
        GetHistoricalTeamStatsRequest,
    )
    from .requests.get_live_player_statistics_op import (
        GetLivePlayerStatisticsRequest,
    )
    from .requests.get_live_team_statistics_op import (
        GetLiveTeamStatisticsRequest,
    )
    from .requests.get_video_replays_op import (
        GetVideoReplaysRequest,
    )
    from .responses.historical_player_stats_response import (
        HistoricalPlayerStatsResponse,
        PersonStat,
        PersonStatLineup,
    )
    from .responses.historical_team_stats_response import (
        HistoricalGameInfo,
        HistoricalTeamStatsResponse,
    )
    from .responses.live_player_statistics_response import (
        LivePlayerStatisticsResponse,
    )
    from .responses.live_team_statistics_response import (
        LiveTeamStatisticsResponse,
    )
    from .responses.video_replays_response import (
        VideoReplaysResponse,
    )

__all__ = [
    "Person",
    "FootballRoster",
    "FootballRostersResponse",
    "PlayWinProbabilityResponse",
    "GetFootballRostersRequest",
    "AirYardType",
    "Award",
    "AwardType",
    "Away",
    "AwayTeam",
    "Background",
    "DesignationEnum",
    "CollegeClassEnum",
    "BenchPress",
    "BroadJump",
    "FortyYardDash",
    "TenYardSplit",
    "ThreeConeDrill",
    "TwentyYardShuffle",
    "VerticalJump",
    "CombineRankingsResponse",
    "EventFilterEnum",
    "CombineProfile",
    "CombinePerson",
    "CombineProfilesResponse",
    "GetCombineProfilesRequest",
    "GetCombineRankingsRequest",
    "BinaryFlagEnum",
    "BoxScoreResponse2",
    "BoxscoreResponse",
    "BoxscoreSchedule",
    "BoxscoreScore",
    "BoxscoreSite",
    "BoxscoreTeam",
    "BroadcastInfo",
    "CameraSource",
    "CareerStats",
    "Clinched",
    "CoachesFilmResponse",
    "CoachesFilmVideo",
    "CoachesFilmVideoType",
    "Conference",
    "ConferenceEnum",
    "Content",
    "ContractInfo",
    "Cta",
    "CurrentGame",
    "CurrentGameCategory",
    "CurrentGameExtension",
    "CurrentGamesResponse",
    "DefCoverageType",
    "DefendersInTheBoxType",
    "DefensiveOverviewStatsResponse",
    "DefensivePassRushStats",
    "DefensivePlayerOverviewStats",
    "DefensiveNearestDefenderStats",
    "DefenseNGSSplitEnum",
    "DefensePositionEnum",
    "DefensePositionGroupEnum",
    "DefenseNGSPositionEnum",
    "DefenseNGSPositionGroupEnum",
    "DefensiveStats",
    "NearestDefenderStatsResponse",
    "Division",
    "DraftDay",
    "DraftPick",
    "DraftResponse",
    "Drive",
    "DriveChart",
    "DropbackTimeType",
    "DownEnum",
    "ExternalID",
    "FantasyPlayerStats",
    "FantasyPlayerStatsPosition",
    "FantasyStatsResponse",
    "FilmCard",
    "FilmroomPlay",
    "FilmroomPlaysResponse",
    "Fixture",
    "FootballGamesResponse",
    "FootballTeamsResponse",
    "GetFootballTeamsRequest",
    "FuturesMarket",
    "FuturesOddsResponse",
    "FuturesOddsResponseData",
    "Game",
    "GameCategory",
    "GameDetail",
    "GameExtension",
    "GameID",
    "GameInsight",
    "GameLocationEnum",
    "GameOdds",
    "GamePhaseEnum",
    "GamePreviewResponse",
    "GameResultEnum",
    "GameSchedule",
    "GameScore",
    "GameSite",
    "GameStatsResponse",
    "GameStatsResponseData",
    "GameStatus",
    "GameStatusEnum",
    "GameTeam",
    "GamecenterResponse",
    "GamecenterSchedule",
    "GamesResponse",
    "GetCoachesFilmVideosRequest",
    "GetDefensiveOverviewStatsBySeasonRequest",
    "GetDefensiveOverviewStatsBySeasonSortKey",
    "GetDefensiveOverviewStatsByWeekRequest",
    "GetDefensiveOverviewStatsByWeekSortKey",
    "GetDefensivePassRushStatsByWeekRequest",
    "GetDefensivePassRushStatsByWeekSortKey",
    "GetDefensivePassRushStatsBySeasonRequest",
    "GetDefensivePassRushStatsBySeasonSortKey",
    "GetDefensiveNearestDefenderStatsBySeasonRequest",
    "GetDefensiveNearestDefenderStatsBySeasonSortKey",
    "GetDefensiveNearestDefenderStatsByWeekRequest",
    "GetDefensiveNearestDefenderStatsByWeekSortKey",
    "GetDefensiveStatsBySeasonSortKey",
    "GetDraftInfoRequest",
    "GetDraftPicksReportRequest",
    "GetFantasyStatsBySeasonPositionGroup",
    "GetFantasyStatsBySeasonRequest",
    "GetFantasyStatsBySeasonSortKey",
    "GetFilmroomPlaysRequest",
    "GetFootballBoxScoreRequest",
    "GetFootballGamesRequest",
    "GetGameInsightsRequest",
    "GetGameMatchupRankingsRequest",
    "GetGamePreviewRequest",
    "GetGameTeamRankingsRequest",
    "GetGamecenterRequest",
    "GetInjuryReportsRequest",
    "GetLiveGameScoresRequest",
    "GetLiveGameStatsRequest",
    "GetMultipleRankingsAllTeamsRequest",
    "GetNgsArticlesRequest",
    "GetNgsChartsRequest",
    "GetNgsCurrentScheduleRequest",
    "GetNgsGameOverviewRequest",
    "GetNgsHighlightsRequest",
    "GetNgsLeadersRequest",
    "GetNgsLiveScoresRequest",
    "GetNgsMixedContentRequest",
    "GetNgsPassingStatsRequest",
    "GetNgsReceivingStatsRequest",
    "GetNgsRushingStatsRequest",
    "GetNgsScheduleRequest",
    "GetNgsSeasonLeadersRequest",
    "GetNgsTeamsRequest",
    "GetNgsVideoClipsRequest",
    "GetPlayByPlayRequest",
    "GetPlayListRequest",
    "ProPlay",
    "PlaylistResponse",
    "GetPlayerDetailsRequest",
    "GetPlayerPassingStatsBySeasonRequest",
    "GetPlayerPassingStatsByWeekRequest",
    "GetPlayerReceivingStatsBySeasonRequest",
    "GetPlayerReceivingStatsByWeekRequest",
    "GetPlayerRequest",
    "GetPlayerRushingStatsBySeasonRequest",
    "GetPlayerRushingStatsBySeasonSortKey",
    "GetPlayerRushingStatsByWeekRequest",
    "GetPlayerRushingStatsByWeekSortKey",
    "GetPlayersTeamRosterRequest",
    "GetPlaysWinProbabilityRequest",
    "GetProjectedStatsRequest",
    "GetScheduleSeasonWeeksRequest",
    "GetScheduledGameRequest",
    "GetScheduledGamesRequest",
    "GetSeasonContentInsightsRequest",
    "GetSeasonPlayerStatsPosition",
    "GetSeasonPlayerStatsRequest",
    "GetSeasonWeeksRequest",
    "GetStandingsRequest",
    "GetStatsBoxscoreRequest",
    "GetSummaryPlayRequest",
    "GetTeamDefensePassStatsBySeasonRequest",
    "GetTeamDefensePassStatsBySeasonSortKey",
    "GetTeamDefenseRushStatsBySeasonRequest",
    "GetTeamDefenseRushStatsBySeasonSortKey",
    "GetTeamDefenseStatsBySeasonRequest",
    "GetTeamDefenseStatsBySeasonSortKey",
    "GetTeamDefenseStatsBySeasonSplit",
    "GetTeamDefensePassStatsByWeekRequest",
    "GetTeamDefensePassStatsByWeekSortKey",
    "GetTeamDefenseRushStatsByWeekRequest",
    "GetTeamDefenseRushStatsByWeekSortKey",
    "GetTeamDefenseStatsByWeekRequest",
    "GetTeamDefenseStatsByWeekSortKey",
    "GetTeamDefenseStatsByWeekSplit",
    "GetTeamInjuriesRequest",
    "GetTeamOffenseStatsBySeasonRequest",
    "GetTeamOffenseStatsBySeasonSortKey",
    "GetTeamOffenseStatsBySeasonSplit",
    "GetTeamOffenseStatsByWeekRequest",
    "GetTeamOffenseStatsByWeekSortKey",
    "GetTeamOffenseStatsByWeekSplit",
    "GetTeamOffensePassStatsBySeasonRequest",
    "GetTeamOffensePassStatsBySeasonSortKey",
    "GetTeamOffensePassStatsByWeekRequest",
    "GetTeamOffensePassStatsByWeekSortKey",
    "GetTeamOffenseRushStatsByWeekRequest",
    "GetTeamOffenseRushStatsByWeekSortKey",
    "GetTeamOffenseRushStatsBySeasonRequest",
    "GetTeamOffenseRushStatsBySeasonSortKey",
    "GetTeamNeedsRequest",
    "GetWeekOfDateRequest",
    "TeamOffenseRushStats",
    "TeamOffenseRushStatsResponse",
    "GetTeamRosterRequest",
    "GetTeamScheduleRequest",
    "GetTeamStandingsRequest",
    "GetTransactionsRequest",
    "GetTransactionsTransactionType",
    "GetVenuesRequest",
    "GetWeeklyBettingOddsRequest",
    "GetWeeklyGameDetailsRequest",
    "GetWeeklyTeamRosterRequest",
    "GetWinProbabilityMinRequest",
    "Home",
    "HomeFilmCardsResponse",
    "HomeTeam",
    "Image",
    "Included",
    "InjuryEntry",
    "InjuryEntryGameStatus",
    "InjuryReportResponse",
    "Insight",
    "InsightPosition",
    "InternationalWatchOption",
    "KickingStats",
    "Leaders",
    "LeagueAverageReceiverSeparation",
    "LeagueAverageSeparationToQb",
    "LinkParams",
    "LiveGame",
    "LiveScoresResponse",
    "MatchupRankingsResponse",
    "MeridiemEnum",
    "Meta",
    "MoneyLine",
    "MultipleRankingsCategory",
    "MultipleRankingsCategoryPagination",
    "NFLAuth",
    "NFLPLUSPLUSNFLPLUSCOACHESFILM",
    "NFLPLUSPremiumNFLPLUSCOACHESFILM",
    "NflPlusPlus",
    "NflPlusPlusRequirements",
    "NflPlusPremium",
    "NflPlusPremiumRequirements",
    "NgsCurrentScheduleResponse",
    "NgsGameScoreDetail",
    "NgsLiveGameScore",
    "NgsLiveScoresResponse",
    "NgsTeamInfo",
    "NgsTeamScore",
    # NGS Entity models
    "NgsArticlesResponse",
    "NgsChart",
    "NgsChartPlayer",
    "NgsChartPlayersResponse",
    "NgsChartsResponse",
    "NgsCompletionLeader",
    "NgsCompletionLeaderEntry",
    "NgsCompletionLeadersResponse",
    "NgsContentItem",
    "NgsContentMetadata",
    "NgsContentPagination",
    "NgsContentTag",
    "NgsDistanceLeader",
    "NgsDistanceLeaderEntry",
    "NgsDistanceLeadersResponse",
    "NgsERYLeader",
    "NgsERYLeaderEntry",
    "NgsERYLeadersResponse",
    "NgsGameCenterOverviewResponse",
    "NgsGameLeaders",
    "NgsGamePassDistanceLeader",
    "NgsGameSackLeader",
    "NgsGameScheduleInfo",
    "NgsGameSpeedLeader",
    "NgsHighlight",
    "NgsHighlightsResponse",
    "NgsLeagueAverage",
    "NgsMixedContentResponse",
    "NgsPassDistanceLeadersMap",
    "NgsPasserInfo",
    "NgsPassersOverview",
    "NgsPassInfo",
    "NgsPassingStatsResponse",
    "NgsPassingStat",
    "NgsPassingZone",
    "NgsPassRusherInfo",
    "NgsPassRushersOverview",
    "NgsPlay",
    "NgsPlayStat",
    "NgsReceptionInfo",
    "NgsReceiverInfo",
    "NgsReceiversOverview",
    "NgsReceivingStatsResponse",
    "NgsReceivingStat",
    "NgsRushersOverview",
    "NgsRusherInfo",
    "NgsRushInfo",
    "NgsRushingStatsResponse",
    "NgsRushingStat",
    "NgsRushLocationStats",
    "NgsSackLeader",
    "NgsSackLeaderEntry",
    "NgsSackLeadersMap",
    "NgsSackLeadersResponse",
    "NgsSpeedLeader",
    "NgsSpeedLeaderEntry",
    "NgsSpeedLeadersMap",
    "NgsSpeedLeadersResponse",
    "NgsTackleInfo",
    "NgsTackleLeader",
    "NgsTackleLeaderEntry",
    "NgsTackleLeadersResponse",
    "NgsThumbnail",
    "NgsVideosResponse",
    "NgsYACLeader",
    "NgsYACLeaderEntry",
    "NgsYACLeadersResponse",
    "OddsSelection",
    "OffensivePlayerPositionEnum",
    "OffensiveSkillPositionEnum",
    "OverallRecord",
    "OverallRecordPoints",
    "OverallRecordType",
    "Page",
    "Pagination",
    "PassDistanceLeaders",
    "PassRushStatsResponse",
    "PassRushers",
    "PasserStats",
    "Passers",
    "PassingStats",
    "PassingStatsCategoryEnum",
    "PassingStatsResponse",
    "Penalty",
    "Personnel",
    "Play",
    "PlayByPlayResponse",
    "PlayDetail",
    "PlayDirection",
    "PlayParticipant",
    "PlayParticipantStats",
    "PlayPlayer",
    "PlayStat",
    "PlayState",
    "PlaySummaryResponse",
    "PlayTypeEnum",
    "PlayWinProbability",
    "Player",
    "PlayerDetail",
    "PlayerGameStats",
    "PlayerPassingStats",
    "PlayerProjection",
    "PlayerReceivingStats",
    "PlayerRushingStats",
    "PlayerSearchResponse",
    "PlayerSearchResult",
    "PlayerStats",
    "PlayerStatsResponse",
    "PlayerStatsResponsePagination",
    "PlayerStatsResponsePlayer",
    "PlayerStatsResponseStats",
    "PlayerWeekProjectedPoints",
    "PlayerWeekProjectedPointsAttributes",
    "PlayerWeekProjectedPointsType",
    "PlayerWeekProjectedStats",
    "PlayerWeekProjectedStatsAttributes",
    "PlayerWeekProjectedStatsType",
    "PointSpread",
    "PointsRecord",
    "PointsRecordPoints",
    "PositionGroup",
    "PracticeStatus",
    "PracticeStatusEnum",
    "Preview",
    "QuarterEnum",
    "ProGame",
    "ProGameCategory",
    "ProGameExtension",
    "ProGameStatus",
    "ProPremium",
    "ProPremiumNFLPLUSCOACHESFILM",
    "ProPremiumRequirements",
    "ProTeam",
    "ProTeamConferenceAbbr",
    "ProTeamTeamType",
    "ProWeek",
    "ProWeekWeekType",
    "ProjectedStatsResponse",
    "ProjectedStatsResponsePagination",
    "PromoAsset",
    "QbAlignment",
    "ReceiverAlignment",
    "Receivers",
    "ReceivingStats",
    "ReceivingStatsCategoryEnum",
    "ReceivingStatsResponse",
    "Record",
    "RefreshTokenRequest",
    "RefreshTokenRequestNetworkType",
    "Relationships",
    "RelationshipsTypePlayerWeekProjectedPoints",
    "RelationshipsTypePlayerWeekProjectedStats",
    "Replay",
    "ResponseMetadata",
    "Result",
    "Role",
    "Roster",
    "RosterResponse",
    "RushDirection",
    "Rushers",
    "RushingStats",
    "RushingStatsResponse",
    "ScheduleTeam",
    "ScheduledGame",
    "Score",
    "ScoreType",
    "ScoringPlay",
    "SearchPlayersRequest",
    "SeasonStats",
    "SeasonTypeEnum",
    "SeasonWeeksResponse",
    "SecondTeamType",
    "Security",
    "SeparationType",
    "Site",
    "SiteRoofTypeEnum",
    "SocialMedia",
    "SortOrderEnum",
    "SpeedLeaders",
    "Standings",
    "StandingsRecord",
    "StandingsRecordPoints",
    "StandingsResponse",
    "StandingsResponseWeek",
    "StandingsTeam",
    "StatCategory",
    "Statistic",
    "StatisticRanking",
    "Streak",
    "StreamingNetwork",
    "SubType",
    "Summary",
    "Tag",
    "TaggedVideos",
    "TargetLocation",
    "Team",
    "TeamBoxscore",
    "TeamConferenceAbbr",
    "TeamDefensePassStats",
    "TeamDefensePassStatsResponse",
    "TeamDefenseRushStats",
    "TeamDefenseRushStatsResponse",
    "TeamDefenseStats",
    "TeamDefenseStatsResponse",
    "TeamGameStats",
    "TeamInfo",
    "TeamInjuryReport",
    "TeamMatchupRankings",
    "TeamNeedsResponse",
    "TeamOffenseStats",
    "TeamOffenseStatsResponse",
    "TeamOffensePassStats",
    "TeamOffensePassStatsResponse",
    "TeamRankingEntry",
    "TeamRankings",
    "TeamRankingsResponse",
    "TeamRosterResponse",
    "TeamScore",
    "TeamStats",
    "TeamTeamType",
    "TeamTypeEnum",
    "TeamVenue",
    "Territory",
    "TicketVendor",
    "TimeToSackLeaders",
    "TokenRequest",
    "TokenRequestNetworkType",
    "TokenResponse",
    "Totals",
    "Transaction",
    "TransactionType",
    "TransactionsResponse",
    "TypePlayer",
    "Venue",
    "VenueInfo",
    "VenuesResponse",
    "Video",
    "VideoAuthorizations",
    "VideoGamePlayIds",
    "VideoTag",
    "VideoThumbnail",
    "Week",
    "WeekPoint",
    "WeekSlugEnum",
    "WeekStat",
    "WeekWeekType",
    "WeeklyGameDetail",
    "WeeklyGameDetailCategory",
    "WeeklyGameDetailExtension",
    "WeeklyGameDetailStatus",
    "WeeklyOddsResponse",
    "WeeklyPassingStatsResponse",
    "WeeklyPlayer",
    "WeeklyPlayerPassingStats",
    "WeeklyPlayerRushingStats",
    "WeeklyRosterResponse",
    "WeeklyRushingStatsResponse",
    "WeeksResponse",
    "WinProbabilityResponse",
    "YardsToGoEnum",
    "YardsToGoType",
    "Zone",
    # Historical stats
    "GetHistoricalTeamStatsRequest",
    "GetHistoricalPlayerStatsRequest",
    "HistoricalTeamStatsResponse",
    "HistoricalStatCategories",
    "HistoricalGameInfo",
    "HistoricalPlayerStatsResponse",
    "PersonStat",
    "PersonStatLineup",
    # Live stats
    "GetLiveTeamStatisticsRequest",
    "GetLivePlayerStatisticsRequest",
    "LiveTeamStatisticsResponse",
    "LiveTeamStatEntry",
    "LivePlayerStatisticsResponse",
    "LivePlayerStatEntry",
    "LivePlayerTeamEntry",
    # Experience
    "GetGameDetailsBySlugRequest",
    "GetGameDetailsRequest",
    # Content
    "GetVideoReplaysRequest",
    "VideoReplaysResponse",
]

_dynamic_imports: dict[str, str] = {
    "PlayWinProbabilityResponse": ".responses.play_win_probability_response",
    "Person": ".entities.person",
    "FootballRoster": ".entities.football_roster",
    "FootballRostersResponse": ".responses.football_rosters_response",
    "GetFootballRostersRequest": ".requests.get_football_rosters_op",
    "DesignationEnum": ".enums.combine_enums",
    "CollegeClassEnum": ".enums.combine_enums",
    "BenchPress": ".entities.combine_events",
    "BroadJump": ".entities.combine_events",
    "FortyYardDash": ".entities.combine_events",
    "TenYardSplit": ".entities.combine_events",
    "ThreeConeDrill": ".entities.combine_events",
    "TwentyYardShuffle": ".entities.combine_events",
    "VerticalJump": ".entities.combine_events",
    "CombineProfile": ".entities.combine_profile",
    "CombinePerson": ".entities.combine_profile",
    "CombineProfilesResponse": ".responses.combine_profiles_response",
    "GetCombineProfilesRequest": ".requests.get_combine_profiles_op",
    "GetCombineRankingsRequest": ".requests.get_combine_rankings_op",
    "GetWeekOfDateRequest": ".requests.get_week_of_date_op",
    "EventFilterEnum": ".enums.combine_enums",
    "CombineRankingsResponse": ".responses.combine_rankings_response",
    "FootballTeamsResponse": ".responses.football_teams_response",
    "GetFootballTeamsRequest": ".requests.get_football_teams_op",
    "Award": ".entities.award",
    "AwardType": ".entities.award",
    "BinaryFlagEnum": ".enums.binary_flag_enum",
    "BoxscoreResponse": ".responses.boxscore_response",
    "Away": ".responses.boxscore_response_2",
    "BoxScoreResponse2": ".responses.boxscore_response_2",
    "Home": ".responses.boxscore_response_2",
    "PlayerStats": ".responses.boxscore_response_2",
    "TeamStats": ".responses.boxscore_response_2",
    "BoxscoreSchedule": ".entities.boxscore_schedule",
    "BoxscoreScore": ".entities.boxscore_score",
    "BoxscoreSite": ".entities.boxscore_site",
    "BoxscoreTeam": ".entities.boxscore_team",
    "BroadcastInfo": ".entities.broadcast_info",
    "InternationalWatchOption": ".entities.broadcast_info",
    "StreamingNetwork": ".entities.broadcast_info",
    "Territory": ".entities.broadcast_info",
    "CareerStats": ".entities.career_stats",
    "Clinched": ".entities.clinched",
    "CoachesFilmResponse": ".responses.coaches_film_response",
    "Background": ".entities.coaches_film_video",
    "CameraSource": ".entities.coaches_film_video",
    "CoachesFilmVideo": ".entities.coaches_film_video",
    "CoachesFilmVideoType": ".entities.coaches_film_video",
    "Cta": ".entities.coaches_film_video",
    "Image": ".entities.coaches_film_video",
    "PromoAsset": ".entities.coaches_film_video",
    "SubType": ".entities.coaches_film_video",
    "Video": ".entities.coaches_film_video",
    "Conference": ".entities.conference",
    "ConferenceEnum": ".enums.conference_enum",
    "ContractInfo": ".entities.contract_info",
    "CurrentGame": ".entities.current_game",
    "CurrentGameCategory": ".entities.current_game",
    "CurrentGameExtension": ".entities.current_game",
    "CurrentGamesResponse": ".responses.current_games_response",
    "DefensiveOverviewStatsResponse": ".responses.defensive_overview_stats_response",
    "DefensivePassRushStats": ".entities.defensive_pass_rush_stats",
    "DefensivePassRushStatsNgsPosition": ".entities.defensive_pass_rush_stats",
    "DefensivePassRushStatsPosition": ".entities.defensive_pass_rush_stats",
    "DefensivePlayerOverviewStats": ".entities.defensive_player_overview_stats",
    "DefensivePlayerOverviewStatsNgsPosition": ".entities.defensive_player_overview_stats",
    "DefensivePlayerOverviewStatsPosition": ".entities.defensive_player_overview_stats",
    "DefensivePlayerStats": ".defensiveplayerstats",
    "DefensivePlayerStatsNgsPosition": ".defensiveplayerstats",
    "DefensivePlayerStatsPosition": ".defensiveplayerstats",
    "DefensivePositionGroupEnum": ".enums.defensive_position_group_enum",
    "DefensiveNearestDefenderStats": ".entities.defensive_nearest_defender_stats",
    "DefenseNGSSplitEnum": ".enums.defensive_splits_enum",
    "DefensePositionEnum": ".enums.position_enums",
    "DefensePositionGroupEnum": ".enums.position_enums",
    "DefenseNGSPositionEnum": ".enums.position_enums",
    "DefenseNGSPositionGroupEnum": ".enums.position_enums",
    "DefensiveStats": ".entities.defensive_stats",
    "DefensiveStatsResponse": ".defensivestatsresponse",
    "Division": ".entities.division",
    "DownEnum": ".enums.down_enum",
    "DraftDay": ".entities.draft_day",
    "DraftPick": ".entities.draft_pick",
    "DraftResponse": ".responses.draft_response",
    "Round": ".responses.draft_response",
    "Drive": ".entities.drive",
    "Result": ".entities.drive",
    "ExternalID": ".entities.external_id",
    "FantasyPlayerStats": ".entities.fantasy_player_stats",
    "FantasyPlayerStatsPosition": ".entities.fantasy_player_stats",
    "PositionGroup": ".entities.fantasy_player_stats",
    "FantasyStatsResponse": ".responses.fantasy_stats_response",
    "FilmCard": ".entities.film_card",
    "LinkParams": ".entities.film_card",
    "FilmroomPlay": ".entities.film_room_play",
    "FilmroomPlaysResponse": ".responses.film_room_plays_response",
    "FootballGamesResponse": ".responses.football_games_response",
    "Fixture": ".entities.futures_market",
    "FuturesMarket": ".entities.futures_market",
    "FuturesOddsResponse": ".responses.futures_odds_response",
    "FuturesOddsResponseData": ".responses.futures_odds_response",
    "Game": ".entities.game",
    "GameCategory": ".entities.game",
    "GameExtension": ".entities.game",
    "GameStatus": ".entities.game",
    "GamecenterResponse": ".responses.game_center_response",
    "Leaders": ".game_center_response",
    "LeagueAverageReceiverSeparation": ".game_center_response",
    "LeagueAverageSeparationToQb": ".game_center_response",
    "PassDistanceLeaders": ".game_center_response",
    "PassRushers": ".game_center_response",
    "Passers": ".game_center_response",
    "Receivers": ".game_center_response",
    "Rushers": ".game_center_response",
    "SpeedLeaders": ".game_center_response",
    "TimeToSackLeaders": ".game_center_response",
    "GamecenterSchedule": ".entities.game_center_schedule",
    "GameDetail": ".entities.game_detail",
    "Content": ".entities.game_insight",
    "GameInsight": ".entities.game_insight",
    "GameLocationEnum": ".enums.game_location_enum",
    "GameOdds": ".entities.game_odds",
    "GamePreviewResponse": ".responses.game_preview_response",
    "Preview": ".game_preview_response",
    "GamePhaseEnum": ".enums.game_phase_enum",
    "GameResultEnum": ".enums.game_result_enum",
    "GameSchedule": ".entities.game_schedule",
    "GameScore": ".entities.game_score",
    "Phase": ".entities.game_score",
    "GameSite": ".entities.game_site",
    "GamesResponse": ".responses.games_response",
    "GameStatsResponse": ".responses.game_stats_response",
    "GameStatsResponseData": ".responses.game_stats_response",
    "GameStatusEnum": ".enums.game_status_enum",
    "GameTeam": ".entities.game_team",
    "Score": ".entities.game_team",
    "GetCoachesFilmVideosRequest": ".requests.get_coaches_film_videos_op",
    "GetDefensiveOverviewStatsBySeasonRequest": ".requests.get_defensive_overview_stats_by_season_op",
    "GetDefensiveOverviewStatsBySeasonSortKey": ".get_defensive_overview_stats_by_season_op",
    "GetDefensiveOverviewStatsByWeekRequest": ".requests.get_defensive_overview_stats_by_week_op",
    "GetDefensiveOverviewStatsByWeekSortKey": ".get_defensive_overview_stats_by_week_op",
    "GetDefensivePassRushStatsByWeekRequest": ".requests.get_defensive_passrush_stats_by_week_op",
    "GetDefensivePassRushStatsByWeekSortKey": ".get_defensive_passrush_stats_by_week_op",
    "GetDefensivePassRushStatsBySeasonRequest": ".requests.get_defensive_passrush_stats_by_season_op",
    "GetDefensivePassRushStatsBySeasonSortKey": ".get_defensive_passrush_stats_by_season_op",
    "GetDefensiveNearestDefenderStatsBySeasonRequest": ".requests.get_defensive_nearest_defender_stats_by_season_op",
    "GetDefensiveNearestDefenderStatsBySeasonSortKey": ".get_defensive_nearest_defender_stats_by_season_op",
    "GetDefensiveNearestDefenderStatsByWeekRequest": ".requests.get_defensive_nearest_defender_stats_by_week_op",
    "GetDefensiveNearestDefenderStatsByWeekSortKey": ".get_defensive_nearest_defender_stats_by_week_op",
    "GetDefensiveStatsBySeasonRequest": ".requests.get_defensive_stats_by_season_op",
    "GetDefensiveStatsBySeasonSortKey": ".get_defensive_stats_by_season_op",
    "GetDraftInfoRequest": ".requests.get_draft_info_op",
    "GetDraftPicksReportRequest": ".requests.get_draft_picks_report_op",
    "GetFantasyStatsBySeasonPositionGroup": ".get_fantasy_stats_by_season_op",
    "GetFantasyStatsBySeasonRequest": ".requests.get_fantasy_stats_by_season_op",
    "GetFantasyStatsBySeasonSortKey": ".get_fantasy_stats_by_season_op",
    "AirYardType": ".get_film_room_plays_op",
    "DefCoverageType": ".get_film_room_plays_op",
    "DefendersInTheBoxType": ".get_film_room_plays_op",
    "DropbackTimeType": ".get_film_room_plays_op",
    "GetFilmroomPlaysRequest": ".requests.get_film_room_plays_op",
    "Personnel": ".get_film_room_plays_op",
    "QbAlignment": ".get_film_room_plays_op",
    "ReceiverAlignment": ".get_film_room_plays_op",
    "RushDirection": ".get_film_room_plays_op",
    "SeparationType": ".get_film_room_plays_op",
    "TargetLocation": ".get_film_room_plays_op",
    "YardsToGoType": ".get_film_room_plays_op",
    "GetFootballBoxScoreRequest": ".requests.get_football_boxscore_op",
    "GetFootballGamesRequest": ".requests.get_football_games_op",
    "GetGamecenterRequest": ".requests.get_game_center_op",
    "GetGameInsightsRequest": ".requests.get_game_insights_op",
    "GetGameMatchupRankingsRequest": ".requests.get_game_matchup_rankings_op",
    "GetGamePreviewRequest": ".requests.get_game_preview_op",
    "GetGameTeamRankingsRequest": ".requests.get_game_team_rankings_op",
    "GetInjuryReportsRequest": ".requests.get_injury_reports_op",
    "GetLiveGameScoresRequest": ".requests.get_live_game_scores_op",
    "GetLiveGameStatsRequest": ".requests.get_live_game_stats_op",
    "GetMultipleRankingsAllTeamsRequest": ".requests.get_multiple_rankings_all_teams_op",
    "GetNgsArticlesRequest": ".requests.get_ngs_news_op",
    "GetNgsChartsRequest": ".requests.get_ngs_content_op",
    "GetNgsCurrentScheduleRequest": ".requests.get_ngs_current_schedule_op",
    "GetNgsGameOverviewRequest": ".requests.get_ngs_game_overview_op",
    "GetNgsHighlightsRequest": ".requests.get_ngs_content_op",
    "GetNgsLeadersRequest": ".requests.get_ngs_leaders_op",
    "GetNgsLiveScoresRequest": ".requests.get_ngs_live_scores_op",
    "GetNgsMixedContentRequest": ".requests.get_ngs_news_op",
    "GetNgsPassingStatsRequest": ".requests.get_ngs_passing_stats_op",
    "GetNgsReceivingStatsRequest": ".requests.get_ngs_receiving_stats_op",
    "GetNgsRushingStatsRequest": ".requests.get_ngs_rushing_stats_op",
    "GetNgsScheduleRequest": ".requests.get_ngs_schedule_op",
    "GetNgsSeasonLeadersRequest": ".requests.get_ngs_leaders_op",
    "GetNgsTeamsRequest": ".requests.get_ngs_teams_op",
    "GetNgsVideoClipsRequest": ".requests.get_ngs_news_op",
    "GetPlayByPlayRequest": ".requests.get_play_by_play_op",
    "GetPlayListRequest": ".requests.get_play_list",
    "PlaylistResponse": ".responses.playlist_response",
    "GetPlayerDetailsRequest": ".requests.get_player_details_op",
    "GetPlayerRequest": ".requests.get_player_op",
    "GetPlayerPassingStatsBySeasonRequest": ".requests.get_player_passing_stats_by_season_op",
    "GetPlayerPassingStatsByWeekRequest": ".requests.get_player_passing_stats_by_week_op",
    "GetPlayerReceivingStatsBySeasonRequest": ".requests.get_player_receiving_stats_by_season_op",
    "GetPlayerReceivingStatsByWeekRequest": ".requests.get_player_receiving_stats_by_week_op",
    "GetPlayerRushingStatsBySeasonRequest": ".requests.get_player_rushing_stats_by_season_op",
    "GetPlayerRushingStatsBySeasonSortKey": ".get_player_rushing_stats_by_season_op",
    "GetPlayerRushingStatsByWeekRequest": ".requests.get_player_rushing_stats_by_week_op",
    "GetPlayerRushingStatsByWeekSortKey": ".get_player_rushing_stats_by_week_op",
    "GetPlayersTeamRosterRequest": ".requests.get_players_team_roster_op",
    "GameID": ".get_plays_win_probability_op",
    "GetPlaysWinProbabilityRequest": ".requests.get_plays_win_probability_op",
    "GetPlaysWinProbabilityResponse": ".requests.get_plays_win_probability_op",
    "GetProjectedStatsRequest": ".requests.get_projected_stats_op",
    "GetScheduledGameRequest": ".requests.get_scheduled_game_op",
    "GetScheduledGamesRequest": ".requests.get_scheduled_games_op",
    "GetScheduleSeasonWeeksRequest": ".requests.get_schedule_season_weeks_op",
    "GetSeasonContentInsightsRequest": ".requests.get_season_content_insights_op",
    "Tag": ".get_season_content_insights_op",
    "GetSeasonPlayerStatsPosition": ".get_season_player_stats_op",
    "GetSeasonPlayerStatsRequest": ".requests.get_season_player_stats_op",
    "StatCategory": ".get_season_player_stats_op",
    "GetSeasonWeeksRequest": ".requests.get_season_weeks_op",
    "GetStandingsRequest": ".requests.get_standings_op",
    "GetStatsBoxscoreRequest": ".requests.get_stats_boxscore_op",
    "GetSummaryPlayRequest": ".requests.get_summary_play_op",
    "GetTeamDefensePassStatsBySeasonRequest": ".requests.get_team_defense_pass_stats_by_season_op",
    "GetTeamDefensePassStatsBySeasonSortKey": ".get_team_defense_pass_stats_by_season_op",
    "GetTeamDefenseRushStatsBySeasonRequest": ".requests.get_team_defense_rush_stats_by_season_op",
    "GetTeamDefenseRushStatsBySeasonSortKey": ".get_team_defense_rush_stats_by_season_op",
    "GetTeamDefenseStatsBySeasonRequest": ".requests.get_team_defense_stats_by_season_op",
    "GetTeamDefenseStatsBySeasonSortKey": ".get_team_defense_stats_by_season_op",
    "GetTeamDefenseStatsBySeasonSplit": ".get_team_defense_stats_by_season_op",
    "GetTeamDefensePassStatsByWeekRequest": ".requests.get_team_defense_pass_stats_by_week_op",
    "GetTeamDefensePassStatsByWeekSortKey": ".get_team_defense_pass_stats_by_week_op",
    "GetTeamDefenseRushStatsByWeekRequest": ".requests.get_team_defense_rush_stats_by_week_op",
    "GetTeamDefenseRushStatsByWeekSortKey": ".get_team_defense_rush_stats_by_week_op",
    "GetTeamDefenseStatsByWeekRequest": ".requests.get_team_defense_stats_by_week_op",
    "GetTeamDefenseStatsByWeekSortKey": ".get_team_defense_stats_by_week_op",
    "GetTeamDefenseStatsByWeekSplit": ".get_team_defense_stats_by_week_op",
    "GetTeamInjuriesRequest": ".requests.get_team_injuries_op",
    "GetTeamOffenseStatsBySeasonRequest": ".requests.get_team_offense_overview_stats_by_season_op",
    "GetTeamOffenseStatsBySeasonSortKey": ".get_team_offense_overview_stats_by_season_op",
    "GetTeamOffenseStatsBySeasonSplit": ".get_team_offense_overview_stats_by_season_op",
    "GetTeamOffenseStatsByWeekRequest": ".requests.get_team_offense_overview_stats_by_week_op",
    "GetTeamOffenseStatsByWeekSortKey": ".get_team_offense_overview_stats_by_week_op",
    "GetTeamOffenseStatsByWeekSplit": ".get_team_offense_overview_stats_by_week_op",
    "GetTeamOffensePassStatsBySeasonRequest": ".requests.get_team_offense_pass_stats_by_season_op",
    "GetTeamOffensePassStatsBySeasonSortKey": ".get_team_offense_pass_stats_by_season_op",
    "GetTeamOffensePassStatsByWeekRequest": ".requests.get_team_offense_pass_stats_by_week_op",
    "GetTeamOffensePassStatsByWeekSortKey": ".get_team_offense_pass_stats_by_week_op",
    "GetTeamOffenseRushStatsBySeasonRequest": ".requests.get_team_offense_rush_stats_by_season_op",
    "GetTeamOffenseRushStatsBySeasonSortKey": ".get_team_offense_rush_stats_by_season_op",
    "GetTeamOffenseRushStatsByWeekRequest": ".requests.get_team_offense_rush_stats_by_week_op",
    "GetTeamOffenseRushStatsByWeekSortKey": ".get_team_offense_rush_stats_by_week_op",
    "GetTeamRosterRequest": ".requests.get_team_roster_op",
    "GetTeamScheduleRequest": ".requests.get_team_schedule_op",
    "GetTeamStandingsRequest": ".requests.get_team_standings_op",
    "GetTeamNeedsRequest": ".requests.get_team_needs_op",
    "GetTransactionsRequest": ".requests.get_transactions_op",
    "GetTransactionsTransactionType": ".get_transactions_op",
    "GetVenuesRequest": ".requests.get_venues_op",
    "GetWeeklyBettingOddsRequest": ".requests.get_weekly_betting_odds_op",
    "GetWeeklyGameDetailsRequest": ".requests.get_weekly_game_details_op",
    "GetWeeklyTeamRosterRequest": ".requests.get_weekly_team_roster_op",
    "GetWinProbabilityMinRequest": ".requests.get_win_probability_min_op",
    "HomeFilmCardsResponse": ".home_filmcards_response",
    "InjuryEntry": ".entities.injury_entry",
    "InjuryEntryGameStatus": ".entities.injury_entry",
    "PracticeStatus": ".entities.injury_entry",
    "InjuryReportResponse": ".responses.injury_report_response",
    "Insight": ".entities.insight",
    "InsightPosition": ".entities.insight",
    "SecondTeamType": ".entities.insight",
    "KickingStats": ".entities.kicking_stats",
    "AwayTeam": ".entities.live_game",
    "HomeTeam": ".entities.live_game",
    "LiveGame": ".entities.live_game",
    "LiveScoresResponse": ".responses.lives_cores_response",
    "MatchupRankingsResponse": ".responses.matchup_rankings_response",
    "MeridiemEnum": ".enums.meridiem_enum",
    "MoneyLine": ".entities.moneyline",
    "MultipleRankingsCategory": ".entities.multiple_rankings_category",
    "MultipleRankingsCategoryPagination": ".entities.multiple_rankings_category",
    "NFLAuth": ".entities.nfl_auth",
    "NgsCurrentScheduleResponse": ".responses.ngs_current_schedule_response",
    "NgsGameScoreDetail": ".responses.ngs_live_scores_response",
    "NgsLiveGameScore": ".responses.ngs_live_scores_response",
    "NgsLiveScoresResponse": ".responses.ngs_live_scores_response",
    "NgsTeamInfo": ".responses.ngs_live_scores_response",
    "NgsTeamScore": ".responses.ngs_live_scores_response",
    # NGS Entity models
    "NgsArticlesResponse": ".responses.ngs_news_response",
    "NgsChart": ".entities.ngs_content",
    "NgsChartPlayer": ".entities.ngs_content",
    "NgsChartPlayersResponse": ".responses.ngs_content_response",
    "NgsChartsResponse": ".responses.ngs_content_response",
    "NgsCompletionLeader": ".entities.ngs_leaders",
    "NgsCompletionLeaderEntry": ".entities.ngs_leaders",
    "NgsCompletionLeadersResponse": ".responses.ngs_leaders_response",
    "NgsContentItem": ".entities.ngs_news",
    "NgsContentMetadata": ".entities.ngs_news",
    "NgsContentPagination": ".entities.ngs_news",
    "NgsContentTag": ".entities.ngs_news",
    "NgsDistanceLeader": ".entities.ngs_leaders",
    "NgsDistanceLeaderEntry": ".entities.ngs_leaders",
    "NgsDistanceLeadersResponse": ".responses.ngs_leaders_response",
    "NgsERYLeader": ".entities.ngs_leaders",
    "NgsERYLeaderEntry": ".entities.ngs_leaders",
    "NgsERYLeadersResponse": ".responses.ngs_leaders_response",
    "NgsGameCenterOverviewResponse": ".responses.ngs_game_overview_response",
    "NgsGameLeaders": ".entities.ngs_game_overview",
    "NgsGamePassDistanceLeader": ".entities.ngs_game_overview",
    "NgsGameSackLeader": ".entities.ngs_game_overview",
    "NgsGameScheduleInfo": ".entities.ngs_game_overview",
    "NgsGameSpeedLeader": ".entities.ngs_game_overview",
    "NgsHighlight": ".entities.ngs_content",
    "NgsHighlightsResponse": ".responses.ngs_content_response",
    "NgsLeagueAverage": ".entities.ngs_game_overview",
    "NgsMixedContentResponse": ".responses.ngs_news_response",
    "NgsPassDistanceLeadersMap": ".entities.ngs_game_overview",
    "NgsPasserInfo": ".entities.ngs_game_overview",
    "NgsPassersOverview": ".entities.ngs_game_overview",
    "NgsPassInfo": ".entities.ngs_game_overview",
    "NgsPassingStatsResponse": ".responses.ngs_stats_response",
    "NgsPassingStat": ".entities.ngs_stats",
    "NgsPassingZone": ".entities.ngs_game_overview",
    "NgsPassRusherInfo": ".entities.ngs_game_overview",
    "NgsPassRushersOverview": ".entities.ngs_game_overview",
    "NgsPlay": ".entities.ngs_play",
    "NgsPlayStat": ".entities.ngs_play",
    "NgsReceptionInfo": ".entities.ngs_game_overview",
    "NgsReceiverInfo": ".entities.ngs_game_overview",
    "NgsReceiversOverview": ".entities.ngs_game_overview",
    "NgsReceivingStatsResponse": ".responses.ngs_stats_response",
    "NgsReceivingStat": ".entities.ngs_stats",
    "NgsRushersOverview": ".entities.ngs_game_overview",
    "NgsRusherInfo": ".entities.ngs_game_overview",
    "NgsRushInfo": ".entities.ngs_game_overview",
    "NgsRushingStatsResponse": ".responses.ngs_stats_response",
    "NgsRushingStat": ".entities.ngs_stats",
    "NgsRushLocationStats": ".entities.ngs_game_overview",
    "NgsSackLeader": ".entities.ngs_leaders",
    "NgsSackLeaderEntry": ".entities.ngs_leaders",
    "NgsSackLeadersMap": ".entities.ngs_game_overview",
    "NgsSackLeadersResponse": ".responses.ngs_leaders_response",
    "NgsSpeedLeader": ".entities.ngs_leaders",
    "NgsSpeedLeaderEntry": ".entities.ngs_leaders",
    "NgsSpeedLeadersMap": ".entities.ngs_game_overview",
    "NgsSpeedLeadersResponse": ".responses.ngs_leaders_response",
    "NgsTackleInfo": ".entities.ngs_game_overview",
    "NgsTackleLeader": ".entities.ngs_leaders",
    "NgsTackleLeaderEntry": ".entities.ngs_leaders",
    "NgsTackleLeadersResponse": ".responses.ngs_leaders_response",
    "NgsThumbnail": ".entities.ngs_news",
    "NgsVideosResponse": ".responses.ngs_news_response",
    "NgsYACLeader": ".entities.ngs_leaders",
    "NgsYACLeaderEntry": ".entities.ngs_leaders",
    "NgsYACLeadersResponse": ".responses.ngs_leaders_response",
    "OddsSelection": ".entities.odds_selection",
    "OffensivePlayerPositionEnum": ".enums.offensive_player_position_enum",
    "OffensiveSkillPositionEnum": ".enums.offensive_skill_position_enum",
    "OverallRecord": ".entities.overall_record",
    "OverallRecordPoints": ".entities.overall_record",
    "OverallRecordType": ".entities.overall_record",
    "Streak": ".entities.overall_record",
    "Pagination": ".entities.pagination",
    "PasserStats": ".entities.passer_stats",
    "Zone": ".entities.passer_stats",
    "PassingStats": ".entities.passing_stats",
    "PassingStatsCategoryEnum": ".enums.passing_stats_category_enum",
    "PassingStatsResponse": ".responses.passing_stats_response",
    "PassRushStatsResponse": ".responses.pass_rush_stats_response",
    "NearestDefenderStatsResponse": ".responses.nearest_defender_stats_response",
    "Penalty": ".entities.penalty",
    "Play": ".entities.play",
    "PlayType": ".entities.play",
    "PlayByPlayResponse": ".responses.play_by_play_response",
    "PlayDetail": ".entities.play_detail",
    "PlayDirection": ".entities.play_detail",
    "PlayState": ".entities.play_detail",
    "Player": ".entities.player",
    "PlayerDetail": ".entities.player_detail",
    "PlayerGameStats": ".entities.player_game_stats",
    "PlayerPassingStats": ".entities.player_passing_stats",
    "PlayerProjection": ".entities.player_projection",
    "Relationships": ".entities.player_projection",
    "RelationshipsTypePlayerWeekProjectedPoints": ".entities.player_projection",
    "RelationshipsTypePlayerWeekProjectedStats": ".entities.player_projection",
    "TypePlayer": ".entities.player_projection",
    "WeekPoint": ".entities.player_projection",
    "WeekStat": ".entities.player_projection",
    "PlayerReceivingStats": ".entities.player_receiving_stats",
    "PlayerRushingStats": ".entities.player_rushing_stats",
    "PlayerSearchResponse": ".player_search_response",
    "PlayerSearchResult": ".entities.player_search_result",
    "PlayerStatsResponse": ".player_stats_response",
    "PlayerStatsResponsePagination": ".player_stats_response",
    "PlayerStatsResponsePlayer": ".player_stats_response",
    "PlayerStatsResponseStats": ".player_stats_response",
    "PlayerWeekProjectedPoints": ".entities.player_week_projected_points",
    "PlayerWeekProjectedPointsAttributes": ".entities.player_week_projected_points",
    "PlayerWeekProjectedPointsType": ".entities.player_week_projected_points",
    "PlayerWeekProjectedStats": ".entities.player_week_projected_stats",
    "PlayerWeekProjectedStatsAttributes": ".entities.player_week_projected_stats",
    "PlayerWeekProjectedStatsType": ".entities.player_week_projected_stats",
    "PlayParticipant": ".entities.play_participant",
    "PlayParticipantStats": ".entities.play_participant",
    "Role": ".entities.play_participant",
    "PlayPlayer": ".entities.play_player",
    "PlayStat": ".entities.play_stat",
    "PlaySummaryResponse": ".responses.play_summary_response",
    "PlayTypeEnum": ".enums.play_type_enum",
    "PlayWinProbability": ".entities.play_win_probability",
    "PointSpread": ".entities.point_spread",
    "PointsRecord": ".entities.points_record",
    "PointsRecordPoints": ".entities.points_record",
    "PracticeStatusEnum": ".enums.practice_status_enum",
    "QuarterEnum": ".enums.quarter_enum",
    "ProGame": ".entities.pro_game",
    "ProGameCategory": ".entities.pro_game",
    "ProGameExtension": ".entities.pro_game",
    "ProGameStatus": ".entities.pro_game",
    "Included": ".projected_stats_response",
    "Meta": ".projected_stats_response",
    "Page": ".projected_stats_response",
    "ProjectedStatsResponse": ".responses.projected_stats_response",
    "ProjectedStatsResponsePagination": ".responses.projected_stats_response",
    "ProTeam": ".entities.pro_team",
    "ProTeamConferenceAbbr": ".entities.pro_team",
    "ProTeamTeamType": ".entities.pro_team",
    "ProWeek": ".entities.pro_week",
    "ProWeekWeekType": ".entities.pro_week",
    "ReceivingStats": ".entities.receiving_stats",
    "ReceivingStatsCategoryEnum": ".enums.receiving_stats_category_enum",
    "ReceivingStatsResponse": ".responses.receiving_stats_response",
    "Record": ".entities.record",
    "RefreshTokenRequest": ".requests.refresh_token_request",
    "RefreshTokenRequestNetworkType": ".requests.refresh_token_request",
    "ResponseMetadata": ".entities.response_metadata",
    "Roster": ".roster_response",
    "RosterResponse": ".roster_response",
    "RushingStats": ".entities.rushing_stats",
    "RushingStatsResponse": ".responses.rushing_stats_response",
    "ScheduledGame": ".entities.scheduled_game",
    "ScheduleTeam": ".entities.schedule_team",
    "ScoreType": ".entities.scoring_play",
    "ScoringPlay": ".entities.scoring_play",
    "SearchPlayersRequest": ".entities.search_players_op",
    "SeasonStats": ".entities.season_stats",
    "SeasonTypeEnum": ".enums.season_type_enum",
    "SeasonWeeksResponse": ".responses.season_weeks_response",
    "Security": ".entities.security",
    "Site": ".entities.site",
    "SiteRoofTypeEnum": ".enums.site_roof_type_enum",
    "SocialMedia": ".entities.social_media",
    "SortOrderEnum": ".enums.sort_order_enum",
    "Standings": ".entities.standings",
    "StandingsTeam": ".entities.standings",
    "StandingsRecord": ".entities.standings_record",
    "StandingsRecordPoints": ".entities.standings_record",
    "StandingsResponse": ".responses.standings_response",
    "StandingsResponseWeek": ".responses.standings_response",
    "Statistic": ".entities.statistic_ranking",
    "StatisticRanking": ".entities.statistic_ranking",
    "Team": ".entities.team",
    "TeamConferenceAbbr": ".entities.team",
    "TeamTeamType": ".entities.team",
    "TeamBoxscore": ".entities.team_boxscore",
    "TeamDefensePassStats": ".entities.team_defense_pass_stats",
    "TeamDefensePassStatsResponse": ".responses.team_defense_pass_stats_response",
    "TeamDefenseRushStats": ".entities.team_defense_rush_stats",
    "TeamDefenseRushStatsResponse": ".responses.team_defense_rush_stats_response",
    "TeamDefenseStats": ".entities.team_defense_stats",
    "TeamDefenseStatsResponse": ".responses.team_defense_stats_response",
    "TeamGameStats": ".entities.team_game_stats",
    "TeamInfo": ".entities.team_info",
    "TeamInjuryReport": ".entities.team_injury_report",
    "TeamMatchupRankings": ".entities.team_matchup_rankings",
    "TeamNeedsResponse": ".responses.team_needs_response",
    "TeamOffenseStats": ".entities.team_offense_overview_stats",
    "TeamOffenseStatsResponse": ".responses.team_offense_overview_stats_response",
    "TeamOffensePassStats": ".entities.team_offense_pass_stats",
    "TeamOffensePassStatsResponse": ".responses.team_offense_pass_stats_response",
    "TeamOffenseRushStats": ".entities.team_offense_rush_stats",
    "TeamOffenseRushStatsResponse": ".responses.team_offense_rush_stats_response",
    "TeamRankingEntry": ".entities.team_ranking_entry",
    "TeamRankings": ".entities.team_rankings",
    "TeamRankingsResponse": ".responses.team_rankings_response",
    "TeamRosterResponse": ".responses.team_roster_response",
    "TeamScore": ".entities.team_score",
    "TeamTypeEnum": ".enums.team_type_enum",
    "TeamVenue": ".entities.team_venue",
    "TicketVendor": ".entities.ticket_vendor",
    "TokenRequest": ".requests.token_request",
    "TokenRequestNetworkType": ".requests.token_request",
    "TokenResponse": ".responses.token_response",
    "Totals": ".entities.totals",
    "Transaction": ".entities.transaction",
    "TransactionType": ".entities.transaction",
    "TransactionsResponse": ".responses.transactions_response",
    "Venue": ".entities.venue",
    "VenueInfo": ".entities.venue_info",
    "VenueInfoRoofType": ".entities.venue_info",
    "VenuesResponse": ".responses.venues_response",
    "NFLPLUSPLUSNFLPLUSCOACHESFILM": ".entities.video_authorizations",
    "NFLPLUSPremiumNFLPLUSCOACHESFILM": ".entities.video_authorizations",
    "NflPlusPlus": ".entities.video_authorizations",
    "NflPlusPlusRequirements": ".entities.video_authorizations",
    "NflPlusPremium": ".entities.video_authorizations",
    "NflPlusPremiumRequirements": ".entities.video_authorizations",
    "ProPremium": ".entities.video_authorizations",
    "ProPremiumNFLPLUSCOACHESFILM": ".entities.video_authorizations",
    "ProPremiumRequirements": ".entities.video_authorizations",
    "VideoAuthorizations": ".entities.video_authorizations",
    "VideoGamePlayIds": ".entities.video_game_play_ids",
    "VideoTag": ".entities.video_tag",
    "VideoThumbnail": ".entities.video_thumbnail",
    "Week": ".entities.week",
    "WeekWeekType": ".entities.week",
    "DriveChart": ".entities.weekly_game_detail",
    "Replay": ".entities.weekly_game_detail",
    "Summary": ".entities.weekly_game_detail",
    "TaggedVideos": ".entities.weekly_game_detail",
    "WeeklyGameDetail": ".entities.weekly_game_detail",
    "WeeklyGameDetailCategory": ".entities.weekly_game_detail",
    "WeeklyGameDetailExtension": ".entities.weekly_game_detail",
    "WeeklyGameDetailStatus": ".entities.weekly_game_detail",
    "WeeklyOddsResponse": ".responses.weekly_odds_response",
    "WeeklyPassingStatsResponse": ".responses.weekly_passing_stats_response",
    "WeeklyPlayer": ".entities.weekly_player",
    "WeeklyPlayerPassingStats": ".entities.weekly_player_passing_stats",
    "WeeklyPlayerRushingStats": ".entities.weekly_player_rushing_stats",
    "WeeklyRosterResponse": ".responses.weekly_roster_response",
    "WeeklyRushingStatsResponse": ".responses.weekly_rushing_stats_response",
    "WeekSlugEnum": ".enums.week_slug_enum",
    "WeeksResponse": ".responses.weeks_response",
    "WinProbabilityResponse": ".responses.win_probability_response",
    "YardsToGoEnum": ".enums.yards_to_go_enum",
    # Historical stats
    "GetHistoricalTeamStatsRequest": ".requests.get_historical_team_stats_op",
    "GetHistoricalPlayerStatsRequest": ".requests.get_historical_player_stats_op",
    "HistoricalTeamStatsResponse": ".responses.historical_team_stats_response",
    "HistoricalStatCategories": ".entities.historical_stat_categories",
    "HistoricalGameInfo": ".responses.historical_team_stats_response",
    "HistoricalPlayerStatsResponse": ".responses.historical_player_stats_response",
    "PersonStat": ".responses.historical_player_stats_response",
    "PersonStatLineup": ".responses.historical_player_stats_response",
    # Live stats
    "GetLiveTeamStatisticsRequest": ".requests.get_live_team_statistics_op",
    "GetLivePlayerStatisticsRequest": ".requests.get_live_player_statistics_op",
    "LiveTeamStatisticsResponse": ".responses.live_team_statistics_response",
    "LiveTeamStatEntry": ".entities.live_stat_entries",
    "LivePlayerStatisticsResponse": ".responses.live_player_statistics_response",
    "LivePlayerStatEntry": ".entities.live_stat_entries",
    "LivePlayerTeamEntry": ".entities.live_stat_entries",
    # Experience
    "GetGameDetailsBySlugRequest": ".requests.get_game_details_by_slug_op",
    "GetGameDetailsRequest": ".requests.get_game_details_op",
    # Content
    "GetVideoReplaysRequest": ".requests.get_video_replays_op",
    "VideoReplaysResponse": ".responses.video_replays_response",
}


def __getattr__(attr_name: str) -> object:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(
            f"No {attr_name} found in _dynamic_imports for module name -> {__name__} "
        )

    try:
        module = dynamic_import(module_name, __package__)
        result = getattr(module, attr_name)
        return result
    except ImportError as e:
        raise ImportError(
            f"Failed to import {attr_name} from {module_name}: {e}"
        ) from e
    except AttributeError as e:
        raise AttributeError(
            f"Failed to get {attr_name} from {module_name}: {e}"
        ) from e


def __dir__():
    lazy_attrs = builtins.list(_dynamic_imports.keys())
    return builtins.sorted(lazy_attrs)
