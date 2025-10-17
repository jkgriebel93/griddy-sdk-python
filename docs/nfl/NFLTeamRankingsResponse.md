# NFLTeamRankingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away_rankings** | [**NFLNFLTeamRankings**](NFLTeamRankings.md) |  | [optional] 
**home_rankings** | [**NFLNFLTeamRankings**](NFLTeamRankings.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_team_rankings_response import NFLTeamRankingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLTeamRankingsResponse from a JSON string
nfl_team_rankings_response_instance = NFLTeamRankingsResponse.from_json(json)
# print the JSON string representation of the object
print(NFLTeamRankingsResponse.to_json())

# convert the object into a dict
nfl_team_rankings_response_dict = nfl_team_rankings_response_instance.to_dict()
# create an instance of NFLTeamRankingsResponse from a dict
nfl_team_rankings_response_from_dict = NFLTeamRankingsResponse.from_dict(nfl_team_rankings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


