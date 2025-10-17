# NFLDeviceInfo

Device information object (normally base64 encoded in requests)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | Device model or form factor | [optional] 
**os_name** | **str** | Operating system name | [optional] 
**os_version** | **str** | Operating system version | [optional] 
**version** | **str** | Browser or application version | [optional] 

## Example

```python
from nfl.models.nfl_device_info import NFLDeviceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NFLDeviceInfo from a JSON string
nfl_device_info_instance = NFLDeviceInfo.from_json(json)
# print the JSON string representation of the object
print(NFLDeviceInfo.to_json())

# convert the object into a dict
nfl_device_info_dict = nfl_device_info_instance.to_dict()
# create an instance of NFLDeviceInfo from a dict
nfl_device_info_from_dict = NFLDeviceInfo.from_dict(nfl_device_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


