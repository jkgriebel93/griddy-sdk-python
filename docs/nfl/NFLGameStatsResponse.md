# NFLGameStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NFLNFLSummary]**](NFLSummary.md) | Array of live game state summaries | [optional] 
**pagination** | [**NFLNFLPagination**](NFLPagination.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_game_stats_response import NFLGameStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLGameStatsResponse from a JSON string
nfl_game_stats_response_instance = NFLGameStatsResponse.from_json(json)
# print the JSON string representation of the object
print(NFLGameStatsResponse.to_json())

# convert the object into a dict
nfl_game_stats_response_dict = nfl_game_stats_response_instance.to_dict()
# create an instance of NFLGameStatsResponse from a dict
nfl_game_stats_response_from_dict = NFLGameStatsResponse.from_dict(nfl_game_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


