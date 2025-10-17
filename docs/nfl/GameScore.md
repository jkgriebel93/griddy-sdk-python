# GameScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away_score** | **int** | Away team current score | [optional] 
**home_score** | **int** | Home team current score | [optional] 
**home_team_score** | [**TeamScore**](TeamScore.md) |  | [optional] 
**phase** | [**GamePhaseEnum**](GamePhaseEnum.md) |  | [optional] 
**time** | **str** | Game clock time or status | [optional] 
**visitor_team_score** | [**TeamScore**](TeamScore.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.game_score import GameScore

# TODO update the JSON string below
json = "{}"
# create an instance of GameScore from a JSON string
game_score_instance = GameScore.from_json(json)
# print the JSON string representation of the object
print(GameScore.to_json())

# convert the object into a dict
game_score_dict = game_score_instance.to_dict()
# create an instance of GameScore from a dict
game_score_from_dict = GameScore.from_dict(game_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


