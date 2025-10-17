# BoxScorePlayerFieldGoalsStatistic


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
**attempts** | **int** |  | [optional] 
**success_cnt** | **int** |  | [optional] 
**blocked_cnt** | **int** |  | [optional] 
**yards** | **int** |  | [optional] 
**avg_yard** | **float** |  | [optional] 
**longest_made_field_goal** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.box_score_player_field_goals_statistic import BoxScorePlayerFieldGoalsStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of BoxScorePlayerFieldGoalsStatistic from a JSON string
box_score_player_field_goals_statistic_instance = BoxScorePlayerFieldGoalsStatistic.from_json(json)
# print the JSON string representation of the object
print(BoxScorePlayerFieldGoalsStatistic.to_json())

# convert the object into a dict
box_score_player_field_goals_statistic_dict = box_score_player_field_goals_statistic_instance.to_dict()
# create an instance of BoxScorePlayerFieldGoalsStatistic from a dict
box_score_player_field_goals_statistic_from_dict = BoxScorePlayerFieldGoalsStatistic.from_dict(box_score_player_field_goals_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


