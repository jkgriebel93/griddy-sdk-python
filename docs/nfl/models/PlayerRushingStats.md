# PlayerRushingStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**att** | **int** | Rushing attempts | [optional] 
**att_pg** | **float** | Attempts per game | [optional] 
**display_name** | **str** | Player&#39;s full name | [optional] 
**eff** | **float** | Efficiency rating | [optional] 
**epa** | **float** | Expected Points Added | [optional] 
**epa_att** | **float** | EPA per attempt | [optional] 
**epa_pg** | **float** | EPA per game | [optional] 
**fum** | **int** | Fumbles | [optional] 
**fum_pg** | **float** | Fumbles per game | [optional] 
**gp** | **int** | Games played | [optional] 
**gs** | **int** | Games started | [optional] 
**headshot** | **str** | URL to player headshot image (contains formatInstructions placeholder) | [optional] 
**in_t_pct** | **float** | Inside tackles percentage (0-1) | [optional] 
**jersey_number** | **int** | Player&#39;s jersey number | [optional] 
**lost** | **int** | Fumbles lost | [optional] 
**lost_pg** | **float** | Fumbles lost per game | [optional] 
**nfl_id** | **str** | NFL player identifier | [optional] 
**ngs_position** | [**OffensivePlayerPositionEnum**](OffensivePlayerPositionEnum.md) |  | [optional] 
**ngs_position_group** | [**OffensivePlayerPositionEnum**](OffensivePlayerPositionEnum.md) |  | [optional] 
**position** | [**OffensivePlayerPositionEnum**](OffensivePlayerPositionEnum.md) |  | [optional] 
**position_group** | [**OffensivePlayerPositionEnum**](OffensivePlayerPositionEnum.md) |  | [optional] 
**qr** | **bool** | Qualified rusher status | [optional] 
**rush10_p_yds** | **int** | Rushes of 10+ yards | [optional] 
**rush10_p_yds_pg** | **float** | 10+ yard rushes per game | [optional] 
**rush15_p_mph** | **int** | Rushes of 15+ mph | [optional] 
**rush15_p_mph_pg** | **float** | 15+ mph rushes per game | [optional] 
**rush20_p_mph** | **int** | Rushes of 20+ mph | [optional] 
**rush20_p_mph_pg** | **float** | 20+ mph rushes per game | [optional] 
**ryoe** | **float** | Rush Yards Over Expected | [optional] 
**ryoe_att** | **float** | RYOE per attempt | [optional] 
**ryoe_pg** | **float** | RYOE per game | [optional] 
**short_name** | **str** | Abbreviated player name | [optional] 
**st_box_pct** | **float** | Stacked box percentage (0-1) | [optional] 
**success** | **float** | Success rate (0-1) | [optional] 
**td** | **int** | Rushing touchdowns | [optional] 
**td_pg** | **float** | Touchdowns per game | [optional] 
**team_id** | **str** | Team identifier | [optional] 
**tg** | **int** | Team games for player | [optional] 
**total_tg** | **int** | Total team games in period | [optional] 
**under_pct** | **float** | Under center percentage (0-1) | [optional] 
**x_ry** | **float** | Expected rushing yards | [optional] 
**x_ry_pg** | **float** | Expected rushing yards per game | [optional] 
**x_ypc** | **float** | Expected yards per carry | [optional] 
**yaco** | **float** | Yards after contact | [optional] 
**yaco_att** | **float** | Yards after contact per attempt | [optional] 
**yaco_pg** | **float** | Yards after contact per game | [optional] 
**ybco** | **float** | Yards before contact | [optional] 
**ybco_pg** | **float** | Yards before contact per game | [optional] 
**yds** | **int** | Rushing yards | [optional] 
**yds_pg** | **float** | Yards per game | [optional] 
**ypc** | **float** | Yards per carry | [optional] 

## Example

```python
from src.griddy.nfl.models.player_rushing_stats import PlayerRushingStats

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerRushingStats from a JSON string
player_rushing_stats_instance = PlayerRushingStats.from_json(json)
# print the JSON string representation of the object
print(PlayerRushingStats.to_json())

# convert the object into a dict
player_rushing_stats_dict = player_rushing_stats_instance.to_dict()
# create an instance of PlayerRushingStats from a dict
player_rushing_stats_from_dict = PlayerRushingStats.from_dict(player_rushing_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


