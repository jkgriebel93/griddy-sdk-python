import json
import sys
from pprint import pprint

from griddy.nfl import GriddyNFL
from griddy.settings import NFL
from tests.conftest import nfl_auth_info

_, *args = sys.argv

#
# # Lamar Jackson = 46101
if len(args) == 1:
    with open(args[0], "r") as infile:
        custom_auth_info = json.load(infile)
    nfl = GriddyNFL(nfl_auth=nfl_auth_info())
else:
    nfl = GriddyNFL(
        login_email=NFL["login_email"], login_password=NFL["login_password"]
    )

# This game_id is for 2025 Wk 08 Green Bay at Pittsburgh
fapi_game_id = "f773ee57-311e-11f0-b670-ae1250fadad1"
game_id = "2025102610"
result = nfl.draft.get_picks_report(year=2025, limit=10)
pprint(result, indent=4)
