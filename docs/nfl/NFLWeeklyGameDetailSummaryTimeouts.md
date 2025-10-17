# NFLWeeklyGameDetailSummaryTimeouts

Team timeout information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remaining** | **int** | Timeouts remaining | [optional] 
**used** | **int** | Timeouts used | [optional] 

## Example

```python
from nfl.models.nfl_weekly_game_detail_summary_timeouts import NFLWeeklyGameDetailSummaryTimeouts

# TODO update the JSON string below
json = "{}"
# create an instance of NFLWeeklyGameDetailSummaryTimeouts from a JSON string
nfl_weekly_game_detail_summary_timeouts_instance = NFLWeeklyGameDetailSummaryTimeouts.from_json(json)
# print the JSON string representation of the object
print(NFLWeeklyGameDetailSummaryTimeouts.to_json())

# convert the object into a dict
nfl_weekly_game_detail_summary_timeouts_dict = nfl_weekly_game_detail_summary_timeouts_instance.to_dict()
# create an instance of NFLWeeklyGameDetailSummaryTimeouts from a dict
nfl_weekly_game_detail_summary_timeouts_from_dict = NFLWeeklyGameDetailSummaryTimeouts.from_dict(nfl_weekly_game_detail_summary_timeouts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


