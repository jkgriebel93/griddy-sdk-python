"""PFR HTML parsers package.

Re-exports the individual parser classes for convenient access::

    from griddy.pfr.utils.parsers import ScheduleParser, GameDetailsParser
"""

from .awards import AwardsParser
from .birthdays import BirthdaysParser
from .birthplaces import BirthplacesParser
from .coach_profile import CoachProfileParser
from .draft import DraftParser
from .executive_profile import ExecutiveProfileParser
from .fantasy import FantasyParser
from .game_details import GameDetailsParser
from .leaders import LeadersParser
from .multi_team_players import MultiTeamPlayersParser
from .non_qb_passers import NonQBPassersParser
from .non_skill_pos_td import NonSkillPosTdParser
from .octopus_tracker import OctopusTrackerParser
from .official_profile import OfficialProfileParser
from .player_profile import PlayerProfileParser
from .players_born_before import PlayersBornBeforeParser
from .qb_wins import QBWinsParser
from .schedule import ScheduleParser
from .schools import SchoolsParser
from .season_overview import SeasonOverviewParser
from .stadium import StadiumParser
from .statistical_milestones import StatisticalMilestonesParser
from .superbowl import SuperBowlParser
from .team_franchise import FranchiseParser
from .team_season import TeamSeasonParser
from .uniform_numbers import UniformNumbersParser
from .upcoming_milestones import UpcomingMilestonesParser

__all__ = [
    "AwardsParser",
    "BirthdaysParser",
    "BirthplacesParser",
    "PlayersBornBeforeParser",
    "CoachProfileParser",
    "DraftParser",
    "ExecutiveProfileParser",
    "FantasyParser",
    "GameDetailsParser",
    "LeadersParser",
    "MultiTeamPlayersParser",
    "NonQBPassersParser",
    "NonSkillPosTdParser",
    "OctopusTrackerParser",
    "OfficialProfileParser",
    "PlayerProfileParser",
    "QBWinsParser",
    "ScheduleParser",
    "SchoolsParser",
    "SeasonOverviewParser",
    "StadiumParser",
    "SuperBowlParser",
    "FranchiseParser",
    "StatisticalMilestonesParser",
    "TeamSeasonParser",
    "UniformNumbersParser",
    "UpcomingMilestonesParser",
]
