from pprint import pprint

from griddy.nfl import GriddyNFL

# Lamar Jackson = 46101

nfl = GriddyNFL("cookies.txt")
response = nfl.schedules.get_scheduled_games(season=2025, season_type="REG", week=9)
print("\n\n\n=====get_scheduled_games()=====\n\n\n")
pprint(response.model_dump(), indent=4)

response = nfl.games.get_game_preview(
    season=2025,
    season_type="REG",
    week=9,
    visitor_display_name="Baltimore Ravens",
    home_display_name="Miami Dolphins",
)
pprint(response, indent=4)
