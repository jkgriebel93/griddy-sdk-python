# WinProbabilityMetadata

Metadata about win probability calculations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculation_method** | [**CalculationMethodEnum**](CalculationMethodEnum.md) |  | [optional] 
**confidence_interval** | **float** | Statistical confidence interval for the predictions | [optional] 
**last_updated** | **datetime** | When the win probability data was last calculated | [optional] 
**model_version** | **str** | Version of the win probability model used | [optional] 

## Example

```python
from src.griddy.nfl.models.win_probability_metadata import WinProbabilityMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of WinProbabilityMetadata from a JSON string
win_probability_metadata_instance = WinProbabilityMetadata.from_json(json)
# print the JSON string representation of the object
print(WinProbabilityMetadata.to_json())

# convert the object into a dict
win_probability_metadata_dict = win_probability_metadata_instance.to_dict()
# create an instance of WinProbabilityMetadata from a dict
win_probability_metadata_from_dict = WinProbabilityMetadata.from_dict(win_probability_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


