# PlayerPassingStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**att** | **int** | Attempts | [optional] 
**att_pg** | **float** | Attempts per game | [optional] 
**avg_sep** | **float** | Average receiver separation at target (yards) | [optional] 
**avg_ttp** | **float** | Average time to pass (seconds) | [optional] 
**avg_tts** | **float** | Average time to sack (seconds) | [optional] 
**avg_ttt** | **float** | Average time to throw (seconds) | [optional] 
**ay** | **float** | Air yards | [optional] 
**ay_att** | **float** | Air yards per attempt | [optional] 
**blitz_r** | **float** | Blitz rate faced | [optional] 
**cmp** | **int** | Completions | [optional] 
**cmp_pg** | **float** | Completions per game | [optional] 
**cmp_pct** | **float** | Completion percentage (0-1) | [optional] 
**cpoe** | **float** | Completion percentage over expected | [optional] 
**db** | **int** | Dropbacks | [optional] 
**db_pg** | **float** | Dropbacks per game | [optional] 
**deep_att_pct** | **float** | Deep attempt percentage (20+ air yards) | [optional] 
**display_name** | **str** | Player&#39;s full name | [optional] 
**drop** | **int** | Dropped passes by receivers | [optional] 
**drop_pg** | **float** | Drops per game | [optional] 
**drop_r** | **float** | Drop rate | [optional] 
**epa** | **float** | Expected Points Added | [optional] 
**epa_db** | **float** | EPA per dropback | [optional] 
**epa_pg** | **float** | EPA per game | [optional] 
**gp** | **int** | Games played | [optional] 
**gs** | **int** | Games started | [optional] 
**headshot** | **str** | URL to player headshot image (contains formatInstructions placeholder) | [optional] 
**int** | **int** | Interceptions | [optional] 
**int_pg** | **float** | Interceptions per game | [optional] 
**jersey_number** | **int** | Player&#39;s jersey number | [optional] 
**nfl_id** | **str** | NFL player identifier | [optional] 
**ngs_position** | **str** | Next Gen Stats position | [optional] 
**ngs_position_group** | **str** | Next Gen Stats position group | [optional] 
**pa_db_pct** | **float** | Play action dropback percentage | [optional] 
**position** | **str** | Player position | [optional] 
**position_group** | **str** | Position group | [optional] 
**qbp** | **int** | Times under QB pressure | [optional] 
**qbp_pg** | **float** | QB pressure per game | [optional] 
**qbp_r** | **float** | QB pressure rate | [optional] 
**qp** | **bool** | Qualified passer status | [optional] 
**rating** | **float** | Passer rating | [optional] 
**sack** | **int** | Times sacked | [optional] 
**sack_pg** | **float** | Sacks per game | [optional] 
**short_name** | **str** | Abbreviated player name | [optional] 
**td** | **int** | Touchdown passes | [optional] 
**td_pg** | **float** | Touchdowns per game | [optional] 
**team_id** | **str** | Team identifier | [optional] 
**tg** | **int** | Team games for player | [optional] 
**total_tg** | **int** | Total team games in period | [optional] 
**tw_att_pg** | **float** | Two-minute attempts per game | [optional] 
**tw_att_pct** | **float** | Two-minute drill attempt percentage | [optional] 
**x_cmp** | **float** | Expected completion percentage | [optional] 
**x_yac** | **float** | Expected yards after catch | [optional] 
**yac** | **float** | Yards after catch | [optional] 
**yac_pct** | **float** | YAC percentage of total yards | [optional] 
**yds** | **int** | Passing yards | [optional] 
**yds_pg** | **float** | Yards per game | [optional] 
**ypa** | **float** | Yards per attempt | [optional] 

## Example

```python
from src.griddy.nfl.models.player_passing_stats import PlayerPassingStats

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerPassingStats from a JSON string
player_passing_stats_instance = PlayerPassingStats.from_json(json)
# print the JSON string representation of the object
print(PlayerPassingStats.to_json())

# convert the object into a dict
player_passing_stats_dict = player_passing_stats_instance.to_dict()
# create an instance of PlayerPassingStats from a dict
player_passing_stats_from_dict = PlayerPassingStats.from_dict(player_passing_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


