# TeamDefensePassStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blitz_pct** | **float** | Blitz percentage (0-1) | [optional] 
**epa_pass** | **float** | EPA allowed on passing plays (negative is better for defense) | [optional] 
**epa_pass_pp** | **float** | EPA allowed per pass play | [optional] 
**go** | **float** | Get-off metric (coverage disruption) | [optional] 
**gp** | **int** | Games played | [optional] 
**var_pass** | **int** | Pass attempts faced | [optional] 
**pass_pct** | **float** | Percentage of plays that were passes (0-1) | [optional] 
**pass_td** | **int** | Passing touchdowns allowed | [optional] 
**pass_yds** | **int** | Passing yards allowed | [optional] 
**pass_ypg** | **float** | Pass yards allowed per game | [optional] 
**pass_ypp** | **float** | Passing yards allowed per pass attempt | [optional] 
**qbp** | **int** | Quarterback pressures generated | [optional] 
**qbp_pct** | **float** | Quarterback pressure rate (0-1) | [optional] 
**sack** | **int** | Sacks | [optional] 
**sack_pct** | **float** | Sack rate (0-1) | [optional] 
**sacked_yds** | **int** | Sack yards generated | [optional] 
**sacked_ypg** | **float** | Sack yards generated per game | [optional] 
**sep** | **float** | Average receiver separation allowed at target (yards) | [optional] 
**team_id** | **str** | Team identifier | [optional] 
**total** | **int** | Total defensive plays | [optional] 
**ttp** | **float** | Time to pressure (seconds) | [optional] 
**ttt** | **float** | Average time to throw allowed (seconds) | [optional] 
**yac** | **int** | Yards after catch allowed | [optional] 
**yacoe** | **int** | Yards after catch over expected allowed (negative is better) | [optional] 

## Example

```python
from src.griddy.nfl.models.team_defense_pass_stats import TeamDefensePassStats

# TODO update the JSON string below
json = "{}"
# create an instance of TeamDefensePassStats from a JSON string
team_defense_pass_stats_instance = TeamDefensePassStats.from_json(json)
# print the JSON string representation of the object
print(TeamDefensePassStats.to_json())

# convert the object into a dict
team_defense_pass_stats_dict = team_defense_pass_stats_instance.to_dict()
# create an instance of TeamDefensePassStats from a dict
team_defense_pass_stats_from_dict = TeamDefensePassStats.from_dict(team_defense_pass_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


