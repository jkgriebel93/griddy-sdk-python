# NFLRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**losses** | **int** |  | [optional] 
**ties** | **int** |  | [optional] 
**wins** | **int** |  | [optional] 

## Example

```python
from nfl.models.nfl_record import NFLRecord

# TODO update the JSON string below
json = "{}"
# create an instance of NFLRecord from a JSON string
nfl_record_instance = NFLRecord.from_json(json)
# print the JSON string representation of the object
print(NFLRecord.to_json())

# convert the object into a dict
nfl_record_dict = nfl_record_instance.to_dict()
# create an instance of NFLRecord from a dict
nfl_record_from_dict = NFLRecord.from_dict(nfl_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


