# NFLBoxScoreResponsePlayerStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away** | [**NFLNFLBoxScoreResponsePlayerStatsAway**](NFLBoxScoreResponsePlayerStatsAway.md) |  | [optional] 
**home** | [**NFLNFLBoxScoreResponsePlayerStatsAway**](NFLBoxScoreResponsePlayerStatsAway.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_box_score_response_player_stats import NFLBoxScoreResponsePlayerStats

# TODO update the JSON string below
json = "{}"
# create an instance of NFLBoxScoreResponsePlayerStats from a JSON string
nfl_box_score_response_player_stats_instance = NFLBoxScoreResponsePlayerStats.from_json(json)
# print the JSON string representation of the object
print(NFLBoxScoreResponsePlayerStats.to_json())

# convert the object into a dict
nfl_box_score_response_player_stats_dict = nfl_box_score_response_player_stats_instance.to_dict()
# create an instance of NFLBoxScoreResponsePlayerStats from a dict
nfl_box_score_response_player_stats_from_dict = NFLBoxScoreResponsePlayerStats.from_dict(nfl_box_score_response_player_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


