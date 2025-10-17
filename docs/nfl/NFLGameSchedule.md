# NFLGameSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_date** | **str** | Game date MM/DD/YYYY | [optional] 
**game_id** | **int** |  | [optional] 
**game_key** | **int** |  | [optional] 
**game_time** | **datetime** |  | [optional] 
**game_time_eastern** | **str** | Eastern time | [optional] 
**game_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 
**home_display_name** | **str** |  | [optional] 
**home_nickname** | **str** |  | [optional] 
**home_team** | [**NFLNFLTeamInfo**](NFLTeamInfo.md) |  | [optional] 
**home_team_abbr** | **str** |  | [optional] 
**home_team_id** | **str** |  | [optional] 
**iso_time** | **int** | ISO timestamp in milliseconds | [optional] 
**network_channel** | **str** | Broadcast network | [optional] 
**ngs_game** | **bool** | Next Gen Stats available | [optional] 
**released_to_clubs** | **bool** |  | [optional] 
**score** | [**NFLNFLGameScore**](NFLGameScore.md) |  | [optional] 
**season** | **int** |  | [optional] 
**season_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 
**site** | [**NFLNFLVenueInfo**](NFLVenueInfo.md) |  | [optional] 
**smart_id** | **str** |  | [optional] 
**validated** | **bool** |  | [optional] 
**visitor_display_name** | **str** |  | [optional] 
**visitor_nickname** | **str** |  | [optional] 
**visitor_team** | [**NFLNFLTeamInfo**](NFLTeamInfo.md) |  | [optional] 
**visitor_team_abbr** | **str** |  | [optional] 
**visitor_team_id** | **str** |  | [optional] 
**week** | **int** |  | [optional] 
**week_name_abbr** | **str** |  | [optional] 

## Example

```python
from nfl.models.nfl_game_schedule import NFLGameSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of NFLGameSchedule from a JSON string
nfl_game_schedule_instance = NFLGameSchedule.from_json(json)
# print the JSON string representation of the object
print(NFLGameSchedule.to_json())

# convert the object into a dict
nfl_game_schedule_dict = nfl_game_schedule_instance.to_dict()
# create an instance of NFLGameSchedule from a dict
nfl_game_schedule_from_dict = NFLGameSchedule.from_dict(nfl_game_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


