from pprint import pprint

from griddy.nfl import GriddyNFL

# Lamar Jackson = 46101

nfl = GriddyNFL("cookies.txt")
response = nfl.schedules.get_scheduled_games(season=2025,
                                             season_type="REG",
                                             week=9)
sched_games = [g.model_dump() for g in response.games]
print("\n\n\n=====get_scheduled_games()=====\n\n\n")
pprint(sched_games[0], indent=4)

response = nfl.schedules.get_current_week_games()
print("\n\n\n=====get_current_week_games()=====\n\n\n")
pprint(response.model_dump(), indent=4)


response = nfl.schedules.get_future_betting_odds()
print("\n\n\n=====get_future_betting_odds()=====\n\n\n")
pprint(response.model_dump(), indent=4)


response = nfl.schedules.get_team_standings(season=2025,
                                            season_type="REG",
                                            week=9)
print("\n\n\n=====get_future_betting_odds()=====\n\n\n")
pprint(response.model_dump(), indent=4)