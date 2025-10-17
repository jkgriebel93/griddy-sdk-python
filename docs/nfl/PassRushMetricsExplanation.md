# PassRushMetricsExplanation

Explanation of pass rush metrics and calculations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pass_rush_rating** | [**PassRushMetricsExplanationPassRushRating**](PassRushMetricsExplanationPassRushRating.md) |  | [optional] 
**pressure_rate** | [**DefensiveOverviewMetricsExplanationPressureRate**](DefensiveOverviewMetricsExplanationPressureRate.md) |  | [optional] 
**time_to_sack** | [**PassRushMetricsExplanationTimeToSack**](PassRushMetricsExplanationTimeToSack.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.pass_rush_metrics_explanation import PassRushMetricsExplanation

# TODO update the JSON string below
json = "{}"
# create an instance of PassRushMetricsExplanation from a JSON string
pass_rush_metrics_explanation_instance = PassRushMetricsExplanation.from_json(json)
# print the JSON string representation of the object
print(PassRushMetricsExplanation.to_json())

# convert the object into a dict
pass_rush_metrics_explanation_dict = pass_rush_metrics_explanation_instance.to_dict()
# create an instance of PassRushMetricsExplanation from a dict
pass_rush_metrics_explanation_from_dict = PassRushMetricsExplanation.from_dict(pass_rush_metrics_explanation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


