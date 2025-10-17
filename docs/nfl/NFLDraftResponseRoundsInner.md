# NFLDraftResponseRoundsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**picks** | [**List[NFLNFLDraftPick]**](NFLDraftPick.md) |  | [optional] 
**round** | **int** |  | [optional] 

## Example

```python
from nfl.models.nfl_draft_response_rounds_inner import NFLDraftResponseRoundsInner

# TODO update the JSON string below
json = "{}"
# create an instance of NFLDraftResponseRoundsInner from a JSON string
nfl_draft_response_rounds_inner_instance = NFLDraftResponseRoundsInner.from_json(json)
# print the JSON string representation of the object
print(NFLDraftResponseRoundsInner.to_json())

# convert the object into a dict
nfl_draft_response_rounds_inner_dict = nfl_draft_response_rounds_inner_instance.to_dict()
# create an instance of NFLDraftResponseRoundsInner from a dict
nfl_draft_response_rounds_inner_from_dict = NFLDraftResponseRoundsInner.from_dict(nfl_draft_response_rounds_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


