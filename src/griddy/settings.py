from pathlib import Path
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings


class NFLSettings(BaseSettings):
    model_config = {"env_prefix": "NFL_"}

    api_key: Optional[str] = None
    sdk_build: str = "15170"
    client_key: Optional[str] = None
    client_secret: Optional[str] = None
    auth_url: str = "https://auth-id.nfl.com/"
    account_url: str = "https://auth-id.nfl.com/accounts.getAccountInfo"
    token_url: str = "https://api.nfl.com/identity/v3/token"
    base_api_url: str = "https://api.nfl.com/football/v2/"
    pro_api_base_url: str = "https://pro.nfl.com/api/"
    login_email: Optional[str] = None
    login_password: Optional[str] = None


class BrowserlessSettings(BaseSettings):
    model_config = {"env_prefix": "BROWSERLESS_"}

    host: Optional[str] = None
    token: Optional[str] = None


class GriddySettings(BaseSettings):
    nfl: NFLSettings = Field(default_factory=NFLSettings)
    browserless: BrowserlessSettings = Field(default_factory=BrowserlessSettings)

    @property
    def fixture_dir(self) -> Path:
        return Path(__file__).resolve().parents[2] / "tests" / "fixtures"


settings = GriddySettings()

# Convenience aliases for backwards compatibility
NFL = settings.nfl
BROWSERLESS_HOST = settings.browserless.host
BROWSERLESS_TOKEN = settings.browserless.token
FIXTURE_DIR = settings.fixture_dir
