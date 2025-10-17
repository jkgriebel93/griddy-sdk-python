# DeviceInfo

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
from src.griddy.nfl.models.device_info import DeviceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInfo from a JSON string
device_info_instance = DeviceInfo.from_json(json)
# print the JSON string representation of the object
print(DeviceInfo.to_json())

# convert the object into a dict
device_info_dict = device_info_instance.to_dict()
# create an instance of DeviceInfo from a dict
device_info_from_dict = DeviceInfo.from_dict(device_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


