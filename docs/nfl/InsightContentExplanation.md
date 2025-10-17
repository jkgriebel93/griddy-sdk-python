# InsightContentExplanation

Explanation of insight content types and usage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evergreen_content** | [**InsightContentExplanationEvergreenContent**](InsightContentExplanationEvergreenContent.md) |  | [optional] 
**fantasy_insights** | [**InsightContentExplanationFantasyInsights**](InsightContentExplanationFantasyInsights.md) |  | [optional] 
**postgame_insights** | [**InsightContentExplanationPostgameInsights**](InsightContentExplanationPostgameInsights.md) |  | [optional] 
**pregame_insights** | [**InsightContentExplanationPregameInsights**](InsightContentExplanationPregameInsights.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.insight_content_explanation import InsightContentExplanation

# TODO update the JSON string below
json = "{}"
# create an instance of InsightContentExplanation from a JSON string
insight_content_explanation_instance = InsightContentExplanation.from_json(json)
# print the JSON string representation of the object
print(InsightContentExplanation.to_json())

# convert the object into a dict
insight_content_explanation_dict = insight_content_explanation_instance.to_dict()
# create an instance of InsightContentExplanation from a dict
insight_content_explanation_from_dict = InsightContentExplanation.from_dict(insight_content_explanation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


