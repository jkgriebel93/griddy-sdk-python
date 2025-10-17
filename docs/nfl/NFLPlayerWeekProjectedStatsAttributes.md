# NFLPlayerWeekProjectedStatsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assisted_tackles** | **float** |  | [optional] 
**defense_interceptions** | **float** |  | [optional] 
**dt_blocked_kicks** | **float** |  | [optional] 
**dt_fumbles_forced** | **float** |  | [optional] 
**dt_fumbles_recovered** | **float** |  | [optional] 
**dt_interceptions** | **float** |  | [optional] 
**dt_kickoff_return_yards** | **float** |  | [optional] 
**dt_points_allowed** | **float** |  | [optional] 
**dt_sacks** | **float** |  | [optional] 
**dt_safeties** | **float** |  | [optional] 
**dt_touchdowns** | **float** |  | [optional] 
**dt_yards_allowed** | **float** |  | [optional] 
**fg_attempts** | **float** |  | [optional] 
**fg_made20to29** | **float** |  | [optional] 
**fg_made30to39** | **float** |  | [optional] 
**fg_made40to49** | **float** |  | [optional] 
**fg_made50** | **float** |  | [optional] 
**forced_fumbles** | **float** |  | [optional] 
**fumbles** | **float** |  | [optional] 
**fumbles_lost** | **float** |  | [optional] 
**fumbles_recovered** | **float** |  | [optional] 
**games_played** | **int** |  | [optional] 
**interceptions_thrown** | **float** |  | [optional] 
**kickoff_return_touchdowns** | **float** |  | [optional] 
**kickoff_return_yards** | **float** |  | [optional] 
**pass_defended** | **float** |  | [optional] 
**passing_attempts** | **float** |  | [optional] 
**passing_completions** | **float** |  | [optional] 
**passing_touchdowns** | **float** |  | [optional] 
**passing_yards** | **float** |  | [optional] 
**pat_made** | **float** |  | [optional] 
**pat_missed** | **float** |  | [optional] 
**player_id** | **str** |  | [optional] 
**receiving_touchdowns** | **float** |  | [optional] 
**receiving_yards** | **float** |  | [optional] 
**receptions** | **float** |  | [optional] 
**rushing_attempts** | **float** |  | [optional] 
**rushing_touchdowns** | **float** |  | [optional] 
**rushing_yards** | **float** |  | [optional] 
**sacks** | **float** |  | [optional] 
**season** | **int** |  | [optional] 
**tackles** | **float** |  | [optional] 
**week** | **int** |  | [optional] 

## Example

```python
from nfl.models.nfl_player_week_projected_stats_attributes import NFLPlayerWeekProjectedStatsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPlayerWeekProjectedStatsAttributes from a JSON string
nfl_player_week_projected_stats_attributes_instance = NFLPlayerWeekProjectedStatsAttributes.from_json(json)
# print the JSON string representation of the object
print(NFLPlayerWeekProjectedStatsAttributes.to_json())

# convert the object into a dict
nfl_player_week_projected_stats_attributes_dict = nfl_player_week_projected_stats_attributes_instance.to_dict()
# create an instance of NFLPlayerWeekProjectedStatsAttributes from a dict
nfl_player_week_projected_stats_attributes_from_dict = NFLPlayerWeekProjectedStatsAttributes.from_dict(nfl_player_week_projected_stats_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


