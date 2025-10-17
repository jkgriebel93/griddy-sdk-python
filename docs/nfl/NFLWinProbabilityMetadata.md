# NFLWinProbabilityMetadata

Metadata about win probability calculations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculation_method** | [**NFLNFLCalculationMethodEnum**](NFLCalculationMethodEnum.md) |  | [optional] 
**confidence_interval** | **float** | Statistical confidence interval for the predictions | [optional] 
**last_updated** | **datetime** | When the win probability data was last calculated | [optional] 
**model_version** | **str** | Version of the win probability model used | [optional] 

## Example

```python
from nfl.models.nfl_win_probability_metadata import NFLWinProbabilityMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of NFLWinProbabilityMetadata from a JSON string
nfl_win_probability_metadata_instance = NFLWinProbabilityMetadata.from_json(json)
# print the JSON string representation of the object
print(NFLWinProbabilityMetadata.to_json())

# convert the object into a dict
nfl_win_probability_metadata_dict = nfl_win_probability_metadata_instance.to_dict()
# create an instance of NFLWinProbabilityMetadata from a dict
nfl_win_probability_metadata_from_dict = NFLWinProbabilityMetadata.from_dict(nfl_win_probability_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


