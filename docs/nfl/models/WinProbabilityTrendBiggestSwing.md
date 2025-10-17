# WinProbabilityTrendBiggestSwing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**play** | [**PlayWinProbability**](PlayWinProbability.md) |  | [optional] 
**probability_change** | **float** | Absolute change in win probability | [optional] 

## Example

```python
from src.griddy.nfl.models.win_probability_trend_biggest_swing import WinProbabilityTrendBiggestSwing

# TODO update the JSON string below
json = "{}"
# create an instance of WinProbabilityTrendBiggestSwing from a JSON string
win_probability_trend_biggest_swing_instance = WinProbabilityTrendBiggestSwing.from_json(json)
# print the JSON string representation of the object
print(WinProbabilityTrendBiggestSwing.to_json())

# convert the object into a dict
win_probability_trend_biggest_swing_dict = win_probability_trend_biggest_swing_instance.to_dict()
# create an instance of WinProbabilityTrendBiggestSwing from a dict
win_probability_trend_biggest_swing_from_dict = WinProbabilityTrendBiggestSwing.from_dict(win_probability_trend_biggest_swing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


