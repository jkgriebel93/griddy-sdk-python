# NFLDefensiveOverviewMetricsExplanation

Explanation of defensive overview metrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hard_stops** | [**NFLNFLDefensiveOverviewMetricsExplanationHardStops**](NFLDefensiveOverviewMetricsExplanationHardStops.md) |  | [optional] 
**pressure_rate** | [**NFLNFLDefensiveOverviewMetricsExplanationPressureRate**](NFLDefensiveOverviewMetricsExplanationPressureRate.md) |  | [optional] 
**tackle_stops** | [**NFLNFLDefensiveOverviewMetricsExplanationTackleStops**](NFLDefensiveOverviewMetricsExplanationTackleStops.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_defensive_overview_metrics_explanation import NFLDefensiveOverviewMetricsExplanation

# TODO update the JSON string below
json = "{}"
# create an instance of NFLDefensiveOverviewMetricsExplanation from a JSON string
nfl_defensive_overview_metrics_explanation_instance = NFLDefensiveOverviewMetricsExplanation.from_json(json)
# print the JSON string representation of the object
print(NFLDefensiveOverviewMetricsExplanation.to_json())

# convert the object into a dict
nfl_defensive_overview_metrics_explanation_dict = nfl_defensive_overview_metrics_explanation_instance.to_dict()
# create an instance of NFLDefensiveOverviewMetricsExplanation from a dict
nfl_defensive_overview_metrics_explanation_from_dict = NFLDefensiveOverviewMetricsExplanation.from_dict(nfl_defensive_overview_metrics_explanation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


