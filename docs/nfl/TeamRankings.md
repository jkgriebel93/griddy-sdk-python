# TeamRankings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | [optional] 
**season_type** | [**SeasonTypeEnum**](SeasonTypeEnum.md) |  | [optional] 
**statistics** | [**List[StatisticRanking]**](StatisticRanking.md) |  | [optional] 
**team_id** | **str** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.team_rankings import TeamRankings

# TODO update the JSON string below
json = "{}"
# create an instance of TeamRankings from a JSON string
team_rankings_instance = TeamRankings.from_json(json)
# print the JSON string representation of the object
print(TeamRankings.to_json())

# convert the object into a dict
team_rankings_dict = team_rankings_instance.to_dict()
# create an instance of TeamRankings from a dict
team_rankings_from_dict = TeamRankings.from_dict(team_rankings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


