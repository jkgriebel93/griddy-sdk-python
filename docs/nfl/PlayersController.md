# nfl.PlayersController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_player**](PlayersController.md#get_player) | **GET** /api/players/player | Get Player Details
[**get_projected_stats**](PlayersController.md#get_projected_stats) | **GET** /api/players/projectedStats | Get Projected Player Statistics
[**search_players**](PlayersController.md#search_players) | **GET** /api/players/search | Search Players


# **get_player**
> NFLNFLPlayerDetail get_player(nfl_id)

Get Player Details

Retrieves detailed information about a specific NFL player including physical attributes,
team information, draft details, and current status.


### Example

* Bearer Authentication (NFLAuth):

```python
import nfl
from nfl.models.nflnfl_player_detail import NFLNFLPlayerDetail
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
    api_instance = nfl.PlayersController(api_client)
    nfl_id = 54517 # int | NFL player identifier

    try:
        # Get Player Details
        api_response = api_instance.get_player(nfl_id)
        print("The response of PlayersController->get_player:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersController->get_player: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfl_id** | **int**| NFL player identifier | 

### Return type

[**NFLNFLPlayerDetail**](NFLPlayerDetail.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved player details |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized - Invalid or missing authentication token |  -  |
**404** | Player not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projected_stats**
> NFLNFLProjectedStatsResponse get_projected_stats(season, week, filter_nfl_team_id=filter_nfl_team_id, page_size=page_size)

Get Projected Player Statistics

Retrieves projected fantasy statistics for players based on team, season, and week.
Returns data in JSON:API format with relationships between players and their projected stats.


### Example

* Bearer Authentication (NFLAuth):

```python
import nfl
from nfl.models.nflnfl_projected_stats_response import NFLNFLProjectedStatsResponse
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
    api_instance = nfl.PlayersController(api_client)
    season = 2025 # int | Season year
    week = 4 # int | Week number within the season
    filter_nfl_team_id = '10403000-5851-f9d5-da45-78365a05b6b0' # str | Filter by NFL team ID (UUID format) (optional)
    page_size = 20 # int | Number of results per page (optional) (default to 20)

    try:
        # Get Projected Player Statistics
        api_response = api_instance.get_projected_stats(season, week, filter_nfl_team_id=filter_nfl_team_id, page_size=page_size)
        print("The response of PlayersController->get_projected_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersController->get_projected_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **week** | **int**| Week number within the season | 
 **filter_nfl_team_id** | **str**| Filter by NFL team ID (UUID format) | [optional] 
 **page_size** | **int**| Number of results per page | [optional] [default to 20]

### Return type

[**NFLNFLProjectedStatsResponse**](NFLProjectedStatsResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved projected statistics |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_players**
> NFLNFLPlayerSearchResponse search_players(term)

Search Players

Searches for NFL players by name or term. Returns a list of players matching the search criteria
including both active and retired players.


### Example

* Bearer Authentication (NFLAuth):

```python
import nfl
from nfl.models.nflnfl_player_search_response import NFLNFLPlayerSearchResponse
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
    api_instance = nfl.PlayersController(api_client)
    term = 'Pickens' # str | Search term for player name (first or last name)

    try:
        # Search Players
        api_response = api_instance.search_players(term)
        print("The response of PlayersController->search_players:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersController->search_players: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| Search term for player name (first or last name) | 

### Return type

[**NFLNFLPlayerSearchResponse**](NFLPlayerSearchResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved search results |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

