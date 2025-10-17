# GameStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Summary]**](Summary.md) | Array of live game state summaries | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.game_stats_response import GameStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GameStatsResponse from a JSON string
game_stats_response_instance = GameStatsResponse.from_json(json)
# print the JSON string representation of the object
print(GameStatsResponse.to_json())

# convert the object into a dict
game_stats_response_dict = game_stats_response_instance.to_dict()
# create an instance of GameStatsResponse from a dict
game_stats_response_from_dict = GameStatsResponse.from_dict(game_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


