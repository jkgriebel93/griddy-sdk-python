# NFLWeeklyGameDetailSummaryTeam

Team game state in summary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_possession** | **bool** | Whether the team currently has possession | [optional] 
**score** | [**NFLNFLWeeklyGameDetailSummaryScore**](NFLWeeklyGameDetailSummaryScore.md) |  | [optional] 
**team_id** | **str** | Team identifier (UUID format) | [optional] 
**timeouts** | [**NFLNFLWeeklyGameDetailSummaryTimeouts**](NFLWeeklyGameDetailSummaryTimeouts.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_weekly_game_detail_summary_team import NFLWeeklyGameDetailSummaryTeam

# TODO update the JSON string below
json = "{}"
# create an instance of NFLWeeklyGameDetailSummaryTeam from a JSON string
nfl_weekly_game_detail_summary_team_instance = NFLWeeklyGameDetailSummaryTeam.from_json(json)
# print the JSON string representation of the object
print(NFLWeeklyGameDetailSummaryTeam.to_json())

# convert the object into a dict
nfl_weekly_game_detail_summary_team_dict = nfl_weekly_game_detail_summary_team_instance.to_dict()
# create an instance of NFLWeeklyGameDetailSummaryTeam from a dict
nfl_weekly_game_detail_summary_team_from_dict = NFLWeeklyGameDetailSummaryTeam.from_dict(nfl_weekly_game_detail_summary_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


