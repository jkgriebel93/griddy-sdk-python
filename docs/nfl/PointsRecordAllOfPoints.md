# PointsRecordAllOfPoints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**against** | **int** |  | [optional] 
**var_for** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.points_record_all_of_points import PointsRecordAllOfPoints

# TODO update the JSON string below
json = "{}"
# create an instance of PointsRecordAllOfPoints from a JSON string
points_record_all_of_points_instance = PointsRecordAllOfPoints.from_json(json)
# print the JSON string representation of the object
print(PointsRecordAllOfPoints.to_json())

# convert the object into a dict
points_record_all_of_points_dict = points_record_all_of_points_instance.to_dict()
# create an instance of PointsRecordAllOfPoints from a dict
points_record_all_of_points_from_dict = PointsRecordAllOfPoints.from_dict(points_record_all_of_points_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


