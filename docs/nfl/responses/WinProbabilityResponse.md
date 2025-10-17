# WinProbabilityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **int** | Game identifier (10-digit format YYYYMMDDNN) | [optional] 
**game_key** | **int** | Unique game key identifier | [optional] 
**plays** | [**List[PlayWinProbability]**](PlayWinProbability.md) | Chronological list of all plays with win probability data | [optional] 
**pregame_away_team_win_probability** | **float** | Away team&#39;s win probability before the game started | [optional] 
**pregame_home_team_win_probability** | **float** | Home team&#39;s win probability before the game started | [optional] 

## Example

```python
from src.griddy.nfl.models.win_probability_response import WinProbabilityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WinProbabilityResponse from a JSON string
win_probability_response_instance = WinProbabilityResponse.from_json(json)
# print the JSON string representation of the object
print(WinProbabilityResponse.to_json())

# convert the object into a dict
win_probability_response_dict = win_probability_response_instance.to_dict()
# create an instance of WinProbabilityResponse from a dict
win_probability_response_from_dict = WinProbabilityResponse.from_dict(win_probability_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


