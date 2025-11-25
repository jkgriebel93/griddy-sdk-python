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
team_id = "10403900-8251-6892-d81c-4348525c2d47"
player_id = "2560726"
reg_game_id = "2025102610"

result = nfl.betting.get_weekly_betting_odds(season=2025, season_type="REG", week=13)


is_pydantic = True

if is_pydantic:
    if isinstance(result, list):
        for r in result:
            if isinstance(r, dict):
                pprint(r, indent=4)
            else:
                pprint(r.model_dump(), indent=4)
    else:
        pprint(result.model_dump(), indent=4)
else:
    print(json.dumps(result, indent=4))
