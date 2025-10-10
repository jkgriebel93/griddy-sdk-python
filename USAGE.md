<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from openapi import SDK


with SDK(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.content.get_game_preview(season=2025, season_type="REG", week=4, visitor_display_name="Minnesota Vikings", home_display_name="Pittsburgh Steelers")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from openapi import SDK

async def main():

    async with SDK(
        server_url="https://api.example.com",
        nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as sdk:

        res = await sdk.content.get_game_preview_async(season=2025, season_type="REG", week=4, visitor_display_name="Minnesota Vikings", home_display_name="Pittsburgh Steelers")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->