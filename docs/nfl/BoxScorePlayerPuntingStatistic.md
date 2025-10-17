# BoxScorePlayerPuntingStatistic


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
**yards** | **int** |  | [optional] 
**gross_avg_punt_length** | **int** |  | [optional] 
**blocked_cnt** | **int** |  | [optional] 
**longest_punt** | **int** |  | [optional] 
**touchback_cnts** | **int** |  | [optional] 
**inside20_cnt** | **int** |  | [optional] 
**net_punting_avg** | **int** |  | [optional] 
**return_yards** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.box_score_player_punting_statistic import BoxScorePlayerPuntingStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of BoxScorePlayerPuntingStatistic from a JSON string
box_score_player_punting_statistic_instance = BoxScorePlayerPuntingStatistic.from_json(json)
# print the JSON string representation of the object
print(BoxScorePlayerPuntingStatistic.to_json())

# convert the object into a dict
box_score_player_punting_statistic_dict = box_score_player_punting_statistic_instance.to_dict()
# create an instance of BoxScorePlayerPuntingStatistic from a dict
box_score_player_punting_statistic_from_dict = BoxScorePlayerPuntingStatistic.from_dict(box_score_player_punting_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


