from griddy.nfl import GriddyNFL

nfl = GriddyNFL("cookies.txt")

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
from pprint import pprint
pprint(replay.model_dump(), indent=4)
