# NFLGameScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away_score** | **int** | Away team current score | [optional] 
**home_score** | **int** | Home team current score | [optional] 
**home_team_score** | [**NFLNFLTeamScore**](NFLTeamScore.md) |  | [optional] 
**phase** | [**NFLNFLGamePhaseEnum**](NFLGamePhaseEnum.md) |  | [optional] 
**time** | **str** | Game clock time or status | [optional] 
**visitor_team_score** | [**NFLNFLTeamScore**](NFLTeamScore.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_game_score import NFLGameScore

# TODO update the JSON string below
json = "{}"
# create an instance of NFLGameScore from a JSON string
nfl_game_score_instance = NFLGameScore.from_json(json)
# print the JSON string representation of the object
print(NFLGameScore.to_json())

# convert the object into a dict
nfl_game_score_dict = nfl_game_score_instance.to_dict()
# create an instance of NFLGameScore from a dict
nfl_game_score_from_dict = NFLGameScore.from_dict(nfl_game_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


