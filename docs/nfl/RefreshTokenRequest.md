# RefreshTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_key** | **str** | Client application identifier key | [optional] 
**client_secret** | **str** | Client application secret for authentication | [optional] 
**device_id** | **str** | Unique device identifier (UUID format) | [optional] 
**device_info** | **str** | Base64-encoded JSON containing device information such as: {\&quot;model\&quot;:\&quot;desktop\&quot;,\&quot;version\&quot;:\&quot;Chrome\&quot;,\&quot;osName\&quot;:\&quot;Windows\&quot;,\&quot;osVersion\&quot;:\&quot;10\&quot;}  | [optional] 
**network_type** | [**NetworkTypeEnum**](NetworkTypeEnum.md) |  | [optional] 
**refresh_token** | **str** | Valid refresh token from previous authentication | [optional] 
**signature_timestamp** | **str** | Unix timestamp for signature verification | [optional] 
**uid** | **str** | User identifier hash | [optional] 
**uid_signature** | **str** | HMAC signature for request verification | [optional] 

## Example

```python
from src.griddy.nfl.models.refresh_token_request import RefreshTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshTokenRequest from a JSON string
refresh_token_request_instance = RefreshTokenRequest.from_json(json)
# print the JSON string representation of the object
print(RefreshTokenRequest.to_json())

# convert the object into a dict
refresh_token_request_dict = refresh_token_request_instance.to_dict()
# create an instance of RefreshTokenRequest from a dict
refresh_token_request_from_dict = RefreshTokenRequest.from_dict(refresh_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


