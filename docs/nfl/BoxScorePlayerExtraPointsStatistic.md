# BoxScorePlayerExtraPointsStatistic


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
**attempt_cnt** | **int** |  | [optional] 
**success_cnt** | **int** |  | [optional] 
**blocked_cnt** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.box_score_player_extra_points_statistic import BoxScorePlayerExtraPointsStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of BoxScorePlayerExtraPointsStatistic from a JSON string
box_score_player_extra_points_statistic_instance = BoxScorePlayerExtraPointsStatistic.from_json(json)
# print the JSON string representation of the object
print(BoxScorePlayerExtraPointsStatistic.to_json())

# convert the object into a dict
box_score_player_extra_points_statistic_dict = box_score_player_extra_points_statistic_instance.to_dict()
# create an instance of BoxScorePlayerExtraPointsStatistic from a dict
box_score_player_extra_points_statistic_from_dict = BoxScorePlayerExtraPointsStatistic.from_dict(box_score_player_extra_points_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


