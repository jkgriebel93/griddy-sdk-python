# NFLMatchupRankingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **int** |  | [optional] 
**game_key** | **int** |  | [optional] 
**home_team_matchup_rankings** | [**NFLNFLTeamMatchupRankings**](NFLTeamMatchupRankings.md) |  | [optional] 
**season** | **int** |  | [optional] 
**season_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 
**visitor_team_matchup_rankings** | [**NFLNFLTeamMatchupRankings**](NFLTeamMatchupRankings.md) |  | [optional] 
**week** | **int** |  | [optional] 

## Example

```python
from nfl.models.nfl_matchup_rankings_response import NFLMatchupRankingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLMatchupRankingsResponse from a JSON string
nfl_matchup_rankings_response_instance = NFLMatchupRankingsResponse.from_json(json)
# print the JSON string representation of the object
print(NFLMatchupRankingsResponse.to_json())

# convert the object into a dict
nfl_matchup_rankings_response_dict = nfl_matchup_rankings_response_instance.to_dict()
# create an instance of NFLMatchupRankingsResponse from a dict
nfl_matchup_rankings_response_from_dict = NFLMatchupRankingsResponse.from_dict(nfl_matchup_rankings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


