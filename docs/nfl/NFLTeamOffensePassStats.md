# NFLTeamOffensePassStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**att** | **int** | Pass attempts (not including sacks) | [optional] 
**blitz_pct** | **float** | Blitz percentage faced (0-1) | [optional] 
**epa_pass** | **float** | EPA on passing plays (positive is better for offense) | [optional] 
**epa_pass_pp** | **float** | EPA per pass play | [optional] 
**gp** | **int** | Games played | [optional] 
**pa_pct** | **float** | Play action percentage (0-1) | [optional] 
**var_pass** | **int** | Pass attempts (including sacks) | [optional] 
**pass_pct** | **float** | Percentage of plays that were passes (0-1) | [optional] 
**pass_td** | **int** | Passing touchdowns | [optional] 
**pass_yds** | **int** | Passing yards | [optional] 
**pass_ypg** | **float** | Pass yards per game | [optional] 
**pass_ypp** | **float** | Passing yards per pass attempt | [optional] 
**qbp** | **int** | Times quarterback was pressured | [optional] 
**qbp_pct** | **float** | Quarterback pressure rate (0-1) | [optional] 
**sack** | **int** | Sacks taken | [optional] 
**sack_pct** | **float** | Sack rate (0-1) | [optional] 
**sacked_yds** | **int** | Sack yards lost | [optional] 
**sacked_ypg** | **float** | Sack yards lost per game | [optional] 
**sep** | **float** | Average receiver separation at target (yards) | [optional] 
**team_id** | **str** | Team identifier | [optional] 
**total** | **int** | Total offensive plays | [optional] 
**ttp** | **float** | Time to pressure (seconds) | [optional] 
**ttt** | **float** | Average time to throw (seconds) | [optional] 
**yac** | **int** | Yards after catch | [optional] 
**yacoe** | **int** | Yards after catch over expected (positive is better) | [optional] 

## Example

```python
from nfl.models.nfl_team_offense_pass_stats import NFLTeamOffensePassStats

# TODO update the JSON string below
json = "{}"
# create an instance of NFLTeamOffensePassStats from a JSON string
nfl_team_offense_pass_stats_instance = NFLTeamOffensePassStats.from_json(json)
# print the JSON string representation of the object
print(NFLTeamOffensePassStats.to_json())

# convert the object into a dict
nfl_team_offense_pass_stats_dict = nfl_team_offense_pass_stats_instance.to_dict()
# create an instance of NFLTeamOffensePassStats from a dict
nfl_team_offense_pass_stats_from_dict = NFLTeamOffensePassStats.from_dict(nfl_team_offense_pass_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


