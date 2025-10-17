# nfl.PlaysController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_summary_play**](PlaysController.md#get_summary_play) | **GET** /api/plays/summaryPlay | Get Play Summary


# **get_summary_play**
> NFLNFLPlaySummaryResponse get_summary_play(game_id, play_id)

Get Play Summary

Retrieves detailed information about a specific play in a game including play description,
statistics, involved players, win probability, and expected points.


### Example

* Bearer Authentication (NFLAuth):

```python
import nfl
from nfl.models.nflnfl_play_summary_response import NFLNFLPlaySummaryResponse
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
    api_instance = nfl.PlaysController(api_client)
    game_id = 'f665fc10-311e-11f0-b670-ae1250fadad1' # str | Game identifier (UUID format)
    play_id = 40 # int | Play identifier within the game

    try:
        # Get Play Summary
        api_response = api_instance.get_summary_play(game_id, play_id)
        print("The response of PlaysController->get_summary_play:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaysController->get_summary_play: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **str**| Game identifier (UUID format) | 
 **play_id** | **int**| Play identifier within the game | 

### Return type

[**NFLNFLPlaySummaryResponse**](NFLPlaySummaryResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved play summary |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**404** | Play not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

