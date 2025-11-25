from datetime import date
from typing import List, Mapping, Optional

from griddy.nfl import errors, models, utils
from griddy.nfl._hooks import HookContext
from griddy.nfl.endpoints.pro import ProSDK
from griddy.nfl.types import UNSET, OptionalNullable
from griddy.nfl.utils import get_security_from_env
from griddy.nfl.utils.unmarshal_json_response import unmarshal_json_response


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
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

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
            # TODO: Fix Pydantic models
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
