# Request Comparison Tool Guide

This guide explains how to use the request comparison tool to debug differences between direct HTTP requests and SDK requests.

## What It Does

The `request_comparator.py` tool:
1. **Captures** SDK requests made via httpx
2. **Displays** detailed request information (URL, headers, params)
3. **Compares** SDK requests with direct requests side-by-side
4. **Highlights** differences in headers, query parameters, and URLs

## Quick Start

```python
from request_comparator import RequestComparator, compare_requests, print_direct_request_details

# 1. Prepare direct request info
direct_request_info = {
    'url': 'https://example.com/api/endpoint',
    'method': 'GET',
    'headers': {...}
}

# 2. Display direct request details (NEW!)
print_direct_request_details(direct_request_info)

# 3. Create comparator and start capturing
comparator = RequestComparator()
comparator.start_capture()

# 4. Make your SDK call
sdk_response = nfl.player_statistics.get_player_passing_stats_by_season(...)

# 5. Stop capturing
comparator.stop_capture()

# 6. Compare requests
compare_requests(direct_request_info, comparator.get_last_request())
```

### Save to File

```python
# Write comparison to a file
with open('comparison.log', 'w') as f:
    print_direct_request_details(direct_request_info, file=f)
    compare_requests(direct_request_info, comparator.get_last_request(), file=f)
```

## Example Output

When you run the comparison, you'll see:

### 1. Direct Request Details (NEW!)
```
================================================================================
DIRECT REQUEST (requests library)
================================================================================
Method: GET
URL: https://pro.nfl.com/api/secured/stats/...

URL Components:
  Scheme: https
  Host: pro.nfl.com
  Path: /api/secured/stats/players-offense/passing/season

Query Parameters:
  limit = 1
  season = 2024
  seasonType = REG

Headers:
  accept: application/json
  authorization: Bearer eyJ0eXAiOiJKV1QiL...
  user-agent: Mozilla/5.0 (Windows NT...
================================================================================
```

### 2. Captured SDK Request
```
================================================================================
CAPTURED SDK REQUEST (SYNC)
================================================================================
Method: GET
URL: https://pro.nfl.com/api/secured/stats/...

URL Components:
  Scheme: https
  Host: pro.nfl.com
  Path: /api/secured/stats/players-offense/passing/season

Query Parameters:
  limit = 1
  season = 2024
  seasonType = REG

Headers:
  accept: application/json
  authorization: Bearer eyJ0eXAiOiJKV1QiL...
  user-agent: Mozilla/5.0 (Windows NT...
================================================================================
```

### 3. Side-by-Side Comparison
```
====================================================================================================
REQUEST COMPARISON
====================================================================================================

URL COMPONENTS-------------------------------------------------------------------------------------
Component        Direct Request                          SDK Request                             Match
----------------------------------------------------------------------------------------------------
Scheme           https                                   https                                   ✓
Host             pro.nfl.com                             pro.nfl.com                             ✓
Path             /api/secured/stats/...                  /api/secured/stats/...                  ✓
Method           GET                                     GET                                     ✓

QUERY PARAMETERS---------------------------------------------------------------------------------------
Parameter            Direct Request                     SDK Request                         Match
----------------------------------------------------------------------------------------------------
✓ limit              1                                  1                                   ✓
✗ season             2024                               2025                                ✗
✓ seasonType         REG                                REG                                 ✓

HEADERS------------------------------------------------------------------------------------------------
Header                   Direct Request                    SDK Request                        Match
----------------------------------------------------------------------------------------------------
>>> accept               application/json                  application/json                   ✓
>>> authorization        Bearer eyJ0eXAiOiJKV1QiL...       Bearer eyJ0eXAiOiJKV1QiL...        ✓
✗   user-agent           Mozilla/5.0 (Windows NT...        griddy-sdk/1.0                     ✗

COOKIES-------------------------------------------------------------------------------------------------
Cookie Name              Direct Request                    SDK Request                        Match
----------------------------------------------------------------------------------------------------
glt_mock_api_key         mock_login_token_12345            mock_login_token_12345             ✓
session_id               mock_session_abc                  mock_session_abc                   ✓

SUMMARY-------------------------------------------------------------------------------------------------
Query Parameters: 2/3 match
Headers: 8/10 match
Cookies: 2/2 match

Query parameter mismatches: season
Header mismatches: user-agent
====================================================================================================
```

## Features

### New: Direct Request Display
- `print_direct_request_details()` - Shows your direct request in the same detailed format as SDK requests
- Parses URL into components (scheme, host, path)
- Extracts and displays query parameters
- Shows all headers with sensitive data truncation
- Perfect for comparing apples-to-apples before the comparison

### Automatic Capture
The comparator intercepts all httpx requests automatically:
- Captures sync requests (httpx.Client)
- Captures async requests (httpx.AsyncClient)
- No changes needed to SDK code

### Detailed Comparison
- ✅ Shows exact differences
- ✅ Highlights mismatched values
- ✅ Groups important headers (auth, cookies, etc.)
- ✅ Parses and compares individual cookies
- ✅ Truncates long values for readability
- ✅ Shows match counts and summaries

### Cookie Comparison
The tool automatically parses cookies from the Cookie header and compares them individually:
- Extracts cookie name-value pairs from both direct and SDK requests
- Displays each cookie separately with ✓/✗ match indicators
- Shows which specific cookies are missing or have different values
- Includes cookie comparison in the summary statistics
- Handles cookie values with proper truncation for long values

Example output:
```
COOKIES-------------------------------------------------------------------------------------------------
Cookie Name              Direct Request                    SDK Request                        Match
----------------------------------------------------------------------------------------------------
glt_mock_api_key         mock_login_token_12345            mock_login_token_12345             ✓
session_id               mock_session_abc                  MISSING                            ✗
user_token               abc123def456                      abc123def456                       ✓
```

### File Output (NEW!)
Save all output to a file for detailed analysis:
```python
OUTPUT_FILE = "request_comparison.log"

with open(OUTPUT_FILE, 'w') as f:
    # All these functions accept a file parameter
    print_direct_request_details(direct_info, file=f)
    # ... SDK calls ...
    compare_requests(direct_info, comparator.get_last_request(), file=f)
```

See `griddy_test.py` for a complete example that logs to both console and file!

### Debug Output
Enable SDK debug logging for even more detail:
```python
import os
os.environ['GRIDDY_NFL_DEBUG'] = '1'
```

This will also show:
- Request body content
- Response status and body
- Internal SDK logging

## Advanced Usage

### Capture Multiple Requests
```python
comparator = RequestComparator()
comparator.start_capture()

# Make multiple SDK calls
sdk.endpoint1.method()
sdk.endpoint2.method()
sdk.endpoint3.method()

comparator.stop_capture()

# Access all captured requests
for req in comparator.captured_requests:
    print(req['url'])

# Or just the last one
last_req = comparator.get_last_request()
```

### Clear Captured Requests
```python
comparator.clear()  # Remove all captured requests
```

### Context Manager (Auto-cleanup)
```python
with RequestComparator() as comparator:
    comparator.start_capture()
    # Make SDK calls
    sdk_response = nfl.some_method()
    # Automatically stops capture when exiting
```

## Troubleshooting

### No Request Captured
If you see "Warning: No SDK request was captured!":
1. Make sure you called `start_capture()` before the SDK call
2. Verify the SDK call actually executed (no exceptions)
3. Check if the SDK method makes HTTP requests

### Import Errors
Make sure `request_comparator.py` is in your Python path or the same directory as your script.

### httpx vs requests
This tool only captures httpx requests (used by the SDK). Direct `requests` library calls won't be captured - that's the point! You manually provide direct request info for comparison.

## Configuration

### Enable/Disable File Output

In `griddy_test.py`, control file output with:
```python
# Save to file
OUTPUT_FILE = "request_comparison.log"

# Or disable file output (console only)
OUTPUT_FILE = None
```

### Custom File Names

Use dynamic file names with timestamps:
```python
from datetime import datetime
OUTPUT_FILE = f"comparison_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
```

## Tips

1. **Start simple**: Compare one endpoint at a time
2. **Focus on differences**: The ✗ marks show what's different
3. **Check important headers first**: authorization, cookie, user-agent
4. **Use cookie comparison**: Individual cookies are parsed and compared separately
5. **Use with SDK debug logging**: Set `GRIDDY_NFL_DEBUG=1`
6. **Use file output**: Set `OUTPUT_FILE` for detailed analysis
7. **Compare both displays**: Look at direct request details AND SDK request details before comparing

## See Also

- `griddy_test.py` - Example implementation
- `src/griddy/nfl/basesdk.py:235-241` - SDK's built-in request logging
- `src/griddy/nfl/utils/logger.py` - SDK logging configuration
