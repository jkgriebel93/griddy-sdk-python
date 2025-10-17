# WinProbabilityTrend

Win probability trend analysis

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**biggest_swing** | [**WinProbabilityTrendBiggestSwing**](WinProbabilityTrendBiggestSwing.md) |  | [optional] 
**final_probability** | [**WinProbabilityTrendFinalProbability**](WinProbabilityTrendFinalProbability.md) |  | [optional] 
**turning_points** | [**List[PlayWinProbability]**](PlayWinProbability.md) | Key plays that significantly changed win probability | [optional] 

## Example

```python
from src.griddy.nfl.models.win_probability_trend import WinProbabilityTrend

# TODO update the JSON string below
json = "{}"
# create an instance of WinProbabilityTrend from a JSON string
win_probability_trend_instance = WinProbabilityTrend.from_json(json)
# print the JSON string representation of the object
print(WinProbabilityTrend.to_json())

# convert the object into a dict
win_probability_trend_dict = win_probability_trend_instance.to_dict()
# create an instance of WinProbabilityTrend from a dict
win_probability_trend_from_dict = WinProbabilityTrend.from_dict(win_probability_trend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


