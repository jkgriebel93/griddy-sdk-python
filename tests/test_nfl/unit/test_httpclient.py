"""
Unit tests for griddy.nfl.httpclient module
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import httpx
import pytest

from griddy.nfl.httpclient import (
    AsyncHttpClient,
    ClientOwner,
    HttpClient,
    close_clients,
)


@pytest.mark.unit
class TestHttpClientProtocol:
    """Test cases for HttpClient protocol"""

    def test_httpx_client_implements_protocol(self):
        """Test that httpx.Client implements HttpClient protocol"""
        client = httpx.Client()

        assert isinstance(client, HttpClient)
        assert hasattr(client, "send")
        assert hasattr(client, "build_request")
        assert hasattr(client, "close")

        client.close()

    def test_http_client_send_method(self):
        """Test HttpClient send method"""
        client = httpx.Client()

        request = client.build_request("GET", "https://httpbin.org/get")
        # We're just testing that the protocol is satisfied, not making real requests
        assert callable(client.send)

        client.close()

    def test_http_client_build_request_method(self):
        """Test HttpClient build_request method"""
        client = httpx.Client()

        request = client.build_request(
            "POST",
            "https://example.com/api",
            json={"key": "value"},
            headers={"X-Custom": "header"},
        )

        assert isinstance(request, httpx.Request)
        assert request.method == "POST"
        assert "example.com" in str(request.url)

        client.close()

    def test_http_client_close_method(self):
        """Test HttpClient close method"""
        client = httpx.Client()

        # Should not raise
        client.close()

        # Closing again should also not raise
        client.close()


@pytest.mark.unit
class TestAsyncHttpClientProtocol:
    """Test cases for AsyncHttpClient protocol"""

    def test_httpx_async_client_implements_protocol(self):
        """Test that httpx.AsyncClient implements AsyncHttpClient protocol"""
        client = httpx.AsyncClient()

        assert isinstance(client, AsyncHttpClient)
        assert hasattr(client, "send")
        assert hasattr(client, "build_request")
        assert hasattr(client, "aclose")

    @pytest.mark.asyncio
    async def test_async_http_client_send_method(self):
        """Test AsyncHttpClient send method"""
        async with httpx.AsyncClient() as client:
            request = client.build_request("GET", "https://httpbin.org/get")
            assert callable(client.send)

    @pytest.mark.asyncio
    async def test_async_http_client_build_request_method(self):
        """Test AsyncHttpClient build_request method"""
        async with httpx.AsyncClient() as client:
            request = client.build_request(
                "PUT",
                "https://example.com/api/resource",
                json={"data": "value"},
                params={"param": "value"},
            )

            assert isinstance(request, httpx.Request)
            assert request.method == "PUT"
            assert "example.com" in str(request.url)

    @pytest.mark.asyncio
    async def test_async_http_client_aclose_method(self):
        """Test AsyncHttpClient aclose method"""
        client = httpx.AsyncClient()

        # Should not raise
        await client.aclose()

        # Closing again should also not raise
        await client.aclose()


@pytest.mark.unit
class TestClientOwnerProtocol:
    """Test cases for ClientOwner protocol"""

    def test_client_owner_with_both_clients(self):
        """Test ClientOwner with both sync and async clients"""

        class TestOwner:
            def __init__(self):
                self.client = httpx.Client()
                self.async_client = httpx.AsyncClient()

        owner = TestOwner()

        assert isinstance(owner.client, HttpClient)
        assert isinstance(owner.async_client, AsyncHttpClient)

    def test_client_owner_with_none_clients(self):
        """Test ClientOwner with None clients"""

        class TestOwner:
            def __init__(self):
                self.client = None
                self.async_client = None

        owner = TestOwner()

        assert owner.client is None
        assert owner.async_client is None

    def test_client_owner_protocol_attributes(self):
        """Test that ClientOwner protocol requires client attributes"""

        class ValidOwner:
            client = None
            async_client = None

        owner = ValidOwner()


@pytest.mark.unit
class TestCloseClients:
    """Test cases for close_clients function"""

    def test_close_clients_with_user_supplied_clients(self):
        """Test close_clients when clients are user-supplied (should not close them)"""
        sync_client = Mock(spec=HttpClient)
        async_client = Mock(spec=AsyncHttpClient)

        owner = Mock(spec=ClientOwner)
        owner.client = sync_client
        owner.async_client = async_client

        # User supplied both clients
        close_clients(
            owner,
            sync_client,
            sync_client_supplied=True,
            async_client=async_client,
            async_client_supplied=True,
        )

        # Clients should NOT be closed when user-supplied
        sync_client.close.assert_not_called()
        # Owner references should be cleared
        assert owner.client is None
        assert owner.async_client is None

    def test_close_clients_with_sdk_created_sync_client(self):
        """Test close_clients when sync client was created by SDK"""
        sync_client = Mock(spec=HttpClient)
        owner = Mock(spec=ClientOwner)
        owner.client = sync_client
        owner.async_client = None

        # SDK created the sync client
        close_clients(
            owner,
            sync_client,
            sync_client_supplied=False,
            async_client=None,
            async_client_supplied=True,
        )

        # SDK-created client should be closed
        sync_client.close.assert_called_once()
        assert owner.client is None

    def test_close_clients_handles_sync_close_exception(self):
        """Test close_clients handles exceptions during sync client close"""
        sync_client = Mock(spec=HttpClient)
        sync_client.close.side_effect = Exception("Close failed")

        owner = Mock(spec=ClientOwner)
        owner.client = sync_client
        owner.async_client = None

        # Should not raise even if close fails
        close_clients(
            owner,
            sync_client,
            sync_client_supplied=False,
            async_client=None,
            async_client_supplied=True,
        )

        sync_client.close.assert_called_once()
        assert owner.client is None

    @pytest.mark.asyncio
    async def test_close_clients_with_sdk_created_async_client_no_loop(self):
        """Test close_clients with SDK-created async client (no running loop)"""
        async_client = Mock(spec=AsyncHttpClient)
        async_client.aclose = AsyncMock()

        owner = Mock(spec=ClientOwner)
        owner.client = None
        owner.async_client = async_client

        # Mock get_running_loop to raise RuntimeError (no loop)
        with patch("asyncio.get_running_loop", side_effect=RuntimeError("No loop")):
            with patch("asyncio.run") as mock_run:
                close_clients(
                    owner,
                    sync_client=None,
                    sync_client_supplied=True,
                    async_client=async_client,
                    async_client_supplied=False,
                )

                # Should call asyncio.run to close the client
                mock_run.assert_called_once()

        assert owner.async_client is None

    def test_close_clients_with_none_clients(self):
        """Test close_clients when both clients are None"""
        owner = Mock(spec=ClientOwner)
        owner.client = None
        owner.async_client = None

        # Should not raise
        close_clients(
            owner,
            sync_client=None,
            sync_client_supplied=False,
            async_client=None,
            async_client_supplied=False,
        )

        assert owner.client is None
        assert owner.async_client is None

    def test_close_clients_clears_owner_references(self):
        """Test that close_clients always clears owner references"""
        sync_client = Mock(spec=HttpClient)
        async_client = Mock(spec=AsyncHttpClient)

        owner = Mock(spec=ClientOwner)
        owner.client = sync_client
        owner.async_client = async_client

        close_clients(
            owner,
            sync_client,
            sync_client_supplied=True,
            async_client=async_client,
            async_client_supplied=True,
        )

        # References should be cleared regardless of supplied status
        assert owner.client is None
        assert owner.async_client is None

    def test_close_clients_handles_async_close_best_effort(self):
        """Test close_clients handles async close failures gracefully"""
        async_client = Mock(spec=AsyncHttpClient)
        async_client.aclose = AsyncMock()

        owner = Mock(spec=ClientOwner)
        owner.client = None
        owner.async_client = async_client

        # Mock both get_running_loop and asyncio.run to fail
        with patch("asyncio.get_running_loop", side_effect=RuntimeError("No loop")):
            with patch("asyncio.run", side_effect=RuntimeError("Cannot run")):
                # Should not raise - best effort
                close_clients(
                    owner,
                    sync_client=None,
                    sync_client_supplied=True,
                    async_client=async_client,
                    async_client_supplied=False,
                )

        assert owner.async_client is None


@pytest.mark.unit
class TestProtocolCompatibility:
    """Test protocol compatibility with various implementations"""

    def test_custom_http_client_implementation(self):
        """Test that custom HttpClient implementations satisfy the protocol"""

        class CustomHttpClient:
            def send(self, request, *, stream=False, auth=None, follow_redirects=None):
                return httpx.Response(
                    status_code=200,
                    request=request,
                )

            def build_request(
                self,
                method,
                url,
                *,
                content=None,
                data=None,
                files=None,
                json=None,
                params=None,
                headers=None,
                cookies=None,
                timeout=None,
                extensions=None,
            ):
                return httpx.Request(method, url)

            def close(self):
                pass

        custom_client = CustomHttpClient()
        assert isinstance(custom_client, HttpClient)

    def test_custom_async_http_client_implementation(self):
        """Test that custom AsyncHttpClient implementations satisfy the protocol"""

        class CustomAsyncHttpClient:
            async def send(
                self, request, *, stream=False, auth=None, follow_redirects=None
            ):
                return httpx.Response(
                    status_code=200,
                    request=request,
                )

            def build_request(
                self,
                method,
                url,
                *,
                content=None,
                data=None,
                files=None,
                json=None,
                params=None,
                headers=None,
                cookies=None,
                timeout=None,
                extensions=None,
            ):
                return httpx.Request(method, url)

            async def aclose(self):
                pass

        custom_client = CustomAsyncHttpClient()
        assert isinstance(custom_client, AsyncHttpClient)

    def test_mock_clients_satisfy_protocols(self):
        """Test that mocked clients satisfy the protocols"""
        sync_mock = Mock(spec=HttpClient)
        async_mock = Mock(spec=AsyncHttpClient)

        assert isinstance(sync_mock, HttpClient)
        assert isinstance(async_mock, AsyncHttpClient)
