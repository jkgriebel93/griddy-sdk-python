# DraftPick


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**college** | **str** |  | [optional] 
**is_compensatory** | **bool** |  | [optional] 
**original_team** | [**Team**](Team.md) |  | [optional] 
**overall_pick** | **int** |  | [optional] 
**pick** | **int** |  | [optional] 
**player** | [**Player**](Player.md) |  | [optional] 
**position** | **str** |  | [optional] 
**round** | **int** |  | [optional] 
**team** | [**Team**](Team.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.draft_pick import DraftPick

# TODO update the JSON string below
json = "{}"
# create an instance of DraftPick from a JSON string
draft_pick_instance = DraftPick.from_json(json)
# print the JSON string representation of the object
print(DraftPick.to_json())

# convert the object into a dict
draft_pick_dict = draft_pick_instance.to_dict()
# create an instance of DraftPick from a dict
draft_pick_from_dict = DraftPick.from_dict(draft_pick_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


