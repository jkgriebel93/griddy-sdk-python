# LiveGameSummaryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **str** |  | [optional] 
**offset** | **int** |  | [optional] 
**attendance** | **int** |  | [optional] 
**clock** | **str** |  | [optional] 
**distance** | **int** |  | [optional] 
**down** | **int** |  | [optional] 
**game_book_url** | **str** |  | [optional] 
**is_goal_to_go** | **bool** |  | [optional] 
**is_red_zone** | **bool** |  | [optional] 
**phase** | [**GamePhaseEnum**](GamePhaseEnum.md) |  | [optional] 
**quarter** | [**GameQuarterEnum**](GameQuarterEnum.md) |  | [optional] 
**weather** | **str** |  | [optional] 
**yard_line** | **str** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**away_team** | [**GameSummaryTeam**](GameSummaryTeam.md) |  | [optional] 
**home_team** | [**GameSummaryTeam**](GameSummaryTeam.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.live_game_summary_data import LiveGameSummaryData

# TODO update the JSON string below
json = "{}"
# create an instance of LiveGameSummaryData from a JSON string
live_game_summary_data_instance = LiveGameSummaryData.from_json(json)
# print the JSON string representation of the object
print(LiveGameSummaryData.to_json())

# convert the object into a dict
live_game_summary_data_dict = live_game_summary_data_instance.to_dict()
# create an instance of LiveGameSummaryData from a dict
live_game_summary_data_from_dict = LiveGameSummaryData.from_dict(live_game_summary_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


