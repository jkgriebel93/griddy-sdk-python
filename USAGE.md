<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from griddy.nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as griddy_nfl:

    res = griddy_nfl.content.get_game_preview(season=2025, season_type=models.SeasonTypeEnum.REG, week=4, visitor_display_name="Minnesota Vikings", home_display_name="Pittsburgh Steelers")

    assert res is not None

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from griddy.nfl import GriddyNFL, models

async def main():

    async with GriddyNFL(
        server_url="https://api.example.com",
        nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as griddy_nfl:

        res = await griddy_nfl.content.get_game_preview_async(season=2025, season_type=models.SeasonTypeEnum.REG, week=4, visitor_display_name="Minnesota Vikings", home_display_name="Pittsburgh Steelers")

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->