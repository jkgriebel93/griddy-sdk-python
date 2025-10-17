import sys

from griddy import nfl
from griddy.nfl import NFLAPIClient, NFLConfiguration

_, bearer_token = sys.argv

config = NFLConfiguration(access_token=bearer_token)

with NFLAPIClient(configuration=config) as api_client:
    api_instance = nfl.FootballController(api_client=api_client)
    season = 2025
    type_ = nfl.SeasonTypeEnum.REG
    week = 7

    try:
        response = api_instance.get_weekly_game_details(season=season,
                                                        type=type_,
                                                        week=week)
        print("API Response:\n\n\n")
        from pprint import pprint
        pprint(response, indent=4)
    except Exception as e:
        raise e
