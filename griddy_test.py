from pprint import pprint

from griddy.nfl import GriddyNFL

# Lamar Jackson = 46101

nfl = GriddyNFL("cookies.txt")
all_teams_response = nfl.teams.get_all_teams()
example_team = all_teams_response[0]
pprint(example_team.model_dump(), indent=4)
