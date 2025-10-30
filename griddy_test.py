from pprint import pprint

from griddy.nfl import GriddyNFL

# Lamar Jackson = 46101

nfl = GriddyNFL("cookies.txt")
response = nfl.schedules.get_scheduled_games(season=2025,
                                             week=9,
                                             season_type="REG")
pprint([g.model_dump() for g in response.games], indent=4)
