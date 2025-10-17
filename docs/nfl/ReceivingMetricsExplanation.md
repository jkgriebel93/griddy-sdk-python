# ReceivingMetricsExplanation

Explanation of receiving metrics and calculations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catch_rate_over_expected** | [**ReceivingMetricsExplanationCatchRateOverExpected**](ReceivingMetricsExplanationCatchRateOverExpected.md) |  | [optional] 
**receiver_separation** | [**ReceivingMetricsExplanationReceiverSeparation**](ReceivingMetricsExplanationReceiverSeparation.md) |  | [optional] 
**yards_after_catch_over_expected** | [**ReceivingMetricsExplanationYardsAfterCatchOverExpected**](ReceivingMetricsExplanationYardsAfterCatchOverExpected.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.receiving_metrics_explanation import ReceivingMetricsExplanation

# TODO update the JSON string below
json = "{}"
# create an instance of ReceivingMetricsExplanation from a JSON string
receiving_metrics_explanation_instance = ReceivingMetricsExplanation.from_json(json)
# print the JSON string representation of the object
print(ReceivingMetricsExplanation.to_json())

# convert the object into a dict
receiving_metrics_explanation_dict = receiving_metrics_explanation_instance.to_dict()
# create an instance of ReceivingMetricsExplanation from a dict
receiving_metrics_explanation_from_dict = ReceivingMetricsExplanation.from_dict(receiving_metrics_explanation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


