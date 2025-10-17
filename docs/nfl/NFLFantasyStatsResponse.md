# NFLFantasyStatsResponse


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
**players** | [**List[NFLNFLFantasyPlayerStats]**](NFLFantasyPlayerStats.md) |  | [optional] 
**last_n_weeks** | **int** | Number of recent weeks analyzed (if applied) | [optional] 
**min_offensive_snaps** | **int** | Minimum offensive snaps filter applied | [optional] 
**position_group** | [**List[NFLNFLFantasyPositionGroupEnum]**](NFLFantasyPositionGroupEnum.md) |  | [optional] 
**team_offense** | **str** | Offensive team filter applied (if any) | [optional] 
**week** | [**List[NFLNFLWeekSlugEnum]**](NFLWeekSlugEnum.md) | Specific weeks included in analysis | [optional] 

## Example

```python
from nfl.models.nfl_fantasy_stats_response import NFLFantasyStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLFantasyStatsResponse from a JSON string
nfl_fantasy_stats_response_instance = NFLFantasyStatsResponse.from_json(json)
# print the JSON string representation of the object
print(NFLFantasyStatsResponse.to_json())

# convert the object into a dict
nfl_fantasy_stats_response_dict = nfl_fantasy_stats_response_instance.to_dict()
# create an instance of NFLFantasyStatsResponse from a dict
nfl_fantasy_stats_response_from_dict = NFLFantasyStatsResponse.from_dict(nfl_fantasy_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


