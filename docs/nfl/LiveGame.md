# LiveGame

Live game scoring and status information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away_team** | [**LiveGameAwayTeam**](LiveGameAwayTeam.md) |  | [optional] 
**game_id** | **str** | Game identifier | [optional] 
**home_team** | [**LiveGameAwayTeam**](LiveGameAwayTeam.md) |  | [optional] 
**last_play** | **str** | Description of last play | [optional] 
**possession** | **str** | Team abbreviation with current possession | [optional] 
**quarter** | **str** | Current quarter/period | [optional] 
**red_zone** | **bool** | Whether team is in red zone | [optional] 
**status** | [**GameStatusEnum**](GameStatusEnum.md) |  | [optional] 
**time_remaining** | **str** | Time remaining in current period | [optional] 

## Example

```python
from src.griddy.nfl.models.live_game import LiveGame

# TODO update the JSON string below
json = "{}"
# create an instance of LiveGame from a JSON string
live_game_instance = LiveGame.from_json(json)
# print the JSON string representation of the object
print(LiveGame.to_json())

# convert the object into a dict
live_game_dict = live_game_instance.to_dict()
# create an instance of LiveGame from a dict
live_game_from_dict = LiveGame.from_dict(live_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


