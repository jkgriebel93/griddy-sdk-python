# FantasyStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Maximum number of results returned | [optional] 
**offset** | **int** | Number of records skipped | [optional] 
**season** | **int** | Season year | [optional] 
**season_type** | [**SeasonTypeEnum**](SeasonTypeEnum.md) |  | [optional] 
**sort_key** | **str** | Field used for sorting | [optional] 
**sort_value** | [**SortOrderEnum**](SortOrderEnum.md) |  | [optional] 
**total** | **int** | Total number of items matching the criteria | [optional] 
**players** | [**List[FantasyPlayerStats]**](FantasyPlayerStats.md) |  | [optional] 
**last_n_weeks** | **int** | Number of recent weeks analyzed (if applied) | [optional] 
**min_offensive_snaps** | **int** | Minimum offensive snaps filter applied | [optional] 
**position_group** | [**List[FantasyPositionGroupEnum]**](FantasyPositionGroupEnum.md) |  | [optional] 
**team_offense** | **str** | Offensive team filter applied (if any) | [optional] 
**week** | [**List[WeekSlugEnum]**](WeekSlugEnum.md) | Specific weeks included in analysis | [optional] 

## Example

```python
from src.griddy.nfl.models.fantasy_stats_response import FantasyStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FantasyStatsResponse from a JSON string
fantasy_stats_response_instance = FantasyStatsResponse.from_json(json)
# print the JSON string representation of the object
print(FantasyStatsResponse.to_json())

# convert the object into a dict
fantasy_stats_response_dict = fantasy_stats_response_instance.to_dict()
# create an instance of FantasyStatsResponse from a dict
fantasy_stats_response_from_dict = FantasyStatsResponse.from_dict(fantasy_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


