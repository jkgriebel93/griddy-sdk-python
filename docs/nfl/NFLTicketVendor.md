# NFLTicketVendor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_url** | **str** | Vendor-specific ticket URL | [optional] 
**vendor_name** | **str** | Vendor identifier | [optional] 

## Example

```python
from nfl.models.nfl_ticket_vendor import NFLTicketVendor

# TODO update the JSON string below
json = "{}"
# create an instance of NFLTicketVendor from a JSON string
nfl_ticket_vendor_instance = NFLTicketVendor.from_json(json)
# print the JSON string representation of the object
print(NFLTicketVendor.to_json())

# convert the object into a dict
nfl_ticket_vendor_dict = nfl_ticket_vendor_instance.to_dict()
# create an instance of NFLTicketVendor from a dict
nfl_ticket_vendor_from_dict = NFLTicketVendor.from_dict(nfl_ticket_vendor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


