# FootballGamesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**games** | [**List[Game]**](Game.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.football_games_response import FootballGamesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FootballGamesResponse from a JSON string
football_games_response_instance = FootballGamesResponse.from_json(json)
# print the JSON string representation of the object
print(FootballGamesResponse.to_json())

# convert the object into a dict
football_games_response_dict = football_games_response_instance.to_dict()
# create an instance of FootballGamesResponse from a dict
football_games_response_from_dict = FootballGamesResponse.from_dict(football_games_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


