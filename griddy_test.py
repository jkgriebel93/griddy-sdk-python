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
sum_play = nfl.games.get_summary_play(game_id=fapi_game_id, play_id=74)
print(sum_play.model_dump_json(indent=4))
