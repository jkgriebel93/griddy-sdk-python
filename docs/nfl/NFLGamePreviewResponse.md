# NFLGamePreviewResponse

Game preview content (may be empty if no preview available)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview** | **object** | Preview content and analysis | [optional] 

## Example

```python
from nfl.models.nfl_game_preview_response import NFLGamePreviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLGamePreviewResponse from a JSON string
nfl_game_preview_response_instance = NFLGamePreviewResponse.from_json(json)
# print the JSON string representation of the object
print(NFLGamePreviewResponse.to_json())

# convert the object into a dict
nfl_game_preview_response_dict = nfl_game_preview_response_instance.to_dict()
# create an instance of NFLGamePreviewResponse from a dict
nfl_game_preview_response_from_dict = NFLGamePreviewResponse.from_dict(nfl_game_preview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


