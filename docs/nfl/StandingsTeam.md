# StandingsTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_logo** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.standings_team import StandingsTeam

# TODO update the JSON string below
json = "{}"
# create an instance of StandingsTeam from a JSON string
standings_team_instance = StandingsTeam.from_json(json)
# print the JSON string representation of the object
print(StandingsTeam.to_json())

# convert the object into a dict
standings_team_dict = standings_team_instance.to_dict()
# create an instance of StandingsTeam from a dict
standings_team_from_dict = StandingsTeam.from_dict(standings_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


