import base64
import importlib
import json
import sys
import weakref
from typing import TYPE_CHECKING, Dict, Optional, cast
from uuid import uuid4

import httpx

from griddy import settings

from ..nfl import models, utils
from ._hooks import SDKHooks
from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, ClientOwner, HttpClient, close_clients
from .sdkconfiguration import SDKConfiguration
from .types import UNSET, OptionalNullable
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig
from .utils.security import do_browser_auth

if TYPE_CHECKING:
    from griddy.nfl.endpoints.pro.betting import Betting
    from griddy.nfl.endpoints.pro.content import Content
    from griddy.nfl.endpoints.pro.games import ProGames
    from griddy.nfl.endpoints.pro.players import Players
    from griddy.nfl.endpoints.pro.schedules import Schedules
    from griddy.nfl.endpoints.pro.stats import StatsSDK
    from griddy.nfl.endpoints.pro.teams import Teams
    from griddy.nfl.endpoints.pro.transactions import Transactions
    from griddy.nfl.endpoints.regular.authentication import Authentication
    from griddy.nfl.endpoints.regular.football.combine import Combine
    from griddy.nfl.endpoints.regular.football.draft import Draft
    from griddy.nfl.endpoints.regular.football.games import Games
    from griddy.nfl.endpoints.regular.football.injuries import Injuries
    from griddy.nfl.endpoints.regular.football.rosters import Rosters
    from griddy.nfl.endpoints.regular.football.standings import Standings
    from griddy.nfl.endpoints.regular.football.teams import Teams as FootballTeams
    from griddy.nfl.endpoints.regular.football.venues import Venues
    from griddy.nfl.endpoints.regular.football.weeks import Weeks


class GriddyNFL(BaseSDK):
    r"""NFL REST APIs: Regular API - NFL's public API for accessing game schedules, team information, standings, statistics, and venue data. This API provides comprehensive access to NFL data including real-time game information, team rosters, seasonal statistics, and historical data. The NFL Pro API is for accessing advanced statistics, film room content, player data, and fantasy information. This API provides comprehensive access to NFL Pro features including Next Gen Stats, Film Room analysis, player projections, and game insights."""

    combine: "Combine"
    r"""Combine information"""
    draft: "Draft"
    r"""Draft information"""
    injuries: "Injuries"
    r"""Injury reports"""
    games: "Games"
    r"""Game information from the regular API"""
    rosters: "Rosters"
    r"""Base team rosters"""
    standings: "Standings"
    r"""Standings information"""
    # TODO: Refactor/reconcile this with the Pro Team model and any other variants
    football_teams: "FootballTeams"
    r"""FootballTeams"""
    venues: "Venues"
    r"""Venue information"""
    weeks: "Weeks"
    r"""Weekly information"""
    ##### Pro SDKs #####
    stats: "StatsSDK"
    r"""Aggregated player and team statistics (access via stats.passing, stats.rushing, etc.)"""
    betting: "Betting"
    r"""Betting related resources"""
    content: "Content"
    r"""Game previews, film cards, and insights"""
    players: "Players"
    r"""Player information, statistics, and projections"""
    pro_games: "ProGames"
    r"""Game information and statistics"""
    schedules: "Schedules"
    r"""Game schedules, matchup rankings, and injury reports"""
    betting: "Betting"
    r"""Game betting odds and lines"""
    transactions: "Transactions"
    r"""Endpoint for fetching transactions"""
    fantasy_statistics: "FantasyStatistics"
    r"""Fantasy football player statistics and scoring metrics"""
    teams: "Teams"
    r"""Team information, rosters, and schedules"""

    authentication: "Authentication"
    r"""Token generation and refresh operations for NFL API access"""

    _sub_sdk_map = {
        "authentication": (
            "griddy.nfl.endpoints.regular.authentication",
            "Authentication",
        ),
        "combine": ("griddy.nfl.endpoints.regular.football.combine", "Combine"),
        "draft": ("griddy.nfl.endpoints.regular.football.draft", "Draft"),
        # TODO: There will be a collision when we get to the top-level experience endpoint
        "injuries": ("griddy.nfl.endpoints.regular.football.injuries", "Injuries"),
        "games": ("griddy.nfl.endpoints.regular.football.games", "Games"),
        "rosters": ("griddy.nfl.endpoints.regular.football.rosters", "Rosters"),
        "standings": ("griddy.nfl.endpoints.regular.football.standings", "Standings"),
        "football_teams": ("griddy.nfl.endpoints.regular.football.teams", "Teams"),
        "venues": ("griddy.nfl.endpoints.regular.football.venues", "Venues"),
        "weeks": ("griddy.nfl.endpoints.regular.football.weeks", "Weeks"),
        "content": ("griddy.nfl.endpoints.pro.content", "Content"),
        "players": ("griddy.nfl.endpoints.pro.players", "Players"),
        "stats": ("griddy.nfl.endpoints.pro.stats", "StatsSDK"),
        # TODO: Refactor so that this call will be invoked as nfl.pro.games
        "pro_games": ("griddy.nfl.endpoints.pro.games", "ProGames"),
        "schedules": ("griddy.nfl.endpoints.pro.schedules", "Schedules"),
        "betting": ("griddy.nfl.endpoints.pro.betting", "Betting"),
        "defensive_pass_rush_statistics": (
            "griddy.nfl.defensive_pass_rush_statistics",
            "DefensivePassRushStatistics",
        ),
        "fantasy_statistics": ("griddy.nfl.fantasy_statistics", "FantasyStatistics"),
        "teams": ("griddy.nfl.endpoints.pro.teams", "Teams"),
        "transactions": ("griddy.nfl.endpoints.pro.transactions", "Transactions"),
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
        nfl_auth: Optional[Dict] = None,
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
        r"""Instantiates the SDK configuring it with the provided parameters.

        :param nfl_auth: The file path of a Netscape formatted cookies file used to set up NFL auth.
        :param server_idx: The index of the server to use for all methods
        :param server_url: The server URL to use for all methods
        :param url_params: Parameters to optionally template the server URL with
        :param client: The HTTP client to use for all synchronous methods
        :param async_client: The Async HTTP client to use for all asynchronous methods
        :param retry_config: The retry configuration to use for all supported methods
        :param timeout_ms: Optional request timeout applied to each operation in milliseconds
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

    def dynamic_import(self, modname, retries=3):
        for attempt in range(retries):
            try:
                return importlib.import_module(modname)
            except KeyError:
                # Clear any half-initialized module and retry
                sys.modules.pop(modname, None)
                if attempt == retries - 1:
                    break
        raise KeyError(f"Failed to import module '{modname}' after {retries} attempts")

    def __getattr__(self, name: str):
        if name in self._sub_sdk_map:
            module_path, class_name = self._sub_sdk_map[name]
            try:
                module = self.dynamic_import(module_path)
                klass = getattr(module, class_name)
                instance = klass(self.sdk_configuration, parent_ref=self)
                setattr(self, name, instance)
                return instance
            except ImportError as e:
                print(f"module_path:{module_path}")
                print(f"class_name: {class_name}")
                raise AttributeError(
                    f"Failed to import module {module_path} for attribute {name}: {e}"
                ) from e
            except AttributeError as e:
                raise AttributeError(
                    f"Failed to find class {class_name} in module {module_path} for attribute {name}: {e}"
                ) from e

        raise AttributeError(
            f"'{type(self).__name__}' object has no attribute '{name}'"
        )

    def __dir__(self):
        default_attrs = list(super().__dir__())
        lazy_attrs = list(self._sub_sdk_map.keys())
        return sorted(list(set(default_attrs + lazy_attrs)))

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
