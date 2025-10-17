# nfl.ContentInsightsController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_season_content_insights**](ContentInsightsController.md#get_season_content_insights) | **GET** /api/content/insights/season | Get Season Content Insights


# **get_season_content_insights**
> List[NFLNFLInsight] get_season_content_insights(season, limit=limit, tags=tags, team_id=team_id, nfl_id=nfl_id)

Get Season Content Insights

Retrieves curated editorial insights and analytics content for NFL players during
a specified season. Returns expert commentary combining Next Gen Stats data with
editorial analysis, including pregame previews, postgame breakdowns, fantasy insights,
and evergreen content. Supports filtering by player, team, content tags, and publication
limits for targeted content discovery.


### Example

* Bearer Authentication (NFLAuth):

```python
import nfl
from nfl.models.nflnfl_insight import NFLNFLInsight
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
    api_instance = nfl.ContentInsightsController(api_client)
    season = 2025 # int | Season year
    limit = 20 # int | Maximum number of insights to return (optional) (default to 20)
    tags = ['[\"nfl-pro\"]'] # List[str] | Content tags to filter by (supports multiple comma-separated tags) (optional)
    team_id = '3900' # str | Filter by specific team identifier (optional)
    nfl_id = '46101' # str | Filter by specific player NFL identifier (optional)

    try:
        # Get Season Content Insights
        api_response = api_instance.get_season_content_insights(season, limit=limit, tags=tags, team_id=team_id, nfl_id=nfl_id)
        print("The response of ContentInsightsController->get_season_content_insights:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentInsightsController->get_season_content_insights: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **limit** | **int**| Maximum number of insights to return | [optional] [default to 20]
 **tags** | [**List[str]**](str.md)| Content tags to filter by (supports multiple comma-separated tags) | [optional] 
 **team_id** | **str**| Filter by specific team identifier | [optional] 
 **nfl_id** | **str**| Filter by specific player NFL identifier | [optional] 

### Return type

[**List[NFLNFLInsight]**](NFLInsight.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved insights |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

