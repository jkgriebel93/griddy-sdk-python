# NFLPlayerStatsResponsePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from nfl.models.nfl_player_stats_response_pagination import NFLPlayerStatsResponsePagination

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPlayerStatsResponsePagination from a JSON string
nfl_player_stats_response_pagination_instance = NFLPlayerStatsResponsePagination.from_json(json)
# print the JSON string representation of the object
print(NFLPlayerStatsResponsePagination.to_json())

# convert the object into a dict
nfl_player_stats_response_pagination_dict = nfl_player_stats_response_pagination_instance.to_dict()
# create an instance of NFLPlayerStatsResponsePagination from a dict
nfl_player_stats_response_pagination_from_dict = NFLPlayerStatsResponsePagination.from_dict(nfl_player_stats_response_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


