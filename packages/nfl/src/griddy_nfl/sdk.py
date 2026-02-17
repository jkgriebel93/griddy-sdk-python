"""NFL SDK client for accessing NFL data from multiple API endpoints.

This module provides the GriddyNFL class, the main entry point for accessing
NFL data including games, stats, rosters, and Next Gen Stats.

Example:
    >>> from griddy_nfl import GriddyNFL
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

from . import models, settings, utils
from ._hooks import SDKHooks
from ._lazy_load import LazySubSDKMixin
from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, ClientOwner, HttpClient, close_clients
from .sdkconfiguration import SDKConfiguration
from .types import UNSET, OptionalNullable
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig
from .utils.security import do_browser_auth

if TYPE_CHECKING:
    from griddy_nfl.endpoints.ngs import NextGenStats
    from griddy_nfl.endpoints.pro.betting import Betting
    from griddy_nfl.endpoints.pro.content import Content
    from griddy_nfl.endpoints.pro.games import ProGames
    from griddy_nfl.endpoints.pro.players import Players
    from griddy_nfl.endpoints.pro.schedules import Schedules
    from griddy_nfl.endpoints.pro.stats import StatsSDK
    from griddy_nfl.endpoints.pro.teams import Teams
    from griddy_nfl.endpoints.pro.transactions import Transactions
    from griddy_nfl.endpoints.regular.authentication import Authentication
    from griddy_nfl.endpoints.regular.content import VideoContent
    from griddy_nfl.endpoints.regular.experience import Experience
    from griddy_nfl.endpoints.regular.football.combine import Combine
    from griddy_nfl.endpoints.regular.football.draft import Draft
    from griddy_nfl.endpoints.regular.football.games import Games
    from griddy_nfl.endpoints.regular.football.rosters import Rosters
    from griddy_nfl.endpoints.regular.football.standings import Standings
    from griddy_nfl.endpoints.regular.football.stats import FootballStatsSDK
    from griddy_nfl.endpoints.regular.football.teams import Teams as FootballTeams
    from griddy_nfl.endpoints.regular.football.venues import Venues
    from griddy_nfl.endpoints.regular.football.weeks import Weeks


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
        >>> from griddy_nfl import GriddyNFL
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
            "griddy_nfl.endpoints.regular.authentication",
            "Authentication",
        ),
        "combine": ("griddy_nfl.endpoints.regular.football.combine", "Combine"),
        "draft": ("griddy_nfl.endpoints.regular.football.draft", "Draft"),
        # TODO: There will be a collision when we get to the top-level experience endpoint
        "injuries": ("griddy_nfl.endpoints.regular.football.injuries", "Injuries"),
        "games": ("griddy_nfl.endpoints.regular.football.games", "Games"),
        "rosters": ("griddy_nfl.endpoints.regular.football.rosters", "Rosters"),
        "standings": ("griddy_nfl.endpoints.regular.football.standings", "Standings"),
        "football_teams": ("griddy_nfl.endpoints.regular.football.teams", "Teams"),
        "venues": ("griddy_nfl.endpoints.regular.football.venues", "Venues"),
        "weeks": ("griddy_nfl.endpoints.regular.football.weeks", "Weeks"),
        "football_stats": (
            "griddy_nfl.endpoints.regular.football.stats",
            "FootballStatsSDK",
        ),
        "experience": (
            "griddy_nfl.endpoints.regular.experience",
            "Experience",
        ),
        "video_content": (
            "griddy_nfl.endpoints.regular.content",
            "VideoContent",
        ),
        "content": ("griddy_nfl.endpoints.pro.content", "Content"),
        "players": ("griddy_nfl.endpoints.pro.players", "Players"),
        "stats": ("griddy_nfl.endpoints.pro.stats", "StatsSDK"),
        # TODO: Refactor so that this call will be invoked as nfl.pro.games
        "pro_games": ("griddy_nfl.endpoints.pro.games", "ProGames"),
        "schedules": ("griddy_nfl.endpoints.pro.schedules", "Schedules"),
        "betting": ("griddy_nfl.endpoints.pro.betting", "Betting"),
        "defensive_pass_rush_statistics": (
            "griddy_nfl.defensive_pass_rush_statistics",
            "DefensivePassRushStatistics",
        ),
        "fantasy_statistics": ("griddy_nfl.fantasy_statistics", "FantasyStatistics"),
        "teams": ("griddy_nfl.endpoints.pro.teams", "Teams"),
        "transactions": ("griddy_nfl.endpoints.pro.transactions", "Transactions"),
        "ngs": ("griddy_nfl.endpoints.ngs", "NextGenStats"),
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
        nfl_auth: Optional[Dict[str, Any]] = None,
        login_email: Optional[str] = None,
        login_password: Optional[str] = None,
        headless_login: Optional[bool] = False,
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

        You must provide authentication either via a pre-obtained auth token
        (nfl_auth) or via email/password for browser-based authentication.

        Args:
            nfl_auth: Dictionary containing authentication information,
                must include 'accessToken' key. Example:
                {"accessToken": "your_nfl_access_token"}
            login_email: Email address for NFL.com account. Used with
                login_password for browser-based authentication.
            login_password: Password for NFL.com account.
            headless_login: If True, run browser in headless mode during
                authentication. Defaults to False.
            server_idx: Index of the server to use from the server list.
            server_url: Override the default server URL.
            url_params: Parameters to template into the server URL.
            client: Custom synchronous HTTP client (must implement HttpClient).
            async_client: Custom async HTTP client (must implement AsyncHttpClient).
            retry_config: Configuration for automatic request retries.
            timeout_ms: Request timeout in milliseconds.
            debug_logger: Custom logger for debug output.

        Raises:
            ValueError: If neither nfl_auth nor email/password is provided,
                or if both are provided.

        Example:
            >>> # With pre-obtained token
            >>> nfl = GriddyNFL(nfl_auth={"accessToken": "your_token"})
            >>> # With email/password
            >>> nfl = GriddyNFL(
            ...     login_email="user@example.com",
            ...     login_password="password",
            ...     headless_login=True,
            ... )
        """
        client_supplied = True
        if client is None:
            client = httpx.Client(follow_redirects=True)
            client_supplied = False

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        async_client_supplied = True
        if async_client is None:
            async_client = httpx.AsyncClient(follow_redirects=True)
            async_client_supplied = False

        if debug_logger is None:
            debug_logger = get_default_logger()

        assert issubclass(
            type(async_client), AsyncHttpClient
        ), "The provided async_client must implement the AsyncHttpClient protocol."

        auth_params_error = (
            "You must provide either nfl_auth, OR email/password combination."
        )
        if all([nfl_auth, login_email, login_password]):
            raise ValueError(auth_params_error)
        elif not any([nfl_auth, login_email, login_password]):
            raise ValueError(auth_params_error)

        if not nfl_auth:
            nfl_auth = do_browser_auth(
                email=login_email, password=login_password, headless=headless_login
            )

            print("Writing auth creds to file")
            with open("creds.json", "w") as outfile:
                json.dump(nfl_auth, outfile, indent=4)

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
