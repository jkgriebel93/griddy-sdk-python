import os
from uuid import uuid4


class Base:
    user_agent = os.getenv("USER_AGENT", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0")
    token_refresh_threshold = os.getenv("TOKEN_REFRESH_THRESHOLD", 30)


class NFL(Base):
    api_key = os.getenv("NFL_API_KEY")
    sdk_build = os.getenv("NFL_SDK_BUILD", "15170")

    clientKey = os.getenv("NFL_CLIENT_KEY")
    clientSecret = os.getenv("NFL_CLIENT_SECRET")
    deviceId = os.getenv("NFL_DEVICE_ID", str(uuid4()))

    auth_url = "https://auth-id.nfl.com/"
    account_url = "https://auth-id.nfl.com/accounts.getAccountInfo"
    token_url = "https://api.nfl.com/identity/v3/token"

    regular_api_base_url = "https://api.nfl.com"
    pro_api_base_url = "https://pro.nfl.com/api"

