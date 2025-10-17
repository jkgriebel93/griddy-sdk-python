# NFLTeamInjuryReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**injuries** | [**List[NFLNFLInjuryEntry]**](NFLInjuryEntry.md) |  | [optional] 
**last_updated** | **datetime** |  | [optional] 
**team** | [**NFLNFLTeam**](NFLTeam.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_team_injury_report import NFLTeamInjuryReport

# TODO update the JSON string below
json = "{}"
# create an instance of NFLTeamInjuryReport from a JSON string
nfl_team_injury_report_instance = NFLTeamInjuryReport.from_json(json)
# print the JSON string representation of the object
print(NFLTeamInjuryReport.to_json())

# convert the object into a dict
nfl_team_injury_report_dict = nfl_team_injury_report_instance.to_dict()
# create an instance of NFLTeamInjuryReport from a dict
nfl_team_injury_report_from_dict = NFLTeamInjuryReport.from_dict(nfl_team_injury_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


