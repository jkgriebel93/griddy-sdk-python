# NFLCurrentGamesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**games** | [**List[NFLNFLCurrentGame]**](NFLCurrentGame.md) |  | [optional] 
**games_played_smart_ids** | **List[str]** | Smart IDs of games already played | [optional] 
**number_of_games** | **int** | Total number of games in the week | [optional] 
**number_of_games_played** | **int** | Number of games already played | [optional] 
**season** | **int** | Current season year | [optional] 
**season_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 
**week** | **int** | Current week number | [optional] 

## Example

```python
from nfl.models.nfl_current_games_response import NFLCurrentGamesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLCurrentGamesResponse from a JSON string
nfl_current_games_response_instance = NFLCurrentGamesResponse.from_json(json)
# print the JSON string representation of the object
print(NFLCurrentGamesResponse.to_json())

# convert the object into a dict
nfl_current_games_response_dict = nfl_current_games_response_instance.to_dict()
# create an instance of NFLCurrentGamesResponse from a dict
nfl_current_games_response_from_dict = NFLCurrentGamesResponse.from_dict(nfl_current_games_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


