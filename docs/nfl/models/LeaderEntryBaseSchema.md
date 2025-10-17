# LeaderEntryBaseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from src.griddy.nfl.models.leader_entry_base_schema import LeaderEntryBaseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LeaderEntryBaseSchema from a JSON string
leader_entry_base_schema_instance = LeaderEntryBaseSchema.from_json(json)
# print the JSON string representation of the object
print(LeaderEntryBaseSchema.to_json())

# convert the object into a dict
leader_entry_base_schema_dict = leader_entry_base_schema_instance.to_dict()
# create an instance of LeaderEntryBaseSchema from a dict
leader_entry_base_schema_from_dict = LeaderEntryBaseSchema.from_dict(leader_entry_base_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


