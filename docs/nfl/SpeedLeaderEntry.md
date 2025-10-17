# SpeedLeaderEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_speed** | **float** |  | [optional] 
**gsis_play_id** | **int** |  | [optional] 
**esb_id** | **str** |  | [optional] 
**jersey_number** | **int** |  | [optional] 
**player_name** | **str** |  | [optional] 
**position** | [**NextGenStatsPositionEnum**](NextGenStatsPositionEnum.md) |  | [optional] 
**short_name** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**headshot** | **str** | URL to player headshot image (contains formatInstructions placeholder) | [optional] 

## Example

```python
from src.griddy.nfl.models.speed_leader_entry import SpeedLeaderEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SpeedLeaderEntry from a JSON string
speed_leader_entry_instance = SpeedLeaderEntry.from_json(json)
# print the JSON string representation of the object
print(SpeedLeaderEntry.to_json())

# convert the object into a dict
speed_leader_entry_dict = speed_leader_entry_instance.to_dict()
# create an instance of SpeedLeaderEntry from a dict
speed_leader_entry_from_dict = SpeedLeaderEntry.from_dict(speed_leader_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


