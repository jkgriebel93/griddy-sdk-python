from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Protocol, Type, Union
from urllib.parse import urlencode

from bs4 import BeautifulSoup

from griddy.core.basesdk import BaseEndpointConfig
from griddy.core.basesdk import BaseSDK as CoreBaseSDK

from . import errors, models
from .errors import ParsingError
from .parsers._helpers import uncomment_tables
from .sdkconfiguration import SDKConfiguration
from .utils.browserless import AsyncBrowserless, Browserless


class PfrParser(Protocol):
    """Protocol that all PFR parsers must satisfy.

    Parse methods must accept an HTML string and return a plain ``dict``
    (for single-model endpoints) or a ``list[dict]`` (for list endpoints).
    Pydantic model construction is handled by the base SDK, not the parser.
    """

    def __call__(self, html: str) -> Union[Dict[str, Any], List[Dict[str, Any]]]: ...


@dataclass
class EndpointConfig(BaseEndpointConfig):
    """Configuration for a PFR HTML-scraping endpoint."""

    path_template: str = ""
    wait_for_element: str = ""
    parser: PfrParser = None  # type: ignore[assignment]
    path_params: Dict[str, Any] = field(default_factory=dict)
    query_params: Dict[str, str] = field(default_factory=dict)


class BaseSDK(CoreBaseSDK[SDKConfiguration]):
    """PFR-specific BaseSDK with PFR error classes and security model."""

    def __init__(
        self, sdk_config: SDKConfiguration, parent_ref: Optional[object] = None
    ):
        super().__init__(sdk_config=sdk_config, parent_ref=parent_ref)
        self.browserless = Browserless()
        self.async_browserless = AsyncBrowserless()

    @property
    def _default_error_cls(self) -> Type[Exception]:
        return errors.GriddyPFRDefaultError

    @property
    def _no_response_error_cls(self) -> Type[Exception]:
        return errors.NoResponseError

    @property
    def _security_model_cls(self) -> Any:
        return models.Security

    @property
    def _security_env_mapping(self) -> Optional[Dict[str, str]]:
        return {"pfr_auth": "GRIDDY_PFR_AUTH"}

    def _build_url(self, config: EndpointConfig) -> str:
        base_url, _ = self.sdk_configuration.get_server_details()
        path = config.path_template.format(**config.path_params)
        url = f"{base_url}{path}"
        if config.query_params:
            url = f"{url}?{urlencode(config.query_params)}"
        return url

    @staticmethod
    def _preprocess_html(html: str) -> str:
        """Pre-process raw HTML before passing it to a parser.

        Uncomments hidden ``<table>`` elements that PFR wraps in HTML
        comments so they are visible to downstream BeautifulSoup queries.
        """
        soup = BeautifulSoup(html, "html.parser")
        uncomment_tables(soup)
        return str(soup)

    def _parse_and_validate(self, config: EndpointConfig, html: str) -> Any:
        html = self._preprocess_html(html)
        try:
            result = config.parser(html)
        except ParsingError:
            raise

        if isinstance(result, list):
            return [config.response_type.model_validate(item) for item in result]
        return config.response_type.model_validate(result)

    def _execute_endpoint(self, config: EndpointConfig) -> Any:
        """Execute a PFR scraping endpoint using its configuration.

        Resolves the base URL, templates path params, fetches HTML via
        Browserless, and runs the configured parser.
        """
        url = self._build_url(config)

        html = self.browserless.get_page_content(
            url,
            wait_for_element=config.wait_for_element,
        )

        try:
            return self._parse_and_validate(config, html)
        except ParsingError as exc:
            exc.url = url
            raise

    async def _execute_endpoint_async(self, config: EndpointConfig) -> Any:
        """Async version of :meth:`_execute_endpoint`.

        Uses :class:`AsyncBrowserless` for non-blocking HTML fetching.
        """
        url = self._build_url(config)

        html = await self.async_browserless.get_page_content(
            url,
            wait_for_element=config.wait_for_element,
        )

        try:
            return self._parse_and_validate(config, html)
        except ParsingError as exc:
            exc.url = url
            raise
