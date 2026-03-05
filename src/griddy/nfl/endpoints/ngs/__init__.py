"""Next Gen Stats (NGS) API endpoints.

This module provides access to NFL Next Gen Stats data from nextgenstats.nfl.com,
including player statistics, game information, charts, highlights, and leaderboards.
"""

from typing import TYPE_CHECKING, Optional

from griddy.core._lazy_load import LazySubSDKMixin
from griddy.nfl.basesdk import BaseSDK
from griddy.nfl.sdkconfiguration import SERVERS, SDKConfiguration

# NGS server URL (also available in SERVERS dict)
NGS_SERVER_URL = SERVERS["ngs"]


if TYPE_CHECKING:
    from griddy.nfl.endpoints.ngs.content import NgsContent
    from griddy.nfl.endpoints.ngs.games import NgsGames
    from griddy.nfl.endpoints.ngs.leaders import NgsLeaders
    from griddy.nfl.endpoints.ngs.league import NgsLeague
    from griddy.nfl.endpoints.ngs.news import NgsNews
    from griddy.nfl.endpoints.ngs.stats import NgsStats


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


class NextGenStats(LazySubSDKMixin, NgsBaseSDK):
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
            "griddy.nfl.endpoints.ngs.league",
            "NgsLeague",
        ),
        "games": (
            "griddy.nfl.endpoints.ngs.games",
            "NgsGames",
        ),
        "stats": (
            "griddy.nfl.endpoints.ngs.stats",
            "NgsStats",
        ),
        "leaders": (
            "griddy.nfl.endpoints.ngs.leaders",
            "NgsLeaders",
        ),
        "content": (
            "griddy.nfl.endpoints.ngs.content",
            "NgsContent",
        ),
        "news": (
            "griddy.nfl.endpoints.ngs.news",
            "NgsNews",
        ),
    }
