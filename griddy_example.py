import json
import sys
from datetime import date
from pprint import pprint

from griddy.nfl import GriddyNFL
from griddy.settings import NFL

_, *args = sys.argv

#
# # Lamar Jackson = 46101
if len(args) == 1:
    with open(args[0], "r") as infile:
        custom_auth_info = json.load(infile)
    nfl = GriddyNFL(nfl_auth=custom_auth_info)
else:
    nfl = GriddyNFL(
        login_email=NFL["login_email"], login_password=NFL["login_password"]
    )

# This game_id is for 2025 Wk 08 Green Bay at Pittsburgh
fapi_game_id = "f773ee57-311e-11f0-b670-ae1250fadad1"
team_id = "10403800-517c-7b8c-65a3-c61b95d86123"
player_id = "2560726"
reg_game_id = "2025102610"

result = nfl.pro_games.get_game_team_rankings(
    season=2025,
    season_type="REG",
    home_team_id="10403900-8251-6892-d81c-4348525c2d47",
    away_team_id="10401800-ab22-323d-721a-cee4713c4c2d",
    week=8,
)


is_pydantic = False

if is_pydantic:
    if isinstance(result, list):
        for r in result:
            pprint(r.model_dump(), indent=4)
    else:
        pprint(result.model_dump(), indent=4)
else:
    print(json.dumps(result, indent=4))
