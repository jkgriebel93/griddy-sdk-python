# NFLReceivingMetricsExplanation

Explanation of receiving metrics and calculations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catch_rate_over_expected** | [**NFLNFLReceivingMetricsExplanationCatchRateOverExpected**](NFLReceivingMetricsExplanationCatchRateOverExpected.md) |  | [optional] 
**receiver_separation** | [**NFLNFLReceivingMetricsExplanationReceiverSeparation**](NFLReceivingMetricsExplanationReceiverSeparation.md) |  | [optional] 
**yards_after_catch_over_expected** | [**NFLNFLReceivingMetricsExplanationYardsAfterCatchOverExpected**](NFLReceivingMetricsExplanationYardsAfterCatchOverExpected.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_receiving_metrics_explanation import NFLReceivingMetricsExplanation

# TODO update the JSON string below
json = "{}"
# create an instance of NFLReceivingMetricsExplanation from a JSON string
nfl_receiving_metrics_explanation_instance = NFLReceivingMetricsExplanation.from_json(json)
# print the JSON string representation of the object
print(NFLReceivingMetricsExplanation.to_json())

# convert the object into a dict
nfl_receiving_metrics_explanation_dict = nfl_receiving_metrics_explanation_instance.to_dict()
# create an instance of NFLReceivingMetricsExplanation from a dict
nfl_receiving_metrics_explanation_from_dict = NFLReceivingMetricsExplanation.from_dict(nfl_receiving_metrics_explanation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


