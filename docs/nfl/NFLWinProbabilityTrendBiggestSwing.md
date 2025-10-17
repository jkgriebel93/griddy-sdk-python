# NFLWinProbabilityTrendBiggestSwing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**play** | [**NFLNFLPlayWinProbability**](NFLPlayWinProbability.md) |  | [optional] 
**probability_change** | **float** | Absolute change in win probability | [optional] 

## Example

```python
from nfl.models.nfl_win_probability_trend_biggest_swing import NFLWinProbabilityTrendBiggestSwing

# TODO update the JSON string below
json = "{}"
# create an instance of NFLWinProbabilityTrendBiggestSwing from a JSON string
nfl_win_probability_trend_biggest_swing_instance = NFLWinProbabilityTrendBiggestSwing.from_json(json)
# print the JSON string representation of the object
print(NFLWinProbabilityTrendBiggestSwing.to_json())

# convert the object into a dict
nfl_win_probability_trend_biggest_swing_dict = nfl_win_probability_trend_biggest_swing_instance.to_dict()
# create an instance of NFLWinProbabilityTrendBiggestSwing from a dict
nfl_win_probability_trend_biggest_swing_from_dict = NFLWinProbabilityTrendBiggestSwing.from_dict(nfl_win_probability_trend_biggest_swing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


