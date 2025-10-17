# NFLScoringPlay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away_score** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**game_clock** | **str** |  | [optional] 
**home_score** | **int** |  | [optional] 
**quarter** | **int** |  | [optional] 
**score_type** | [**NFLNFLScoreTypeEnum**](NFLScoreTypeEnum.md) |  | [optional] 
**team** | [**NFLNFLTeam**](NFLTeam.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_scoring_play import NFLScoringPlay

# TODO update the JSON string below
json = "{}"
# create an instance of NFLScoringPlay from a JSON string
nfl_scoring_play_instance = NFLScoringPlay.from_json(json)
# print the JSON string representation of the object
print(NFLScoringPlay.to_json())

# convert the object into a dict
nfl_scoring_play_dict = nfl_scoring_play_instance.to_dict()
# create an instance of NFLScoringPlay from a dict
nfl_scoring_play_from_dict = NFLScoringPlay.from_dict(nfl_scoring_play_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


