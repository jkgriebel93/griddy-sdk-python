# NFLStandingsTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_logo** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from nfl.models.nfl_standings_team import NFLStandingsTeam

# TODO update the JSON string below
json = "{}"
# create an instance of NFLStandingsTeam from a JSON string
nfl_standings_team_instance = NFLStandingsTeam.from_json(json)
# print the JSON string representation of the object
print(NFLStandingsTeam.to_json())

# convert the object into a dict
nfl_standings_team_dict = nfl_standings_team_instance.to_dict()
# create an instance of NFLStandingsTeam from a dict
nfl_standings_team_from_dict = NFLStandingsTeam.from_dict(nfl_standings_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


