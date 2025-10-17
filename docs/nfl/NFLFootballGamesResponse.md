# NFLFootballGamesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**games** | [**List[NFLNFLGame]**](NFLGame.md) |  | [optional] 
**pagination** | [**NFLNFLPagination**](NFLPagination.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_football_games_response import NFLFootballGamesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLFootballGamesResponse from a JSON string
nfl_football_games_response_instance = NFLFootballGamesResponse.from_json(json)
# print the JSON string representation of the object
print(NFLFootballGamesResponse.to_json())

# convert the object into a dict
nfl_football_games_response_dict = nfl_football_games_response_instance.to_dict()
# create an instance of NFLFootballGamesResponse from a dict
nfl_football_games_response_from_dict = NFLFootballGamesResponse.from_dict(nfl_football_games_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


