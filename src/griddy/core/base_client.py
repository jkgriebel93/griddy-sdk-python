"""Base HTTP client for all Griddy SDK modules."""

import time
from urllib.parse import urljoin

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .exceptions import APIError, RateLimitError, NotFoundError, AuthenticationError
from .utils import retry_on_rate_limit


class BaseClient:
    """Base HTTP client with common functionality for all data source clients."""

    def __init__(
        self,
        base_url: str,
        timeout: int = 30,
        max_retries: int = 3,
        rate_limit_delay: float = 1.0,
        headers: dict[str, str] | None = None,
    ):
        """
        Initialize the base client.

        Args:
            base_url: Base URL for the API
            timeout: Request timeout in seconds
            max_retries: Maximum number of retries for failed requests
            rate_limit_delay: Delay between requests to avoid rate limiting
            headers: Additional headers to include in requests
        """
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.rate_limit_delay = rate_limit_delay
        self._last_request_time = 0.0

        # Create session with retry strategy
        self.session = requests.Session()

        # Configure retry strategy
        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            method_whitelist=["HEAD", "GET", "OPTIONS"],
            backoff_factor=1.0,
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        # Set default headers
        default_headers = {
            "User-Agent": "Griddy-SDK/0.1.0",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        if headers:
            default_headers.update(headers)

        self.session.headers.update(default_headers)

    def _enforce_rate_limit(self) -> None:
        """Enforce rate limiting between requests."""
        if self.rate_limit_delay > 0:
            time_since_last = time.time() - self._last_request_time
            if time_since_last < self.rate_limit_delay:
                time.sleep(self.rate_limit_delay - time_since_last)
        self._last_request_time = time.time()

    def _handle_response(self, response: requests.Response) -> dict[str, any]:
        """
        Handle HTTP response and raise appropriate exceptions.

        Args:
            response: HTTP response object

        Returns:
            Parsed JSON response data

        Raises:
            APIError: For general API errors
            RateLimitError: For rate limit errors
            NotFoundError: For 404 errors
            AuthenticationError: For authentication errors
        """
        try:
            response_data = response.json() if response.content else {}
        except ValueError:
            response_data = {"message": response.text}

        if response.status_code == 200:
            return response_data
        elif response.status_code == 404:
            raise NotFoundError(
                f"Resource not found: {response.url}",
                status_code=response.status_code,
                response_data=response_data,
            )
        elif response.status_code == 401:
            raise AuthenticationError(
                "Authentication failed",
                status_code=response.status_code,
                response_data=response_data,
            )
        elif response.status_code == 429:
            retry_after = None
            if "Retry-After" in response.headers:
                try:
                    retry_after = int(response.headers["Retry-After"])
                except ValueError:
                    pass

            raise RateLimitError(
                "Rate limit exceeded",
                status_code=response.status_code,
                response_data=response_data,
                retry_after=retry_after,
            )
        else:
            error_message = response_data.get("message", f"HTTP {response.status_code}")
            raise APIError(
                error_message,
                status_code=response.status_code,
                response_data=response_data,
            )

    @retry_on_rate_limit(max_retries=3)
    def get(
        self,
        endpoint: str,
        params: dict[str, any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> dict[str, any]:
        """
        Make a GET request.

        Args:
            endpoint: API endpoint
            params: Query parameters
            headers: Additional headers

        Returns:
            Response data
        """
        self._enforce_rate_limit()

        url = urljoin(self.base_url + "/", endpoint.lstrip("/"))

        response = self.session.get(
            url,
            params=params,
            headers=headers,
            timeout=self.timeout,
        )

        return self._handle_response(response)

    @retry_on_rate_limit(max_retries=3)
    def post(
        self,
        endpoint: str,
        data: dict[str, any] | None = None,
        json_data: dict[str, any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> dict[str, any]:
        """
        Make a POST request.

        Args:
            endpoint: API endpoint
            data: Form data
            json_data: JSON data
            headers: Additional headers

        Returns:
            Response data
        """
        self._enforce_rate_limit()

        url = urljoin(self.base_url + "/", endpoint.lstrip("/"))

        response = self.session.post(
            url,
            data=data,
            json=json_data,
            headers=headers,
            timeout=self.timeout,
        )

        return self._handle_response(response)

    def close(self) -> None:
        """Close the HTTP session."""
        self.session.close()