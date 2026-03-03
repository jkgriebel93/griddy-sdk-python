"""NFL SDK client for accessing NFL data from multiple API endpoints.

This module provides the GriddyNFL class, the main entry point for accessing
NFL data including games, stats, rosters, and Next Gen Stats.

Example:
    >>> from griddy.nfl import GriddyNFL
    >>> nfl = GriddyNFL(nfl_auth={"accessToken": "your_token"})
    >>> games = nfl.games.get_games(season=2024, week=1)
    >>> stats = nfl.stats.passing.get_passing_stats(season=2024)
"""

import base64
import json
import weakref
from typing import TYPE_CHECKING, Any, Dict, Optional, cast
from uuid import uuid4

import httpx

from griddy import settings
from griddy.core._lazy_load import LazySubSDKMixin

from ..nfl import models, utils
from ._hooks import SDKHooks
from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, ClientOwner, HttpClient, close_clients
from .sdkconfiguration import SDKConfiguration
from .types import UNSET, OptionalNullable
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig

if TYPE_CHECKING:
    from griddy.nfl.endpoints.ngs import NextGenStats
    from griddy.nfl.endpoints.pro.betting import Betting
    from griddy.nfl.endpoints.pro.content import Content
    from griddy.nfl.endpoints.pro.games import ProGames
    from griddy.nfl.endpoints.pro.players import Players
    from griddy.nfl.endpoints.pro.schedules import Schedules
    from griddy.nfl.endpoints.pro.stats import StatsSDK
    from griddy.nfl.endpoints.pro.teams import Teams
    from griddy.nfl.endpoints.pro.transactions import Transactions
    from griddy.nfl.endpoints.regular.authentication import Authentication
    from griddy.nfl.endpoints.regular.content import VideoContent
    from griddy.nfl.endpoints.regular.experience import Experience
    from griddy.nfl.endpoints.regular.football.combine import Combine
    from griddy.nfl.endpoints.regular.football.draft import Draft
    from griddy.nfl.endpoints.regular.football.games import Games
    from griddy.nfl.endpoints.regular.football.rosters import Rosters
    from griddy.nfl.endpoints.regular.football.standings import Standings
    from griddy.nfl.endpoints.regular.football.stats import FootballStatsSDK
    from griddy.nfl.endpoints.regular.football.teams import Teams as FootballTeams
    from griddy.nfl.endpoints.regular.football.venues import Venues
    from griddy.nfl.endpoints.regular.football.weeks import Weeks


class GriddyNFL(LazySubSDKMixin, BaseSDK):
    """Main client for accessing NFL data from multiple API endpoints.

    GriddyNFL provides unified access to NFL data through three API categories:

    - **Regular API**: Public NFL.com endpoints for games, rosters, standings
    - **Pro API**: Advanced statistics, betting odds, player projections
    - **Next Gen Stats**: Player tracking data and advanced analytics

    Sub-SDKs are loaded lazily on first access to minimize startup time.

    Attributes:
        authentication: Token generation and refresh operations.
        combine: NFL Combine workout data and results.
        draft: NFL Draft picks and information.
        games: Game schedules, scores, and details.
        rosters: Team rosters and player assignments.
        standings: Division and conference standings.
        football_teams: Team information and details.
        venues: Stadium information.
        weeks: Season week information.
        stats: Aggregated player/team statistics (passing, rushing, etc.).
        betting: Betting odds and lines.
        content: Game previews and film cards.
        players: Player information and projections.
        pro_games: Advanced game data.
        schedules: Matchup rankings and injury reports.
        transactions: Player transactions.
        teams: Pro team information.
        ngs: Next Gen Stats (tracking data, leaderboards, charts).

    Example:
        >>> from griddy.nfl import GriddyNFL
        >>> # Initialize with auth token
        >>> nfl = GriddyNFL(nfl_auth={"accessToken": "your_token"})
        >>> # Get games
        >>> games = nfl.games.get_games(season=2024, week=1)
        >>> # Get Next Gen Stats
        >>> passing = nfl.ngs.stats.get_passing_stats(season=2024)
        >>> # Use as context manager
        >>> with GriddyNFL(nfl_auth=auth) as nfl:
        ...     games = nfl.games.get_games(season=2024)
    """

    # Regular API endpoints
    authentication: "Authentication"
    """Token generation and refresh operations for NFL API access."""
    combine: "Combine"
    """NFL Combine workout data and results."""
    draft: "Draft"
    """NFL Draft picks and information."""
    games: "Games"
    """Game schedules, scores, and details from the regular API."""
    rosters: "Rosters"
    """Team rosters and player assignments."""
    standings: "Standings"
    """Division and conference standings."""
    football_teams: "FootballTeams"
    """Team information and details."""
    venues: "Venues"
    """Stadium and venue information."""
    weeks: "Weeks"
    """Season week information."""

    football_stats: "FootballStatsSDK"
    """Historical and live football statistics (football_stats.historical, football_stats.live)."""
    experience: "Experience"
    """Game details by slug or ID, with optional replays and drive charts."""
    video_content: "VideoContent"
    """Video replay content for games."""

    # Pro API endpoints
    stats: "StatsSDK"
    """Aggregated player and team statistics (stats.passing, stats.rushing, etc.)."""
    betting: "Betting"
    """Betting odds and lines."""
    content: "Content"
    """Game previews, film cards, and insights."""
    players: "Players"
    """Player information, statistics, and projections."""
    pro_games: "ProGames"
    """Advanced game data and statistics."""
    schedules: "Schedules"
    """Matchup rankings and injury reports."""
    transactions: "Transactions"
    """Player transactions and roster moves."""
    fantasy_statistics: "FantasyStatistics"
    """Fantasy football statistics and scoring metrics."""
    teams: "Teams"
    """Pro team information, rosters, and schedules."""

    # Next Gen Stats
    ngs: "NextGenStats"
    """Next Gen Stats data (tracking statistics, leaderboards, charts, highlights)."""

    _sub_sdk_map = {
        "authentication": (
            "griddy.nfl.endpoints.regular.authentication",
            "Authentication",
        ),
        "combine": ("griddy.nfl.endpoints.regular.football.combine", "Combine"),
        "draft": ("griddy.nfl.endpoints.regular.football.draft", "Draft"),
        "games": ("griddy.nfl.endpoints.regular.football.games", "Games"),
        "rosters": ("griddy.nfl.endpoints.regular.football.rosters", "Rosters"),
        "standings": ("griddy.nfl.endpoints.regular.football.standings", "Standings"),
        "football_teams": ("griddy.nfl.endpoints.regular.football.teams", "Teams"),
        "venues": ("griddy.nfl.endpoints.regular.football.venues", "Venues"),
        "weeks": ("griddy.nfl.endpoints.regular.football.weeks", "Weeks"),
        "football_stats": (
            "griddy.nfl.endpoints.regular.football.stats",
            "FootballStatsSDK",
        ),
        "experience": (
            "griddy.nfl.endpoints.regular.experience",
            "Experience",
        ),
        "video_content": (
            "griddy.nfl.endpoints.regular.content",
            "VideoContent",
        ),
        "content": ("griddy.nfl.endpoints.pro.content", "Content"),
        "players": ("griddy.nfl.endpoints.pro.players", "Players"),
        "stats": ("griddy.nfl.endpoints.pro.stats", "StatsSDK"),
        # TODO: Refactor so that this call will be invoked as nfl.pro.games
        "pro_games": ("griddy.nfl.endpoints.pro.games", "ProGames"),
        "schedules": ("griddy.nfl.endpoints.pro.schedules", "Schedules"),
        "betting": ("griddy.nfl.endpoints.pro.betting", "Betting"),
        "teams": ("griddy.nfl.endpoints.pro.teams", "Teams"),
        "transactions": ("griddy.nfl.endpoints.pro.transactions", "Transactions"),
        "ngs": ("griddy.nfl.endpoints.ngs", "NextGenStats"),
    }

    _client_data = {
        "clientKey": settings.NFL["clientKey"],
        "clientSecret": settings.NFL["clientSecret"],
        "deviceId": str(uuid4()),
        "deviceInfo": base64.b64encode(
            json.dumps(
                {
                    "model": "desktop",
                    "version": "Chrome",
                    "osName": "Windows",
                    "osVersion": "10.0",
                },
                separators=(",", ":"),
            ).encode()
        ).decode(),
        "networkType": "other",
        "peacockUUID": "undefined",
    }

    def __init__(
        self,
        nfl_auth: Dict[str, Any],
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
    ) -> None:
        """Initialize the GriddyNFL client.

        Args:
            nfl_auth: Dictionary containing authentication information,
                must include 'accessToken' key. Example:
                {"accessToken": "your_nfl_access_token"}
            server_idx: Index of the server to use from the server list.
            server_url: Override the default server URL.
            url_params: Parameters to template into the server URL.
            client: Custom synchronous HTTP client (must implement HttpClient).
            async_client: Custom async HTTP client (must implement AsyncHttpClient).
            retry_config: Configuration for automatic request retries.
            timeout_ms: Request timeout in milliseconds.
            debug_logger: Custom logger for debug output.

        Example:
            >>> nfl = GriddyNFL(nfl_auth={"accessToken": "your_token"})
        """
        client_supplied = True
        if client is None:
            client = httpx.Client(follow_redirects=True)
            client_supplied = False

        if not issubclass(type(client), HttpClient):
            raise TypeError(
                "The provided client must implement the HttpClient protocol."
            )

        async_client_supplied = True
        if async_client is None:
            async_client = httpx.AsyncClient(follow_redirects=True)
            async_client_supplied = False

        if debug_logger is None:
            debug_logger = get_default_logger()

        if not issubclass(type(async_client), AsyncHttpClient):
            raise TypeError(
                "The provided async_client must implement the AsyncHttpClient protocol."
            )

        security = models.Security(nfl_auth=nfl_auth["accessToken"])

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        BaseSDK.__init__(
            self,
            SDKConfiguration(
                client=client,
                client_supplied=client_supplied,
                async_client=async_client,
                async_client_supplied=async_client_supplied,
                security=security,
                server_url=server_url,
                server_idx=server_idx,
                retry_config=retry_config,
                timeout_ms=timeout_ms,
                debug_logger=debug_logger,
                custom_auth_info=nfl_auth,
            ),
            parent_ref=self,
        )

        hooks = SDKHooks()

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        self.sdk_configuration = hooks.sdk_init(self.sdk_configuration)

        weakref.finalize(
            self,
            close_clients,
            cast(ClientOwner, self.sdk_configuration),
            self.sdk_configuration.client,
            self.sdk_configuration.client_supplied,
            self.sdk_configuration.async_client,
            self.sdk_configuration.async_client_supplied,
        )

    @classmethod
    def authenticate_via_browser(
        cls,
        login_email: str,
        login_password: str,
        headless: bool = False,
        save_credentials_path: Optional[str] = None,
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
    ) -> "GriddyNFL":
        """Create a GriddyNFL instance by authenticating via browser.

        Uses Playwright to log into NFL.com and capture auth tokens.

        Args:
            login_email: Email address for NFL.com account.
            login_password: Password for NFL.com account.
            headless: If True, run browser in headless mode. Defaults to False.
            save_credentials_path: If provided, save credentials to this file path.
            server_idx: Index of the server to use from the server list.
            server_url: Override the default server URL.
            url_params: Parameters to template into the server URL.
            client: Custom synchronous HTTP client (must implement HttpClient).
            async_client: Custom async HTTP client (must implement AsyncHttpClient).
            retry_config: Configuration for automatic request retries.
            timeout_ms: Request timeout in milliseconds.
            debug_logger: Custom logger for debug output.

        Returns:
            A fully-initialized GriddyNFL instance.

        Example:
            >>> nfl = GriddyNFL.authenticate_via_browser(
            ...     login_email="user@example.com",
            ...     login_password="password",
            ...     headless=True,
            ...     save_credentials_path="creds.json",
            ... )
        """
        from .utils.security import do_browser_auth

        if debug_logger is None:
            debug_logger = get_default_logger()

        nfl_auth = do_browser_auth(
            email=login_email,
            password=login_password,
            headless=headless,
            logger=debug_logger,
        )

        if save_credentials_path is not None:
            with open(save_credentials_path, "w") as outfile:
                json.dump(nfl_auth, outfile, indent=4)

        return cls(
            nfl_auth=nfl_auth,
            server_idx=server_idx,
            server_url=server_url,
            url_params=url_params,
            client=client,
            async_client=async_client,
            retry_config=retry_config,
            timeout_ms=timeout_ms,
            debug_logger=debug_logger,
        )

    def __enter__(self):
        return self

    async def __aenter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if (
            self.sdk_configuration.client is not None
            and not self.sdk_configuration.client_supplied
        ):
            self.sdk_configuration.client.close()
        self.sdk_configuration.client = None

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if (
            self.sdk_configuration.async_client is not None
            and not self.sdk_configuration.async_client_supplied
        ):
            await self.sdk_configuration.async_client.aclose()
        self.sdk_configuration.async_client = None
