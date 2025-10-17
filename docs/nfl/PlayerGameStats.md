# PlayerGameStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defensive** | [**DefensiveStats**](DefensiveStats.md) |  | [optional] 
**kicking** | [**KickingStats**](KickingStats.md) |  | [optional] 
**passing** | [**PassingStats**](PassingStats.md) |  | [optional] 
**player** | [**Player**](Player.md) |  | [optional] 
**receiving** | [**ReceivingStats**](ReceivingStats.md) |  | [optional] 
**rushing** | [**RushingStats**](RushingStats.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.player_game_stats import PlayerGameStats

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerGameStats from a JSON string
player_game_stats_instance = PlayerGameStats.from_json(json)
# print the JSON string representation of the object
print(PlayerGameStats.to_json())

# convert the object into a dict
player_game_stats_dict = player_game_stats_instance.to_dict()
# create an instance of PlayerGameStats from a dict
player_game_stats_from_dict = PlayerGameStats.from_dict(player_game_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


