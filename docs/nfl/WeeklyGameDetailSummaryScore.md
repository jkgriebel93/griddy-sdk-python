# WeeklyGameDetailSummaryScore

Team score breakdown by quarter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ot** | **int** | Overtime points | [optional] 
**q1** | **int** | First quarter points | [optional] 
**q2** | **int** | Second quarter points | [optional] 
**q3** | **int** | Third quarter points | [optional] 
**q4** | **int** | Fourth quarter points | [optional] 
**total** | **int** | Total points scored | [optional] 

## Example

```python
from src.griddy.nfl.models.weekly_game_detail_summary_score import WeeklyGameDetailSummaryScore

# TODO update the JSON string below
json = "{}"
# create an instance of WeeklyGameDetailSummaryScore from a JSON string
weekly_game_detail_summary_score_instance = WeeklyGameDetailSummaryScore.from_json(json)
# print the JSON string representation of the object
print(WeeklyGameDetailSummaryScore.to_json())

# convert the object into a dict
weekly_game_detail_summary_score_dict = weekly_game_detail_summary_score_instance.to_dict()
# create an instance of WeeklyGameDetailSummaryScore from a dict
weekly_game_detail_summary_score_from_dict = WeeklyGameDetailSummaryScore.from_dict(weekly_game_detail_summary_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


