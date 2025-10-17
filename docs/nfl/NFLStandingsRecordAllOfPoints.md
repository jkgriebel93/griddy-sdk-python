# NFLStandingsRecordAllOfPoints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**against** | **int** | Points allowed | [optional] 
**var_for** | **int** | Points scored | [optional] 

## Example

```python
from nfl.models.nfl_standings_record_all_of_points import NFLStandingsRecordAllOfPoints

# TODO update the JSON string below
json = "{}"
# create an instance of NFLStandingsRecordAllOfPoints from a JSON string
nfl_standings_record_all_of_points_instance = NFLStandingsRecordAllOfPoints.from_json(json)
# print the JSON string representation of the object
print(NFLStandingsRecordAllOfPoints.to_json())

# convert the object into a dict
nfl_standings_record_all_of_points_dict = nfl_standings_record_all_of_points_instance.to_dict()
# create an instance of NFLStandingsRecordAllOfPoints from a dict
nfl_standings_record_all_of_points_from_dict = NFLStandingsRecordAllOfPoints.from_dict(nfl_standings_record_all_of_points_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


