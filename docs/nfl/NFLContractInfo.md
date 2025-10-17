# NFLContractInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration_year** | **int** | Contract expiration year | [optional] 
**guaranteed** | **float** | Guaranteed money | [optional] 
**signing_bonus** | **float** | Signing bonus | [optional] 
**total_value** | **float** | Total contract value | [optional] 
**years** | **int** | Contract length in years | [optional] 

## Example

```python
from nfl.models.nfl_contract_info import NFLContractInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NFLContractInfo from a JSON string
nfl_contract_info_instance = NFLContractInfo.from_json(json)
# print the JSON string representation of the object
print(NFLContractInfo.to_json())

# convert the object into a dict
nfl_contract_info_dict = nfl_contract_info_instance.to_dict()
# create an instance of NFLContractInfo from a dict
nfl_contract_info_from_dict = NFLContractInfo.from_dict(nfl_contract_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


