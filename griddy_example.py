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
# result = nfl.football_teams.get_teams(season=2025)
result = nfl.football.get_transactions(
    start_date=date(year=2025, month=10, day=1),
    end_date=date(year=2025, month=10, day=31),
)

is_pydantic = True

if is_pydantic:
    pprint(result.model_dump(), indent=4)
else:
    print(json.dumps(result, indent=4))
