# LiveScoresResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**games** | [**List[LiveGame]**](LiveGame.md) | Array of live game data (empty when no games are active) | [optional] 
**season** | **str** | Season year | [optional] 
**season_type** | [**SeasonTypeEnum**](SeasonTypeEnum.md) |  | [optional] 
**week** | **str** | Week number | [optional] 

## Example

```python
from src.griddy.nfl.models.live_scores_response import LiveScoresResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LiveScoresResponse from a JSON string
live_scores_response_instance = LiveScoresResponse.from_json(json)
# print the JSON string representation of the object
print(LiveScoresResponse.to_json())

# convert the object into a dict
live_scores_response_dict = live_scores_response_instance.to_dict()
# create an instance of LiveScoresResponse from a dict
live_scores_response_from_dict = LiveScoresResponse.from_dict(live_scores_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


