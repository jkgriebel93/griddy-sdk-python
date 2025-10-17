# NFLWeeklyRushingStatsResponse


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
**rushers** | [**List[NFLNFLWeeklyPlayerRushingStats]**](NFLWeeklyPlayerRushingStats.md) |  | [optional] 
**qualified_rusher** | **bool** | Whether results are filtered to qualified rushers only | [optional] 
**team_offense** | **str** | Team filter applied (if any) | [optional] 
**week** | [**NFLNFLWeekSlugEnum**](NFLWeekSlugEnum.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_weekly_rushing_stats_response import NFLWeeklyRushingStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLWeeklyRushingStatsResponse from a JSON string
nfl_weekly_rushing_stats_response_instance = NFLWeeklyRushingStatsResponse.from_json(json)
# print the JSON string representation of the object
print(NFLWeeklyRushingStatsResponse.to_json())

# convert the object into a dict
nfl_weekly_rushing_stats_response_dict = nfl_weekly_rushing_stats_response_instance.to_dict()
# create an instance of NFLWeeklyRushingStatsResponse from a dict
nfl_weekly_rushing_stats_response_from_dict = NFLWeeklyRushingStatsResponse.from_dict(nfl_weekly_rushing_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


