import base64
import importlib
import json
import sys
import time
import urllib
import weakref
from typing import TYPE_CHECKING, Any, Callable, Dict, Optional, Union, cast
from uuid import uuid4

import httpx
import requests

from griddy import settings

from ..core.utils import extract_cookies_as_dict
from ..nfl import models, utils
from ._hooks import SDKHooks
from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, ClientOwner, HttpClient, close_clients
from .sdkconfiguration import SDKConfiguration
from .types import UNSET, OptionalNullable
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig

if TYPE_CHECKING:
    from griddy.nfl.endpoints.pro.content import Content
    from griddy.nfl.endpoints.pro.games import Games
    from griddy.nfl.endpoints.pro.players import Players
    from griddy.nfl.endpoints.pro.schedules import Schedules
    from griddy.nfl.endpoints.pro.teams import Teams

    from .authentication import Authentication
    from .betting import Betting
    from .defensive_pass_rush_statistics import DefensivePassRushStatistics
    from .defensive_player_overview import DefensivePlayerOverview
    from .defensive_statistics import DefensiveStatistics
    from .experience import Experience
    from .fantasy_statistics import FantasyStatistics
    from .filmroom import Filmroom
    from .football import Football
    from .player_passing_statistics import PlayerPassingStatistics
    from .player_receiving_statistics import PlayerReceivingStatistics
    from .player_rushing_statistics import PlayerRushingStatistics
    from .player_statistics import PlayerStatistics
    from .plays import Plays
    from .scores import Scores
    from .secured_videos import SecuredVideos
    from .stats_sdk import StatsSDK
    from .team_defense_pass_statistics import TeamDefensePassStatistics
    from .team_defense_rush_statistics import TeamDefenseRushStatistics
    from .team_defense_statistics import TeamDefenseStatistics
    from .team_offense_overview_statistics import TeamOffenseOverviewStatistics
    from .team_offense_pass_statistics import TeamOffensePassStatistics
    from .win_probability import WinProbability


class GriddyNFL(BaseSDK):
    r"""NFL REST APIs: Regular API - NFL's public API for accessing game schedules, team information, standings, statistics, and venue data. This API provides comprehensive access to NFL data including real-time game information, team rosters, seasonal statistics, and historical data. The NFL Pro API is for accessing advanced statistics, film room content, player data, and fantasy information. This API provides comprehensive access to NFL Pro features including Next Gen Stats, Film Room analysis, player projections, and game insights."""

    content: "Content"
    r"""Game previews, film cards, and insights"""
    players: "Players"
    r"""Player information, statistics, and projections"""
    games: "Games"
    r"""Game information and statistics"""
    plays: "Plays"
    r"""Play-by-play data and film room analysis"""
    schedules: "Schedules"
    r"""Game schedules, matchup rankings, and injury reports"""
    betting: "Betting"
    r"""Game betting odds and lines"""
    scores: "Scores"
    r"""Real-time scoring and game status endpoints"""
    win_probability: "WinProbability"
    r"""Game and play-level win probability analytics"""
    defensive_statistics: "DefensiveStatistics"
    r"""Individual defensive player statistics and coverage analytics"""
    defensive_player_overview: "DefensivePlayerOverview"
    r"""Comprehensive individual defensive player statistics and analytics"""
    defensive_pass_rush_statistics: "DefensivePassRushStatistics"
    r"""Individual defensive player pass rush statistics and analytics"""
    fantasy_statistics: "FantasyStatistics"
    r"""Fantasy football player statistics and scoring metrics"""
    player_statistics: "PlayerStatistics"
    r"""Individual player passing statistics and analytics"""
    player_passing_statistics: "PlayerPassingStatistics"
    r"""Individual player passing statistics and analytics by week"""
    player_receiving_statistics: "PlayerReceivingStatistics"
    r"""Individual player receiving statistics and analytics"""
    player_rushing_statistics: "PlayerRushingStatistics"
    r"""Individual player rushing statistics and analytics"""
    team_defense_statistics: "TeamDefenseStatistics"
    r"""Comprehensive team defensive statistics and situational analytics"""
    team_defense_pass_statistics: "TeamDefensePassStatistics"
    r"""Comprehensive team defensive pass statistics and situational analytics"""
    team_defense_rush_statistics: "TeamDefenseRushStatistics"
    r"""Comprehensive team defensive rush statistics and situational analytics"""
    team_offense_overview_statistics: "TeamOffenseOverviewStatistics"
    r"""Comprehensive team offensive overview statistics and situational analytics"""
    team_offense_pass_statistics: "TeamOffensePassStatistics"
    r"""Comprehensive team offensive pass statistics and situational analytics"""
    secured_videos: "SecuredVideos"
    r"""Premium coaches film video content with multiple camera angles"""
    filmroom: "Filmroom"
    r"""Advanced play analysis and film study data"""
    stats: "StatsSDK"
    r"""Comprehensive game and team statistics endpoints"""
    teams: "Teams"
    r"""Team information, rosters, and schedules"""
    experience: "Experience"
    r"""Experience API endpoints for games and teams"""
    football: "Football"
    r"""Football API endpoints for games, standings, stats, and venues"""
    authentication: "Authentication"
    r"""Token generation and refresh operations for NFL API access"""
    _sub_sdk_map = {
        "content": ("griddy.nfl.endpoints.pro.content", "Content"),
        "players": ("griddy.nfl.endpoints.pro.players", "Players"),
        "games": ("griddy.nfl.endpoints.pro.games", "Games"),
        "plays": ("griddy.nfl.plays", "Plays"),
        "schedules": ("griddy.nfl.endpoints.pro.schedules", "Schedules"),
        "betting": ("griddy.nfl.betting", "Betting"),
        "scores": ("griddy.nfl.scores", "Scores"),
        "win_probability": ("griddy.nfl.win_probability", "WinProbability"),
        "defensive_statistics": (
            "griddy.nfl.defensive_statistics",
            "DefensiveStatistics",
        ),
        "defensive_player_overview": (
            "griddy.nfl.defensive_player_overview",
            "DefensivePlayerOverview",
        ),
        "defensive_pass_rush_statistics": (
            "griddy.nfl.defensive_pass_rush_statistics",
            "DefensivePassRushStatistics",
        ),
        "fantasy_statistics": ("griddy.nfl.fantasy_statistics", "FantasyStatistics"),
        "player_statistics": ("griddy.nfl.player_statistics", "PlayerStatistics"),
        "player_passing_statistics": (
            "griddy.nfl.player_passing_statistics",
            "PlayerPassingStatistics",
        ),
        "player_receiving_statistics": (
            "griddy.nfl.player_receiving_statistics",
            "PlayerReceivingStatistics",
        ),
        "player_rushing_statistics": (
            "griddy.nfl.player_rushing_statistics",
            "PlayerRushingStatistics",
        ),
        "team_defense_statistics": (
            "griddy.nfl.team_defense_statistics",
            "TeamDefenseStatistics",
        ),
        "team_defense_pass_statistics": (
            "griddy.nfl.team_defense_pass_statistics",
            "TeamDefensePassStatistics",
        ),
        "team_defense_rush_statistics": (
            "griddy.nfl.team_defense_rush_statistics",
            "TeamDefenseRushStatistics",
        ),
        "team_offense_overview_statistics": (
            "griddy.nfl.team_offense_overview_statistics",
            "TeamOffenseOverviewStatistics",
        ),
        "team_offense_pass_statistics": (
            "griddy.nfl.team_offense_pass_statistics",
            "TeamOffensePassStatistics",
        ),
        "secured_videos": ("griddy.nfl.secured_videos", "SecuredVideos"),
        "filmroom": ("griddy.nfl.filmroom", "Filmroom"),
        "stats": ("griddy.nfl.stats_sdk", "StatsSDK"),
        "teams": ("griddy.nfl.endpoints.pro.teams", "Teams"),
        "experience": ("griddy.nfl.experience", "Experience"),
        "football": ("griddy.nfl.football", "Football"),
        "authentication": ("griddy.nfl.authentication", "Authentication"),
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
        nfl_auth: Dict,
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
