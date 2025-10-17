# DefensivePassRushStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Players full name | [optional] 
**game_snap** | **int** | Defensive snaps played | [optional] 
**gp** | **int** | Games played | [optional] 
**gs** | **int** | Games started | [optional] 
**headshot** | **str** | URL to player headshot image (contains formatInstructions placeholder) | [optional] 
**jersey_number** | **int** | Player jersey number | [optional] 
**nfl_id** | **str** | NFL player identifier | [optional] 
**ngs_position** | [**NextGenStatsPositionEnum**](NextGenStatsPositionEnum.md) |  | [optional] 
**ngs_position_group** | [**DefensivePositionGroupEnum**](DefensivePositionGroupEnum.md) |  | [optional] 
**position** | [**DefensivePositionEnum**](DefensivePositionEnum.md) |  | [optional] 
**position_group** | [**DefensivePositionGroupEnum**](DefensivePositionGroupEnum.md) |  | [optional] 
**pr** | **int** | Pass rush grade/rating | [optional] 
**pr_go** | **float** | Pass rush get-off metric | [optional] 
**pr_r** | **float** | Pass rush rate (0-1) | [optional] 
**qbp** | **int** | Quarterback pressures | [optional] 
**qbp_r** | **float** | Quarterback pressure rate (0-1) | [optional] 
**qd** | **bool** | Qualified defender status | [optional] 
**qp** | **int** | Quarterback hits | [optional] 
**sack** | **float** | Sacks (can be fractional for shared sacks) | [optional] 
**sack_r** | **float** | Sack rate (0-1) | [optional] 
**short_name** | **str** | Abbreviated player name | [optional] 
**team_id** | **str** | Team identifier | [optional] 
**team_snap** | **int** | Total team defensive snaps | [optional] 
**tg** | **int** | Team games for player | [optional] 
**total_tg** | **int** | Total team games in period | [optional] 
**ttp** | **float** | Time to pressure (seconds) | [optional] 
**tts** | **float** | Time to sack (seconds) | [optional] 
**turn_qbp** | **int** | Quarterback pressures that resulted in turnovers | [optional] 

## Example

```python
from src.griddy.nfl.models.defensive_pass_rush_stats import DefensivePassRushStats

# TODO update the JSON string below
json = "{}"
# create an instance of DefensivePassRushStats from a JSON string
defensive_pass_rush_stats_instance = DefensivePassRushStats.from_json(json)
# print the JSON string representation of the object
print(DefensivePassRushStats.to_json())

# convert the object into a dict
defensive_pass_rush_stats_dict = defensive_pass_rush_stats_instance.to_dict()
# create an instance of DefensivePassRushStats from a dict
defensive_pass_rush_stats_from_dict = DefensivePassRushStats.from_dict(defensive_pass_rush_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


