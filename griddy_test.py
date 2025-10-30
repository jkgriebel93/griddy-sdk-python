from pprint import pprint
from griddy.nfl.endpoints.pro.players import get_player
from griddy.nfl import GriddyNFL

simple_response = get_player(46101)
pprint(simple_response.json(), indent=4)

nfl = GriddyNFL("cookies.txt")
player_response = nfl.players.get_player(nfl_id=46101)
pprint(player_response.model_dump(), indent=4)



response = nfl.football.get_weekly_game_details(
    season=2025,
    type_="REG",
    week=5,
    include_drive_chart=True,
    include_replays=True,
    include_standings=True,
    include_tagged_videos=False,
)
game = response[0]
replay = game.replays[0]
pprint(replay.model_dump(), indent=4)


