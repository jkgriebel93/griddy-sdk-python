# NFLTeamDefensePassStatsResponse


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
**defense** | [**List[NFLNFLTeamDefensePassStats]**](NFLTeamDefensePassStats.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_team_defense_pass_stats_response import NFLTeamDefensePassStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLTeamDefensePassStatsResponse from a JSON string
nfl_team_defense_pass_stats_response_instance = NFLTeamDefensePassStatsResponse.from_json(json)
# print the JSON string representation of the object
print(NFLTeamDefensePassStatsResponse.to_json())

# convert the object into a dict
nfl_team_defense_pass_stats_response_dict = nfl_team_defense_pass_stats_response_instance.to_dict()
# create an instance of NFLTeamDefensePassStatsResponse from a dict
nfl_team_defense_pass_stats_response_from_dict = NFLTeamDefensePassStatsResponse.from_dict(nfl_team_defense_pass_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


