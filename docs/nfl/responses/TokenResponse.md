# TokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | JWT access token containing user permissions, subscription plans, location data, and roles. Include this token in the Authorization header as \&quot;Bearer {accessToken}\&quot; for authenticated requests. | [optional] 
**expires_in** | **int** | Unix timestamp when the access token expires | [optional] 
**refresh_token** | **str** | New refresh token for future token refresh requests | [optional] 

## Example

```python
from src.griddy.nfl.models.token_response import TokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenResponse from a JSON string
token_response_instance = TokenResponse.from_json(json)
# print the JSON string representation of the object
print(TokenResponse.to_json())

# convert the object into a dict
token_response_dict = token_response_instance.to_dict()
# create an instance of TokenResponse from a dict
token_response_from_dict = TokenResponse.from_dict(token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


