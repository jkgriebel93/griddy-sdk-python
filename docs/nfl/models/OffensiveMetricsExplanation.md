# OffensiveMetricsExplanation

Explanation of offensive metrics and calculations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**epa** | [**OffensiveMetricsExplanationEpa**](OffensiveMetricsExplanationEpa.md) |  | [optional] 
**red_zone_efficiency** | [**OffensiveMetricsExplanationRedZoneEfficiency**](OffensiveMetricsExplanationRedZoneEfficiency.md) |  | [optional] 
**third_down_conversion** | [**OffensiveMetricsExplanationThirdDownConversion**](OffensiveMetricsExplanationThirdDownConversion.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.offensive_metrics_explanation import OffensiveMetricsExplanation

# TODO update the JSON string below
json = "{}"
# create an instance of OffensiveMetricsExplanation from a JSON string
offensive_metrics_explanation_instance = OffensiveMetricsExplanation.from_json(json)
# print the JSON string representation of the object
print(OffensiveMetricsExplanation.to_json())

# convert the object into a dict
offensive_metrics_explanation_dict = offensive_metrics_explanation_instance.to_dict()
# create an instance of OffensiveMetricsExplanation from a dict
offensive_metrics_explanation_from_dict = OffensiveMetricsExplanation.from_dict(offensive_metrics_explanation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


