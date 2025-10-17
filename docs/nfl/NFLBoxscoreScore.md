# NFLBoxscoreScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home_team_score** | [**NFLNFLTeamScore**](NFLTeamScore.md) |  | [optional] 
**phase** | **str** | Game phase (P&#x3D;Pregame, 1-4&#x3D;Quarter, F&#x3D;Final) | [optional] 
**visitor_team_score** | [**NFLNFLTeamScore**](NFLTeamScore.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_boxscore_score import NFLBoxscoreScore

# TODO update the JSON string below
json = "{}"
# create an instance of NFLBoxscoreScore from a JSON string
nfl_boxscore_score_instance = NFLBoxscoreScore.from_json(json)
# print the JSON string representation of the object
print(NFLBoxscoreScore.to_json())

# convert the object into a dict
nfl_boxscore_score_dict = nfl_boxscore_score_instance.to_dict()
# create an instance of NFLBoxscoreScore from a dict
nfl_boxscore_score_from_dict = NFLBoxscoreScore.from_dict(nfl_boxscore_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


