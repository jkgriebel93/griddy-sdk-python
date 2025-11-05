import time
from unittest.mock import MagicMock, Mock, patch
from uuid import uuid4

import responses

from griddy.nfl import models
from griddy.nfl._hooks.hack_auth import HackAuthHook
from griddy.nfl._hooks.types import BeforeRequestContext, HookContext
from griddy.nfl.sdk import GriddyNFL


class TestHackAuthHook:
    @patch("griddy.nfl._hooks.hack_auth.requests.post")
    def test_do_refresh_token_makes_correct_request(self, mock_post):
        test_refresh_token = str(uuid4())
        fake_auth_response = {
            "expiresIn": time.time() + 3600,
            "refreshToken": str(uuid4()),
            "accessToken": "TEST_ACCESS_TOKEN",
        }

        # Configure the mock
        mock_response = MagicMock()
        mock_response.json.return_value = fake_auth_response
        mock_post.return_value = mock_response

        # Create hook and call _do_refresh_token
        hook = HackAuthHook()
        result = hook._do_refresh_token(refresh_token=test_refresh_token)

        # Verify requests.post was called with correct parameters
        mock_post.assert_called_once()
        call_args = mock_post.call_args

        # Verify URL
        assert "url" in call_args.kwargs
        assert call_args.kwargs["url"].endswith("/refresh")

        # Verify data includes refresh token and base request data
        assert "data" in call_args.kwargs
        assert call_args.kwargs["data"]["refreshToken"] == test_refresh_token
        assert "clientKey" in call_args.kwargs["data"]
        assert "clientSecret" in call_args.kwargs["data"]
        assert "deviceId" in call_args.kwargs["data"]

        # Verify the result matches the mocked response
        assert result == fake_auth_response

        # Verify raise_for_status was called
        mock_response.raise_for_status.assert_called_once()

    @responses.activate
    def test_before_request_calls_refresh_when_inside_window(self):

        fake_auth_response = {
            "expiresIn": time.time() + 3600,
            "refreshToken": str(uuid4()),
            "accessToken": "FUBAR",
        }

        responses.add(
            responses.POST,
            "https://api.nfl.com/identity/v3/token/refresh",
            json=fake_auth_response,
            status=200,
        )
        mock_request = MagicMock()

        original_auth_info = {
            "expiresIn": time.time(),
            "refreshToken": str(uuid4()),
            "accessToken": "ZEBRA",
        }

        nfl = GriddyNFL(nfl_auth=original_auth_info)

        hook = HackAuthHook()
        hook.before_request(
            hook_ctx=BeforeRequestContext(
                hook_ctx=HookContext(
                    config=nfl.sdk_configuration,
                    base_url="https://pro.nfl.com/api",
                    operation_id="getTestOperation",
                    oauth2_scopes=[],
                    security_source=nfl.sdk_configuration.security,
                )
            ),
            request=mock_request,
        )

        post_hook_custom_auth_info = nfl.sdk_configuration.custom_auth_info
        post_hook_security_obj = nfl.sdk_configuration.security

        assert post_hook_custom_auth_info == fake_auth_response
        assert post_hook_security_obj == models.Security(
            nfl_auth=fake_auth_response["accessToken"]
        )
