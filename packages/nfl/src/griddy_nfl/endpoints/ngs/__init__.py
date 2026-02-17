"""Next Gen Stats (NGS) API endpoints.

This module provides access to NFL Next Gen Stats data from nextgenstats.nfl.com,
including player statistics, game information, charts, highlights, and leaderboards.
"""

import importlib
import sys
from typing import TYPE_CHECKING, Optional

from griddy_nfl.basesdk import BaseSDK
from griddy_nfl.sdkconfiguration import SERVERS, SDKConfiguration

# NGS server URL (also available in SERVERS dict)
NGS_SERVER_URL = SERVERS["ngs"]


if TYPE_CHECKING:
    from griddy_nfl.endpoints.ngs.content import NgsContent
    from griddy_nfl.endpoints.ngs.games import NgsGames
    from griddy_nfl.endpoints.ngs.leaders import NgsLeaders
    from griddy_nfl.endpoints.ngs.league import NgsLeague
    from griddy_nfl.endpoints.ngs.news import NgsNews
    from griddy_nfl.endpoints.ngs.stats import NgsStats


class NgsBaseSDK(BaseSDK):
    """Base SDK for Next Gen Stats endpoints.

    Overrides _resolve_base_url to use nextgenstats.nfl.com.
    """

    def _resolve_base_url(
        self,
        server_url: Optional[str] = None,
        url_variables: Optional[dict] = None,
    ) -> str:
        """Override to use NGS server URL by default."""
        if server_url is not None:
            return server_url
        return NGS_SERVER_URL


class NextGenStats(NgsBaseSDK):
    """Next Gen Stats SDK providing access to NGS data.

    This SDK provides access to NFL Next Gen Stats data including:
    - League schedules and team information
    - Live game scores and game center data
    - Player passing, receiving, and rushing statistics
    - Top plays and leaderboards
    - Charts and highlights
    - News articles and videos

    Usage:
        nfl = GriddyNFL()

        # League data
        schedule = nfl.ngs.league.get_current_schedule()
        teams = nfl.ngs.league.get_teams()

        # Statistics
        passing = nfl.ngs.stats.get_passing_stats(season=2025, season_type="REG")

        # Leaders
        fastest = nfl.ngs.leaders.get_fastest_ball_carriers(season=2025)
    """

    league: "NgsLeague"
    r"""League schedules and team information"""
    games: "NgsGames"
    r"""Live scores and game center data"""
    stats: "NgsStats"
    r"""Player passing, receiving, and rushing statistics"""
    leaders: "NgsLeaders"
    r"""Top plays and leaderboards"""
    content: "NgsContent"
    r"""Charts and highlights"""
    news: "NgsNews"
    r"""News articles and videos (uses api.nfl.com)"""

    _sub_sdk_map = {
        "league": (
            "griddy_nfl.endpoints.ngs.league",
            "NgsLeague",
        ),
        "games": (
            "griddy_nfl.endpoints.ngs.games",
            "NgsGames",
        ),
        "stats": (
            "griddy_nfl.endpoints.ngs.stats",
            "NgsStats",
        ),
        "leaders": (
            "griddy_nfl.endpoints.ngs.leaders",
            "NgsLeaders",
        ),
        "content": (
            "griddy_nfl.endpoints.ngs.content",
            "NgsContent",
        ),
        "news": (
            "griddy_nfl.endpoints.ngs.news",
            "NgsNews",
        ),
    }

    def __getattr__(self, name: str):
        """Lazily load sub-SDKs on first access."""
        if name in self._sub_sdk_map:
            module_path, class_name = self._sub_sdk_map[name]
            try:
                # Dynamic import with retry logic (handles occasional KeyError)
                module = None
                for attempt in range(3):
                    try:
                        module = importlib.import_module(module_path)
                        break
                    except KeyError:
                        sys.modules.pop(module_path, None)
                if module is None:
                    raise ImportError(f"Failed to import {module_path}")

                klass = getattr(module, class_name)
                instance = klass(self.sdk_configuration, parent_ref=self.parent_ref)
                setattr(self, name, instance)
                return instance
            except ImportError as e:
                raise AttributeError(
                    f"Failed to import module {module_path} for attribute {name}: {e}"
                ) from e
            except AttributeError as e:
                raise AttributeError(
                    f"Failed to find class {class_name} in module {module_path}: {e}"
                ) from e

        raise AttributeError(
            f"'{type(self).__name__}' object has no attribute '{name}'"
        )

    def __dir__(self):
        """Include lazy-loaded sub-SDKs in dir() output."""
        default_attrs = list(super().__dir__())
        lazy_attrs = list(self._sub_sdk_map.keys())
        return sorted(list(set(default_attrs + lazy_attrs)))
