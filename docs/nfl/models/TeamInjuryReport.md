# TeamInjuryReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**injuries** | [**List[InjuryEntry]**](InjuryEntry.md) |  | [optional] 
**last_updated** | **datetime** |  | [optional] 
**team** | [**Team**](Team.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.team_injury_report import TeamInjuryReport

# TODO update the JSON string below
json = "{}"
# create an instance of TeamInjuryReport from a JSON string
team_injury_report_instance = TeamInjuryReport.from_json(json)
# print the JSON string representation of the object
print(TeamInjuryReport.to_json())

# convert the object into a dict
team_injury_report_dict = team_injury_report_instance.to_dict()
# create an instance of TeamInjuryReport from a dict
team_injury_report_from_dict = TeamInjuryReport.from_dict(team_injury_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


