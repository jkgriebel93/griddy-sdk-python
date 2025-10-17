# NFLLiveGame

Live game scoring and status information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away_team** | [**NFLNFLLiveGameAwayTeam**](NFLLiveGameAwayTeam.md) |  | [optional] 
**game_id** | **str** | Game identifier | [optional] 
**home_team** | [**NFLNFLLiveGameAwayTeam**](NFLLiveGameAwayTeam.md) |  | [optional] 
**last_play** | **str** | Description of last play | [optional] 
**possession** | **str** | Team abbreviation with current possession | [optional] 
**quarter** | **str** | Current quarter/period | [optional] 
**red_zone** | **bool** | Whether team is in red zone | [optional] 
**status** | [**NFLNFLGameStatusEnum**](NFLGameStatusEnum.md) |  | [optional] 
**time_remaining** | **str** | Time remaining in current period | [optional] 

## Example

```python
from nfl.models.nfl_live_game import NFLLiveGame

# TODO update the JSON string below
json = "{}"
# create an instance of NFLLiveGame from a JSON string
nfl_live_game_instance = NFLLiveGame.from_json(json)
# print the JSON string representation of the object
print(NFLLiveGame.to_json())

# convert the object into a dict
nfl_live_game_dict = nfl_live_game_instance.to_dict()
# create an instance of NFLLiveGame from a dict
nfl_live_game_from_dict = NFLLiveGame.from_dict(nfl_live_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


