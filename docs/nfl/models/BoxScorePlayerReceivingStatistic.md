# BoxScorePlayerReceivingStatistic


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
**receptions** | **int** |  | [optional] 
**yards** | **int** |  | [optional] 
**avg_yards** | **float** |  | [optional] 
**longest_pass_reception** | **int** |  | [optional] 
**touchdowns** | **int** |  | [optional] 
**longest_td_reception** | **int** |  | [optional] 
**pass_target** | **int** |  | [optional] 
**yards_after_catch** | **int** |  | [optional] 
**total_computed_yards_after_catch** | **float** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.box_score_player_receiving_statistic import BoxScorePlayerReceivingStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of BoxScorePlayerReceivingStatistic from a JSON string
box_score_player_receiving_statistic_instance = BoxScorePlayerReceivingStatistic.from_json(json)
# print the JSON string representation of the object
print(BoxScorePlayerReceivingStatistic.to_json())

# convert the object into a dict
box_score_player_receiving_statistic_dict = box_score_player_receiving_statistic_instance.to_dict()
# create an instance of BoxScorePlayerReceivingStatistic from a dict
box_score_player_receiving_statistic_from_dict = BoxScorePlayerReceivingStatistic.from_dict(box_score_player_receiving_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


