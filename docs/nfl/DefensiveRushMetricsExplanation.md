# DefensiveRushMetricsExplanation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**box_count** | [**DefensiveRushMetricsExplanationBoxCount**](DefensiveRushMetricsExplanationBoxCount.md) |  | [optional] 
**ryoe** | [**DefensiveRushMetricsExplanationRyoe**](DefensiveRushMetricsExplanationRyoe.md) |  | [optional] 
**stuff_rate** | [**DefensiveRushMetricsExplanationStuffRate**](DefensiveRushMetricsExplanationStuffRate.md) |  | [optional] 
**yards_before_contact** | [**DefensiveRushMetricsExplanationYardsBeforeContact**](DefensiveRushMetricsExplanationYardsBeforeContact.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.defensive_rush_metrics_explanation import DefensiveRushMetricsExplanation

# TODO update the JSON string below
json = "{}"
# create an instance of DefensiveRushMetricsExplanation from a JSON string
defensive_rush_metrics_explanation_instance = DefensiveRushMetricsExplanation.from_json(json)
# print the JSON string representation of the object
print(DefensiveRushMetricsExplanation.to_json())

# convert the object into a dict
defensive_rush_metrics_explanation_dict = defensive_rush_metrics_explanation_instance.to_dict()
# create an instance of DefensiveRushMetricsExplanation from a dict
defensive_rush_metrics_explanation_from_dict = DefensiveRushMetricsExplanation.from_dict(defensive_rush_metrics_explanation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


