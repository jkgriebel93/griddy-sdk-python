# ContractInfo


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
from src.griddy.nfl.models.contract_info import ContractInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContractInfo from a JSON string
contract_info_instance = ContractInfo.from_json(json)
# print the JSON string representation of the object
print(ContractInfo.to_json())

# convert the object into a dict
contract_info_dict = contract_info_instance.to_dict()
# create an instance of ContractInfo from a dict
contract_info_from_dict = ContractInfo.from_dict(contract_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


