# StandingsRecordAllOfPoints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**against** | **int** | Points allowed | [optional] 
**var_for** | **int** | Points scored | [optional] 

## Example

```python
from src.griddy.nfl.models.standings_record_all_of_points import StandingsRecordAllOfPoints

# TODO update the JSON string below
json = "{}"
# create an instance of StandingsRecordAllOfPoints from a JSON string
standings_record_all_of_points_instance = StandingsRecordAllOfPoints.from_json(json)
# print the JSON string representation of the object
print(StandingsRecordAllOfPoints.to_json())

# convert the object into a dict
standings_record_all_of_points_dict = standings_record_all_of_points_instance.to_dict()
# create an instance of StandingsRecordAllOfPoints from a dict
standings_record_all_of_points_from_dict = StandingsRecordAllOfPoints.from_dict(standings_record_all_of_points_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


