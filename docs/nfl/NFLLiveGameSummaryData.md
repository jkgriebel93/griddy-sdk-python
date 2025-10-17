# NFLLiveGameSummaryData


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
**phase** | [**NFLNFLGamePhaseEnum**](NFLGamePhaseEnum.md) |  | [optional] 
**quarter** | [**NFLNFLGameQuarterEnum**](NFLGameQuarterEnum.md) |  | [optional] 
**weather** | **str** |  | [optional] 
**yard_line** | **str** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**away_team** | [**NFLNFLGameSummaryTeam**](NFLGameSummaryTeam.md) |  | [optional] 
**home_team** | [**NFLNFLGameSummaryTeam**](NFLGameSummaryTeam.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_live_game_summary_data import NFLLiveGameSummaryData

# TODO update the JSON string below
json = "{}"
# create an instance of NFLLiveGameSummaryData from a JSON string
nfl_live_game_summary_data_instance = NFLLiveGameSummaryData.from_json(json)
# print the JSON string representation of the object
print(NFLLiveGameSummaryData.to_json())

# convert the object into a dict
nfl_live_game_summary_data_dict = nfl_live_game_summary_data_instance.to_dict()
# create an instance of NFLLiveGameSummaryData from a dict
nfl_live_game_summary_data_from_dict = NFLLiveGameSummaryData.from_dict(nfl_live_game_summary_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


