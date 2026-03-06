import base64
import json
import time
from typing import Any, Dict, Union
from uuid import uuid4

import httpx

from griddy import settings
from griddy.nfl._hooks.types import BeforeRequestContext, BeforeRequestHook
from griddy.nfl.models import NFLAuth, Security


class HackAuthHook(BeforeRequestHook):
    """Before-request hook that injects required NFL headers and auto-refreshes expired auth tokens."""

    refresh_req_data = {
        "clientKey": settings.NFL.client_key,
        "clientSecret": settings.NFL.client_secret,
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

    def _do_refresh_token(self, refresh_token: str) -> Dict[str, Any]:
        """Exchange a refresh token for new auth credentials via the NFL token endpoint.

        Args:
            refresh_token: The current refresh token to exchange.

        Returns:
            Parsed JSON response containing new access token, refresh token, and expiry.
        """
        refresh_url = f"{settings.NFL.token_url}/refresh"
        data = {**self.refresh_req_data, "refreshToken": refresh_token}
        response = httpx.post(url=refresh_url, data=data)
        response.raise_for_status()
        return response.json()

    def before_request(
        self, hook_ctx: BeforeRequestContext, request: httpx.Request
    ) -> Union[httpx.Request, Exception]:
        """Add required NFL headers and refresh the auth token if it is near expiry."""
        request.headers["referer"] = "https://nextgenstats.nfl.com/"
        request.headers["x-override-env"] = "false"
        request.headers["sec-fetch-dest"] = "empty"
        request.headers["sec-fetch-mode"] = "cors"
        request.headers["sec-fetch-site"] = "same-origin"
        request.headers["authority"] = "nextgenstats.nfl.com"

        auth_info = hook_ctx.config.custom_auth_info
        if (
            auth_info.expires_in is not None
            and (auth_info.expires_in - time.time()) < 30
        ):
            resp_data = self._do_refresh_token(refresh_token=auth_info.refresh_token)
            new_auth = NFLAuth.model_validate(resp_data)
            hook_ctx.config.custom_auth_info = new_auth
            hook_ctx.config.security = Security(nfl_auth=new_auth.access_token)
            request.headers["Authorization"] = f"Bearer {new_auth.access_token}"

        return request
