# NFLGamesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**games** | [**List[NFLNFLGame]**](NFLGame.md) |  | [optional] 
**season** | **str** | Season year | [optional] 
**season_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 
**week** | **str** | Week number | [optional] 

## Example

```python
from nfl.models.nfl_games_response import NFLGamesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLGamesResponse from a JSON string
nfl_games_response_instance = NFLGamesResponse.from_json(json)
# print the JSON string representation of the object
print(NFLGamesResponse.to_json())

# convert the object into a dict
nfl_games_response_dict = nfl_games_response_instance.to_dict()
# create an instance of NFLGamesResponse from a dict
nfl_games_response_from_dict = NFLGamesResponse.from_dict(nfl_games_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


