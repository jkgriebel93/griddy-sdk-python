# NFLBoxScorePlayerFieldGoalsStatistic


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
**position** | [**NFLNFLNextGenStatsPositionEnum**](NFLNextGenStatsPositionEnum.md) |  | [optional] 
**attempts** | **int** |  | [optional] 
**success_cnt** | **int** |  | [optional] 
**blocked_cnt** | **int** |  | [optional] 
**yards** | **int** |  | [optional] 
**avg_yard** | **float** |  | [optional] 
**longest_made_field_goal** | **int** |  | [optional] 

## Example

```python
from nfl.models.nfl_box_score_player_field_goals_statistic import NFLBoxScorePlayerFieldGoalsStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of NFLBoxScorePlayerFieldGoalsStatistic from a JSON string
nfl_box_score_player_field_goals_statistic_instance = NFLBoxScorePlayerFieldGoalsStatistic.from_json(json)
# print the JSON string representation of the object
print(NFLBoxScorePlayerFieldGoalsStatistic.to_json())

# convert the object into a dict
nfl_box_score_player_field_goals_statistic_dict = nfl_box_score_player_field_goals_statistic_instance.to_dict()
# create an instance of NFLBoxScorePlayerFieldGoalsStatistic from a dict
nfl_box_score_player_field_goals_statistic_from_dict = NFLBoxScorePlayerFieldGoalsStatistic.from_dict(nfl_box_score_player_field_goals_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


