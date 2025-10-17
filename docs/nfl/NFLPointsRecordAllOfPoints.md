# NFLPointsRecordAllOfPoints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**against** | **int** |  | [optional] 
**var_for** | **int** |  | [optional] 

## Example

```python
from nfl.models.nfl_points_record_all_of_points import NFLPointsRecordAllOfPoints

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPointsRecordAllOfPoints from a JSON string
nfl_points_record_all_of_points_instance = NFLPointsRecordAllOfPoints.from_json(json)
# print the JSON string representation of the object
print(NFLPointsRecordAllOfPoints.to_json())

# convert the object into a dict
nfl_points_record_all_of_points_dict = nfl_points_record_all_of_points_instance.to_dict()
# create an instance of NFLPointsRecordAllOfPoints from a dict
nfl_points_record_all_of_points_from_dict = NFLPointsRecordAllOfPoints.from_dict(nfl_points_record_all_of_points_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


