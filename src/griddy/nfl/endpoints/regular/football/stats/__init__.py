from typing import TYPE_CHECKING, Optional

from griddy.core._lazy_load import LazySubSDKMixin
from griddy.nfl.basesdk import BaseSDK
from griddy.nfl.sdkconfiguration import SDKConfiguration

if TYPE_CHECKING:
    from griddy.nfl.endpoints.regular.football.stats.historical import HistoricalStats
    from griddy.nfl.endpoints.regular.football.stats.live import LiveStats


class FootballStatsSDK(LazySubSDKMixin, BaseSDK):
    r"""Aggregates historical and live football statistics endpoints"""

    historical: "HistoricalStats"
    r"""Historical game statistics (team and player level)"""
    live: "LiveStats"
    r"""Live game statistics (team and player level)"""

    _sub_sdk_map = {
        "historical": (
            "griddy.nfl.endpoints.regular.football.stats.historical",
            "HistoricalStats",
        ),
        "live": (
            "griddy.nfl.endpoints.regular.football.stats.live",
            "LiveStats",
        ),
    }

    def __init__(self, sdk_config: SDKConfiguration, parent_ref: Optional[object]):
        super().__init__(sdk_config=sdk_config, parent_ref=parent_ref)
