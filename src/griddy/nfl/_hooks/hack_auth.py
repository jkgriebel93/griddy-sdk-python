import base64
import json
import time
from typing import Union
from uuid import uuid4

import httpx
import requests

from griddy import settings
from griddy.nfl._hooks.types import BeforeRequestContext, BeforeRequestHook
from griddy.nfl.models import Security


class HackAuthHook(BeforeRequestHook):
    refresh_req_data = {
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

    def _do_refresh_token(self, refresh_token):
        refresh_url = f"{settings.NFL['token_url']}/refresh"
        data = {**self.refresh_req_data, "refreshToken": refresh_token}
        response = requests.post(url=refresh_url, data=data)
        response.raise_for_status()
        return response.json()

    def before_request(
        self, hook_ctx: BeforeRequestContext, request: httpx.Request
    ) -> Union[httpx.Request, Exception]:

        auth_info = hook_ctx.config.custom_auth_info
        if (auth_info["expiresIn"] - time.time()) < 30:
            resp_data = self._do_refresh_token(refresh_token=auth_info["refreshToken"])
            hook_ctx.config.custom_auth_info = resp_data
            hook_ctx.config.security = Security(nfl_auth=resp_data["accessToken"])

        return request
