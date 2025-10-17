# NFLBoxScoreResponsePlayerStatsAway


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defense** | [**List[NFLNFLPlayerGameStats]**](NFLPlayerGameStats.md) |  | [optional] 
**offense** | [**List[NFLNFLPlayerGameStats]**](NFLPlayerGameStats.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_box_score_response_player_stats_away import NFLBoxScoreResponsePlayerStatsAway

# TODO update the JSON string below
json = "{}"
# create an instance of NFLBoxScoreResponsePlayerStatsAway from a JSON string
nfl_box_score_response_player_stats_away_instance = NFLBoxScoreResponsePlayerStatsAway.from_json(json)
# print the JSON string representation of the object
print(NFLBoxScoreResponsePlayerStatsAway.to_json())

# convert the object into a dict
nfl_box_score_response_player_stats_away_dict = nfl_box_score_response_player_stats_away_instance.to_dict()
# create an instance of NFLBoxScoreResponsePlayerStatsAway from a dict
nfl_box_score_response_player_stats_away_from_dict = NFLBoxScoreResponsePlayerStatsAway.from_dict(nfl_box_score_response_player_stats_away_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


