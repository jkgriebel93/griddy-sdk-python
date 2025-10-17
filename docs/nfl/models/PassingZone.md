# PassingZone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**line_of_scrimmage_distance** | [**LineOfScrimmageDistanceEnum**](LineOfScrimmageDistanceEnum.md) |  | [optional] 
**section** | [**PassingSectionEnum**](PassingSectionEnum.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.passing_zone import PassingZone

# TODO update the JSON string below
json = "{}"
# create an instance of PassingZone from a JSON string
passing_zone_instance = PassingZone.from_json(json)
# print the JSON string representation of the object
print(PassingZone.to_json())

# convert the object into a dict
passing_zone_dict = passing_zone_instance.to_dict()
# create an instance of PassingZone from a dict
passing_zone_from_dict = PassingZone.from_dict(passing_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


