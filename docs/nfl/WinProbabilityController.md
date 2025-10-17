# src.griddy.nfl.WinProbabilityController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_plays_win_probability**](WinProbabilityController.md#get_plays_win_probability) | **GET** /api/secured/plays/winProbability | Get Game Win Probability by Plays
[**get_win_probability_min**](WinProbabilityController.md#get_win_probability_min) | **GET** /api/secured/plays/winProbabilityMin | Get Minimal Win Probability Data


# **get_plays_win_probability**
> GetPlaysWinProbability200Response get_plays_win_probability(game_id)

Get Game Win Probability by Plays

Retrieves comprehensive win probability data for every play in specified games.
Returns pre-game win probabilities and detailed play-by-play probability changes,
including Win Probability Added (WPA) metrics for each play. This advanced analytics
endpoint tracks how each play impacts the probability of each team winning the game.
Supports querying multiple games simultaneously.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.get_plays_win_probability200_response import GetPlaysWinProbability200Response
from src.griddy.nfl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = src.griddy.nfl.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: NFLAuth
configuration = src.griddy.nfl.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with src.griddy.nfl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = src.griddy.nfl.WinProbabilityController(api_client)
    game_id = src.griddy.nfl.GetPlaysWinProbabilityGameIdParameter() # GetPlaysWinProbabilityGameIdParameter | Game identifier(s) in 10-digit format (YYYYMMDDNN). Can be a single game ID or multiple game IDs for batch retrieval. 

    try:
        # Get Game Win Probability by Plays
        api_response = api_instance.get_plays_win_probability(game_id)
        print("The response of WinProbabilityController->get_plays_win_probability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WinProbabilityController->get_plays_win_probability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | [**GetPlaysWinProbabilityGameIdParameter**](.md)| Game identifier(s) in 10-digit format (YYYYMMDDNN). Can be a single game ID or multiple game IDs for batch retrieval.  | 

### Return type

[**GetPlaysWinProbability200Response**](GetPlaysWinProbability200Response.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved win probability data |  -  |
**400** | Invalid game ID format |  -  |
**401** | Unauthorized - Invalid or missing authentication token |  -  |
**403** | Forbidden - Insufficient permissions to access secured endpoint |  -  |
**404** | Game not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_win_probability_min**
> WinProbabilityResponse get_win_probability_min(fapi_game_id)

Get Minimal Win Probability Data

Retrieves minimal win probability data for specified games, including pregame
win probabilities and play-by-play probability changes throughout the game.
This endpoint provides essential win probability metrics with optimized data
structure for performance. Supports multiple games in a single request.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.win_probability_response import WinProbabilityResponse
from src.griddy.nfl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = src.griddy.nfl.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: NFLAuth
configuration = src.griddy.nfl.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with src.griddy.nfl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = src.griddy.nfl.WinProbabilityController(api_client)
    fapi_game_id = ['[\"f666051f-311e-11f0-b670-ae1250fadad1\",\"f6660056-311e-11f0-b670-ae1250fadad1\",\"f665fc10-311e-11f0-b670-ae1250fadad1\"]'] # List[str] | Football API game identifiers (UUID format). Supports multiple game IDs to retrieve win probability data for multiple games simultaneously. 

    try:
        # Get Minimal Win Probability Data
        api_response = api_instance.get_win_probability_min(fapi_game_id)
        print("The response of WinProbabilityController->get_win_probability_min:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WinProbabilityController->get_win_probability_min: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fapi_game_id** | [**List[str]**](str.md)| Football API game identifiers (UUID format). Supports multiple game IDs to retrieve win probability data for multiple games simultaneously.  | 

### Return type

[**WinProbabilityResponse**](WinProbabilityResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved win probability data |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized - Invalid or missing authentication token |  -  |
**403** | Forbidden - Insufficient permissions for secured content |  -  |
**404** | Game(s) not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

