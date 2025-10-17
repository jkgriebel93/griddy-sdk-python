# WeeklyGameDetailSummaryTeam

Team game state in summary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_possession** | **bool** | Whether the team currently has possession | [optional] 
**score** | [**WeeklyGameDetailSummaryScore**](WeeklyGameDetailSummaryScore.md) |  | [optional] 
**team_id** | **str** | Team identifier (UUID format) | [optional] 
**timeouts** | [**WeeklyGameDetailSummaryTimeouts**](WeeklyGameDetailSummaryTimeouts.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.weekly_game_detail_summary_team import WeeklyGameDetailSummaryTeam

# TODO update the JSON string below
json = "{}"
# create an instance of WeeklyGameDetailSummaryTeam from a JSON string
weekly_game_detail_summary_team_instance = WeeklyGameDetailSummaryTeam.from_json(json)
# print the JSON string representation of the object
print(WeeklyGameDetailSummaryTeam.to_json())

# convert the object into a dict
weekly_game_detail_summary_team_dict = weekly_game_detail_summary_team_instance.to_dict()
# create an instance of WeeklyGameDetailSummaryTeam from a dict
weekly_game_detail_summary_team_from_dict = WeeklyGameDetailSummaryTeam.from_dict(weekly_game_detail_summary_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


