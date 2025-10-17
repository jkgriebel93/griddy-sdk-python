# DefensivePassMetricsExplanation

Explanation of defensive pass metrics and calculations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**epa_pass** | [**DefensivePassMetricsExplanationEpaPass**](DefensivePassMetricsExplanationEpaPass.md) |  | [optional] 
**receiver_separation** | [**DefensivePassMetricsExplanationReceiverSeparation**](DefensivePassMetricsExplanationReceiverSeparation.md) |  | [optional] 
**yacoe** | [**DefensivePassMetricsExplanationYacoe**](DefensivePassMetricsExplanationYacoe.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.defensive_pass_metrics_explanation import DefensivePassMetricsExplanation

# TODO update the JSON string below
json = "{}"
# create an instance of DefensivePassMetricsExplanation from a JSON string
defensive_pass_metrics_explanation_instance = DefensivePassMetricsExplanation.from_json(json)
# print the JSON string representation of the object
print(DefensivePassMetricsExplanation.to_json())

# convert the object into a dict
defensive_pass_metrics_explanation_dict = defensive_pass_metrics_explanation_instance.to_dict()
# create an instance of DefensivePassMetricsExplanation from a dict
defensive_pass_metrics_explanation_from_dict = DefensivePassMetricsExplanation.from_dict(defensive_pass_metrics_explanation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


