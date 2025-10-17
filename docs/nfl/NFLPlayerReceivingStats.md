# NFLPlayerReceivingStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_rt_dep** | **float** | Average route depth (yards) | [optional] 
**avg_sep** | **float** | Average receiver separation at target (yards) | [optional] 
**ay** | **float** | Air yards | [optional] 
**ay_pg** | **float** | Air yards per game | [optional] 
**ay_tgt** | **float** | Air yards per target | [optional] 
**catch** | **float** | Catch rate (0-1) | [optional] 
**croe** | **float** | Catch Rate Over Expected | [optional] 
**deep_tgt_pct** | **float** | Deep target percentage (20+ air yards) | [optional] 
**display_name** | **str** | Player&#39;s full name | [optional] 
**drop** | **int** | Dropped passes | [optional] 
**drop_pg** | **float** | Drops per game | [optional] 
**drop_tgt** | **float** | Drop rate (0-1) | [optional] 
**epa** | **float** | Expected Points Added | [optional] 
**epa_pg** | **float** | EPA per game | [optional] 
**epa_rt** | **float** | EPA per route run | [optional] 
**epa_tgt** | **float** | EPA per target | [optional] 
**ez_rec** | **int** | End zone receptions | [optional] 
**ez_rec_pg** | **float** | End zone receptions per game | [optional] 
**ez_tgt** | **int** | End zone targets | [optional] 
**ez_tgt_pg** | **float** | End zone targets per game | [optional] 
**fapi_game_id** | **str** | Football API game identifier | [optional] 
**final_score** | **str** | Final score of the game | [optional] 
**game_id** | **int** | Game identifier (10-digit format YYYYMMDDNN) | [optional] 
**game_result** | [**NFLNFLGameResultEnum**](NFLGameResultEnum.md) |  | [optional] 
**gp** | **int** | Games played | [optional] 
**gs** | **int** | Games started | [optional] 
**headshot** | **str** | URL to player headshot image (contains formatInstructions placeholder) | [optional] 
**int** | **int** | Interceptions thrown on targets to this receiver | [optional] 
**int_pg** | **float** | Interceptions per game | [optional] 
**is_home** | **bool** | Whether player&#39;s team was at home | [optional] 
**jersey_number** | **int** | Player&#39;s jersey number | [optional] 
**nfl_id** | **str** | NFL player identifier | [optional] 
**ngs_position** | [**NFLNFLOffensiveSkillPositionEnum**](NFLOffensiveSkillPositionEnum.md) |  | [optional] 
**ngs_position_group** | [**NFLNFLOffensiveSkillPositionEnum**](NFLOffensiveSkillPositionEnum.md) |  | [optional] 
**opponent_team_id** | **str** | Opponent team identifier | [optional] 
**position** | [**NFLNFLOffensiveSkillPositionEnum**](NFLOffensiveSkillPositionEnum.md) |  | [optional] 
**position_group** | [**NFLNFLOffensiveSkillPositionEnum**](NFLOffensiveSkillPositionEnum.md) |  | [optional] 
**qr** | **bool** | Qualified receiver status | [optional] 
**rating** | **float** | Passer rating when targeting this receiver | [optional] 
**rec** | **int** | Receptions | [optional] 
**rec_pg** | **float** | Receptions per game | [optional] 
**rt** | **int** | Routes run | [optional] 
**rt_pg** | **float** | Routes per game | [optional] 
**short_name** | **str** | Abbreviated player name | [optional] 
**td** | **int** | Touchdown receptions | [optional] 
**td_pg** | **float** | Touchdowns per game | [optional] 
**team_id** | **str** | Team identifier | [optional] 
**tg** | **int** | Team games for player | [optional] 
**tgt** | **int** | Targets | [optional] 
**tgt_pg** | **float** | Targets per game | [optional] 
**tgt_rt** | **float** | Target rate (targets per route run) | [optional] 
**total_tg** | **int** | Total team games in period | [optional] 
**tw_pct** | **float** | Tight window percentage | [optional] 
**week_slug** | **str** | Week identifier slug | [optional] 
**x_catch** | **float** | Expected catch rate (0-1) | [optional] 
**x_yac** | **float** | Expected yards after catch | [optional] 
**x_yac_pg** | **float** | Expected YAC per game | [optional] 
**yac** | **float** | Yards after catch | [optional] 
**yac_pg** | **float** | YAC per game | [optional] 
**yac_rec** | **float** | YAC per reception | [optional] 
**yacoe** | **float** | Yards after catch over expected | [optional] 
**yacoe_pg** | **float** | YACOE per game | [optional] 
**yds** | **int** | Receiving yards | [optional] 
**yds_pg** | **float** | Yards per game | [optional] 
**yds_rec** | **float** | Yards per reception | [optional] 
**yds_rt** | **float** | Yards per route run | [optional] 

## Example

```python
from nfl.models.nfl_player_receiving_stats import NFLPlayerReceivingStats

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPlayerReceivingStats from a JSON string
nfl_player_receiving_stats_instance = NFLPlayerReceivingStats.from_json(json)
# print the JSON string representation of the object
print(NFLPlayerReceivingStats.to_json())

# convert the object into a dict
nfl_player_receiving_stats_dict = nfl_player_receiving_stats_instance.to_dict()
# create an instance of NFLPlayerReceivingStats from a dict
nfl_player_receiving_stats_from_dict = NFLPlayerReceivingStats.from_dict(nfl_player_receiving_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


