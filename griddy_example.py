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

player_id = "2560726"
reg_game_id = "2025102610"

lions_uuid = "10401800-ab22-323d-721a-cee4713c4c2d"
packers_uuid = "10401540-f97c-2d19-6fcd-fac6490a48b7"
lions_at_packers_uuid = "f83858b1-311e-11f0-b670-ae1250fadad1"
lions_at_packers_ten_dig_id = "2025101600"

result = nfl.pro_games.get_plays_win_probability(game_id=reg_game_id)
# with open("plays_win_prob.json", "w") as outfile:
#     json.dump(result, outfile, indent=4)
print(result.model_dump_json(indent=4))
