# DraftResponseRoundsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**picks** | [**List[DraftPick]**](DraftPick.md) |  | [optional] 
**round** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.draft_response_rounds_inner import DraftResponseRoundsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DraftResponseRoundsInner from a JSON string
draft_response_rounds_inner_instance = DraftResponseRoundsInner.from_json(json)
# print the JSON string representation of the object
print(DraftResponseRoundsInner.to_json())

# convert the object into a dict
draft_response_rounds_inner_dict = draft_response_rounds_inner_instance.to_dict()
# create an instance of DraftResponseRoundsInner from a dict
draft_response_rounds_inner_from_dict = DraftResponseRoundsInner.from_dict(draft_response_rounds_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


