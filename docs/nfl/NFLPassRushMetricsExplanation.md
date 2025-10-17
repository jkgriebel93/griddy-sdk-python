# NFLPassRushMetricsExplanation

Explanation of pass rush metrics and calculations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pass_rush_rating** | [**NFLNFLPassRushMetricsExplanationPassRushRating**](NFLPassRushMetricsExplanationPassRushRating.md) |  | [optional] 
**pressure_rate** | [**NFLNFLDefensiveOverviewMetricsExplanationPressureRate**](NFLDefensiveOverviewMetricsExplanationPressureRate.md) |  | [optional] 
**time_to_sack** | [**NFLNFLPassRushMetricsExplanationTimeToSack**](NFLPassRushMetricsExplanationTimeToSack.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_pass_rush_metrics_explanation import NFLPassRushMetricsExplanation

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPassRushMetricsExplanation from a JSON string
nfl_pass_rush_metrics_explanation_instance = NFLPassRushMetricsExplanation.from_json(json)
# print the JSON string representation of the object
print(NFLPassRushMetricsExplanation.to_json())

# convert the object into a dict
nfl_pass_rush_metrics_explanation_dict = nfl_pass_rush_metrics_explanation_instance.to_dict()
# create an instance of NFLPassRushMetricsExplanation from a dict
nfl_pass_rush_metrics_explanation_from_dict = NFLPassRushMetricsExplanation.from_dict(nfl_pass_rush_metrics_explanation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


