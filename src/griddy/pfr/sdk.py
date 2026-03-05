"""PFR SDK client for accessing Pro Football Reference data.

This module provides the GriddyPFR class, the main entry point for accessing
Pro Football Reference data.

Example:
    >>> from griddy.pfr import GriddyPFR
    >>> pfr = GriddyPFR()
    >>> games = pfr.schedule.get_season_schedule(season=2015)
"""

from typing import TYPE_CHECKING, Any, Dict, Optional

from griddy.core._lazy_load import LazySubSDKMixin
from griddy.core.base_griddy_sdk import BaseGriddySDK
from griddy.core.hooks.sdkhooks import SDKHooks

from ._hooks.registration import init_hooks
from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, HttpClient
from .sdkconfiguration import SDKConfiguration
from .types import UNSET, OptionalNullable
from .utils import Logger, RetryConfig
from .utils.browserless import BrowserlessConfig

if TYPE_CHECKING:
    from .endpoints.awards import Awards
    from .endpoints.coaches import Coaches
    from .endpoints.draft import Draft
    from .endpoints.executives import Executives
    from .endpoints.fantasy import Fantasy
    from .endpoints.frivolities import Frivolities
    from .endpoints.games import Games
    from .endpoints.hof import Hof
    from .endpoints.leaders import Leaders
    from .endpoints.officials import Officials
    from .endpoints.players import Players
    from .endpoints.probowl import ProBowl
    from .endpoints.schedule import Schedule
    from .endpoints.schools import Schools
    from .endpoints.seasons import Seasons
    from .endpoints.stadiums import Stadiums
    from .endpoints.superbowl import SuperBowl
    from .endpoints.teams import Teams


class GriddyPFR(LazySubSDKMixin, BaseGriddySDK, BaseSDK):
    """Main client for accessing Pro Football Reference data.

    Sub-SDKs are loaded lazily on first access to minimize startup time.

    Example:
        >>> from griddy.pfr import GriddyPFR
        >>> pfr = GriddyPFR()
        >>> games = pfr.schedule.get_season_schedule(season=2015)
    """

    awards: "Awards"
    coaches: "Coaches"
    draft: "Draft"
    executives: "Executives"
    fantasy: "Fantasy"
    frivolities: "Frivolities"
    games: "Games"
    hof: "Hof"
    leaders: "Leaders"
    officials: "Officials"
    players: "Players"
    probowl: "ProBowl"
    schedule: "Schedule"
    schools: "Schools"
    seasons: "Seasons"
    stadiums: "Stadiums"
    superbowl: "SuperBowl"
    teams: "Teams"

    _sub_sdk_map = {
        "awards": ("griddy.pfr.endpoints.awards", "Awards"),
        "coaches": ("griddy.pfr.endpoints.coaches", "Coaches"),
        "draft": ("griddy.pfr.endpoints.draft", "Draft"),
        "executives": ("griddy.pfr.endpoints.executives", "Executives"),
        "fantasy": ("griddy.pfr.endpoints.fantasy", "Fantasy"),
        "frivolities": ("griddy.pfr.endpoints.frivolities", "Frivolities"),
        "games": ("griddy.pfr.endpoints.games", "Games"),
        "hof": ("griddy.pfr.endpoints.hof", "Hof"),
        "leaders": ("griddy.pfr.endpoints.leaders", "Leaders"),
        "officials": ("griddy.pfr.endpoints.officials", "Officials"),
        "players": ("griddy.pfr.endpoints.players", "Players"),
        "probowl": ("griddy.pfr.endpoints.probowl", "ProBowl"),
        "schedule": ("griddy.pfr.endpoints.schedule", "Schedule"),
        "schools": ("griddy.pfr.endpoints.schools", "Schools"),
        "seasons": ("griddy.pfr.endpoints.seasons", "Seasons"),
        "stadiums": ("griddy.pfr.endpoints.stadiums", "Stadiums"),
        "superbowl": ("griddy.pfr.endpoints.superbowl", "SuperBowl"),
        "teams": ("griddy.pfr.endpoints.teams", "Teams"),
    }

    def __init__(
        self,
        pfr_auth: Optional[Dict[str, str]] = None,
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
        browserless_config: Optional[BrowserlessConfig] = None,
    ) -> None:
        """Initialize the GriddyPFR client.

        Args:
            pfr_auth: Optional dictionary containing authentication information.
                PFR does not currently require auth, but this is available for
                future use. Example: {"accessToken": "your_token"}
            server_idx: Index of the server to use from the server list.
            server_url: Override the default server URL.
            url_params: Parameters to template into the server URL.
            client: Custom synchronous HTTP client (must implement HttpClient).
            async_client: Custom async HTTP client (must implement AsyncHttpClient).
            retry_config: Configuration for automatic request retries.
            timeout_ms: Request timeout in milliseconds.
            debug_logger: Custom logger for debug output.
            browserless_config: Configuration for Browserless API requests.
                Overrides default proxy, timeout, and TTL values.
        """
        # Pre-set so PFR BaseSDK.__init__ can pick it up via getattr
        # (MRO super().__init__ doesn't forward extra kwargs).
        self._browserless_config = browserless_config
        self._init_sdk(
            auth=pfr_auth,
            server_idx=server_idx,
            server_url=server_url,
            url_params=url_params,
            client=client,
            async_client=async_client,
            retry_config=retry_config,
            timeout_ms=timeout_ms,
            debug_logger=debug_logger,
        )

    # ------------------------------------------------------------------
    # BaseGriddySDK abstract method implementations
    # ------------------------------------------------------------------

    def _get_debug_logger_env_var(self) -> str:
        return "GRIDDY_PFR_DEBUG"

    def _create_security(self, auth: Any) -> Any:
        if auth and "accessToken" in auth:
            from . import models

            return models.Security(pfr_auth=auth["accessToken"])
        return None

    def _create_sdk_configuration(self, **kwargs: Any) -> Any:
        return SDKConfiguration(**kwargs)

    def _create_hooks(self) -> Any:
        return SDKHooks(init_hooks_fn=init_hooks)
