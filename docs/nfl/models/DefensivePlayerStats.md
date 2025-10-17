# DefensivePlayerStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bh_pct** | **float** | Burn percentage (deep completions allowed rate) | [optional] 
**catch_nd** | **float** | Catch rate allowed (0-1) | [optional] 
**cov** | **int** | Total coverage snaps | [optional] 
**cov_nd** | **int** | Coverage snaps (no data excluded) | [optional] 
**croe_nd** | **float** | Completion Rate Over Expected allowed | [optional] 
**display_name** | **str** | Player&#39;s full name | [optional] 
**game_snap** | **int** | Defensive snaps played | [optional] 
**gp** | **int** | Games played | [optional] 
**gs** | **int** | Games started | [optional] 
**headshot** | **str** | URL to player headshot image (contains formatInstructions placeholder) | [optional] 
**int** | **int** | Interceptions | [optional] 
**jersey_number** | **int** | Player&#39;s jersey number | [optional] 
**nfl_id** | **str** | NFL player identifier | [optional] 
**ngs_position** | [**NextGenStatsPositionEnum**](NextGenStatsPositionEnum.md) |  | [optional] 
**ngs_position_group** | [**DefensivePositionGroupEnum**](DefensivePositionGroupEnum.md) |  | [optional] 
**pass_rating_nd** | **float** | Passer rating allowed when targeted | [optional] 
**position** | [**DefensivePositionEnum**](DefensivePositionEnum.md) |  | [optional] 
**position_group** | [**DefensivePositionGroupEnum**](DefensivePositionGroupEnum.md) |  | [optional] 
**qd** | **bool** | Qualified defender status | [optional] 
**rec_nd** | **int** | Receptions allowed | [optional] 
**rec_td_nd** | **int** | Receiving touchdowns allowed | [optional] 
**rec_yds_nd** | **int** | Receiving yards allowed | [optional] 
**sep** | **float** | Average separation allowed at target (yards) | [optional] 
**short_name** | **str** | Abbreviated player name | [optional] 
**team_id** | **str** | Team identifier | [optional] 
**team_snap** | **int** | Total team defensive snaps | [optional] 
**tg** | **int** | Team games for player | [optional] 
**tgt_epa_nd** | **float** | Target EPA (Expected Points Added) allowed | [optional] 
**tgt_nd** | **int** | Times targeted in coverage | [optional] 
**tgt_rnd** | **float** | Target rate (targets per coverage snap) | [optional] 
**total_tg** | **int** | Total team games in period | [optional] 
**twf_pct** | **float** | Tight window frequency (percentage of targets in tight windows) | [optional] 
**yacpr_nd** | **float** | Yards After Catch allowed per reception | [optional] 

## Example

```python
from src.griddy.nfl.models.defensive_player_stats import DefensivePlayerStats

# TODO update the JSON string below
json = "{}"
# create an instance of DefensivePlayerStats from a JSON string
defensive_player_stats_instance = DefensivePlayerStats.from_json(json)
# print the JSON string representation of the object
print(DefensivePlayerStats.to_json())

# convert the object into a dict
defensive_player_stats_dict = defensive_player_stats_instance.to_dict()
# create an instance of DefensivePlayerStats from a dict
defensive_player_stats_from_dict = DefensivePlayerStats.from_dict(defensive_player_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


