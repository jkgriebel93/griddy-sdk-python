"""Tests for griddy.pfr.basesdk module."""

from typing import Any, Dict, List, Union
from unittest.mock import Mock

import httpx
import pytest

from griddy.core.basesdk import BaseSDK as CoreBaseSDK
from griddy.core.utils.logger import Logger
from griddy.pfr.basesdk import BaseSDK, EndpointConfig, PfrParser
from griddy.pfr.errors import ParsingError
from griddy.pfr.errors.griddypfrdefaulterror import GriddyPFRDefaultError
from griddy.pfr.errors.no_response_error import NoResponseError
from griddy.pfr.models.entities.security import Security
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
class TestPFRBaseSDK:
    def test_inherits_from_core(self):
        assert issubclass(BaseSDK, CoreBaseSDK)

    def test_default_error_cls(self, pfr_base_sdk):
        assert pfr_base_sdk._default_error_cls is GriddyPFRDefaultError

    def test_no_response_error_cls(self, pfr_base_sdk):
        assert pfr_base_sdk._no_response_error_cls is NoResponseError

    def test_security_model_cls(self, pfr_base_sdk):
        assert pfr_base_sdk._security_model_cls is Security

    def test_security_env_mapping(self, pfr_base_sdk):
        assert pfr_base_sdk._security_env_mapping == {"pfr_auth": "GRIDDY_PFR_AUTH"}

    def test_execute_endpoint_enriches_parsing_error_with_url(self, pfr_base_sdk):
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

        pfr_base_sdk.browserless = Mock()
        pfr_base_sdk.browserless.get_page_content.return_value = "<html></html>"

        with pytest.raises(ParsingError) as exc_info:
            pfr_base_sdk._execute_endpoint(config)

        err = exc_info.value
        assert err.selector == "games"
        assert err.url is not None
        assert "/years/2024/games.htm" in err.url
        assert err.html_sample == "<html></html>"


@pytest.mark.unit
class TestPreprocessHtml:
    """Tests for BaseSDK._preprocess_html static method."""

    def test_uncomments_table_in_html_comment(self):
        html = (
            "<html><body>"
            '<!--<table id="hidden"><tr><td>data</td></tr></table>-->'
            "</body></html>"
        )
        result = BaseSDK._preprocess_html(html)
        assert '<table id="hidden">' in result
        assert "<!--" not in result

    def test_leaves_html_without_comments_unchanged(self):
        html = '<html><body><table id="visible"><tr><td>data</td></tr></table></body></html>'
        result = BaseSDK._preprocess_html(html)
        assert '<table id="visible">' in result

    def test_preserves_non_table_comments(self):
        html = "<html><body><!-- just a comment --><p>text</p></body></html>"
        result = BaseSDK._preprocess_html(html)
        assert "<!-- just a comment -->" in result

    def test_uncomments_multiple_tables(self):
        html = (
            "<html><body>"
            '<!--<table id="t1"><tr><td>a</td></tr></table>-->'
            '<!--<table id="t2"><tr><td>b</td></tr></table>-->'
            "</body></html>"
        )
        result = BaseSDK._preprocess_html(html)
        assert '<table id="t1">' in result
        assert '<table id="t2">' in result

    def test_execute_endpoint_preprocesses_before_parsing(self, pfr_base_sdk):
        """Verify _execute_endpoint passes preprocessed HTML to the parser."""
        received_html = []

        def capturing_parser(html):
            received_html.append(html)
            return {"ok": True}

        config = EndpointConfig(
            path_template="/test.htm",
            operation_id="test_op",
            wait_for_element="table#hidden",
            parser=capturing_parser,
            response_type=Mock(),
        )
        config.response_type.model_validate = lambda d: d

        pfr_base_sdk.browserless = Mock()
        pfr_base_sdk.browserless.get_page_content.return_value = (
            '<html><!--<table id="hidden"><tr><td>x</td></tr></table>--></html>'
        )

        pfr_base_sdk._execute_endpoint(config)

        assert len(received_html) == 1
        assert '<table id="hidden">' in received_html[0]
        assert "<!--" not in received_html[0]


@pytest.mark.unit
class TestPfrParserProtocol:
    def test_lambda_returning_dict_satisfies_protocol(self):
        parser: PfrParser = lambda html: {"key": "value"}
        result = parser("<html/>")
        assert isinstance(result, dict)

    def test_lambda_returning_list_satisfies_protocol(self):
        parser: PfrParser = lambda html: [{"key": "value"}]
        result = parser("<html/>")
        assert isinstance(result, list)

    def test_callable_class_satisfies_protocol(self):
        class MyParser:
            def __call__(
                self, html: str
            ) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
                return {"parsed": True}

        parser: PfrParser = MyParser()
        result = parser("<html/>")
        assert result == {"parsed": True}
