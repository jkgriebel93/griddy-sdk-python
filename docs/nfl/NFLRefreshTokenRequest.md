# NFLRefreshTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_key** | **str** | Client application identifier key | [optional] 
**client_secret** | **str** | Client application secret for authentication | [optional] 
**device_id** | **str** | Unique device identifier (UUID format) | [optional] 
**device_info** | **str** | Base64-encoded JSON containing device information such as: {\&quot;model\&quot;:\&quot;desktop\&quot;,\&quot;version\&quot;:\&quot;Chrome\&quot;,\&quot;osName\&quot;:\&quot;Windows\&quot;,\&quot;osVersion\&quot;:\&quot;10\&quot;}  | [optional] 
**network_type** | [**NFLNFLNetworkTypeEnum**](NFLNetworkTypeEnum.md) |  | [optional] 
**refresh_token** | **str** | Valid refresh token from previous authentication | [optional] 
**signature_timestamp** | **str** | Unix timestamp for signature verification | [optional] 
**uid** | **str** | User identifier hash | [optional] 
**uid_signature** | **str** | HMAC signature for request verification | [optional] 

## Example

```python
from nfl.models.nfl_refresh_token_request import NFLRefreshTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NFLRefreshTokenRequest from a JSON string
nfl_refresh_token_request_instance = NFLRefreshTokenRequest.from_json(json)
# print the JSON string representation of the object
print(NFLRefreshTokenRequest.to_json())

# convert the object into a dict
nfl_refresh_token_request_dict = nfl_refresh_token_request_instance.to_dict()
# create an instance of NFLRefreshTokenRequest from a dict
nfl_refresh_token_request_from_dict = NFLRefreshTokenRequest.from_dict(nfl_refresh_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


