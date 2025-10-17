# NFLInsightContentExplanation

Explanation of insight content types and usage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evergreen_content** | [**NFLNFLInsightContentExplanationEvergreenContent**](NFLInsightContentExplanationEvergreenContent.md) |  | [optional] 
**fantasy_insights** | [**NFLNFLInsightContentExplanationFantasyInsights**](NFLInsightContentExplanationFantasyInsights.md) |  | [optional] 
**postgame_insights** | [**NFLNFLInsightContentExplanationPostgameInsights**](NFLInsightContentExplanationPostgameInsights.md) |  | [optional] 
**pregame_insights** | [**NFLNFLInsightContentExplanationPregameInsights**](NFLInsightContentExplanationPregameInsights.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_insight_content_explanation import NFLInsightContentExplanation

# TODO update the JSON string below
json = "{}"
# create an instance of NFLInsightContentExplanation from a JSON string
nfl_insight_content_explanation_instance = NFLInsightContentExplanation.from_json(json)
# print the JSON string representation of the object
print(NFLInsightContentExplanation.to_json())

# convert the object into a dict
nfl_insight_content_explanation_dict = nfl_insight_content_explanation_instance.to_dict()
# create an instance of NFLInsightContentExplanation from a dict
nfl_insight_content_explanation_from_dict = NFLInsightContentExplanation.from_dict(nfl_insight_content_explanation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


