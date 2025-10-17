# Summary

Live game state summary including score, possession, and game situation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attendance** | **int** | Game attendance | [optional] 
**away_team** | [**WeeklyGameDetailSummaryTeam**](WeeklyGameDetailSummaryTeam.md) |  | [optional] 
**clock** | **str** | Current game clock | [optional] 
**distance** | **int** | Yards to go for first down | [optional] 
**down** | **int** | Current down | [optional] 
**game_book_url** | **str** | URL to official NFL game book PDF | [optional] 
**game_id** | **str** | Game identifier (UUID format) | [optional] 
**home_team** | [**WeeklyGameDetailSummaryTeam**](WeeklyGameDetailSummaryTeam.md) |  | [optional] 
**is_goal_to_go** | **bool** | Whether it&#39;s a goal-to-go situation | [optional] 
**is_red_zone** | **bool** | Whether the ball is in the red zone | [optional] 
**offset** | **int** | Time offset in seconds | [optional] 
**phase** | **str** | Current game phase | [optional] 
**quarter** | **str** | Current quarter or period | [optional] 
**start_time** | **datetime** | Game start time | [optional] 
**weather** | **str** | Weather conditions | [optional] 
**yard_line** | **str** | Current field position | [optional] 

## Example

```python
from src.griddy.nfl.models.summary import Summary

# TODO update the JSON string below
json = "{}"
# create an instance of Summary from a JSON string
summary_instance = Summary.from_json(json)
# print the JSON string representation of the object
print(Summary.to_json())

# convert the object into a dict
summary_dict = summary_instance.to_dict()
# create an instance of Summary from a dict
summary_from_dict = Summary.from_dict(summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


