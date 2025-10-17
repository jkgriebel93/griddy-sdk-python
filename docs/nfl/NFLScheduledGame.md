# NFLScheduledGame


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_date** | **date** | Game date (YYYY-MM-DD format) | [optional] 
**game_id** | **int** | Game identifier (format is YYYYMMDDNN) | [optional] 
**game_key** | **int** | Unique game key | [optional] 
**game_time** | **datetime** | Game time in UTC | [optional] 
**game_time_eastern** | **str** | Game time in Eastern timezone (HH:MM:SS) | [optional] 
**game_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 
**home_display_name** | **str** | Home team display name | [optional] 
**home_nickname** | **str** | Home team nickname | [optional] 
**home_team** | [**NFLNFLBoxscoreTeam**](NFLBoxscoreTeam.md) |  | [optional] 
**home_team_abbr** | **str** | Home team abbreviation | [optional] 
**home_team_id** | **str** | Home team identifier | [optional] 
**iso_time** | **int** | Unix timestamp in milliseconds | [optional] 
**network_channel** | **str** | Broadcast network | [optional] 
**ngs_game** | **bool** | Whether Next Gen Stats are available | [optional] 
**released_to_clubs** | **bool** | Whether game info is released to clubs | [optional] 
**score** | [**NFLNFLGameScore**](NFLGameScore.md) |  | [optional] 
**season** | **int** | Season year | [optional] 
**season_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 
**site** | [**NFLNFLSite**](NFLSite.md) |  | [optional] 
**smart_id** | **str** | Smart identifier for the game | [optional] 
**validated** | **bool** | Whether game info is validated | [optional] 
**visitor_display_name** | **str** | Visitor team display name | [optional] 
**visitor_nickname** | **str** | Visitor team nickname | [optional] 
**visitor_team** | [**NFLNFLBoxscoreTeam**](NFLBoxscoreTeam.md) |  | [optional] 
**visitor_team_abbr** | **str** | Visitor team abbreviation | [optional] 
**visitor_team_id** | **str** | Visitor team identifier | [optional] 
**week** | **int** | Week number | [optional] 
**week_name_abbr** | **str** | Week name abbreviation | [optional] 

## Example

```python
from nfl.models.nfl_scheduled_game import NFLScheduledGame

# TODO update the JSON string below
json = "{}"
# create an instance of NFLScheduledGame from a JSON string
nfl_scheduled_game_instance = NFLScheduledGame.from_json(json)
# print the JSON string representation of the object
print(NFLScheduledGame.to_json())

# convert the object into a dict
nfl_scheduled_game_dict = nfl_scheduled_game_instance.to_dict()
# create an instance of NFLScheduledGame from a dict
nfl_scheduled_game_from_dict = NFLScheduledGame.from_dict(nfl_scheduled_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


