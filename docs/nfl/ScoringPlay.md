# ScoringPlay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away_score** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**game_clock** | **str** |  | [optional] 
**home_score** | **int** |  | [optional] 
**quarter** | **int** |  | [optional] 
**score_type** | [**ScoreTypeEnum**](ScoreTypeEnum.md) |  | [optional] 
**team** | [**Team**](Team.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.scoring_play import ScoringPlay

# TODO update the JSON string below
json = "{}"
# create an instance of ScoringPlay from a JSON string
scoring_play_instance = ScoringPlay.from_json(json)
# print the JSON string representation of the object
print(ScoringPlay.to_json())

# convert the object into a dict
scoring_play_dict = scoring_play_instance.to_dict()
# create an instance of ScoringPlay from a dict
scoring_play_from_dict = ScoringPlay.from_dict(scoring_play_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


