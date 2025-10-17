# NFLOffensiveMetricsExplanation

Explanation of offensive metrics and calculations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**epa** | [**NFLNFLOffensiveMetricsExplanationEpa**](NFLOffensiveMetricsExplanationEpa.md) |  | [optional] 
**red_zone_efficiency** | [**NFLNFLOffensiveMetricsExplanationRedZoneEfficiency**](NFLOffensiveMetricsExplanationRedZoneEfficiency.md) |  | [optional] 
**third_down_conversion** | [**NFLNFLOffensiveMetricsExplanationThirdDownConversion**](NFLOffensiveMetricsExplanationThirdDownConversion.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_offensive_metrics_explanation import NFLOffensiveMetricsExplanation

# TODO update the JSON string below
json = "{}"
# create an instance of NFLOffensiveMetricsExplanation from a JSON string
nfl_offensive_metrics_explanation_instance = NFLOffensiveMetricsExplanation.from_json(json)
# print the JSON string representation of the object
print(NFLOffensiveMetricsExplanation.to_json())

# convert the object into a dict
nfl_offensive_metrics_explanation_dict = nfl_offensive_metrics_explanation_instance.to_dict()
# create an instance of NFLOffensiveMetricsExplanation from a dict
nfl_offensive_metrics_explanation_from_dict = NFLOffensiveMetricsExplanation.from_dict(nfl_offensive_metrics_explanation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


