# NFLPlayerGameStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defensive** | [**NFLNFLDefensiveStats**](NFLDefensiveStats.md) |  | [optional] 
**kicking** | [**NFLNFLKickingStats**](NFLKickingStats.md) |  | [optional] 
**passing** | [**NFLNFLPassingStats**](NFLPassingStats.md) |  | [optional] 
**player** | [**NFLNFLPlayer**](NFLPlayer.md) |  | [optional] 
**receiving** | [**NFLNFLReceivingStats**](NFLReceivingStats.md) |  | [optional] 
**rushing** | [**NFLNFLRushingStats**](NFLRushingStats.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_player_game_stats import NFLPlayerGameStats

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPlayerGameStats from a JSON string
nfl_player_game_stats_instance = NFLPlayerGameStats.from_json(json)
# print the JSON string representation of the object
print(NFLPlayerGameStats.to_json())

# convert the object into a dict
nfl_player_game_stats_dict = nfl_player_game_stats_instance.to_dict()
# create an instance of NFLPlayerGameStats from a dict
nfl_player_game_stats_from_dict = NFLPlayerGameStats.from_dict(nfl_player_game_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


