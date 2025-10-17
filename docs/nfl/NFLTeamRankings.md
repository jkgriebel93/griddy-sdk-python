# NFLTeamRankings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | [optional] 
**season_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 
**statistics** | [**List[NFLNFLStatisticRanking]**](NFLStatisticRanking.md) |  | [optional] 
**team_id** | **str** |  | [optional] 

## Example

```python
from nfl.models.nfl_team_rankings import NFLTeamRankings

# TODO update the JSON string below
json = "{}"
# create an instance of NFLTeamRankings from a JSON string
nfl_team_rankings_instance = NFLTeamRankings.from_json(json)
# print the JSON string representation of the object
print(NFLTeamRankings.to_json())

# convert the object into a dict
nfl_team_rankings_dict = nfl_team_rankings_instance.to_dict()
# create an instance of NFLTeamRankings from a dict
nfl_team_rankings_from_dict = NFLTeamRankings.from_dict(nfl_team_rankings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


