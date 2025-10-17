# TeamRankingEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank** | **int** | Team&#39;s rank (1-32) | [optional] 
**stats** | **float** | Statistical value | [optional] 
**team_id** | **str** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.team_ranking_entry import TeamRankingEntry

# TODO update the JSON string below
json = "{}"
# create an instance of TeamRankingEntry from a JSON string
team_ranking_entry_instance = TeamRankingEntry.from_json(json)
# print the JSON string representation of the object
print(TeamRankingEntry.to_json())

# convert the object into a dict
team_ranking_entry_dict = team_ranking_entry_instance.to_dict()
# create an instance of TeamRankingEntry from a dict
team_ranking_entry_from_dict = TeamRankingEntry.from_dict(team_ranking_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


