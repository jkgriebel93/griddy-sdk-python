from typing import Mapping, Optional

from griddy_nfl import models, utils
from griddy_nfl._constants import COLLECTION_ERROR_CODES
from griddy_nfl.basesdk import EndpointConfig
from griddy_nfl.endpoints.pro import ProSDK
from griddy_nfl.types import UNSET, OptionalNullable


# TODO: A bunch of these endpoints seem to have disappeared since a few weeks ago?
class Transactions(ProSDK):

    def _get_transactions_config(
        self,
        *,
        month: int,
        year: int,
        team_id: Optional[str] = None,
        limit: Optional[int] = 20,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        """Create endpoint configuration for get_transactions."""
        return EndpointConfig(
            method="GET",
            path="/api/teams/transactions",
            operation_id="getTransactions",
            request=models.GetTransactionsRequest(
                month=month,
                year=year,
                team_id=team_id,
                limit=limit,
            ),
            response_type=models.TransactionsResponse,
            error_status_codes=COLLECTION_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )

    def get_transactions(
        self,
        *,
        month: int,
        year: int,
        team_id: Optional[str] = None,
        limit: Optional[int] = 20,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TransactionsResponse:
        r"""Get Transactions

        Retrieves recent transactions including trades, signings, releases,
        practice squad moves, and injured reserve designations.


        :param month: Month (number) to fetch transactions for
        :param year: Year (all four digits as int) to fetch transactions for
        :param team_id: Team UUID string
        :param limit: Maximum number of results
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_transactions_config(
            month=month,
            year=year,
            team_id=team_id,
            limit=limit,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_transactions_async(
        self,
        *,
        month: int,
        year: int,
        team_id: Optional[str] = None,
        limit: Optional[int] = 20,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TransactionsResponse:
        r"""Get Transactions

        Retrieves recent transactions including trades, signings, releases,
        practice squad moves, and injured reserve designations.


        :param month: Month (number) to fetch transactions for
        :param year: Year (all four digits as int) to fetch transactions for
        :param team_id: Team UUID string
        :param limit: Maximum number of results
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_transactions_config(
            month=month,
            year=year,
            team_id=team_id,
            limit=limit,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)
