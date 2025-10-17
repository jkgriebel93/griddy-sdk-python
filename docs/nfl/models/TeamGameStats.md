# TeamGameStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_downs** | **int** |  | [optional] 
**fourth_down_conversions** | **str** |  | [optional] 
**passing_yards** | **int** |  | [optional] 
**penalties** | **int** |  | [optional] 
**penalty_yards** | **int** |  | [optional] 
**rushing_yards** | **int** |  | [optional] 
**score** | **int** |  | [optional] 
**team** | [**Team**](Team.md) |  | [optional] 
**third_down_conversions** | **str** |  | [optional] 
**time_of_possession** | **str** |  | [optional] 
**total_yards** | **int** |  | [optional] 
**turnovers** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.team_game_stats import TeamGameStats

# TODO update the JSON string below
json = "{}"
# create an instance of TeamGameStats from a JSON string
team_game_stats_instance = TeamGameStats.from_json(json)
# print the JSON string representation of the object
print(TeamGameStats.to_json())

# convert the object into a dict
team_game_stats_dict = team_game_stats_instance.to_dict()
# create an instance of TeamGameStats from a dict
team_game_stats_from_dict = TeamGameStats.from_dict(team_game_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


