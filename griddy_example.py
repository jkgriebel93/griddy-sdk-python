import json
import sys
from pprint import pprint

from griddy.nfl import GriddyNFL
from griddy.nfl.models.enums.combineenums import EventFilterEnum
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
game_id = "2025102610"
result = nfl.standings.get_standings(season=2025, season_type="REG", week=11, limit=100)

as_json = [sw.model_dump() for sw in result.weeks]
# pprint(result, indent=4)
print(json.dumps(as_json, indent=4))
