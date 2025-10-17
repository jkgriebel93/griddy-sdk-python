# TeamOffenseOverviewStatsResponse


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
**offense** | [**List[TeamOffenseOverviewStats]**](TeamOffenseOverviewStats.md) |  | [optional] 
**split** | **List[str]** | Applied offensive situation splits | [optional] 
**team_defense** | **str** | Team filter applied (if any) | [optional] 

## Example

```python
from src.griddy.nfl.models.team_offense_overview_stats_response import TeamOffenseOverviewStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TeamOffenseOverviewStatsResponse from a JSON string
team_offense_overview_stats_response_instance = TeamOffenseOverviewStatsResponse.from_json(json)
# print the JSON string representation of the object
print(TeamOffenseOverviewStatsResponse.to_json())

# convert the object into a dict
team_offense_overview_stats_response_dict = team_offense_overview_stats_response_instance.to_dict()
# create an instance of TeamOffenseOverviewStatsResponse from a dict
team_offense_overview_stats_response_from_dict = TeamOffenseOverviewStatsResponse.from_dict(team_offense_overview_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


