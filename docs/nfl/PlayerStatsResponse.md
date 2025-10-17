# PlayerStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PlayerStatsResponsePagination**](PlayerStatsResponsePagination.md) |  | [optional] 
**players** | [**List[PlayerStatsResponsePlayersInner]**](PlayerStatsResponsePlayersInner.md) |  | [optional] 
**season** | **int** |  | [optional] 
**season_type** | [**SeasonTypeEnum**](SeasonTypeEnum.md) |  | [optional] 
**stat_category** | **str** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.player_stats_response import PlayerStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerStatsResponse from a JSON string
player_stats_response_instance = PlayerStatsResponse.from_json(json)
# print the JSON string representation of the object
print(PlayerStatsResponse.to_json())

# convert the object into a dict
player_stats_response_dict = player_stats_response_instance.to_dict()
# create an instance of PlayerStatsResponse from a dict
player_stats_response_from_dict = PlayerStatsResponse.from_dict(player_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


