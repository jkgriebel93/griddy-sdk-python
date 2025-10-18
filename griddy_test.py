import json

from griddy import nfl
from griddy.nfl import NFLAPIClient, NFLConfiguration

creds_file = ".nfl-auth.json"

config = NFLConfiguration(access_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRJZCI6ImU1MzVjN2MwLTgxN2YtNDc3Ni04OTkwLTU2NTU2ZjhiMTkyOCIsImNsaWVudEtleSI6IjRjRlVXNkRtd0pwelQ5TDdMckczcVJBY0FCRzVzMDRnIiwiZGV2aWNlSWQiOiJiYjg3ZWE4Ny03M2Q4LTQxNjItOTRmYS00YTNjYTMzYzZmYTIiLCJpc3MiOiJORkwiLCJwbGFucyI6W3sicGxhbiI6ImZyZWUiLCJleHBpcmF0aW9uRGF0ZSI6IjIwMjYtMTAtMTciLCJzb3VyY2UiOiJORkwiLCJzdGFydERhdGUiOiIyMDI1LTEwLTE3Iiwic3RhdHVzIjoiQUNUSVZFIiwidHJpYWwiOmZhbHNlfSx7InBsYW4iOiJORkxfUExVU19QUkVNSVVNIiwiYmlsbGluZ1R5cGUiOiJtb250aGx5IiwiZXhwaXJhdGlvbkRhdGUiOiIyMDI1LTEwLTI4IiwiZXh0ZXJuYWxTdWJzY3JpcHRpb25JZCI6Ind6cmw0ZDBpd2wxbiIsInNvdXJjZSI6IldFQiIsInN0YXJ0RGF0ZSI6IjIwMjUtMDktMjgiLCJzdGF0dXMiOiJBQ1RJVkUiLCJ0cmlhbCI6ZmFsc2V9XSwiRGlzcGxheU5hbWUiOiJXRUJfREVTS1RPUF9ERVNLVE9QIiwiTm90ZXMiOiIiLCJmb3JtRmFjdG9yIjoiREVTS1RPUCIsImx1cmFBcHBLZXkiOiJTWnM1N2RCR1J4Ykw3MjhsVnA3RFlRIiwicGxhdGZvcm0iOiJERVNLVE9QIiwicHJvZHVjdE5hbWUiOiJXRUIiLCJyb2xlcyI6WyJjb250ZW50IiwiZXhwZXJpZW5jZSIsImZvb3RiYWxsIiwidXRpbGl0aWVzIiwidGVhbXMiLCJwbGF5IiwibGl2ZSIsImlkZW50aXR5IiwibmdzX3N0YXRzIiwicGF5bWVudHNfYXBpIiwibmdzX3RyYWNraW5nIiwibmdzX3BsYXRmb3JtIiwibmdzX2NvbnRlbnQiLCJuZ3NfY29tYmluZSIsIm5nc19hZHZhbmNlZF9zdGF0cyIsIm5mbF9wcm8iLCJlY29tbSIsIm5mbF9pZF9hcGkiLCJ1dGlsaXRpZXNfbG9jYXRpb24iLCJpZGVudGl0eV9vaWRjIiwibmdzX3NzZSIsImFjY291bnRzIiwiY29uc2VudHMiLCJzdWJfcGFydG5lcnNoaXBzIiwiY29uY3VycmVuY3kiLCJrZXlzdG9yZSIsImZyZWUiLCJORkxfUExVU19QUkVNSVVNIl0sIm5ldHdvcmtUeXBlIjoib3RoZXIiLCJjaXR5IjoiYXRsYW50YSIsImNvdW50cnlDb2RlIjoiVVMiLCJkbWFDb2RlIjoiNTI0IiwiaG1hVGVhbXMiOlsiMTA0MDAyMDAtZjQwMS00ZTUzLTUxNzUtMDk3NGU0ZjE2Y2Y3Il0sInJlZ2lvbiI6IkdBIiwiemlwQ29kZSI6IjMwMzQ5IiwiYnJvd3NlciI6IkNocm9tZSIsImNlbGx1bGFyIjpmYWxzZSwiZW52aXJvbm1lbnQiOiJwcm9kdWN0aW9uIiwidWlkIjoiZGY5OTBhY2Q5NTFlNGJkNjk0MGMzYmFiYzQzNDE1ODQiLCJleHAiOjE3NjA3MTI1NDF9.clzL1DtdmP8fQPbRl0BqvqzNBmJEYst74o-cFJW5SWo",
                          creds_file=creds_file)
for attr in ["access_token", "expires_in", "refresh_token", "account_info"]:
    print(f"Attribute: {attr}")
    print(f"Value: {getattr(config, attr, None)}")

response = config._construct_token_request_data(is_refresh=False)
print(f"Token response status code: {response.status_code}")
print(f"Response data: \n\n{json.dumps(response.json(), indent=4)}\n\n")

config._handle_token_response(response=response)
print("After calling _handle_token_response:")

old_vals = {}
for attr in ["access_token", "expires_in", "refresh_token", "account_info"]:
    print(f"Attribute: {attr}")
    value = getattr(config, attr, None)
    print(f"Value: {value}")
    old_vals[attr] = value

config.token_refresh_hook()

post_refresh_vals = {}
print("Values after invoking token_refresh_hook")
for attr in ["access_token", "expires_in", "refresh_token", "account_info"]:
    print(f"Attribute: {attr}")
    value = getattr(config, attr, None)
    print(f"Value: {value}")
    post_refresh_vals[attr] = value

print("Which values have changed?")

for attr in ["access_token", "expires_in", "refresh_token", "account_info"]:
    is_different = old_vals[attr] != post_refresh_vals[attr]
    print(f"{attr} changed? {is_different}")


def dont_execute():
    with NFLAPIClient(configuration=config) as api_client:
        api_instance = nfl.FootballController(api_client=api_client)
        player_stats = nfl.PlayerStatisticsController(api_client=api_client)

        season = 2025
        type_ = nfl.SeasonTypeEnum.REG
        week = 7

        try:
            wgd_resp = api_instance.get_weekly_game_details(season=season,
                                                            type=type_,
                                                            week=week)
            # stats_response = player_stats.get_player_passing_stats_by_season(season=season,
            #                                                                  season_type=type_)
            # print(f"Weekly Game Details Response Status: {wgd_resp.status_code}")
            # print(f"Player Stats Response Status: {stats_response.status_code}")

            print("API Response:\n\n\n")
            from pprint import pprint
            pprint(wgd_resp[0].to_dict(), indent=4)

        except Exception as e:
            raise e

dont_execute()

