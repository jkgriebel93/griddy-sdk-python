"""Example script for testing all NGS SDK methods."""

import json
import sys
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

game_id = 2025090400
play_list_response = nfl.pro_games.get_playlist(game_id=str(game_id))
plays_as_json = [p.model_dump() for p in play_list_response.plays]
from pprint import pprint

pprint(plays_as_json, indent=4)
