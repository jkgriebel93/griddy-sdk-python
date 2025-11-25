from datetime import date
from typing import List, Mapping, Optional

from . import errors, models, utils
from ._hooks import HookContext
from .basesdk import BaseSDK
from .types import UNSET, OptionalNullable
from .utils import get_security_from_env
from .utils.unmarshal_json_response import unmarshal_json_response


# TODO: A bunch of these endpoints seem to have disappeared since a few weeks ago?
class Football(BaseSDK):
    r"""Football API endpoints for games, standings, stats, and venues"""

    # TODO: Box score, play by play return 404. Was this always the case?
    # In fact, all the paths from here on seem to return 404. Not sure if these were
    # Never valid, or if something changed.

    def get_transactions(
        self,
        *,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        team_id: Optional[str] = None,
        transaction_type: Optional[models.GetTransactionsTransactionType] = None,
        limit: Optional[int] = 20,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TransactionsResponse:
        r"""Get Transactions

        Retrieves recent transactions including trades, signings, releases,
        practice squad moves, and injured reserve designations.


        :param start_date: Start date for transactions (ISO 8601)
        :param end_date: End date for transactions (ISO 8601)
        :param team_id: Filter by team
        :param transaction_type: Type of transaction
        :param limit: Maximum number of results
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.GetTransactionsRequest(
            start_date=start_date,
            end_date=end_date,
            team_id=team_id,
            transaction_type=transaction_type,
            limit=limit,
        )

        req = self._build_request(
            method="GET",
            path="/football/v2/transactions",
            base_url=base_url,
            url_variables=url_variables,
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

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="getTransactions",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            # return unmarshal_json_response(models.TransactionsResponse, http_res)
            return http_res.json()
        if utils.match_response(http_res, ["400", "401", "4XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.GriddyNFLDefaultError(
                "API error occurred", http_res, http_res_text
            )
        if utils.match_response(http_res, ["500", "5XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.GriddyNFLDefaultError(
                "API error occurred", http_res, http_res_text
            )

        raise errors.GriddyNFLDefaultError("Unexpected response received", http_res)
