# DraftInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pick** | **int** | Overall pick number | [optional] 
**round** | **int** | Draft round | [optional] 
**team** | **str** | Team that drafted player | [optional] 
**year** | **int** | Draft year | [optional] 

## Example

```python
from src.griddy.nfl.models.draft_info import DraftInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DraftInfo from a JSON string
draft_info_instance = DraftInfo.from_json(json)
# print the JSON string representation of the object
print(DraftInfo.to_json())

# convert the object into a dict
draft_info_dict = draft_info_instance.to_dict()
# create an instance of DraftInfo from a dict
draft_info_from_dict = DraftInfo.from_dict(draft_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


