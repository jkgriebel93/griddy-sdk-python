# BoxScoreResponsePlayerStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away** | [**BoxScoreResponsePlayerStatsAway**](BoxScoreResponsePlayerStatsAway.md) |  | [optional] 
**home** | [**BoxScoreResponsePlayerStatsAway**](BoxScoreResponsePlayerStatsAway.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.box_score_response_player_stats import BoxScoreResponsePlayerStats

# TODO update the JSON string below
json = "{}"
# create an instance of BoxScoreResponsePlayerStats from a JSON string
box_score_response_player_stats_instance = BoxScoreResponsePlayerStats.from_json(json)
# print the JSON string representation of the object
print(BoxScoreResponsePlayerStats.to_json())

# convert the object into a dict
box_score_response_player_stats_dict = box_score_response_player_stats_instance.to_dict()
# create an instance of BoxScoreResponsePlayerStats from a dict
box_score_response_player_stats_from_dict = BoxScoreResponsePlayerStats.from_dict(box_score_response_player_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


