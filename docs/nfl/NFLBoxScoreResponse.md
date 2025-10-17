# NFLBoxScoreResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game** | [**NFLNFLGame**](NFLGame.md) |  | [optional] 
**player_stats** | [**NFLNFLBoxScoreResponsePlayerStats**](NFLBoxScoreResponsePlayerStats.md) |  | [optional] 
**scoring_summary** | [**List[NFLNFLScoringPlay]**](NFLScoringPlay.md) |  | [optional] 
**team_stats** | [**NFLNFLBoxScoreResponseTeamStats**](NFLBoxScoreResponseTeamStats.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_box_score_response import NFLBoxScoreResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLBoxScoreResponse from a JSON string
nfl_box_score_response_instance = NFLBoxScoreResponse.from_json(json)
# print the JSON string representation of the object
print(NFLBoxScoreResponse.to_json())

# convert the object into a dict
nfl_box_score_response_dict = nfl_box_score_response_instance.to_dict()
# create an instance of NFLBoxScoreResponse from a dict
nfl_box_score_response_from_dict = NFLBoxScoreResponse.from_dict(nfl_box_score_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


