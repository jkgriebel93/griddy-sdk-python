# NFLTeamDefenseRushStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**epa_rush** | **float** | EPA allowed on rushing plays (negative is better for defense) | [optional] 
**epa_rush_pp** | **float** | EPA allowed per rush play | [optional] 
**gp** | **int** | Games played | [optional] 
**in_pct** | **float** | Percentage of rushes between tackles (inside) | [optional] 
**light_pct** | **float** | Percentage of rushes against light box (6 or fewer defenders) | [optional] 
**out_pct** | **float** | Percentage of rushes outside tackles | [optional] 
**run** | **int** | Rush attempts faced | [optional] 
**run_pct** | **float** | Percentage of plays that were rushes (0-1) | [optional] 
**rush10_p_yds** | **int** | Rush attempts of 10+ yards allowed | [optional] 
**rush_td** | **int** | Rushing touchdowns allowed | [optional] 
**rush_yds** | **int** | Rushing yards allowed | [optional] 
**rush_ypg** | **float** | Rush yards allowed per game | [optional] 
**rush_ypp** | **float** | Rushing yards allowed per rush attempt | [optional] 
**ryoe** | **float** | Rush Yards Over Expected allowed (negative is better) | [optional] 
**ryoe_att** | **float** | RYOE per rush attempt | [optional] 
**stacked_pct** | **float** | Percentage of rushes against stacked box (8+ defenders) | [optional] 
**stuff_pct** | **float** | Stuff rate - percentage of rushes stopped for 0 or negative yards | [optional] 
**team_id** | **str** | Team identifier | [optional] 
**total** | **int** | Total defensive plays | [optional] 
**yaco_att** | **float** | Yards after contact per attempt allowed | [optional] 
**ybco_att** | **float** | Yards before contact per attempt allowed | [optional] 

## Example

```python
from nfl.models.nfl_team_defense_rush_stats import NFLTeamDefenseRushStats

# TODO update the JSON string below
json = "{}"
# create an instance of NFLTeamDefenseRushStats from a JSON string
nfl_team_defense_rush_stats_instance = NFLTeamDefenseRushStats.from_json(json)
# print the JSON string representation of the object
print(NFLTeamDefenseRushStats.to_json())

# convert the object into a dict
nfl_team_defense_rush_stats_dict = nfl_team_defense_rush_stats_instance.to_dict()
# create an instance of NFLTeamDefenseRushStats from a dict
nfl_team_defense_rush_stats_from_dict = NFLTeamDefenseRushStats.from_dict(nfl_team_defense_rush_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


