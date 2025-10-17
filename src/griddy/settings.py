import os
from uuid import uuid4

BASE = {
    "user_agent": os.getenv(
        "USER_AGENT",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    ),
    "token_refresh_threshold": 30,
}

NFL = {
    **BASE,
    "api_key": os.getenv("NFL_API_KEY"),
    "sdk_build": os.getenv("NFL_SDK_BUILD", "15170"),
    "clientKey": os.getenv("NFL_CLIENT_KEY"),
    "clientSecret": os.getenv("NFL_CLIENT_SECRET"),
    "deviceId": os.getenv("NFL_DEVICE_ID", str(uuid4())),
    "deviceInfo": os.getenv(
        "NFL_DEVICE_ID"
    ),  # TODO: An example of this is in the source code somewhere
    "auth_url": "https://auth-id.nfl.com/",
    "account_url": "https://auth-id.nfl.com/accounts.getAccountInfo",
    "token_url": "https://api.nfl.com/identity/v3/token",
    "base_api_url": "https://api.nfl.com/football/v2",
}
