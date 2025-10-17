# NFLPlayerStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**NFLNFLPlayerStatsResponsePagination**](NFLPlayerStatsResponsePagination.md) |  | [optional] 
**players** | [**List[NFLNFLPlayerStatsResponsePlayersInner]**](NFLPlayerStatsResponsePlayersInner.md) |  | [optional] 
**season** | **int** |  | [optional] 
**season_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 
**stat_category** | **str** |  | [optional] 

## Example

```python
from nfl.models.nfl_player_stats_response import NFLPlayerStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPlayerStatsResponse from a JSON string
nfl_player_stats_response_instance = NFLPlayerStatsResponse.from_json(json)
# print the JSON string representation of the object
print(NFLPlayerStatsResponse.to_json())

# convert the object into a dict
nfl_player_stats_response_dict = nfl_player_stats_response_instance.to_dict()
# create an instance of NFLPlayerStatsResponse from a dict
nfl_player_stats_response_from_dict = NFLPlayerStatsResponse.from_dict(nfl_player_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


