# NFLDefensivePassMetricsExplanation

Explanation of defensive pass metrics and calculations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**epa_pass** | [**NFLNFLDefensivePassMetricsExplanationEpaPass**](NFLDefensivePassMetricsExplanationEpaPass.md) |  | [optional] 
**receiver_separation** | [**NFLNFLDefensivePassMetricsExplanationReceiverSeparation**](NFLDefensivePassMetricsExplanationReceiverSeparation.md) |  | [optional] 
**yacoe** | [**NFLNFLDefensivePassMetricsExplanationYacoe**](NFLDefensivePassMetricsExplanationYacoe.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_defensive_pass_metrics_explanation import NFLDefensivePassMetricsExplanation

# TODO update the JSON string below
json = "{}"
# create an instance of NFLDefensivePassMetricsExplanation from a JSON string
nfl_defensive_pass_metrics_explanation_instance = NFLDefensivePassMetricsExplanation.from_json(json)
# print the JSON string representation of the object
print(NFLDefensivePassMetricsExplanation.to_json())

# convert the object into a dict
nfl_defensive_pass_metrics_explanation_dict = nfl_defensive_pass_metrics_explanation_instance.to_dict()
# create an instance of NFLDefensivePassMetricsExplanation from a dict
nfl_defensive_pass_metrics_explanation_from_dict = NFLDefensivePassMetricsExplanation.from_dict(nfl_defensive_pass_metrics_explanation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


