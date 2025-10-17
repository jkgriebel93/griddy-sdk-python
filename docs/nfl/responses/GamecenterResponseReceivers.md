# GamecenterResponseReceivers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home** | [**List[ReceiverStats]**](ReceiverStats.md) |  | [optional] 
**league_average_receiver_separation** | [**GamecenterResponseReceiversLeagueAverageReceiverSeparation**](GamecenterResponseReceiversLeagueAverageReceiverSeparation.md) |  | [optional] 
**visitor** | [**List[ReceiverStats]**](ReceiverStats.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.gamecenter_response_receivers import GamecenterResponseReceivers

# TODO update the JSON string below
json = "{}"
# create an instance of GamecenterResponseReceivers from a JSON string
gamecenter_response_receivers_instance = GamecenterResponseReceivers.from_json(json)
# print the JSON string representation of the object
print(GamecenterResponseReceivers.to_json())

# convert the object into a dict
gamecenter_response_receivers_dict = gamecenter_response_receivers_instance.to_dict()
# create an instance of GamecenterResponseReceivers from a dict
gamecenter_response_receivers_from_dict = GamecenterResponseReceivers.from_dict(gamecenter_response_receivers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


