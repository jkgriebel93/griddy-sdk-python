# NFLGamecenterSchedule


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
from nfl.models.nfl_gamecenter_schedule import NFLGamecenterSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of NFLGamecenterSchedule from a JSON string
nfl_gamecenter_schedule_instance = NFLGamecenterSchedule.from_json(json)
# print the JSON string representation of the object
print(NFLGamecenterSchedule.to_json())

# convert the object into a dict
nfl_gamecenter_schedule_dict = nfl_gamecenter_schedule_instance.to_dict()
# create an instance of NFLGamecenterSchedule from a dict
nfl_gamecenter_schedule_from_dict = NFLGamecenterSchedule.from_dict(nfl_gamecenter_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


