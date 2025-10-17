# WeeklyGameDetailSummaryTimeouts

Team timeout information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remaining** | **int** | Timeouts remaining | [optional] 
**used** | **int** | Timeouts used | [optional] 

## Example

```python
from src.griddy.nfl.models.weekly_game_detail_summary_timeouts import WeeklyGameDetailSummaryTimeouts

# TODO update the JSON string below
json = "{}"
# create an instance of WeeklyGameDetailSummaryTimeouts from a JSON string
weekly_game_detail_summary_timeouts_instance = WeeklyGameDetailSummaryTimeouts.from_json(json)
# print the JSON string representation of the object
print(WeeklyGameDetailSummaryTimeouts.to_json())

# convert the object into a dict
weekly_game_detail_summary_timeouts_dict = weekly_game_detail_summary_timeouts_instance.to_dict()
# create an instance of WeeklyGameDetailSummaryTimeouts from a dict
weekly_game_detail_summary_timeouts_from_dict = WeeklyGameDetailSummaryTimeouts.from_dict(weekly_game_detail_summary_timeouts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


