# ExperienceGamesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**games** | [**List[Game]**](Game.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.experience_games_response import ExperienceGamesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExperienceGamesResponse from a JSON string
experience_games_response_instance = ExperienceGamesResponse.from_json(json)
# print the JSON string representation of the object
print(ExperienceGamesResponse.to_json())

# convert the object into a dict
experience_games_response_dict = experience_games_response_instance.to_dict()
# create an instance of ExperienceGamesResponse from a dict
experience_games_response_from_dict = ExperienceGamesResponse.from_dict(experience_games_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


