# PlayStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_code** | **str** | Team abbreviation | [optional] 
**gsis_id** | **str** | Player GSIS ID | [optional] 
**play_id** | **int** |  | [optional] 
**player_name** | **str** | Player name | [optional] 
**stat_id** | **int** | Type of statistic | [optional] 
**yards** | **int** | Yards gained/lost | [optional] 

## Example

```python
from src.griddy.nfl.models.play_stat import PlayStat

# TODO update the JSON string below
json = "{}"
# create an instance of PlayStat from a JSON string
play_stat_instance = PlayStat.from_json(json)
# print the JSON string representation of the object
print(PlayStat.to_json())

# convert the object into a dict
play_stat_dict = play_stat_instance.to_dict()
# create an instance of PlayStat from a dict
play_stat_from_dict = PlayStat.from_dict(play_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


