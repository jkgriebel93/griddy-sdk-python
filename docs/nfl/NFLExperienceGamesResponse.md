# NFLExperienceGamesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**games** | [**List[NFLNFLGame]**](NFLGame.md) |  | [optional] 
**pagination** | [**NFLNFLPagination**](NFLPagination.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_experience_games_response import NFLExperienceGamesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLExperienceGamesResponse from a JSON string
nfl_experience_games_response_instance = NFLExperienceGamesResponse.from_json(json)
# print the JSON string representation of the object
print(NFLExperienceGamesResponse.to_json())

# convert the object into a dict
nfl_experience_games_response_dict = nfl_experience_games_response_instance.to_dict()
# create an instance of NFLExperienceGamesResponse from a dict
nfl_experience_games_response_from_dict = NFLExperienceGamesResponse.from_dict(nfl_experience_games_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


