# NFLPlayerStatsResponsePlayersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | [**NFLNFLPlayer**](NFLPlayer.md) |  | [optional] 
**stats** | **object** | Statistics object varies by category | [optional] 
**team** | [**NFLNFLTeam**](NFLTeam.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_player_stats_response_players_inner import NFLPlayerStatsResponsePlayersInner

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPlayerStatsResponsePlayersInner from a JSON string
nfl_player_stats_response_players_inner_instance = NFLPlayerStatsResponsePlayersInner.from_json(json)
# print the JSON string representation of the object
print(NFLPlayerStatsResponsePlayersInner.to_json())

# convert the object into a dict
nfl_player_stats_response_players_inner_dict = nfl_player_stats_response_players_inner_instance.to_dict()
# create an instance of NFLPlayerStatsResponsePlayersInner from a dict
nfl_player_stats_response_players_inner_from_dict = NFLPlayerStatsResponsePlayersInner.from_dict(nfl_player_stats_response_players_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


