# BoxScoreResponsePlayerStatsAway


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defense** | [**List[PlayerGameStats]**](PlayerGameStats.md) |  | [optional] 
**offense** | [**List[PlayerGameStats]**](PlayerGameStats.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.box_score_response_player_stats_away import BoxScoreResponsePlayerStatsAway

# TODO update the JSON string below
json = "{}"
# create an instance of BoxScoreResponsePlayerStatsAway from a JSON string
box_score_response_player_stats_away_instance = BoxScoreResponsePlayerStatsAway.from_json(json)
# print the JSON string representation of the object
print(BoxScoreResponsePlayerStatsAway.to_json())

# convert the object into a dict
box_score_response_player_stats_away_dict = box_score_response_player_stats_away_instance.to_dict()
# create an instance of BoxScoreResponsePlayerStatsAway from a dict
box_score_response_player_stats_away_from_dict = BoxScoreResponsePlayerStatsAway.from_dict(box_score_response_player_stats_away_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


