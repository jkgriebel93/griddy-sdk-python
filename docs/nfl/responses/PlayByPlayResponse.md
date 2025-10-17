# PlayByPlayResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_drive** | [**Drive**](Drive.md) |  | [optional] 
**drives** | [**List[Drive]**](Drive.md) |  | [optional] 
**game** | [**Game**](Game.md) |  | [optional] 
**last_play** | [**Play**](Play.md) |  | [optional] 
**scoring_summary** | [**List[ScoringPlay]**](ScoringPlay.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.play_by_play_response import PlayByPlayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlayByPlayResponse from a JSON string
play_by_play_response_instance = PlayByPlayResponse.from_json(json)
# print the JSON string representation of the object
print(PlayByPlayResponse.to_json())

# convert the object into a dict
play_by_play_response_dict = play_by_play_response_instance.to_dict()
# create an instance of PlayByPlayResponse from a dict
play_by_play_response_from_dict = PlayByPlayResponse.from_dict(play_by_play_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


