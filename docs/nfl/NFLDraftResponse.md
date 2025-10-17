# NFLDraftResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rounds** | [**List[NFLNFLDraftResponseRoundsInner]**](NFLDraftResponseRoundsInner.md) |  | [optional] 
**year** | **int** |  | [optional] 

## Example

```python
from nfl.models.nfl_draft_response import NFLDraftResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLDraftResponse from a JSON string
nfl_draft_response_instance = NFLDraftResponse.from_json(json)
# print the JSON string representation of the object
print(NFLDraftResponse.to_json())

# convert the object into a dict
nfl_draft_response_dict = nfl_draft_response_instance.to_dict()
# create an instance of NFLDraftResponse from a dict
nfl_draft_response_from_dict = NFLDraftResponse.from_dict(nfl_draft_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


