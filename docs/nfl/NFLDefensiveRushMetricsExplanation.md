# NFLDefensiveRushMetricsExplanation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**box_count** | [**NFLNFLDefensiveRushMetricsExplanationBoxCount**](NFLDefensiveRushMetricsExplanationBoxCount.md) |  | [optional] 
**ryoe** | [**NFLNFLDefensiveRushMetricsExplanationRyoe**](NFLDefensiveRushMetricsExplanationRyoe.md) |  | [optional] 
**stuff_rate** | [**NFLNFLDefensiveRushMetricsExplanationStuffRate**](NFLDefensiveRushMetricsExplanationStuffRate.md) |  | [optional] 
**yards_before_contact** | [**NFLNFLDefensiveRushMetricsExplanationYardsBeforeContact**](NFLDefensiveRushMetricsExplanationYardsBeforeContact.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_defensive_rush_metrics_explanation import NFLDefensiveRushMetricsExplanation

# TODO update the JSON string below
json = "{}"
# create an instance of NFLDefensiveRushMetricsExplanation from a JSON string
nfl_defensive_rush_metrics_explanation_instance = NFLDefensiveRushMetricsExplanation.from_json(json)
# print the JSON string representation of the object
print(NFLDefensiveRushMetricsExplanation.to_json())

# convert the object into a dict
nfl_defensive_rush_metrics_explanation_dict = nfl_defensive_rush_metrics_explanation_instance.to_dict()
# create an instance of NFLDefensiveRushMetricsExplanation from a dict
nfl_defensive_rush_metrics_explanation_from_dict = NFLDefensiveRushMetricsExplanation.from_dict(nfl_defensive_rush_metrics_explanation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


