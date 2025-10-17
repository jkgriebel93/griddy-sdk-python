# NFLResponseMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generated_at** | **datetime** | Response generation timestamp | [optional] 

## Example

```python
from nfl.models.nfl_response_metadata import NFLResponseMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of NFLResponseMetadata from a JSON string
nfl_response_metadata_instance = NFLResponseMetadata.from_json(json)
# print the JSON string representation of the object
print(NFLResponseMetadata.to_json())

# convert the object into a dict
nfl_response_metadata_dict = nfl_response_metadata_instance.to_dict()
# create an instance of NFLResponseMetadata from a dict
nfl_response_metadata_from_dict = NFLResponseMetadata.from_dict(nfl_response_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


