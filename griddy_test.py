from pprint import pprint

from griddy.nfl import GriddyNFL

# Lamar Jackson = 46101

nfl = GriddyNFL("cookies.txt")
response = nfl.schedules.get_schedule_season_weeks(season=2025)
print("\n\n\n=====get_scheduled_games()=====\n\n\n")
pprint(response.model_dump(), indent=4)
