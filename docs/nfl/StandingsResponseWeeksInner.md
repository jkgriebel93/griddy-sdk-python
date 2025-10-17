# StandingsResponseWeeksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**standings** | [**List[Standings]**](Standings.md) |  | [optional] 
**week** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.standings_response_weeks_inner import StandingsResponseWeeksInner

# TODO update the JSON string below
json = "{}"
# create an instance of StandingsResponseWeeksInner from a JSON string
standings_response_weeks_inner_instance = StandingsResponseWeeksInner.from_json(json)
# print the JSON string representation of the object
print(StandingsResponseWeeksInner.to_json())

# convert the object into a dict
standings_response_weeks_inner_dict = standings_response_weeks_inner_instance.to_dict()
# create an instance of StandingsResponseWeeksInner from a dict
standings_response_weeks_inner_from_dict = StandingsResponseWeeksInner.from_dict(standings_response_weeks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


