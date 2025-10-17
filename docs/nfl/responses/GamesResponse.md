# GamesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**games** | [**List[Game]**](Game.md) |  | [optional] 
**season** | **str** | Season year | [optional] 
**season_type** | [**SeasonTypeEnum**](SeasonTypeEnum.md) |  | [optional] 
**week** | **str** | Week number | [optional] 

## Example

```python
from src.griddy.nfl.models.games_response import GamesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GamesResponse from a JSON string
games_response_instance = GamesResponse.from_json(json)
# print the JSON string representation of the object
print(GamesResponse.to_json())

# convert the object into a dict
games_response_dict = games_response_instance.to_dict()
# create an instance of GamesResponse from a dict
games_response_from_dict = GamesResponse.from_dict(games_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


