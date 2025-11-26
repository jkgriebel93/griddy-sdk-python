from typing import Mapping, Optional

from griddy.nfl import models, utils
from griddy.nfl._constants import COLLECTION_ERROR_CODES
from griddy.nfl.endpoints.pro import ProSDK
from griddy.nfl.types import UNSET, OptionalNullable


# TODO: A bunch of these endpoints seem to have disappeared since a few weeks ago?
class Transactions(ProSDK):

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
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetTransactionsRequest(
            month=month,
            year=year,
            team_id=team_id,
            limit=limit,
        )

        req = self._build_request(
            method="GET",
            path="/api/teams/transactions",
            base_url=base_url,
            url_variables=None,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        retry_config = self._resolve_retry_config(retries)

        http_res = self.do_request(
            hook_ctx=self._create_hook_context("getTransactions", base_url),
            request=req,
            error_status_codes=COLLECTION_ERROR_CODES,
            retry_config=retry_config,
        )

        # TODO: Fix Pydantic models
        # Once fixed, use: return self._handle_json_response(http_res, models.TransactionsResponse, COLLECTION_ERROR_CODES)
        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return self._handle_json_response(
            http_res, models.TransactionsResponse, COLLECTION_ERROR_CODES
        )
