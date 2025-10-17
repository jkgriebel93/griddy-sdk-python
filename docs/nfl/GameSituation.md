# GameSituation

Game situation context for win probability calculations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**down** | **int** | Current down | [optional] 
**score** | [**GameScore**](GameScore.md) |  | [optional] 
**time_remaining** | **str** | Time remaining in the current quarter | [optional] 
**yard_line** | **str** | Field position where play occurred | [optional] 
**yards_to_go** | **int** | Yards needed for first down | [optional] 

## Example

```python
from src.griddy.nfl.models.game_situation import GameSituation

# TODO update the JSON string below
json = "{}"
# create an instance of GameSituation from a JSON string
game_situation_instance = GameSituation.from_json(json)
# print the JSON string representation of the object
print(GameSituation.to_json())

# convert the object into a dict
game_situation_dict = game_situation_instance.to_dict()
# create an instance of GameSituation from a dict
game_situation_from_dict = GameSituation.from_dict(game_situation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


