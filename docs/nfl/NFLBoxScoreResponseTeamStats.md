# NFLBoxScoreResponseTeamStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away** | [**NFLNFLTeamGameStats**](NFLTeamGameStats.md) |  | [optional] 
**home** | [**NFLNFLTeamGameStats**](NFLTeamGameStats.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_box_score_response_team_stats import NFLBoxScoreResponseTeamStats

# TODO update the JSON string below
json = "{}"
# create an instance of NFLBoxScoreResponseTeamStats from a JSON string
nfl_box_score_response_team_stats_instance = NFLBoxScoreResponseTeamStats.from_json(json)
# print the JSON string representation of the object
print(NFLBoxScoreResponseTeamStats.to_json())

# convert the object into a dict
nfl_box_score_response_team_stats_dict = nfl_box_score_response_team_stats_instance.to_dict()
# create an instance of NFLBoxScoreResponseTeamStats from a dict
nfl_box_score_response_team_stats_from_dict = NFLBoxScoreResponseTeamStats.from_dict(nfl_box_score_response_team_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


