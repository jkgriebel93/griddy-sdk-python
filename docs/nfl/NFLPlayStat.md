# NFLPlayStat


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
from nfl.models.nfl_play_stat import NFLPlayStat

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPlayStat from a JSON string
nfl_play_stat_instance = NFLPlayStat.from_json(json)
# print the JSON string representation of the object
print(NFLPlayStat.to_json())

# convert the object into a dict
nfl_play_stat_dict = nfl_play_stat_instance.to_dict()
# create an instance of NFLPlayStat from a dict
nfl_play_stat_from_dict = NFLPlayStat.from_dict(nfl_play_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


