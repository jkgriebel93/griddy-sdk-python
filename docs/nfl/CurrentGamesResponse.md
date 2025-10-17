# CurrentGamesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**games** | [**List[CurrentGame]**](CurrentGame.md) |  | [optional] 
**games_played_smart_ids** | **List[str]** | Smart IDs of games already played | [optional] 
**number_of_games** | **int** | Total number of games in the week | [optional] 
**number_of_games_played** | **int** | Number of games already played | [optional] 
**season** | **int** | Current season year | [optional] 
**season_type** | [**SeasonTypeEnum**](SeasonTypeEnum.md) |  | [optional] 
**week** | **int** | Current week number | [optional] 

## Example

```python
from src.griddy.nfl.models.current_games_response import CurrentGamesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentGamesResponse from a JSON string
current_games_response_instance = CurrentGamesResponse.from_json(json)
# print the JSON string representation of the object
print(CurrentGamesResponse.to_json())

# convert the object into a dict
current_games_response_dict = current_games_response_instance.to_dict()
# create an instance of CurrentGamesResponse from a dict
current_games_response_from_dict = CurrentGamesResponse.from_dict(current_games_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


