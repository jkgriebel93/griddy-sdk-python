from pprint import pprint
from griddy.nfl import GriddyNFL

# Lamar Jackson = 46101

nfl = GriddyNFL("cookies.txt")
player_response = nfl.players.get_player(nfl_id=46101)
pprint(player_response, indent=4)
