import time
from datetime import datetime
from pprint import pprint

from griddy.nfl import GriddyNFL

# Lamar Jackson = 46101
custom_auth_info = {
    "expiresIn": 1761863985,
    "refreshToken": "bar",
    "accessToken": "foo",
}


print(
    f"Access token expires in: {datetime.fromtimestamp(custom_auth_info['expiresIn'])}"
)

nfl = GriddyNFL(cookies_file="cookies.txt", nfl_auth=custom_auth_info)
response = nfl.schedules.get_scheduled_games(season=2025, season_type="REG", week=9)
print("\n\n\n=====get_scheduled_games()=====\n\n\n")


response = nfl.games.get_game_preview(
    season=2025,
    season_type="REG",
    week=9,
    visitor_display_name="Baltimore Ravens",
    home_display_name="Miami Dolphins",
)
# pprint(response, indent=4)
# This game_id is for 2025 Wk 08 Green Bay at Pittsburgh
fapi_game_id = "f773ee57-311e-11f0-b670-ae1250fadad1"
game_id = "2025102610"

resp = nfl.games.get_stats_boxscore(game_id=game_id)
pprint(resp, indent=4)
