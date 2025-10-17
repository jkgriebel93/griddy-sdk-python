# NFLFantayScoringExplanation

Explanation of fantasy scoring systems

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**half_ppr_scoring** | [**NFLNFLFantayScoringExplanationHalfPprScoring**](NFLFantayScoringExplanationHalfPprScoring.md) |  | [optional] 
**ppr_scoring** | [**NFLNFLFantayScoringExplanationPprScoring**](NFLFantayScoringExplanationPprScoring.md) |  | [optional] 
**standard_scoring** | [**NFLNFLFantayScoringExplanationStandardScoring**](NFLFantayScoringExplanationStandardScoring.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_fantay_scoring_explanation import NFLFantayScoringExplanation

# TODO update the JSON string below
json = "{}"
# create an instance of NFLFantayScoringExplanation from a JSON string
nfl_fantay_scoring_explanation_instance = NFLFantayScoringExplanation.from_json(json)
# print the JSON string representation of the object
print(NFLFantayScoringExplanation.to_json())

# convert the object into a dict
nfl_fantay_scoring_explanation_dict = nfl_fantay_scoring_explanation_instance.to_dict()
# create an instance of NFLFantayScoringExplanation from a dict
nfl_fantay_scoring_explanation_from_dict = NFLFantayScoringExplanation.from_dict(nfl_fantay_scoring_explanation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


