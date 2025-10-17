# NFLTimeToSackLeaderEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tackle_info** | **object** |  | [optional] 
**gsis_play_id** | **int** |  | [optional] 
**esb_id** | **str** |  | [optional] 
**jersey_number** | **int** |  | [optional] 
**player_name** | **str** |  | [optional] 
**position** | [**NFLNFLNextGenStatsPositionEnum**](NFLNextGenStatsPositionEnum.md) |  | [optional] 
**short_name** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**headshot** | **str** | URL to player headshot image (contains formatInstructions placeholder) | [optional] 

## Example

```python
from nfl.models.nfl_time_to_sack_leader_entry import NFLTimeToSackLeaderEntry

# TODO update the JSON string below
json = "{}"
# create an instance of NFLTimeToSackLeaderEntry from a JSON string
nfl_time_to_sack_leader_entry_instance = NFLTimeToSackLeaderEntry.from_json(json)
# print the JSON string representation of the object
print(NFLTimeToSackLeaderEntry.to_json())

# convert the object into a dict
nfl_time_to_sack_leader_entry_dict = nfl_time_to_sack_leader_entry_instance.to_dict()
# create an instance of NFLTimeToSackLeaderEntry from a dict
nfl_time_to_sack_leader_entry_from_dict = NFLTimeToSackLeaderEntry.from_dict(nfl_time_to_sack_leader_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


