# DefensiveMetricsExplanation

Explanation of defensive metrics and calculations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**epa** | [**DefensiveMetricsExplanationEpa**](DefensiveMetricsExplanationEpa.md) |  | [optional] 
**qbp_pct** | [**DefensiveMetricsExplanationQbpPct**](DefensiveMetricsExplanationQbpPct.md) |  | [optional] 
**ryoe** | [**DefensiveMetricsExplanationRyoe**](DefensiveMetricsExplanationRyoe.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.defensive_metrics_explanation import DefensiveMetricsExplanation

# TODO update the JSON string below
json = "{}"
# create an instance of DefensiveMetricsExplanation from a JSON string
defensive_metrics_explanation_instance = DefensiveMetricsExplanation.from_json(json)
# print the JSON string representation of the object
print(DefensiveMetricsExplanation.to_json())

# convert the object into a dict
defensive_metrics_explanation_dict = defensive_metrics_explanation_instance.to_dict()
# create an instance of DefensiveMetricsExplanation from a dict
defensive_metrics_explanation_from_dict = DefensiveMetricsExplanation.from_dict(defensive_metrics_explanation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


