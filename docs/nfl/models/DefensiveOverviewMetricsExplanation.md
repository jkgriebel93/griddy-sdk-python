# DefensiveOverviewMetricsExplanation

Explanation of defensive overview metrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hard_stops** | [**DefensiveOverviewMetricsExplanationHardStops**](DefensiveOverviewMetricsExplanationHardStops.md) |  | [optional] 
**pressure_rate** | [**DefensiveOverviewMetricsExplanationPressureRate**](DefensiveOverviewMetricsExplanationPressureRate.md) |  | [optional] 
**tackle_stops** | [**DefensiveOverviewMetricsExplanationTackleStops**](DefensiveOverviewMetricsExplanationTackleStops.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.defensive_overview_metrics_explanation import DefensiveOverviewMetricsExplanation

# TODO update the JSON string below
json = "{}"
# create an instance of DefensiveOverviewMetricsExplanation from a JSON string
defensive_overview_metrics_explanation_instance = DefensiveOverviewMetricsExplanation.from_json(json)
# print the JSON string representation of the object
print(DefensiveOverviewMetricsExplanation.to_json())

# convert the object into a dict
defensive_overview_metrics_explanation_dict = defensive_overview_metrics_explanation_instance.to_dict()
# create an instance of DefensiveOverviewMetricsExplanation from a dict
defensive_overview_metrics_explanation_from_dict = DefensiveOverviewMetricsExplanation.from_dict(defensive_overview_metrics_explanation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


