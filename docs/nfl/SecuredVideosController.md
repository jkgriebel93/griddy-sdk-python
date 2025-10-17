# nfl.SecuredVideosController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_coaches_film_videos**](SecuredVideosController.md#get_coaches_film_videos) | **GET** /api/secured/videos/coaches | Get Coaches Film Videos


# **get_coaches_film_videos**
> NFLNFLCoachesFilmResponse get_coaches_film_videos(game_id, play_id)

Get Coaches Film Videos

Retrieves premium coaches film video content for specified games and plays.
Returns multiple camera angles (endzone, sideline, broadcast) for each play,
providing comprehensive film study material. Requires NFL Plus Premium subscription
and appropriate geographic restrictions apply (US only).


### Example

* Bearer Authentication (NFLAuth):

```python
import nfl
from nfl.models.nflnfl_coaches_film_response import NFLNFLCoachesFilmResponse
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
    api_instance = nfl.SecuredVideosController(api_client)
    game_id = ['[\"f665fc10-311e-11f0-b670-ae1250fadad1\",\"ae9d66f7-1312-11ef-afd1-646009f18b2e\"]'] # List[str] | Game identifiers (UUID format, supports multiple games)
    play_id = ['[\"267\",\"1162\",\"496\",\"139\"]'] # List[str] | Play identifiers for specific plays within the games

    try:
        # Get Coaches Film Videos
        api_response = api_instance.get_coaches_film_videos(game_id, play_id)
        print("The response of SecuredVideosController->get_coaches_film_videos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecuredVideosController->get_coaches_film_videos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | [**List[str]**](str.md)| Game identifiers (UUID format, supports multiple games) | 
 **play_id** | [**List[str]**](str.md)| Play identifiers for specific plays within the games | 

### Return type

[**NFLNFLCoachesFilmResponse**](NFLCoachesFilmResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved coaches film videos |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized - Invalid or missing authentication token |  -  |
**403** | Forbidden - Insufficient permissions for secured video content or geographic restrictions |  -  |
**404** | Games or plays not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

