# NFLPlaySummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away** | [**List[NFLNFLParticipantPlayerInfo]**](NFLParticipantPlayerInfo.md) | Away team players involved in the play | [optional] 
**game_id** | **int** | Game identifier in integer format | [optional] 
**game_key** | **int** | Unique game key | [optional] 
**gsis_play_id** | **int** | GSIS play identifier | [optional] 
**home** | [**List[NFLNFLParticipantPlayerInfo]**](NFLParticipantPlayerInfo.md) | Home team players involved in the play | [optional] 
**home_is_offense** | **bool** | Whether home team has offensive possession | [optional] 
**play** | [**NFLNFLPlayDetail**](NFLPlayDetail.md) |  | [optional] 
**play_id** | **int** | Play identifier | [optional] 
**schedule** | [**NFLNFLGameSchedule**](NFLGameSchedule.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_play_summary_response import NFLPlaySummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPlaySummaryResponse from a JSON string
nfl_play_summary_response_instance = NFLPlaySummaryResponse.from_json(json)
# print the JSON string representation of the object
print(NFLPlaySummaryResponse.to_json())

# convert the object into a dict
nfl_play_summary_response_dict = nfl_play_summary_response_instance.to_dict()
# create an instance of NFLPlaySummaryResponse from a dict
nfl_play_summary_response_from_dict = NFLPlaySummaryResponse.from_dict(nfl_play_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


