"""Tests for PFR BaseSDK async support."""

from unittest.mock import AsyncMock, Mock

import httpx
import pytest

from griddy.core.utils.logger import Logger
from griddy.pfr.basesdk import BaseSDK, EndpointConfig
from griddy.pfr.errors import ParsingError
from griddy.pfr.sdkconfiguration import SDKConfiguration


@pytest.fixture
def mock_logger():
    return Mock(spec=Logger)


@pytest.fixture
def pfr_base_sdk(mock_logger):
    config = SDKConfiguration(
        client=httpx.Client(),
        client_supplied=False,
        async_client=None,
        async_client_supplied=True,
        debug_logger=mock_logger,
    )
    return BaseSDK(sdk_config=config)


@pytest.mark.unit
class TestPFRBaseSDKAsync:
    def test_has_async_browserless(self, pfr_base_sdk):
        from griddy.pfr.utils.browserless import AsyncBrowserless

        assert isinstance(pfr_base_sdk.async_browserless, AsyncBrowserless)

    @pytest.mark.asyncio
    async def test_execute_endpoint_async_calls_async_browserless(self, pfr_base_sdk):
        config = EndpointConfig(
            path_template="/years/{season}/games.htm",
            operation_id="getSeasonSchedule",
            wait_for_element="#games",
            parser=lambda html: [{"game": "data"}],
            response_type=dict,
            path_params={"season": 2024},
        )

        pfr_base_sdk.async_browserless = Mock()
        pfr_base_sdk.async_browserless.get_page_content = AsyncMock(
            return_value="<html>mock</html>"
        )

        result = await pfr_base_sdk._execute_endpoint_async(config)

        pfr_base_sdk.async_browserless.get_page_content.assert_awaited_once_with(
            "https://www.pro-football-reference.com/years/2024/games.htm",
            wait_for_element="#games",
        )
        assert result == [{"game": "data"}]

    @pytest.mark.asyncio
    async def test_execute_endpoint_async_enriches_parsing_error_with_url(
        self, pfr_base_sdk
    ):
        def bad_parser(html):
            raise ParsingError(
                "Could not find table", selector="games", html_sample=html[:500]
            )

        config = EndpointConfig(
            path_template="/years/{season}/games.htm",
            operation_id="get_schedule",
            wait_for_element="table#games",
            parser=bad_parser,
            response_type=dict,
            path_params={"season": 2024},
        )

        pfr_base_sdk.async_browserless = Mock()
        pfr_base_sdk.async_browserless.get_page_content = AsyncMock(
            return_value="<html></html>"
        )

        with pytest.raises(ParsingError) as exc_info:
            await pfr_base_sdk._execute_endpoint_async(config)

        err = exc_info.value
        assert err.selector == "games"
        assert err.url is not None
        assert "/years/2024/games.htm" in err.url
        assert err.html_sample == "<html></html>"

    @pytest.mark.asyncio
    async def test_execute_endpoint_async_with_validate_model(self, pfr_base_sdk):
        from pydantic import BaseModel

        class FakeModel(BaseModel):
            name: str
            value: int

        config = EndpointConfig(
            path_template="/test/{id}",
            operation_id="test",
            wait_for_element="#el",
            parser=lambda html: {"name": "test", "value": 42},
            response_type=FakeModel,
            path_params={"id": "1"},
            validate_model=True,
        )

        pfr_base_sdk.async_browserless = Mock()
        pfr_base_sdk.async_browserless.get_page_content = AsyncMock(
            return_value="<html/>"
        )

        result = await pfr_base_sdk._execute_endpoint_async(config)

        assert isinstance(result, FakeModel)
        assert result.name == "test"
        assert result.value == 42

    @pytest.mark.asyncio
    async def test_execute_endpoint_async_without_validate_model(self, pfr_base_sdk):
        config = EndpointConfig(
            path_template="/test/{id}",
            operation_id="test",
            wait_for_element="#el",
            parser=lambda html: {"raw": "data"},
            response_type=dict,
            path_params={"id": "1"},
            validate_model=False,
        )

        pfr_base_sdk.async_browserless = Mock()
        pfr_base_sdk.async_browserless.get_page_content = AsyncMock(
            return_value="<html/>"
        )

        result = await pfr_base_sdk._execute_endpoint_async(config)

        assert result == {"raw": "data"}
        assert isinstance(result, dict)

    @pytest.mark.asyncio
    async def test_execute_endpoint_async_with_query_params(self, pfr_base_sdk):
        config = EndpointConfig(
            path_template="/test",
            operation_id="test",
            wait_for_element="#el",
            parser=lambda html: "ok",
            response_type=str,
            query_params={"foo": "bar", "baz": "qux"},
        )

        pfr_base_sdk.async_browserless = Mock()
        pfr_base_sdk.async_browserless.get_page_content = AsyncMock(
            return_value="<html/>"
        )

        await pfr_base_sdk._execute_endpoint_async(config)

        call_args = pfr_base_sdk.async_browserless.get_page_content.call_args
        url = call_args[0][0]
        assert "foo=bar" in url
        assert "baz=qux" in url


@pytest.mark.unit
class TestPFRBaseSDKValidateModel:
    def test_execute_endpoint_with_validate_model(self, pfr_base_sdk):
        from pydantic import BaseModel

        class FakeModel(BaseModel):
            name: str
            value: int

        config = EndpointConfig(
            path_template="/test/{id}",
            operation_id="test",
            wait_for_element="#el",
            parser=lambda html: {"name": "test", "value": 42},
            response_type=FakeModel,
            path_params={"id": "1"},
            validate_model=True,
        )

        pfr_base_sdk.browserless = Mock()
        pfr_base_sdk.browserless.get_page_content.return_value = "<html/>"

        result = pfr_base_sdk._execute_endpoint(config)

        assert isinstance(result, FakeModel)
        assert result.name == "test"
        assert result.value == 42

    def test_execute_endpoint_without_validate_model(self, pfr_base_sdk):
        config = EndpointConfig(
            path_template="/test/{id}",
            operation_id="test",
            wait_for_element="#el",
            parser=lambda html: {"raw": "data"},
            response_type=dict,
            path_params={"id": "1"},
            validate_model=False,
        )

        pfr_base_sdk.browserless = Mock()
        pfr_base_sdk.browserless.get_page_content.return_value = "<html/>"

        result = pfr_base_sdk._execute_endpoint(config)

        assert result == {"raw": "data"}
