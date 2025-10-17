# src.griddy.nfl.ScoresController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_live_game_scores**](ScoresController.md#get_live_game_scores) | **GET** /api/scores/live/games | Get Live Game Scores


# **get_live_game_scores**
> LiveScoresResponse get_live_game_scores(season, season_type, week)

Get Live Game Scores

Retrieves real-time scores and game status for all games in a specified week.
This endpoint updates frequently (15-second cache) to provide live scoring updates
during active games. Returns an empty array when no games are currently being played.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.live_scores_response import LiveScoresResponse
from src.griddy.nfl.models.season_type_enum import SeasonTypeEnum
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
    api_instance = src.griddy.nfl.ScoresController(api_client)
    season = 2025 # int | Season year
    season_type = src.griddy.nfl.SeasonTypeEnum() # SeasonTypeEnum | Type of season
    week = 4 # int | Week number

    try:
        # Get Live Game Scores
        api_response = api_instance.get_live_game_scores(season, season_type, week)
        print("The response of ScoresController->get_live_game_scores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScoresController->get_live_game_scores: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **season_type** | [**SeasonTypeEnum**](.md)| Type of season | 
 **week** | **int**| Week number | 

### Return type

[**LiveScoresResponse**](LiveScoresResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved live scores |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

