# nfl.ContentController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_game_insights**](ContentController.md#get_game_insights) | **GET** /api/content/insights/game | Get Game-Specific Insights
[**get_game_preview**](ContentController.md#get_game_preview) | **GET** /api/content/game/preview | Get Game Preview Content
[**get_home_film_cards**](ContentController.md#get_home_film_cards) | **GET** /api/content/home-film-cards | Get Home Film Cards


# **get_game_insights**
> List[NFLNFLGameInsight] get_game_insights(season, fapi_game_id, away_team_id, home_team_id, limit=limit, tags=tags, exclude_tags=exclude_tags)

Get Game-Specific Insights

Retrieves analytical insights and advanced statistics for a specific game. Can filter by tags and exclude specific content types.

### Example

* Bearer Authentication (NFLAuth):

```python
import nfl
from nfl.models.nflnfl_game_insight import NFLNFLGameInsight
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
    api_instance = nfl.ContentController(api_client)
    season = 2025 # int | Season year
    fapi_game_id = 'f688dfde-311e-11f0-b670-ae1250fadad1' # str | FAPI Game identifier (UUID)
    away_team_id = '3000' # str | Away team identifier
    home_team_id = '3900' # str | Home team identifier
    limit = 20 # int | Maximum number of insights to return (optional) (default to 20)
    tags = 'pro-preview' # str | Comma-separated list of tags to filter by (optional)
    exclude_tags = 'betting' # str | Comma-separated list of tags to exclude (optional)

    try:
        # Get Game-Specific Insights
        api_response = api_instance.get_game_insights(season, fapi_game_id, away_team_id, home_team_id, limit=limit, tags=tags, exclude_tags=exclude_tags)
        print("The response of ContentController->get_game_insights:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentController->get_game_insights: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **fapi_game_id** | **str**| FAPI Game identifier (UUID) | 
 **away_team_id** | **str**| Away team identifier | 
 **home_team_id** | **str**| Home team identifier | 
 **limit** | **int**| Maximum number of insights to return | [optional] [default to 20]
 **tags** | **str**| Comma-separated list of tags to filter by | [optional] 
 **exclude_tags** | **str**| Comma-separated list of tags to exclude | [optional] 

### Return type

[**List[NFLNFLGameInsight]**](NFLGameInsight.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved game insights |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_game_preview**
> NFLNFLGamePreviewResponse get_game_preview(season, season_type, week, visitor_display_name, home_display_name)

Get Game Preview Content

Retrieves preview content and insights for a specific game based on teams and week. Returns preview information, matchup analysis, and key storylines.

### Example

* Bearer Authentication (NFLAuth):

```python
import nfl
from nfl.models.nflnfl_game_preview_response import NFLNFLGamePreviewResponse
from nfl.models.nfl_season_type_enum import NFLSeasonTypeEnum
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
    api_instance = nfl.ContentController(api_client)
    season = 2025 # int | Season year
    season_type = nfl.NFLSeasonTypeEnum() # NFLSeasonTypeEnum | Type of season
    week = 4 # int | Week number
    visitor_display_name = 'Minnesota Vikings' # str | Visiting team display name
    home_display_name = 'Pittsburgh Steelers' # str | Home team display name

    try:
        # Get Game Preview Content
        api_response = api_instance.get_game_preview(season, season_type, week, visitor_display_name, home_display_name)
        print("The response of ContentController->get_game_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentController->get_game_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **season_type** | [**NFLSeasonTypeEnum**](.md)| Type of season | 
 **week** | **int**| Week number | 
 **visitor_display_name** | **str**| Visiting team display name | 
 **home_display_name** | **str**| Home team display name | 

### Return type

[**NFLNFLGamePreviewResponse**](NFLGamePreviewResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved game preview |  -  |
**401** | Unauthorized - Invalid or missing authentication token |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_home_film_cards**
> NFLNFLHomeFilmCardsResponse get_home_film_cards()

Get Home Film Cards

Retrieves featured film room content cards for the home page. Returns weekly playlists and featured player film breakdowns.

### Example

* Bearer Authentication (NFLAuth):

```python
import nfl
from nfl.models.nflnfl_home_film_cards_response import NFLNFLHomeFilmCardsResponse
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
    api_instance = nfl.ContentController(api_client)

    try:
        # Get Home Film Cards
        api_response = api_instance.get_home_film_cards()
        print("The response of ContentController->get_home_film_cards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentController->get_home_film_cards: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NFLNFLHomeFilmCardsResponse**](NFLHomeFilmCardsResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved film cards |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

