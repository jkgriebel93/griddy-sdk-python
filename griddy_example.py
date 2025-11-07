import json
import sys
from pprint import pprint

from griddy.nfl import GriddyNFL
from griddy.settings import NFL

# _, creds_file = sys.argv
#
# # Lamar Jackson = 46101
# with open(creds_file, "r") as infile:
#     custom_auth_info = json.load(infile)
#

nfl = GriddyNFL(login_email=NFL["login_email"], login_password=NFL["login_password"])

# This game_id is for 2025 Wk 08 Green Bay at Pittsburgh
fapi_game_id = "f773ee57-311e-11f0-b670-ae1250fadad1"
game_id = "2025102610"
sched = nfl.schedules.get_scheduled_games(season=2025, season_type="REG", week=1)
pprint(sched.model_dump(), indent=4)
