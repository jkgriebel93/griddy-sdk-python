# TeamDefenseRushStatsResponse


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
**defense** | [**List[TeamDefenseRushStats]**](TeamDefenseRushStats.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.team_defense_rush_stats_response import TeamDefenseRushStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TeamDefenseRushStatsResponse from a JSON string
team_defense_rush_stats_response_instance = TeamDefenseRushStatsResponse.from_json(json)
# print the JSON string representation of the object
print(TeamDefenseRushStatsResponse.to_json())

# convert the object into a dict
team_defense_rush_stats_response_dict = team_defense_rush_stats_response_instance.to_dict()
# create an instance of TeamDefenseRushStatsResponse from a dict
team_defense_rush_stats_response_from_dict = TeamDefenseRushStatsResponse.from_dict(team_defense_rush_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


