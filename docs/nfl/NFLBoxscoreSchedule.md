# NFLBoxscoreSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_date** | **str** |  | [optional] 
**game_id** | **str** |  | [optional] 
**game_key** | **int** |  | [optional] 
**game_time** | **datetime** |  | [optional] 
**game_time_eastern** | **str** |  | [optional] 
**game_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 
**home_display_name** | **str** |  | [optional] 
**home_nickname** | **str** |  | [optional] 
**home_team** | [**NFLNFLBoxscoreTeam**](NFLBoxscoreTeam.md) |  | [optional] 
**home_team_abbr** | **str** |  | [optional] 
**home_team_id** | **str** |  | [optional] 
**iso_time** | **int** | Unix timestamp in milliseconds | [optional] 
**network_channel** | **str** |  | [optional] 
**ngs_game** | **bool** | Whether Next Gen Stats are available | [optional] 
**score** | [**NFLNFLBoxscoreScore**](NFLBoxscoreScore.md) |  | [optional] 
**season** | **int** |  | [optional] 
**season_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 
**site** | [**NFLNFLSite**](NFLSite.md) |  | [optional] 
**smart_id** | **str** |  | [optional] 
**visitor_display_name** | **str** |  | [optional] 
**visitor_nickname** | **str** |  | [optional] 
**visitor_team** | [**NFLNFLBoxscoreTeam**](NFLBoxscoreTeam.md) |  | [optional] 
**visitor_team_abbr** | **str** |  | [optional] 
**visitor_team_id** | **str** |  | [optional] 
**week** | **int** |  | [optional] 
**week_name_abbr** | **str** |  | [optional] 

## Example

```python
from nfl.models.nfl_boxscore_schedule import NFLBoxscoreSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of NFLBoxscoreSchedule from a JSON string
nfl_boxscore_schedule_instance = NFLBoxscoreSchedule.from_json(json)
# print the JSON string representation of the object
print(NFLBoxscoreSchedule.to_json())

# convert the object into a dict
nfl_boxscore_schedule_dict = nfl_boxscore_schedule_instance.to_dict()
# create an instance of NFLBoxscoreSchedule from a dict
nfl_boxscore_schedule_from_dict = NFLBoxscoreSchedule.from_dict(nfl_boxscore_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


