# NFLLiveScoresResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**games** | [**List[NFLNFLLiveGame]**](NFLLiveGame.md) | Array of live game data (empty when no games are active) | [optional] 
**season** | **str** | Season year | [optional] 
**season_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 
**week** | **str** | Week number | [optional] 

## Example

```python
from nfl.models.nfl_live_scores_response import NFLLiveScoresResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLLiveScoresResponse from a JSON string
nfl_live_scores_response_instance = NFLLiveScoresResponse.from_json(json)
# print the JSON string representation of the object
print(NFLLiveScoresResponse.to_json())

# convert the object into a dict
nfl_live_scores_response_dict = nfl_live_scores_response_instance.to_dict()
# create an instance of NFLLiveScoresResponse from a dict
nfl_live_scores_response_from_dict = NFLLiveScoresResponse.from_dict(nfl_live_scores_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


