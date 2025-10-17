# NFLWeeklyGameDetailSummaryScore

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
from nfl.models.nfl_weekly_game_detail_summary_score import NFLWeeklyGameDetailSummaryScore

# TODO update the JSON string below
json = "{}"
# create an instance of NFLWeeklyGameDetailSummaryScore from a JSON string
nfl_weekly_game_detail_summary_score_instance = NFLWeeklyGameDetailSummaryScore.from_json(json)
# print the JSON string representation of the object
print(NFLWeeklyGameDetailSummaryScore.to_json())

# convert the object into a dict
nfl_weekly_game_detail_summary_score_dict = nfl_weekly_game_detail_summary_score_instance.to_dict()
# create an instance of NFLWeeklyGameDetailSummaryScore from a dict
nfl_weekly_game_detail_summary_score_from_dict = NFLWeeklyGameDetailSummaryScore.from_dict(nfl_weekly_game_detail_summary_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


