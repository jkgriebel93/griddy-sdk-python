# NFLDefensiveOverviewStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Maximum number of results returned | [optional] 
**offset** | **int** | Number of records skipped | [optional] 
**season** | **int** | Season year | [optional] 
**season_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 
**sort_key** | **str** | Field used for sorting | [optional] 
**sort_value** | [**NFLNFLSortOrderEnum**](NFLSortOrderEnum.md) |  | [optional] 
**total** | **int** | Total number of items matching the criteria | [optional] 
**defenders** | [**List[NFLNFLDefensivePlayerOverviewStats]**](NFLDefensivePlayerOverviewStats.md) |  | [optional] 
**qualified_defender** | **bool** | Whether results are filtered to qualified defenders only | [optional] 
**team_defense** | **str** | Team filter applied (if any) | [optional] 

## Example

```python
from nfl.models.nfl_defensive_overview_stats_response import NFLDefensiveOverviewStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLDefensiveOverviewStatsResponse from a JSON string
nfl_defensive_overview_stats_response_instance = NFLDefensiveOverviewStatsResponse.from_json(json)
# print the JSON string representation of the object
print(NFLDefensiveOverviewStatsResponse.to_json())

# convert the object into a dict
nfl_defensive_overview_stats_response_dict = nfl_defensive_overview_stats_response_instance.to_dict()
# create an instance of NFLDefensiveOverviewStatsResponse from a dict
nfl_defensive_overview_stats_response_from_dict = NFLDefensiveOverviewStatsResponse.from_dict(nfl_defensive_overview_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


