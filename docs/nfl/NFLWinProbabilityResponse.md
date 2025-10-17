# NFLWinProbabilityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **int** | Game identifier (10-digit format YYYYMMDDNN) | [optional] 
**game_key** | **int** | Unique game key identifier | [optional] 
**plays** | [**List[NFLNFLPlayWinProbability]**](NFLPlayWinProbability.md) | Chronological list of all plays with win probability data | [optional] 
**pregame_away_team_win_probability** | **float** | Away team&#39;s win probability before the game started | [optional] 
**pregame_home_team_win_probability** | **float** | Home team&#39;s win probability before the game started | [optional] 

## Example

```python
from nfl.models.nfl_win_probability_response import NFLWinProbabilityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLWinProbabilityResponse from a JSON string
nfl_win_probability_response_instance = NFLWinProbabilityResponse.from_json(json)
# print the JSON string representation of the object
print(NFLWinProbabilityResponse.to_json())

# convert the object into a dict
nfl_win_probability_response_dict = nfl_win_probability_response_instance.to_dict()
# create an instance of NFLWinProbabilityResponse from a dict
nfl_win_probability_response_from_dict = NFLWinProbabilityResponse.from_dict(nfl_win_probability_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


