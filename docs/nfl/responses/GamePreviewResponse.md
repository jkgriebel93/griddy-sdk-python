# GamePreviewResponse

Game preview content (may be empty if no preview available)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview** | **object** | Preview content and analysis | [optional] 

## Example

```python
from src.griddy.nfl.models.game_preview_response import GamePreviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GamePreviewResponse from a JSON string
game_preview_response_instance = GamePreviewResponse.from_json(json)
# print the JSON string representation of the object
print(GamePreviewResponse.to_json())

# convert the object into a dict
game_preview_response_dict = game_preview_response_instance.to_dict()
# create an instance of GamePreviewResponse from a dict
game_preview_response_from_dict = GamePreviewResponse.from_dict(game_preview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


