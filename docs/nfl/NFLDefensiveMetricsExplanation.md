# NFLDefensiveMetricsExplanation

Explanation of defensive metrics and calculations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**epa** | [**NFLNFLDefensiveMetricsExplanationEpa**](NFLDefensiveMetricsExplanationEpa.md) |  | [optional] 
**qbp_pct** | [**NFLNFLDefensiveMetricsExplanationQbpPct**](NFLDefensiveMetricsExplanationQbpPct.md) |  | [optional] 
**ryoe** | [**NFLNFLDefensiveMetricsExplanationRyoe**](NFLDefensiveMetricsExplanationRyoe.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_defensive_metrics_explanation import NFLDefensiveMetricsExplanation

# TODO update the JSON string below
json = "{}"
# create an instance of NFLDefensiveMetricsExplanation from a JSON string
nfl_defensive_metrics_explanation_instance = NFLDefensiveMetricsExplanation.from_json(json)
# print the JSON string representation of the object
print(NFLDefensiveMetricsExplanation.to_json())

# convert the object into a dict
nfl_defensive_metrics_explanation_dict = nfl_defensive_metrics_explanation_instance.to_dict()
# create an instance of NFLDefensiveMetricsExplanation from a dict
nfl_defensive_metrics_explanation_from_dict = NFLDefensiveMetricsExplanation.from_dict(nfl_defensive_metrics_explanation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


