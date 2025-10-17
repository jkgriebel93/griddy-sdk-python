# NFLWinProbabilityMetrics

Explanation of win probability metrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**critical_plays** | **str** | Plays with high absolute WPA values (typically &gt; 0.10) are considered critical or momentum-shifting plays that significantly impact the game outcome. | [optional] 
**win_probability** | **str** | Probability (0-1) that a team will win the game at any given point. 1.0 &#x3D; 100% chance of winning, 0.0 &#x3D; 0% chance of winning. | [optional] 
**win_probability_added** | **str** | Change in win probability caused by a single play. Positive WPA means the play helped the team&#39;s chances of winning. Negative WPA means the play hurt the team&#39;s chances of winning. The sum of all WPA values for both teams in a game equals zero. | [optional] 

## Example

```python
from nfl.models.nfl_win_probability_metrics import NFLWinProbabilityMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of NFLWinProbabilityMetrics from a JSON string
nfl_win_probability_metrics_instance = NFLWinProbabilityMetrics.from_json(json)
# print the JSON string representation of the object
print(NFLWinProbabilityMetrics.to_json())

# convert the object into a dict
nfl_win_probability_metrics_dict = nfl_win_probability_metrics_instance.to_dict()
# create an instance of NFLWinProbabilityMetrics from a dict
nfl_win_probability_metrics_from_dict = NFLWinProbabilityMetrics.from_dict(nfl_win_probability_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


