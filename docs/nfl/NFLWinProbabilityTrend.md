# NFLWinProbabilityTrend

Win probability trend analysis

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**biggest_swing** | [**NFLNFLWinProbabilityTrendBiggestSwing**](NFLWinProbabilityTrendBiggestSwing.md) |  | [optional] 
**final_probability** | [**NFLNFLWinProbabilityTrendFinalProbability**](NFLWinProbabilityTrendFinalProbability.md) |  | [optional] 
**turning_points** | [**List[NFLNFLPlayWinProbability]**](NFLPlayWinProbability.md) | Key plays that significantly changed win probability | [optional] 

## Example

```python
from nfl.models.nfl_win_probability_trend import NFLWinProbabilityTrend

# TODO update the JSON string below
json = "{}"
# create an instance of NFLWinProbabilityTrend from a JSON string
nfl_win_probability_trend_instance = NFLWinProbabilityTrend.from_json(json)
# print the JSON string representation of the object
print(NFLWinProbabilityTrend.to_json())

# convert the object into a dict
nfl_win_probability_trend_dict = nfl_win_probability_trend_instance.to_dict()
# create an instance of NFLWinProbabilityTrend from a dict
nfl_win_probability_trend_from_dict = NFLWinProbabilityTrend.from_dict(nfl_win_probability_trend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


