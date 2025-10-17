# MatchupRankingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **int** |  | [optional] 
**game_key** | **int** |  | [optional] 
**home_team_matchup_rankings** | [**TeamMatchupRankings**](TeamMatchupRankings.md) |  | [optional] 
**season** | **int** |  | [optional] 
**season_type** | [**SeasonTypeEnum**](SeasonTypeEnum.md) |  | [optional] 
**visitor_team_matchup_rankings** | [**TeamMatchupRankings**](TeamMatchupRankings.md) |  | [optional] 
**week** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.matchup_rankings_response import MatchupRankingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MatchupRankingsResponse from a JSON string
matchup_rankings_response_instance = MatchupRankingsResponse.from_json(json)
# print the JSON string representation of the object
print(MatchupRankingsResponse.to_json())

# convert the object into a dict
matchup_rankings_response_dict = matchup_rankings_response_instance.to_dict()
# create an instance of MatchupRankingsResponse from a dict
matchup_rankings_response_from_dict = MatchupRankingsResponse.from_dict(matchup_rankings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


