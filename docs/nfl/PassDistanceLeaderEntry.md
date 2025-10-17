# PassDistanceLeaderEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pass_info** | **object** |  | [optional] 
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
from src.griddy.nfl.models.pass_distance_leader_entry import PassDistanceLeaderEntry

# TODO update the JSON string below
json = "{}"
# create an instance of PassDistanceLeaderEntry from a JSON string
pass_distance_leader_entry_instance = PassDistanceLeaderEntry.from_json(json)
# print the JSON string representation of the object
print(PassDistanceLeaderEntry.to_json())

# convert the object into a dict
pass_distance_leader_entry_dict = pass_distance_leader_entry_instance.to_dict()
# create an instance of PassDistanceLeaderEntry from a dict
pass_distance_leader_entry_from_dict = PassDistanceLeaderEntry.from_dict(pass_distance_leader_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


