from typing import TYPE_CHECKING, Optional

from griddy.nfl._lazy_load import LazySubSDKMixin
from griddy.nfl.endpoints.pro import ProSDK
from griddy.nfl.sdkconfiguration import SDKConfiguration

if TYPE_CHECKING:
    from griddy.nfl.endpoints.pro.stats.defense import PlayerDefenseStats
    from griddy.nfl.endpoints.pro.stats.fantasy import Fantasy
    from griddy.nfl.endpoints.pro.stats.passing import PlayerPassingStats
    from griddy.nfl.endpoints.pro.stats.receiving import PlayerReceivingStats
    from griddy.nfl.endpoints.pro.stats.rushing import PlayerRushingStats
    from griddy.nfl.endpoints.pro.stats.team_defense import TeamDefenseStats
    from griddy.nfl.endpoints.pro.stats.team_offense import TeamOffenseStats


class StatsSDK(LazySubSDKMixin, ProSDK):
    r"""Aggregates all player and team statistics endpoints"""

    passing: "PlayerPassingStats"
    r"""Player passing statistics"""
    receiving: "PlayerReceivingStats"
    r"""Player receiving statistics"""
    rushing: "PlayerRushingStats"
    r"""Player rushing statistics"""
    defense: "PlayerDefenseStats"
    r"""Player defensive statistics"""
    team_offense: "TeamOffenseStats"
    r"""Team offensive statistics"""
    team_defense: "TeamDefenseStats"
    r"""Team defensive statistics"""
    fantasy: "Fantasy"
    r"""Fantasy statistics"""

    _sub_sdk_map = {
        "passing": (
            "griddy.nfl.endpoints.pro.stats.passing",
            "PlayerPassingStats",
        ),
        "receiving": (
            "griddy.nfl.endpoints.pro.stats.receiving",
            "PlayerReceivingStats",
        ),
        "rushing": (
            "griddy.nfl.endpoints.pro.stats.rushing",
            "PlayerRushingStats",
        ),
        "defense": (
            "griddy.nfl.endpoints.pro.stats.defense",
            "PlayerDefenseStats",
        ),
        "team_offense": (
            "griddy.nfl.endpoints.pro.stats.team_offense",
            "TeamOffenseStats",
        ),
        "team_defense": (
            "griddy.nfl.endpoints.pro.stats.team_defense",
            "TeamDefenseStats",
        ),
        "fantasy": (
            "griddy.nfl.endpoints.pro.stats.fantasy",
            "Fantasy",
        ),
    }

    def __init__(self, sdk_config: SDKConfiguration, parent_ref: Optional[object]):
        super().__init__(sdk_config=sdk_config, parent_ref=parent_ref)
