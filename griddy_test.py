import json
import sys
from pprint import pprint

from griddy.nfl import GriddyNFL

_, creds_file = sys.argv

# Lamar Jackson = 46101
with open(creds_file, "r") as infile:
    custom_auth_info = json.load(infile)


nfl = GriddyNFL(nfl_auth=custom_auth_info)

# This game_id is for 2025 Wk 08 Green Bay at Pittsburgh
fapi_game_id = "f773ee57-311e-11f0-b670-ae1250fadad1"
game_id = "2025102610"

# TODO: I don't like the way you have to call this method.
# I'd like it to be something like nfl.player_stats.passing.get_week
#   I'll need to:
#   1. Create a player SDK class that contains the passing/receiving/rushing stats methods
#   2. Create a stats SDK class that has a player property
#   3. Add the stats mapping to GriddyNFL
defense_stats = nfl.player_defense_stats.get_weekly_pass_rush_summary(
    season=2025, season_type="REG", week="WEEK_8"
)
import json

print(json.dumps(defense_stats, indent=4))
