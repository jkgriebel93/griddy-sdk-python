# PlayerStatsResponsePlayersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | [**Player**](Player.md) |  | [optional] 
**stats** | **object** | Statistics object varies by category | [optional] 
**team** | [**Team**](Team.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.player_stats_response_players_inner import PlayerStatsResponsePlayersInner

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerStatsResponsePlayersInner from a JSON string
player_stats_response_players_inner_instance = PlayerStatsResponsePlayersInner.from_json(json)
# print the JSON string representation of the object
print(PlayerStatsResponsePlayersInner.to_json())

# convert the object into a dict
player_stats_response_players_inner_dict = player_stats_response_players_inner_instance.to_dict()
# create an instance of PlayerStatsResponsePlayersInner from a dict
player_stats_response_players_inner_from_dict = PlayerStatsResponsePlayersInner.from_dict(player_stats_response_players_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


