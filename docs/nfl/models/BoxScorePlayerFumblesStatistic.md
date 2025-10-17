# BoxScorePlayerFumblesStatistic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nfl_id** | **int** |  | [optional] 
**gsis_id** | **str** |  | [optional] 
**esb_id** | **str** |  | [optional] 
**jersey_number** | **int** |  | [optional] 
**player_name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**headshot** | **str** | URL to player headshot image (contains formatInstructions placeholder) | [optional] 
**position** | [**NextGenStatsPositionEnum**](NextGenStatsPositionEnum.md) |  | [optional] 
**fumbles** | **int** |  | [optional] 
**own_fumble_recoveries** | **int** |  | [optional] 
**own_fumble_recovery_yards** | **int** |  | [optional] 
**own_fumble_recovery_tds** | **int** |  | [optional] 
**opponent_fumble_recoveries** | **int** |  | [optional] 
**opponent_fumble_recovery_yards** | **int** |  | [optional] 
**opponent_fumble_recovery_tds** | **int** |  | [optional] 
**forced_fumbles** | **int** |  | [optional] 
**fumble_out_of_bounds** | **int** |  | [optional] 
**miscellaneous_forced_fumbles** | **int** |  | [optional] 
**miscellaneous_fumble_recoveries** | **int** |  | [optional] 
**special_teams_forced_fumbles** | **int** |  | [optional] 
**special_teams_fumble_recoveries** | **int** |  | [optional] 
**lost_possession** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.box_score_player_fumbles_statistic import BoxScorePlayerFumblesStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of BoxScorePlayerFumblesStatistic from a JSON string
box_score_player_fumbles_statistic_instance = BoxScorePlayerFumblesStatistic.from_json(json)
# print the JSON string representation of the object
print(BoxScorePlayerFumblesStatistic.to_json())

# convert the object into a dict
box_score_player_fumbles_statistic_dict = box_score_player_fumbles_statistic_instance.to_dict()
# create an instance of BoxScorePlayerFumblesStatistic from a dict
box_score_player_fumbles_statistic_from_dict = BoxScorePlayerFumblesStatistic.from_dict(box_score_player_fumbles_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


