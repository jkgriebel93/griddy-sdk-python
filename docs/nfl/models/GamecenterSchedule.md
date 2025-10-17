# GamecenterSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_date** | **str** |  | [optional] 
**game_id** | **str** |  | [optional] 
**game_key** | **int** |  | [optional] 
**game_time_eastern** | **str** |  | [optional] 
**home_team_abbr** | **str** |  | [optional] 
**home_team_id** | **str** |  | [optional] 
**season** | **int** |  | [optional] 
**season_type** | **str** |  | [optional] 
**visitor_team_abbr** | **str** |  | [optional] 
**visitor_team_id** | **str** |  | [optional] 
**week** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.gamecenter_schedule import GamecenterSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of GamecenterSchedule from a JSON string
gamecenter_schedule_instance = GamecenterSchedule.from_json(json)
# print the JSON string representation of the object
print(GamecenterSchedule.to_json())

# convert the object into a dict
gamecenter_schedule_dict = gamecenter_schedule_instance.to_dict()
# create an instance of GamecenterSchedule from a dict
gamecenter_schedule_from_dict = GamecenterSchedule.from_dict(gamecenter_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


