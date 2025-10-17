# GameSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_date** | **str** | Game date MM/DD/YYYY | [optional] 
**game_id** | **int** |  | [optional] 
**game_key** | **int** |  | [optional] 
**game_time** | **datetime** |  | [optional] 
**game_time_eastern** | **str** | Eastern time | [optional] 
**game_type** | [**SeasonTypeEnum**](SeasonTypeEnum.md) |  | [optional] 
**home_display_name** | **str** |  | [optional] 
**home_nickname** | **str** |  | [optional] 
**home_team** | [**TeamInfo**](TeamInfo.md) |  | [optional] 
**home_team_abbr** | **str** |  | [optional] 
**home_team_id** | **str** |  | [optional] 
**iso_time** | **int** | ISO timestamp in milliseconds | [optional] 
**network_channel** | **str** | Broadcast network | [optional] 
**ngs_game** | **bool** | Next Gen Stats available | [optional] 
**released_to_clubs** | **bool** |  | [optional] 
**score** | [**GameScore**](GameScore.md) |  | [optional] 
**season** | **int** |  | [optional] 
**season_type** | [**SeasonTypeEnum**](SeasonTypeEnum.md) |  | [optional] 
**site** | [**VenueInfo**](VenueInfo.md) |  | [optional] 
**smart_id** | **str** |  | [optional] 
**validated** | **bool** |  | [optional] 
**visitor_display_name** | **str** |  | [optional] 
**visitor_nickname** | **str** |  | [optional] 
**visitor_team** | [**TeamInfo**](TeamInfo.md) |  | [optional] 
**visitor_team_abbr** | **str** |  | [optional] 
**visitor_team_id** | **str** |  | [optional] 
**week** | **int** |  | [optional] 
**week_name_abbr** | **str** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.game_schedule import GameSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of GameSchedule from a JSON string
game_schedule_instance = GameSchedule.from_json(json)
# print the JSON string representation of the object
print(GameSchedule.to_json())

# convert the object into a dict
game_schedule_dict = game_schedule_instance.to_dict()
# create an instance of GameSchedule from a dict
game_schedule_from_dict = GameSchedule.from_dict(game_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


