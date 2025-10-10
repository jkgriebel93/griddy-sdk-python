<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.content.get_game_preview(request={
        "season": 2025,
        "season_type": models.SeasonTypeEnum.REG,
        "week": 4,
        "visitor_display_name": "Minnesota Vikings",
        "home_display_name": "Pittsburgh Steelers",
    })

    assert res is not None

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from griddy_nfl import GriddyNFL, models

async def main():

    async with GriddyNFL(
        server_url="https://api.example.com",
        nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as gn_client:

        res = await gn_client.content.get_game_preview_async(request={
            "season": 2025,
            "season_type": models.SeasonTypeEnum.REG,
            "week": 4,
            "visitor_display_name": "Minnesota Vikings",
            "home_display_name": "Pittsburgh Steelers",
        })

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->