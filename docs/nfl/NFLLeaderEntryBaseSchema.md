# NFLLeaderEntryBaseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from nfl.models.nfl_leader_entry_base_schema import NFLLeaderEntryBaseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of NFLLeaderEntryBaseSchema from a JSON string
nfl_leader_entry_base_schema_instance = NFLLeaderEntryBaseSchema.from_json(json)
# print the JSON string representation of the object
print(NFLLeaderEntryBaseSchema.to_json())

# convert the object into a dict
nfl_leader_entry_base_schema_dict = nfl_leader_entry_base_schema_instance.to_dict()
# create an instance of NFLLeaderEntryBaseSchema from a dict
nfl_leader_entry_base_schema_from_dict = NFLLeaderEntryBaseSchema.from_dict(nfl_leader_entry_base_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


