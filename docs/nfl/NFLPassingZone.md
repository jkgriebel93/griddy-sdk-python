# NFLPassingZone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**line_of_scrimmage_distance** | [**NFLNFLLineOfScrimmageDistanceEnum**](NFLLineOfScrimmageDistanceEnum.md) |  | [optional] 
**section** | [**NFLNFLPassingSectionEnum**](NFLPassingSectionEnum.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_passing_zone import NFLPassingZone

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPassingZone from a JSON string
nfl_passing_zone_instance = NFLPassingZone.from_json(json)
# print the JSON string representation of the object
print(NFLPassingZone.to_json())

# convert the object into a dict
nfl_passing_zone_dict = nfl_passing_zone_instance.to_dict()
# create an instance of NFLPassingZone from a dict
nfl_passing_zone_from_dict = NFLPassingZone.from_dict(nfl_passing_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


