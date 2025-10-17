# FantayScoringExplanation

Explanation of fantasy scoring systems

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**half_ppr_scoring** | [**FantayScoringExplanationHalfPprScoring**](FantayScoringExplanationHalfPprScoring.md) |  | [optional] 
**ppr_scoring** | [**FantayScoringExplanationPprScoring**](FantayScoringExplanationPprScoring.md) |  | [optional] 
**standard_scoring** | [**FantayScoringExplanationStandardScoring**](FantayScoringExplanationStandardScoring.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.fantay_scoring_explanation import FantayScoringExplanation

# TODO update the JSON string below
json = "{}"
# create an instance of FantayScoringExplanation from a JSON string
fantay_scoring_explanation_instance = FantayScoringExplanation.from_json(json)
# print the JSON string representation of the object
print(FantayScoringExplanation.to_json())

# convert the object into a dict
fantay_scoring_explanation_dict = fantay_scoring_explanation_instance.to_dict()
# create an instance of FantayScoringExplanation from a dict
fantay_scoring_explanation_from_dict = FantayScoringExplanation.from_dict(fantay_scoring_explanation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


