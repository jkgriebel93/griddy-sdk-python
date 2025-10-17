# NFLGamecenterResponseReceivers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home** | [**List[NFLNFLReceiverStats]**](NFLReceiverStats.md) |  | [optional] 
**league_average_receiver_separation** | [**NFLNFLGamecenterResponseReceiversLeagueAverageReceiverSeparation**](NFLGamecenterResponseReceiversLeagueAverageReceiverSeparation.md) |  | [optional] 
**visitor** | [**List[NFLNFLReceiverStats]**](NFLReceiverStats.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_gamecenter_response_receivers import NFLGamecenterResponseReceivers

# TODO update the JSON string below
json = "{}"
# create an instance of NFLGamecenterResponseReceivers from a JSON string
nfl_gamecenter_response_receivers_instance = NFLGamecenterResponseReceivers.from_json(json)
# print the JSON string representation of the object
print(NFLGamecenterResponseReceivers.to_json())

# convert the object into a dict
nfl_gamecenter_response_receivers_dict = nfl_gamecenter_response_receivers_instance.to_dict()
# create an instance of NFLGamecenterResponseReceivers from a dict
nfl_gamecenter_response_receivers_from_dict = NFLGamecenterResponseReceivers.from_dict(nfl_gamecenter_response_receivers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


