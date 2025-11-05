import time
from unittest.mock import MagicMock, Mock, patch
from uuid import uuid4

import responses
from pytest_httpx import HTTPXMock

from griddy.nfl import models
from griddy.nfl._hooks.hack_auth import HackAuthHook
from griddy.nfl._hooks.types import BeforeRequestContext, HookContext
from griddy.nfl.sdk import GriddyNFL

fake_sched_resp = {
    "weeks": [
        {
            "season": 2025,
            "seasonType": "PRE",
            "week": 0,
            "byeTeams": [],
            "dateBegin": "2025-07-28",
            "dateEnd": "2025-08-06",
            "weekType": "HOF",
            "weekSlug": "HOF",
            "text": "HOF Game",
            "seasonTypeWeek": "PRE-0",
        },
        {
            "season": 2025,
            "seasonType": "PRE",
            "week": 1,
            "byeTeams": [],
            "dateBegin": "2025-08-06",
            "dateEnd": "2025-08-13",
            "weekType": "PRE",
            "weekSlug": "P1",
            "text": "Preseason 1",
            "seasonTypeWeek": "PRE-1",
        },
        {
            "season": 2025,
            "seasonType": "PRE",
            "week": 2,
            "byeTeams": [],
            "dateBegin": "2025-08-13",
            "dateEnd": "2025-08-20",
            "weekType": "PRE",
            "weekSlug": "P2",
            "text": "Preseason 2",
            "seasonTypeWeek": "PRE-2",
        },
        {
            "season": 2025,
            "seasonType": "PRE",
            "week": 3,
            "byeTeams": [],
            "dateBegin": "2025-08-20",
            "dateEnd": "2025-08-27",
            "weekType": "PRE",
            "weekSlug": "P3",
            "text": "Preseason 3",
            "seasonTypeWeek": "PRE-3",
        },
        {
            "season": 2025,
            "seasonType": "REG",
            "week": 1,
            "byeTeams": [],
            "dateBegin": "2025-08-27",
            "dateEnd": "2025-09-10",
            "weekType": "REG",
            "weekSlug": "WEEK_1",
            "text": "Week 1",
            "seasonTypeWeek": "REG-1",
        },
        {
            "season": 2025,
            "seasonType": "REG",
            "week": 2,
            "byeTeams": [],
            "dateBegin": "2025-09-10",
            "dateEnd": "2025-09-17",
            "weekType": "REG",
            "weekSlug": "WEEK_2",
            "text": "Week 2",
            "seasonTypeWeek": "REG-2",
        },
        {
            "season": 2025,
            "seasonType": "REG",
            "week": 3,
            "byeTeams": [],
            "dateBegin": "2025-09-17",
            "dateEnd": "2025-09-24",
            "weekType": "REG",
            "weekSlug": "WEEK_3",
            "text": "Week 3",
            "seasonTypeWeek": "REG-3",
        },
        {
            "season": 2025,
            "seasonType": "REG",
            "week": 4,
            "byeTeams": [],
            "dateBegin": "2025-09-24",
            "dateEnd": "2025-10-01",
            "weekType": "REG",
            "weekSlug": "WEEK_4",
            "text": "Week 4",
            "seasonTypeWeek": "REG-4",
        },
        {
            "season": 2025,
            "seasonType": "REG",
            "week": 5,
            "byeTeams": [
                {
                    "id": "10400200-f401-4e53-5175-0974e4f16cf7",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/ATL",
                    "fullName": "Atlanta Falcons",
                },
                {
                    "id": "10400810-db30-43d6-221c-620006f3ca19",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/CHI",
                    "fullName": "Chicago Bears",
                },
                {
                    "id": "10401800-ab22-323d-721a-cee4713c4c2d",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/GB",
                    "fullName": "Green Bay Packers",
                },
                {
                    "id": "10403900-8251-6892-d81c-4348525c2d47",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/PIT",
                    "fullName": "Pittsburgh Steelers",
                },
            ],
            "dateBegin": "2025-10-01",
            "dateEnd": "2025-10-08",
            "weekType": "REG",
            "weekSlug": "WEEK_5",
            "text": "Week 5",
            "seasonTypeWeek": "REG-5",
        },
        {
            "season": 2025,
            "seasonType": "REG",
            "week": 6,
            "byeTeams": [
                {
                    "id": "10402120-b0bc-693d-098a-803014096eb0",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/HOU",
                    "fullName": "Houston Texans",
                },
                {
                    "id": "10403000-5851-f9d5-da45-78365a05b6b0",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/MIN",
                    "fullName": "Minnesota Vikings",
                },
            ],
            "dateBegin": "2025-10-08",
            "dateEnd": "2025-10-15",
            "weekType": "REG",
            "weekSlug": "WEEK_6",
            "text": "Week 6",
            "seasonTypeWeek": "REG-6",
        },
        {
            "season": 2025,
            "seasonType": "REG",
            "week": 7,
            "byeTeams": [
                {
                    "id": "10400325-48de-3d6a-be29-8f829437f4c8",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/BAL",
                    "fullName": "Baltimore Ravens",
                },
                {
                    "id": "10400610-c40e-a673-1743-2ce2a5d5d731",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/BUF",
                    "fullName": "Buffalo Bills",
                },
            ],
            "dateBegin": "2025-10-15",
            "dateEnd": "2025-10-22",
            "weekType": "REG",
            "weekSlug": "WEEK_7",
            "text": "Week 7",
            "seasonTypeWeek": "REG-7",
        },
        {
            "season": 2025,
            "seasonType": "REG",
            "week": 8,
            "byeTeams": [
                {
                    "id": "10403800-517c-7b8c-65a3-c61b95d86123",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/ARI",
                    "fullName": "Arizona Cardinals",
                },
                {
                    "id": "10401540-f97c-2d19-6fcd-fac6490a48b7",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/DET",
                    "fullName": "Detroit Lions",
                },
                {
                    "id": "10402250-89fe-7b86-ef98-9062cd354256",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/JAX",
                    "fullName": "Jacksonville Jaguars",
                },
                {
                    "id": "10402520-96bf-e9f2-4f68-8521ca896060",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/LV",
                    "fullName": "Las Vegas Raiders",
                },
                {
                    "id": "10402510-8931-0d5f-9815-79bb79649a65",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/LA",
                    "fullName": "Los Angeles Rams",
                },
                {
                    "id": "10404600-adcd-28ac-5826-b4d95ec2a228",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/SEA",
                    "fullName": "Seattle Seahawks",
                },
            ],
            "dateBegin": "2025-10-22",
            "dateEnd": "2025-10-29",
            "weekType": "REG",
            "weekSlug": "WEEK_8",
            "text": "Week 8",
            "seasonTypeWeek": "REG-8",
        },
        {
            "season": 2025,
            "seasonType": "REG",
            "week": 9,
            "byeTeams": [
                {
                    "id": "10401050-5e38-b907-1be1-55b91b19c057",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/CLE",
                    "fullName": "Cleveland Browns",
                },
                {
                    "id": "10403430-1bc3-42c4-c7d8-39f38aed5f12",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/NYJ",
                    "fullName": "New York Jets",
                },
                {
                    "id": "10403700-b939-3cbd-3d16-24d4d6742fa2",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/PHI",
                    "fullName": "Philadelphia Eagles",
                },
                {
                    "id": "10404900-d59e-b449-ef75-961e09ca027e",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/TB",
                    "fullName": "Tampa Bay Buccaneers",
                },
            ],
            "dateBegin": "2025-10-29",
            "dateEnd": "2025-11-05",
            "weekType": "REG",
            "weekSlug": "WEEK_9",
            "text": "Week 9",
            "seasonTypeWeek": "REG-9",
        },
        {
            "season": 2025,
            "seasonType": "REG",
            "week": 10,
            "byeTeams": [
                {
                    "id": "10400920-57c1-7656-e77e-1af3d900483e",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/CIN",
                    "fullName": "Cincinnati Bengals",
                },
                {
                    "id": "10401200-a308-98ca-ad5f-95df2fefea68",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/DAL",
                    "fullName": "Dallas Cowboys",
                },
                {
                    "id": "10402310-a47e-10ea-7442-16b633633637",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/KC",
                    "fullName": "Kansas City Chiefs",
                },
                {
                    "id": "10402100-447f-396e-8149-0a434ffb2f23",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/TEN",
                    "fullName": "Tennessee Titans",
                },
            ],
            "dateBegin": "2025-11-05",
            "dateEnd": "2025-11-12",
            "weekType": "REG",
            "weekSlug": "WEEK_10",
            "text": "Week 10",
            "seasonTypeWeek": "REG-10",
        },
        {
            "season": 2025,
            "seasonType": "REG",
            "week": 11,
            "byeTeams": [
                {
                    "id": "10402200-2ea3-84c3-e627-6a6b3b39d56d",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/IND",
                    "fullName": "Indianapolis Colts",
                },
                {
                    "id": "10403300-f235-cf9b-6d3a-2f182be48dd1",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/NO",
                    "fullName": "New Orleans Saints",
                },
            ],
            "dateBegin": "2025-11-12",
            "dateEnd": "2025-11-19",
            "weekType": "REG",
            "weekSlug": "WEEK_11",
            "text": "Week 11",
            "seasonTypeWeek": "REG-11",
        },
        {
            "season": 2025,
            "seasonType": "REG",
            "week": 12,
            "byeTeams": [
                {
                    "id": "10401400-b89b-96e5-55d1-caa7e18de3d8",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/DEN",
                    "fullName": "Denver Broncos",
                },
                {
                    "id": "10404400-3b35-073f-197e-194bb8240723",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/LAC",
                    "fullName": "Los Angeles Chargers",
                },
                {
                    "id": "10402700-1662-d8ad-f45c-0b0ea460d045",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/MIA",
                    "fullName": "Miami Dolphins",
                },
                {
                    "id": "10405110-ec3c-669e-2614-db3dc1736e95",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/WAS",
                    "fullName": "Washington Commanders",
                },
            ],
            "dateBegin": "2025-11-19",
            "dateEnd": "2025-11-26",
            "weekType": "REG",
            "weekSlug": "WEEK_12",
            "text": "Week 12",
            "seasonTypeWeek": "REG-12",
        },
        {
            "season": 2025,
            "seasonType": "REG",
            "week": 13,
            "byeTeams": [],
            "dateBegin": "2025-11-26",
            "dateEnd": "2025-12-03",
            "weekType": "REG",
            "weekSlug": "WEEK_13",
            "text": "Week 13",
            "seasonTypeWeek": "REG-13",
        },
        {
            "season": 2025,
            "seasonType": "REG",
            "week": 14,
            "byeTeams": [
                {
                    "id": "10400750-259b-33ac-eee3-a3852e83cd1f",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/CAR",
                    "fullName": "Carolina Panthers",
                },
                {
                    "id": "10403200-69ab-9ea6-5af5-e240fbc08bea",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/NE",
                    "fullName": "New England Patriots",
                },
                {
                    "id": "10403410-997c-9c75-256b-3b012f468bd0",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/NYG",
                    "fullName": "New York Giants",
                },
                {
                    "id": "10404500-e7cb-7fce-3f10-4eeb269bd179",
                    "currentLogo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/SF",
                    "fullName": "San Francisco 49ers",
                },
            ],
            "dateBegin": "2025-12-03",
            "dateEnd": "2025-12-10",
            "weekType": "REG",
            "weekSlug": "WEEK_14",
            "text": "Week 14",
            "seasonTypeWeek": "REG-14",
        },
        {
            "season": 2025,
            "seasonType": "REG",
            "week": 15,
            "byeTeams": [],
            "dateBegin": "2025-12-10",
            "dateEnd": "2025-12-17",
            "weekType": "REG",
            "weekSlug": "WEEK_15",
            "text": "Week 15",
            "seasonTypeWeek": "REG-15",
        },
        {
            "season": 2025,
            "seasonType": "REG",
            "week": 16,
            "byeTeams": [],
            "dateBegin": "2025-12-17",
            "dateEnd": "2025-12-24",
            "weekType": "REG",
            "weekSlug": "WEEK_16",
            "text": "Week 16",
            "seasonTypeWeek": "REG-16",
        },
        {
            "season": 2025,
            "seasonType": "REG",
            "week": 17,
            "byeTeams": [],
            "dateBegin": "2025-12-24",
            "dateEnd": "2025-12-31",
            "weekType": "REG",
            "weekSlug": "WEEK_17",
            "text": "Week 17",
            "seasonTypeWeek": "REG-17",
        },
        {
            "season": 2025,
            "seasonType": "REG",
            "week": 18,
            "byeTeams": [],
            "dateBegin": "2025-12-31",
            "dateEnd": "2026-01-07",
            "weekType": "REG",
            "weekSlug": "WEEK_18",
            "text": "Week 18",
            "seasonTypeWeek": "REG-18",
        },
    ],
    "pagination": {"limit": 40, "token": None},
    "season": "2025",
}


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

    @patch("griddy.nfl._hooks.hack_auth.HackAuthHook.before_request")
    def test_hook_invoked_before_sdk_request(self, mock_before_request, httpx_mock):
        """Test that HackAuthHook.before_request is called when SDK makes a request"""
        # Configure mock to pass through the request unchanged
        mock_before_request.side_effect = lambda hook_ctx, request: request

        httpx_mock.add_response(
            url="https://pro.nfl.com/api/schedules/weeks?season=2025",
            json=fake_sched_resp,
        )

        # Create SDK instance with valid auth that won't trigger refresh
        auth_info = {
            "expiresIn": time.time() + 3600,  # Valid for 1 hour
            "refreshToken": str(uuid4()),
            "accessToken": "TEST_TOKEN",
        }

        nfl = GriddyNFL(nfl_auth=auth_info)

        # Verify the hook was registered by checking the hooks list
        hooks = nfl.sdk_configuration.__dict__["_hooks"]
        assert len(hooks.before_request_hooks) > 0, "No before_request hooks registered"

        # Verify at least one hook is HackAuthHook
        has_hack_auth_hook = any(
            isinstance(hook, HackAuthHook) for hook in hooks.before_request_hooks
        )
        assert has_hack_auth_hook, "HackAuthHook was not registered"

        nfl.schedules.get_schedule_season_weeks(season=2025)

        assert (
            mock_before_request.call_count == 1
        ), "HackAuthHook.before_request was not called"
