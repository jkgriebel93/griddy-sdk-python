# NFLTeamRankingEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank** | **int** | Team&#39;s rank (1-32) | [optional] 
**stats** | **float** | Statistical value | [optional] 
**team_id** | **str** |  | [optional] 

## Example

```python
from nfl.models.nfl_team_ranking_entry import NFLTeamRankingEntry

# TODO update the JSON string below
json = "{}"
# create an instance of NFLTeamRankingEntry from a JSON string
nfl_team_ranking_entry_instance = NFLTeamRankingEntry.from_json(json)
# print the JSON string representation of the object
print(NFLTeamRankingEntry.to_json())

# convert the object into a dict
nfl_team_ranking_entry_dict = nfl_team_ranking_entry_instance.to_dict()
# create an instance of NFLTeamRankingEntry from a dict
nfl_team_ranking_entry_from_dict = NFLTeamRankingEntry.from_dict(nfl_team_ranking_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


