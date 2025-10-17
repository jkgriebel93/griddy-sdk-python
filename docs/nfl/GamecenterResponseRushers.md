# GamecenterResponseRushers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home** | [**List[RusherStats]**](RusherStats.md) |  | [optional] 
**visitor** | [**List[RusherStats]**](RusherStats.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.gamecenter_response_rushers import GamecenterResponseRushers

# TODO update the JSON string below
json = "{}"
# create an instance of GamecenterResponseRushers from a JSON string
gamecenter_response_rushers_instance = GamecenterResponseRushers.from_json(json)
# print the JSON string representation of the object
print(GamecenterResponseRushers.to_json())

# convert the object into a dict
gamecenter_response_rushers_dict = gamecenter_response_rushers_instance.to_dict()
# create an instance of GamecenterResponseRushers from a dict
gamecenter_response_rushers_from_dict = GamecenterResponseRushers.from_dict(gamecenter_response_rushers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


