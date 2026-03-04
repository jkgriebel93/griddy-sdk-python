"""Base SDK class providing shared initialization, context management, and cleanup.

All top-level SDK classes (GriddyNFL, GriddyPFR) inherit from this mixin
to share HTTP client setup, debug logging, hook wiring, and the
"Context Manager + ResourceWarning" cleanup pattern.
"""

import asyncio
import warnings
from abc import abstractmethod
from typing import Any, Dict, Optional

import httpx

from griddy.core.httpclient import AsyncHttpClient, HttpClient
from griddy.core.types import UNSET, OptionalNullable
from griddy.core.utils.logger import Logger, get_default_logger
from griddy.core.utils.retries import RetryConfig
from griddy.core.utils.url import template_url


class BaseGriddySDK:
    """Mixin providing shared init, context management, and cleanup for top-level SDKs.

    Subclasses must implement four abstract methods to customise
    provider-specific behaviour (debug env var, security model,
    SDK configuration, and hooks).
    """

    # ------------------------------------------------------------------
    # Abstract customisation points
    # ------------------------------------------------------------------

    @abstractmethod
    def _get_debug_logger_env_var(self) -> str:
        """Return the environment variable name for debug logging."""
        ...

    @abstractmethod
    def _create_security(self, auth: Any) -> Any:
        """Create a provider-specific security model from *auth*, or ``None``."""
        ...

    @abstractmethod
    def _create_sdk_configuration(self, **kwargs: Any) -> Any:
        """Create and return a provider-specific ``SDKConfiguration``."""
        ...

    @abstractmethod
    def _create_hooks(self) -> Any:
        """Create and return a provider-specific ``SDKHooks`` instance."""
        ...

    # ------------------------------------------------------------------
    # Shared initialisation
    # ------------------------------------------------------------------

    def _init_sdk(
        self,
        auth: Any,
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
        **extra_config: Any,
    ) -> None:
        """Shared init logic for all top-level SDKs."""

        # 1. HTTP client creation + validation
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

        if not issubclass(type(async_client), AsyncHttpClient):
            raise TypeError(
                "The provided async_client must implement the AsyncHttpClient protocol."
            )

        # 2. Debug logger
        if debug_logger is None:
            debug_logger = get_default_logger(env_var=self._get_debug_logger_env_var())

        # 3. Security
        security = self._create_security(auth)

        # 4. Server URL templating
        if server_url is not None and url_params is not None:
            server_url = template_url(server_url, url_params)

        # 5. SDKConfiguration + BaseSDK.__init__ (via MRO)
        sdk_config = self._create_sdk_configuration(
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
            **extra_config,
        )

        super(BaseGriddySDK, self).__init__(sdk_config=sdk_config, parent_ref=self)

        # 6. Hooks
        hooks = self._create_hooks()
        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks
        self.sdk_configuration = hooks.sdk_init(self.sdk_configuration)

    # ------------------------------------------------------------------
    # Context managers
    # ------------------------------------------------------------------

    def __enter__(self):
        return self

    async def __aenter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.aclose()

    # ------------------------------------------------------------------
    # Public cleanup
    # ------------------------------------------------------------------

    def close(self) -> None:
        """Close all SDK-owned HTTP clients (sync entry-point)."""
        if (
            self.sdk_configuration.client is not None
            and not self.sdk_configuration.client_supplied
        ):
            self.sdk_configuration.client.close()
        self.sdk_configuration.client = None

        # Best-effort cleanup of the async client so that a single
        # ``close()`` or sync context-manager exit silences __del__.
        if (
            self.sdk_configuration.async_client is not None
            and not self.sdk_configuration.async_client_supplied
        ):
            try:
                loop = asyncio.get_running_loop()
                asyncio.run_coroutine_threadsafe(
                    self.sdk_configuration.async_client.aclose(), loop
                )
            except RuntimeError:
                try:
                    asyncio.run(self.sdk_configuration.async_client.aclose())
                except RuntimeError:
                    pass  # best effort
        self.sdk_configuration.async_client = None

    async def aclose(self) -> None:
        """Close all SDK-owned HTTP clients (async entry-point)."""
        if (
            self.sdk_configuration.client is not None
            and not self.sdk_configuration.client_supplied
        ):
            self.sdk_configuration.client.close()
        self.sdk_configuration.client = None

        if (
            self.sdk_configuration.async_client is not None
            and not self.sdk_configuration.async_client_supplied
        ):
            await self.sdk_configuration.async_client.aclose()
        self.sdk_configuration.async_client = None

    # ------------------------------------------------------------------
    # ResourceWarning on garbage collection
    # ------------------------------------------------------------------

    def __del__(self) -> None:
        if not hasattr(self, "sdk_configuration"):
            return

        has_unclosed = (
            self.sdk_configuration.client is not None
            and not self.sdk_configuration.client_supplied
        ) or (
            self.sdk_configuration.async_client is not None
            and not self.sdk_configuration.async_client_supplied
        )

        if has_unclosed:
            warnings.warn(
                f"Unclosed {type(self).__name__}. "
                f"Use close() or a context manager.",
                ResourceWarning,
                stacklevel=2,
            )
