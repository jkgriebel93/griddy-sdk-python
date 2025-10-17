# NFLTeamOffenseOverviewStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**epa** | **float** | Total EPA (positive is better for offense) | [optional] 
**epa_pp** | **float** | EPA per play | [optional] 
**epa_pass** | **float** | EPA on passing plays | [optional] 
**epa_pass_pp** | **float** | EPA per pass play | [optional] 
**epa_rush** | **float** | EPA on rushing plays | [optional] 
**epa_rush_pp** | **float** | EPA per rush play | [optional] 
**gp** | **int** | Games played | [optional] 
**var_pass** | **int** | Pass attempts (including sacks) | [optional] 
**pass_pct** | **float** | Percentage of plays that were passes (0-1) | [optional] 
**pass_td** | **int** | Passing touchdowns | [optional] 
**pass_yds** | **int** | Passing yards | [optional] 
**pass_ypg** | **float** | Pass yards per game | [optional] 
**pass_ypp** | **float** | Passing yards per pass attempt | [optional] 
**ppg** | **float** | Points per game | [optional] 
**red_zone_pct** | **float** | Red zone touchdown percentage (0-1) | [optional] 
**run** | **int** | Rush attempts | [optional] 
**rush_td** | **int** | Rushing touchdowns | [optional] 
**rush_yds** | **int** | Rushing yards | [optional] 
**rush_ypg** | **float** | Rush yards per game | [optional] 
**rush_ypp** | **float** | Rushing yards per rush attempt | [optional] 
**td** | **int** | Total touchdowns | [optional] 
**team_id** | **str** | Team identifier | [optional] 
**third_down_pct** | **float** | Third down conversion percentage (0-1) | [optional] 
**to** | **int** | Turnovers | [optional] 
**total** | **int** | Total offensive plays | [optional] 
**yds** | **int** | Total offensive yards | [optional] 
**ypg** | **float** | Yards per game | [optional] 
**ypp** | **float** | Yards per play | [optional] 

## Example

```python
from nfl.models.nfl_team_offense_overview_stats import NFLTeamOffenseOverviewStats

# TODO update the JSON string below
json = "{}"
# create an instance of NFLTeamOffenseOverviewStats from a JSON string
nfl_team_offense_overview_stats_instance = NFLTeamOffenseOverviewStats.from_json(json)
# print the JSON string representation of the object
print(NFLTeamOffenseOverviewStats.to_json())

# convert the object into a dict
nfl_team_offense_overview_stats_dict = nfl_team_offense_overview_stats_instance.to_dict()
# create an instance of NFLTeamOffenseOverviewStats from a dict
nfl_team_offense_overview_stats_from_dict = NFLTeamOffenseOverviewStats.from_dict(nfl_team_offense_overview_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


