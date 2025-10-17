# NFLTeamDefenseStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defensive_touchdown** | **int** | Defensive touchdowns scored | [optional] 
**epa** | **float** | Total EPA allowed (negative is better for defense) | [optional] 
**epa_pp** | **float** | EPA allowed per play | [optional] 
**epa_pass** | **float** | EPA allowed on passing plays | [optional] 
**epa_pass_pp** | **float** | EPA allowed per pass play | [optional] 
**epa_rush** | **float** | EPA allowed on rushing plays | [optional] 
**epa_rush_pp** | **float** | EPA allowed per rush play | [optional] 
**forced_fumble** | **int** | Forced fumbles | [optional] 
**fumble_recovered** | **int** | Fumble recoveries | [optional] 
**gp** | **int** | Games played | [optional] 
**interception** | **int** | Interceptions | [optional] 
**var_pass** | **int** | Pass attempts faced | [optional] 
**pass_pct** | **float** | Percentage of plays that were passes (0-1) | [optional] 
**pass_td** | **int** | Passing touchdowns allowed | [optional] 
**pass_yds** | **int** | Passing yards allowed | [optional] 
**pass_ypg** | **float** | Pass yards allowed per game | [optional] 
**pass_ypp** | **float** | Passing yards allowed per pass attempt | [optional] 
**ppg** | **float** | Points allowed per game | [optional] 
**qbp** | **int** | Quarterback pressures generated | [optional] 
**qbp_pct** | **float** | Quarterback pressure rate (0-1) | [optional] 
**run** | **int** | Rush attempts faced | [optional] 
**rush_td** | **int** | Rushing touchdowns allowed | [optional] 
**rush_yds** | **int** | Rushing yards allowed | [optional] 
**rush_ypg** | **float** | Rush yards allowed per game | [optional] 
**rush_ypp** | **float** | Rushing yards allowed per rush attempt | [optional] 
**ryoe** | **float** | Rush Yards Over Expected allowed (negative is better for defense) | [optional] 
**sacked_yds** | **int** | Sack yards generated | [optional] 
**sacked_ypg** | **float** | Sack yards generated per game | [optional] 
**td** | **int** | Total touchdowns allowed | [optional] 
**team_id** | **str** | Team identifier | [optional] 
**total** | **int** | Total defensive plays | [optional] 
**total_takeaways** | **int** | Total takeaways (interceptions + fumble recoveries) | [optional] 
**ttt** | **float** | Average time to throw allowed (seconds) | [optional] 
**yds** | **int** | Total yards allowed | [optional] 
**ypg** | **float** | Yards allowed per game | [optional] 
**ypp** | **float** | Yards allowed per play | [optional] 

## Example

```python
from nfl.models.nfl_team_defense_stats import NFLTeamDefenseStats

# TODO update the JSON string below
json = "{}"
# create an instance of NFLTeamDefenseStats from a JSON string
nfl_team_defense_stats_instance = NFLTeamDefenseStats.from_json(json)
# print the JSON string representation of the object
print(NFLTeamDefenseStats.to_json())

# convert the object into a dict
nfl_team_defense_stats_dict = nfl_team_defense_stats_instance.to_dict()
# create an instance of NFLTeamDefenseStats from a dict
nfl_team_defense_stats_from_dict = NFLTeamDefenseStats.from_dict(nfl_team_defense_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


