# PlayerStatsResponsePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.player_stats_response_pagination import PlayerStatsResponsePagination

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerStatsResponsePagination from a JSON string
player_stats_response_pagination_instance = PlayerStatsResponsePagination.from_json(json)
# print the JSON string representation of the object
print(PlayerStatsResponsePagination.to_json())

# convert the object into a dict
player_stats_response_pagination_dict = player_stats_response_pagination_instance.to_dict()
# create an instance of PlayerStatsResponsePagination from a dict
player_stats_response_pagination_from_dict = PlayerStatsResponsePagination.from_dict(player_stats_response_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


