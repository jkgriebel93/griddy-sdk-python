# nfl.AuthenticationController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_token**](AuthenticationController.md#generate_token) | **POST** /identity/v3/token | Generate Initial Access Token
[**refresh_token**](AuthenticationController.md#refresh_token) | **POST** /identity/v3/token/refresh | Refresh Access Token


# **generate_token**
> NFLNFLTokenResponse generate_token(nfl_token_request)

Generate Initial Access Token

Creates a new access token and refresh token for a client device. This is the initial authentication endpoint that establishes a session for accessing NFL APIs. Requires client credentials and device information.

### Example

* Bearer Authentication (NFLAuth):

```python
import nfl
from nfl.models.nflnfl_token_response import NFLNFLTokenResponse
from nfl.models.nfl_token_request import NFLTokenRequest
from nfl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = nfl.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: NFLAuth
configuration = nfl.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nfl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nfl.AuthenticationController(api_client)
    nfl_token_request = {"clientKey":"4cFUW6DmwJpzT9L7LrG3qRAcABG5s04g","clientSecret":"CZuvCL49d9OwfGsR","deviceId":"3cfdef35-c7fe-4f2d-8630-1ec72f52b44d","deviceInfo":"eyJtb2RlbCI6ImRlc2t0b3AiLCJ2ZXJzaW9uIjoiQ2hyb21lIiwib3NOYW1lIjoiV2luZG93cyIsIm9zVmVyc2lvbiI6IjEwIn0=","networkType":"other"} # NFLTokenRequest | 

    try:
        # Generate Initial Access Token
        api_response = api_instance.generate_token(nfl_token_request)
        print("The response of AuthenticationController->generate_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationController->generate_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfl_token_request** | [**NFLTokenRequest**](NFLTokenRequest.md)|  | 

### Return type

[**NFLNFLTokenResponse**](NFLTokenResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully generated tokens |  -  |
**400** | Invalid request parameters |  -  |
**401** | Invalid client credentials |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token**
> NFLNFLTokenResponse refresh_token(nfl_refresh_token_request)

Refresh Access Token

Refreshes an existing access token using a valid refresh token. This endpoint extends the user's session by generating new access and refresh tokens. Requires the previous refresh token and signature verification.

### Example

* Bearer Authentication (NFLAuth):

```python
import nfl
from nfl.models.nflnfl_token_response import NFLNFLTokenResponse
from nfl.models.nfl_refresh_token_request import NFLRefreshTokenRequest
from nfl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = nfl.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: NFLAuth
configuration = nfl.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nfl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nfl.AuthenticationController(api_client)
    nfl_refresh_token_request = {"clientKey":"4cFUW6DmwJpzT9L7LrG3qRAcABG5s04g","clientSecret":"CZuvCL49d9OwfGsR","deviceId":"3cfdef35-c7fe-4f2d-8630-1ec72f52b44d","deviceInfo":"eyJtb2RlbCI6ImRlc2t0b3AiLCJ2ZXJzaW9uIjoiQ2hyb21lIiwib3NOYW1lIjoiV2luZG93cyIsIm9zVmVyc2lvbiI6IjEwIn0=","networkType":"other","refreshToken":"640b00c7-33d8-44f2-ab46-e3d1284a4061","signatureTimestamp":"1758729181","uid":"df990acd951e4bd6940c3babc4341584","uidSignature":"587bdNt6EKYhhX9ASFOELX+2lqE="} # NFLRefreshTokenRequest | 

    try:
        # Refresh Access Token
        api_response = api_instance.refresh_token(nfl_refresh_token_request)
        print("The response of AuthenticationController->refresh_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationController->refresh_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfl_refresh_token_request** | [**NFLRefreshTokenRequest**](NFLRefreshTokenRequest.md)|  | 

### Return type

[**NFLNFLTokenResponse**](NFLTokenResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully refreshed tokens |  -  |
**400** | Invalid request parameters |  -  |
**401** | Invalid or expired refresh token |  -  |
**403** | Invalid signature verification |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

