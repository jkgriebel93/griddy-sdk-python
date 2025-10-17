# NFLDraftInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pick** | **int** | Overall pick number | [optional] 
**round** | **int** | Draft round | [optional] 
**team** | **str** | Team that drafted player | [optional] 
**year** | **int** | Draft year | [optional] 

## Example

```python
from nfl.models.nfl_draft_info import NFLDraftInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NFLDraftInfo from a JSON string
nfl_draft_info_instance = NFLDraftInfo.from_json(json)
# print the JSON string representation of the object
print(NFLDraftInfo.to_json())

# convert the object into a dict
nfl_draft_info_dict = nfl_draft_info_instance.to_dict()
# create an instance of NFLDraftInfo from a dict
nfl_draft_info_from_dict = NFLDraftInfo.from_dict(nfl_draft_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


