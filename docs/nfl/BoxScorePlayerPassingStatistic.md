# BoxScorePlayerPassingStatistic


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
**completions** | **int** |  | [optional] 
**completion_pct** | **float** |  | [optional] 
**yards** | **int** |  | [optional] 
**yards_per_attempt** | **float** |  | [optional] 
**lost_sacked_yards** | **int** |  | [optional] 
**sacks** | **int** |  | [optional] 
**touchdowns** | **int** |  | [optional] 
**longest_pass_completion** | **int** |  | [optional] 
**longest_td_pass** | **int** |  | [optional] 
**interceptions** | **int** |  | [optional] 
**qb_rating** | **float** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.box_score_player_passing_statistic import BoxScorePlayerPassingStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of BoxScorePlayerPassingStatistic from a JSON string
box_score_player_passing_statistic_instance = BoxScorePlayerPassingStatistic.from_json(json)
# print the JSON string representation of the object
print(BoxScorePlayerPassingStatistic.to_json())

# convert the object into a dict
box_score_player_passing_statistic_dict = box_score_player_passing_statistic_instance.to_dict()
# create an instance of BoxScorePlayerPassingStatistic from a dict
box_score_player_passing_statistic_from_dict = BoxScorePlayerPassingStatistic.from_dict(box_score_player_passing_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


