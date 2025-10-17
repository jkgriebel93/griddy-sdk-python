# NFLGameSituation

Game situation context for win probability calculations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**down** | **int** | Current down | [optional] 
**score** | [**NFLNFLGameScore**](NFLGameScore.md) |  | [optional] 
**time_remaining** | **str** | Time remaining in the current quarter | [optional] 
**yard_line** | **str** | Field position where play occurred | [optional] 
**yards_to_go** | **int** | Yards needed for first down | [optional] 

## Example

```python
from nfl.models.nfl_game_situation import NFLGameSituation

# TODO update the JSON string below
json = "{}"
# create an instance of NFLGameSituation from a JSON string
nfl_game_situation_instance = NFLGameSituation.from_json(json)
# print the JSON string representation of the object
print(NFLGameSituation.to_json())

# convert the object into a dict
nfl_game_situation_dict = nfl_game_situation_instance.to_dict()
# create an instance of NFLGameSituation from a dict
nfl_game_situation_from_dict = NFLGameSituation.from_dict(nfl_game_situation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


