# PlaySummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away** | [**List[ParticipantPlayerInfo]**](ParticipantPlayerInfo.md) | Away team players involved in the play | [optional] 
**game_id** | **int** | Game identifier in integer format | [optional] 
**game_key** | **int** | Unique game key | [optional] 
**gsis_play_id** | **int** | GSIS play identifier | [optional] 
**home** | [**List[ParticipantPlayerInfo]**](ParticipantPlayerInfo.md) | Home team players involved in the play | [optional] 
**home_is_offense** | **bool** | Whether home team has offensive possession | [optional] 
**play** | [**PlayDetail**](PlayDetail.md) |  | [optional] 
**play_id** | **int** | Play identifier | [optional] 
**schedule** | [**GameSchedule**](GameSchedule.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.play_summary_response import PlaySummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlaySummaryResponse from a JSON string
play_summary_response_instance = PlaySummaryResponse.from_json(json)
# print the JSON string representation of the object
print(PlaySummaryResponse.to_json())

# convert the object into a dict
play_summary_response_dict = play_summary_response_instance.to_dict()
# create an instance of PlaySummaryResponse from a dict
play_summary_response_from_dict = PlaySummaryResponse.from_dict(play_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


