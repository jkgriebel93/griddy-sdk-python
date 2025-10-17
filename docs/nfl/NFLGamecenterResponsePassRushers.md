# NFLGamecenterResponsePassRushers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home** | [**List[NFLNFLPassRusherStats]**](NFLPassRusherStats.md) |  | [optional] 
**league_average_separation_to_qb** | [**NFLNFLGamecenterResponsePassRushersLeagueAverageSeparationToQb**](NFLGamecenterResponsePassRushersLeagueAverageSeparationToQb.md) |  | [optional] 
**visitor** | [**List[NFLNFLPassRusherStats]**](NFLPassRusherStats.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_gamecenter_response_pass_rushers import NFLGamecenterResponsePassRushers

# TODO update the JSON string below
json = "{}"
# create an instance of NFLGamecenterResponsePassRushers from a JSON string
nfl_gamecenter_response_pass_rushers_instance = NFLGamecenterResponsePassRushers.from_json(json)
# print the JSON string representation of the object
print(NFLGamecenterResponsePassRushers.to_json())

# convert the object into a dict
nfl_gamecenter_response_pass_rushers_dict = nfl_gamecenter_response_pass_rushers_instance.to_dict()
# create an instance of NFLGamecenterResponsePassRushers from a dict
nfl_gamecenter_response_pass_rushers_from_dict = NFLGamecenterResponsePassRushers.from_dict(nfl_gamecenter_response_pass_rushers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


