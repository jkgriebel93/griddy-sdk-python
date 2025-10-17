# NFLStandingsResponseWeeksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**standings** | [**List[NFLNFLStandings]**](NFLStandings.md) |  | [optional] 
**week** | **int** |  | [optional] 

## Example

```python
from nfl.models.nfl_standings_response_weeks_inner import NFLStandingsResponseWeeksInner

# TODO update the JSON string below
json = "{}"
# create an instance of NFLStandingsResponseWeeksInner from a JSON string
nfl_standings_response_weeks_inner_instance = NFLStandingsResponseWeeksInner.from_json(json)
# print the JSON string representation of the object
print(NFLStandingsResponseWeeksInner.to_json())

# convert the object into a dict
nfl_standings_response_weeks_inner_dict = nfl_standings_response_weeks_inner_instance.to_dict()
# create an instance of NFLStandingsResponseWeeksInner from a dict
nfl_standings_response_weeks_inner_from_dict = NFLStandingsResponseWeeksInner.from_dict(nfl_standings_response_weeks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


