import builtins
from typing import TYPE_CHECKING

from griddy.core._import import dynamic_import

if TYPE_CHECKING:
    from griddy.pfr.models.base import PFRBaseModel
    from griddy.pfr.models.entities.awards import (
        AwardHistory,
        AwardWinner,
        HallOfFame,
        HofPlayer,
        ProBowlPlayer,
        ProBowlRoster,
    )
    from griddy.pfr.models.entities.birthdays import (
        BirthdayPlayer,
        Birthdays,
    )
    from griddy.pfr.models.entities.birthplaces import (
        BirthplaceFiltered,
        BirthplaceLanding,
        BirthplaceLocation,
        BirthplacePlayer,
    )
    from griddy.pfr.models.entities.coach_profile import (
        ChallengeResult,
        CoachBio,
        CoachingHistoryEntry,
        CoachingRank,
        CoachingResult,
        CoachingResultTotal,
        CoachingTreeEntry,
        CoachProfile,
    )
    from griddy.pfr.models.entities.cups_of_coffee import (
        CoffeeEntry,
        CupsOfCoffee,
    )
    from griddy.pfr.models.entities.draft import (
        CombineEntry,
        CombineResults,
        DraftPick,
        TeamDraft,
        TeamDraftPick,
        YearDraft,
    )
    from griddy.pfr.models.entities.executive_profile import (
        ExecutiveBio,
        ExecutiveProfile,
        ExecutiveResult,
        ExecutiveResultsTotal,
    )
    from griddy.pfr.models.entities.fantasy import (
        FantasyMatchupPlayer,
        FantasyMatchups,
        FantasyPlayer,
        FantasyPointsAllowed,
        FantasyPointsAllowedTeam,
        RedZonePassing,
        RedZonePassingPlayer,
        RedZoneReceiving,
        RedZoneReceivingPlayer,
        RedZoneRushing,
        RedZoneRushingPlayer,
        TopFantasyPlayers,
    )
    from griddy.pfr.models.entities.game_details import (
        Drive,
        ExpectedPoints,
        GameDetails,
        LinescoreEntry,
        PlayerDefense,
        PlayerKicking,
        PlayerOffense,
        PlayerReturn,
        Scorebox,
        ScoreboxMeta,
        ScoreboxTeam,
        ScoringPlay,
        SnapCount,
        Starter,
    )
    from griddy.pfr.models.entities.last_undefeated import (
        LastUndefeated,
        LastUndefeatedEntry,
    )
    from griddy.pfr.models.entities.leaders import (
        Leaderboard,
        LeaderEntry,
    )
    from griddy.pfr.models.entities.multi_sport_players import (
        MultiSportPlayer,
        MultiSportPlayers,
        OtherSportLink,
    )
    from griddy.pfr.models.entities.multi_team_players import (
        MultiTeamPlayers,
        MultiTeamPlayerStats,
        StatsTable,
        TopPlayerSummary,
    )
    from griddy.pfr.models.entities.non_qb_passers import (
        NonQBPasserEntry,
        NonQBPassers,
    )
    from griddy.pfr.models.entities.non_skill_pos_td import (
        NonSkillPosTdEntry,
        NonSkillPosTdScorers,
    )
    from griddy.pfr.models.entities.octopus_tracker import (
        OctopusEntry,
        OctopusTracker,
    )
    from griddy.pfr.models.entities.official_profile import (
        OfficialBio,
        OfficialGame,
        OfficialProfile,
        OfficialSeasonStat,
    )
    from griddy.pfr.models.entities.overtime_ties import (
        OvertimeTieEntry,
        OvertimeTies,
    )
    from griddy.pfr.models.entities.player_profile import (
        BirthPlace,
        DraftInfo,
        JerseyNumber,
        PlayerBio,
        PlayerNames,
        PlayerProfile,
        PlayerStatistics,
        RoundAndOverall,
        Transaction,
    )
    from griddy.pfr.models.entities.players_born_before import (
        PlayerBornBefore,
        PlayersBornBefore,
    )
    from griddy.pfr.models.entities.pronunciation_guide import (
        PronunciationEntry,
        PronunciationGuide,
    )
    from griddy.pfr.models.entities.qb_wins import (
        QBWinEntry,
        QBWins,
    )
    from griddy.pfr.models.entities.schedule_game import (
        ScheduleGame,
    )
    from griddy.pfr.models.entities.schools import (
        College,
        CollegeList,
        HighSchool,
        HighSchoolList,
    )
    from griddy.pfr.models.entities.season import (
        ConferenceStanding,
        PlayoffGame,
        PlayoffStanding,
        SeasonOverview,
        SeasonStats,
        WeekGame,
        WeekSummary,
    )
    from griddy.pfr.models.entities.security import Security
    from griddy.pfr.models.entities.stadium import (
        StadiumBestGame,
        StadiumBio,
        StadiumGameLeader,
        StadiumGameSummary,
        StadiumLeader,
        StadiumProfile,
        StadiumTeam,
    )
    from griddy.pfr.models.entities.standings_on_date import (
        StandingsOnDate,
        StandingsTeamEntry,
    )
    from griddy.pfr.models.entities.statistical_milestones import (
        CareerLeader,
        MilestoneEntry,
        StatisticalMilestones,
    )
    from griddy.pfr.models.entities.superbowl import (
        SuperBowlGame,
        SuperBowlHistory,
        SuperBowlLeaderEntry,
        SuperBowlLeaders,
        SuperBowlLeaderTable,
        SuperBowlQB,
        SuperBowlStanding,
        SuperBowlStandings,
    )
    from griddy.pfr.models.entities.team_franchise import (
        Franchise,
        FranchiseLeader,
        FranchiseMeta,
        FranchiseSeasonRecord,
    )
    from griddy.pfr.models.entities.team_season import (
        SeasonGame,
        TeamSeason,
        TeamSeasonMeta,
    )
    from griddy.pfr.models.entities.uniform_numbers import (
        UniformNumberPlayer,
        UniformNumbers,
    )
    from griddy.pfr.models.entities.upcoming_milestones import (
        UpcomingLeaderboardEntry,
        UpcomingMilestoneEntry,
        UpcomingMilestones,
    )

__all__ = [
    "PFRBaseModel",
    "BirthdayPlayer",
    "Birthdays",
    "BirthplaceFiltered",
    "BirthplaceLanding",
    "BirthplaceLocation",
    "BirthplacePlayer",
    "PlayerBornBefore",
    "PlayersBornBefore",
    "NonQBPasserEntry",
    "NonQBPassers",
    "NonSkillPosTdEntry",
    "NonSkillPosTdScorers",
    "OctopusEntry",
    "OctopusTracker",
    "OvertimeTieEntry",
    "OvertimeTies",
    "LastUndefeated",
    "LastUndefeatedEntry",
    "StandingsOnDate",
    "StandingsTeamEntry",
    "CoffeeEntry",
    "CupsOfCoffee",
    "QBWinEntry",
    "QBWins",
    "AwardHistory",
    "AwardWinner",
    "HallOfFame",
    "HofPlayer",
    "ProBowlPlayer",
    "ProBowlRoster",
    "FantasyMatchupPlayer",
    "FantasyMatchups",
    "FantasyPlayer",
    "FantasyPointsAllowed",
    "FantasyPointsAllowedTeam",
    "RedZonePassing",
    "RedZonePassingPlayer",
    "RedZoneReceiving",
    "RedZoneReceivingPlayer",
    "RedZoneRushing",
    "RedZoneRushingPlayer",
    "TopFantasyPlayers",
    "ExecutiveBio",
    "ExecutiveProfile",
    "ExecutiveResult",
    "ExecutiveResultsTotal",
    "CombineEntry",
    "CombineResults",
    "DraftPick",
    "TeamDraft",
    "TeamDraftPick",
    "YearDraft",
    "ChallengeResult",
    "CoachBio",
    "CoachingHistoryEntry",
    "CoachingRank",
    "CoachingResult",
    "CoachingResultTotal",
    "CoachingTreeEntry",
    "CoachProfile",
    "OfficialBio",
    "OfficialGame",
    "OfficialProfile",
    "OfficialSeasonStat",
    "Leaderboard",
    "LeaderEntry",
    "Drive",
    "ExpectedPoints",
    "GameDetails",
    "LinescoreEntry",
    "PlayerDefense",
    "PlayerKicking",
    "PlayerOffense",
    "PlayerReturn",
    "BirthPlace",
    "DraftInfo",
    "JerseyNumber",
    "PlayerBio",
    "PlayerNames",
    "PlayerProfile",
    "PlayerStatistics",
    "RoundAndOverall",
    "ScheduleGame",
    "ConferenceStanding",
    "PlayoffGame",
    "PlayoffStanding",
    "SeasonOverview",
    "SeasonStats",
    "WeekGame",
    "WeekSummary",
    "StadiumBestGame",
    "StadiumBio",
    "StadiumGameLeader",
    "StadiumGameSummary",
    "StadiumLeader",
    "StadiumProfile",
    "StadiumTeam",
    "Scorebox",
    "ScoreboxMeta",
    "ScoreboxTeam",
    "ScoringPlay",
    "FranchiseLeader",
    "FranchiseMeta",
    "FranchiseSeasonRecord",
    "SeasonGame",
    "Security",
    "SnapCount",
    "Starter",
    "Franchise",
    "TeamSeason",
    "TeamSeasonMeta",
    "Transaction",
    "SuperBowlGame",
    "SuperBowlHistory",
    "SuperBowlLeaderEntry",
    "SuperBowlLeaderTable",
    "SuperBowlLeaders",
    "SuperBowlQB",
    "SuperBowlStanding",
    "SuperBowlStandings",
    "College",
    "CollegeList",
    "HighSchool",
    "HighSchoolList",
    "MultiSportPlayer",
    "MultiSportPlayers",
    "OtherSportLink",
    "PronunciationEntry",
    "PronunciationGuide",
    "MultiTeamPlayerStats",
    "MultiTeamPlayers",
    "StatsTable",
    "TopPlayerSummary",
    "CareerLeader",
    "MilestoneEntry",
    "StatisticalMilestones",
    "UniformNumberPlayer",
    "UniformNumbers",
    "UpcomingLeaderboardEntry",
    "UpcomingMilestoneEntry",
    "UpcomingMilestones",
]

_dynamic_imports: dict[str, str] = {
    "PFRBaseModel": ".base",
    "BirthdayPlayer": ".entities.birthdays",
    "Birthdays": ".entities.birthdays",
    "BirthplaceFiltered": ".entities.birthplaces",
    "BirthplaceLanding": ".entities.birthplaces",
    "BirthplaceLocation": ".entities.birthplaces",
    "BirthplacePlayer": ".entities.birthplaces",
    "PlayerBornBefore": ".entities.players_born_before",
    "PlayersBornBefore": ".entities.players_born_before",
    "NonQBPasserEntry": ".entities.non_qb_passers",
    "NonQBPassers": ".entities.non_qb_passers",
    "NonSkillPosTdEntry": ".entities.non_skill_pos_td",
    "NonSkillPosTdScorers": ".entities.non_skill_pos_td",
    "OctopusEntry": ".entities.octopus_tracker",
    "OctopusTracker": ".entities.octopus_tracker",
    "OvertimeTieEntry": ".entities.overtime_ties",
    "OvertimeTies": ".entities.overtime_ties",
    "LastUndefeated": ".entities.last_undefeated",
    "LastUndefeatedEntry": ".entities.last_undefeated",
    "StandingsOnDate": ".entities.standings_on_date",
    "StandingsTeamEntry": ".entities.standings_on_date",
    "CoffeeEntry": ".entities.cups_of_coffee",
    "CupsOfCoffee": ".entities.cups_of_coffee",
    "QBWinEntry": ".entities.qb_wins",
    "QBWins": ".entities.qb_wins",
    "AwardHistory": ".entities.awards",
    "AwardWinner": ".entities.awards",
    "HallOfFame": ".entities.awards",
    "HofPlayer": ".entities.awards",
    "ProBowlPlayer": ".entities.awards",
    "ProBowlRoster": ".entities.awards",
    "FantasyMatchupPlayer": ".entities.fantasy",
    "FantasyMatchups": ".entities.fantasy",
    "FantasyPlayer": ".entities.fantasy",
    "FantasyPointsAllowed": ".entities.fantasy",
    "FantasyPointsAllowedTeam": ".entities.fantasy",
    "RedZonePassing": ".entities.fantasy",
    "RedZonePassingPlayer": ".entities.fantasy",
    "RedZoneReceiving": ".entities.fantasy",
    "RedZoneReceivingPlayer": ".entities.fantasy",
    "RedZoneRushing": ".entities.fantasy",
    "RedZoneRushingPlayer": ".entities.fantasy",
    "TopFantasyPlayers": ".entities.fantasy",
    "ExecutiveBio": ".entities.executive_profile",
    "ExecutiveProfile": ".entities.executive_profile",
    "ExecutiveResult": ".entities.executive_profile",
    "ExecutiveResultsTotal": ".entities.executive_profile",
    "CombineEntry": ".entities.draft",
    "CombineResults": ".entities.draft",
    "DraftPick": ".entities.draft",
    "TeamDraft": ".entities.draft",
    "TeamDraftPick": ".entities.draft",
    "YearDraft": ".entities.draft",
    "ChallengeResult": ".entities.coach_profile",
    "CoachBio": ".entities.coach_profile",
    "CoachingHistoryEntry": ".entities.coach_profile",
    "CoachingRank": ".entities.coach_profile",
    "CoachingResult": ".entities.coach_profile",
    "CoachingResultTotal": ".entities.coach_profile",
    "CoachingTreeEntry": ".entities.coach_profile",
    "CoachProfile": ".entities.coach_profile",
    "OfficialBio": ".entities.official_profile",
    "OfficialGame": ".entities.official_profile",
    "OfficialProfile": ".entities.official_profile",
    "OfficialSeasonStat": ".entities.official_profile",
    "BirthPlace": ".entities.player_profile",
    "DraftInfo": ".entities.player_profile",
    "Leaderboard": ".entities.leaders",
    "LeaderEntry": ".entities.leaders",
    "Drive": ".entities.game_details",
    "ExpectedPoints": ".entities.game_details",
    "GameDetails": ".entities.game_details",
    "JerseyNumber": ".entities.player_profile",
    "LinescoreEntry": ".entities.game_details",
    "PlayerBio": ".entities.player_profile",
    "PlayerDefense": ".entities.game_details",
    "PlayerNames": ".entities.player_profile",
    "PlayerKicking": ".entities.game_details",
    "PlayerOffense": ".entities.game_details",
    "PlayerProfile": ".entities.player_profile",
    "PlayerReturn": ".entities.game_details",
    "PlayerStatistics": ".entities.player_profile",
    "RoundAndOverall": ".entities.player_profile",
    "Scorebox": ".entities.game_details",
    "ScoreboxMeta": ".entities.game_details",
    "ScoreboxTeam": ".entities.game_details",
    "ScoringPlay": ".entities.game_details",
    "ScheduleGame": ".entities.schedule_game",
    "ConferenceStanding": ".entities.season",
    "PlayoffGame": ".entities.season",
    "PlayoffStanding": ".entities.season",
    "SeasonOverview": ".entities.season",
    "SeasonStats": ".entities.season",
    "WeekGame": ".entities.season",
    "WeekSummary": ".entities.season",
    "StadiumBestGame": ".entities.stadium",
    "StadiumBio": ".entities.stadium",
    "StadiumGameLeader": ".entities.stadium",
    "StadiumGameSummary": ".entities.stadium",
    "StadiumLeader": ".entities.stadium",
    "StadiumProfile": ".entities.stadium",
    "StadiumTeam": ".entities.stadium",
    "FranchiseLeader": ".entities.team_franchise",
    "FranchiseMeta": ".entities.team_franchise",
    "FranchiseSeasonRecord": ".entities.team_franchise",
    "SeasonGame": ".entities.team_season",
    "Security": ".entities.security",
    "SnapCount": ".entities.game_details",
    "Starter": ".entities.game_details",
    "Franchise": ".entities.team_franchise",
    "TeamSeason": ".entities.team_season",
    "TeamSeasonMeta": ".entities.team_season",
    "Transaction": ".entities.player_profile",
    "SuperBowlGame": ".entities.superbowl",
    "SuperBowlHistory": ".entities.superbowl",
    "SuperBowlLeaderEntry": ".entities.superbowl",
    "SuperBowlLeaderTable": ".entities.superbowl",
    "SuperBowlLeaders": ".entities.superbowl",
    "SuperBowlQB": ".entities.superbowl",
    "SuperBowlStanding": ".entities.superbowl",
    "SuperBowlStandings": ".entities.superbowl",
    "College": ".entities.schools",
    "CollegeList": ".entities.schools",
    "HighSchool": ".entities.schools",
    "HighSchoolList": ".entities.schools",
    "MultiSportPlayer": ".entities.multi_sport_players",
    "MultiSportPlayers": ".entities.multi_sport_players",
    "OtherSportLink": ".entities.multi_sport_players",
    "PronunciationEntry": ".entities.pronunciation_guide",
    "PronunciationGuide": ".entities.pronunciation_guide",
    "MultiTeamPlayerStats": ".entities.multi_team_players",
    "MultiTeamPlayers": ".entities.multi_team_players",
    "StatsTable": ".entities.multi_team_players",
    "TopPlayerSummary": ".entities.multi_team_players",
    "CareerLeader": ".entities.statistical_milestones",
    "MilestoneEntry": ".entities.statistical_milestones",
    "StatisticalMilestones": ".entities.statistical_milestones",
    "UniformNumberPlayer": ".entities.uniform_numbers",
    "UniformNumbers": ".entities.uniform_numbers",
    "UpcomingLeaderboardEntry": ".entities.upcoming_milestones",
    "UpcomingMilestoneEntry": ".entities.upcoming_milestones",
    "UpcomingMilestones": ".entities.upcoming_milestones",
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
