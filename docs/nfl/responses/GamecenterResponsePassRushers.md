# GamecenterResponsePassRushers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home** | [**List[PassRusherStats]**](PassRusherStats.md) |  | [optional] 
**league_average_separation_to_qb** | [**GamecenterResponsePassRushersLeagueAverageSeparationToQb**](GamecenterResponsePassRushersLeagueAverageSeparationToQb.md) |  | [optional] 
**visitor** | [**List[PassRusherStats]**](PassRusherStats.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.gamecenter_response_pass_rushers import GamecenterResponsePassRushers

# TODO update the JSON string below
json = "{}"
# create an instance of GamecenterResponsePassRushers from a JSON string
gamecenter_response_pass_rushers_instance = GamecenterResponsePassRushers.from_json(json)
# print the JSON string representation of the object
print(GamecenterResponsePassRushers.to_json())

# convert the object into a dict
gamecenter_response_pass_rushers_dict = gamecenter_response_pass_rushers_instance.to_dict()
# create an instance of GamecenterResponsePassRushers from a dict
gamecenter_response_pass_rushers_from_dict = GamecenterResponsePassRushers.from_dict(gamecenter_response_pass_rushers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


