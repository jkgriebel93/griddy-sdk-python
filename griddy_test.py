import time
from datetime import datetime
import sys
from pprint import pprint

from griddy.nfl import GriddyNFL

_, access_token, refresh_token, expires_in = sys.argv

# Lamar Jackson = 46101
custom_auth_info = {
    "expiresIn": float(expires_in),
    "refreshToken": refresh_token,
    "accessToken": access_token,
}


nfl = GriddyNFL(nfl_auth=custom_auth_info)

# This game_id is for 2025 Wk 08 Green Bay at Pittsburgh
fapi_game_id = "f773ee57-311e-11f0-b670-ae1250fadad1"
game_id = "2025102610"

resp = nfl.games.get_playlist(game_id=game_id)
pprint(resp, indent=4)
