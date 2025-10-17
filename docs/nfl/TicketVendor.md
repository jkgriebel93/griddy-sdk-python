# TicketVendor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_url** | **str** | Vendor-specific ticket URL | [optional] 
**vendor_name** | **str** | Vendor identifier | [optional] 

## Example

```python
from src.griddy.nfl.models.ticket_vendor import TicketVendor

# TODO update the JSON string below
json = "{}"
# create an instance of TicketVendor from a JSON string
ticket_vendor_instance = TicketVendor.from_json(json)
# print the JSON string representation of the object
print(TicketVendor.to_json())

# convert the object into a dict
ticket_vendor_dict = ticket_vendor_instance.to_dict()
# create an instance of TicketVendor from a dict
ticket_vendor_from_dict = TicketVendor.from_dict(ticket_vendor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


