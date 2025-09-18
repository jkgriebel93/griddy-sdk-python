"""Tests for cookie extraction utilities."""

import pytest
from datetime import datetime, timezone
from pathlib import Path
import tempfile
import os

from griddy.core.utils import (
    Cookie,
    parse_cookies_txt,
    extract_cookies_for_url,
    cookies_to_dict,
    cookies_to_header,
    extract_cookies_as_dict,
    extract_cookies_as_header
)


class TestCookie:
    """Test cases for Cookie class."""

    def test_cookie_creation(self):
        """Test creating a cookie object."""
        cookie = Cookie(
            domain="example.com",
            path="/",
            secure=True,
            expires=None,
            name="session_id",
            value="abc123",
            include_subdomains=False
        )

        assert cookie.domain == "example.com"
        assert cookie.name == "session_id"
        assert cookie.value == "abc123"
        assert cookie.secure is True
        assert cookie.expires is None

    def test_cookie_expiration_check(self):
        """Test cookie expiration checking."""
        # Non-expiring cookie
        cookie = Cookie("example.com", "/", False, None, "test", "value")
        assert not cookie.is_expired

        # Expired cookie
        past_timestamp = int(datetime(2020, 1, 1).timestamp())
        expired_cookie = Cookie("example.com", "/", False, past_timestamp, "test", "value")
        assert expired_cookie.is_expired

        # Future cookie
        future_timestamp = int(datetime(2030, 1, 1).timestamp())
        future_cookie = Cookie("example.com", "/", False, future_timestamp, "test", "value")
        assert not future_cookie.is_expired

    def test_domain_matching(self):
        """Test domain matching logic."""
        # Exact domain match
        cookie = Cookie("example.com", "/", False, None, "test", "value")
        assert cookie.matches_domain("example.com")
        assert not cookie.matches_domain("other.com")
        assert not cookie.matches_domain("sub.example.com")

        # Subdomain cookie (starts with .)
        subdomain_cookie = Cookie(".example.com", "/", False, None, "test", "value")
        assert subdomain_cookie.matches_domain("example.com")
        assert subdomain_cookie.matches_domain("sub.example.com")
        assert subdomain_cookie.matches_domain("deep.sub.example.com")
        assert not subdomain_cookie.matches_domain("other.com")

        # Include subdomains flag
        include_subs = Cookie("example.com", "/", False, None, "test", "value", include_subdomains=True)
        assert include_subs.matches_domain("example.com")
        assert include_subs.matches_domain("sub.example.com")

    def test_path_matching(self):
        """Test path matching logic."""
        # Root path
        root_cookie = Cookie("example.com", "/", False, None, "test", "value")
        assert root_cookie.matches_path("/")
        assert root_cookie.matches_path("/any/path")

        # Specific path
        path_cookie = Cookie("example.com", "/admin", False, None, "test", "value")
        assert path_cookie.matches_path("/admin")
        assert path_cookie.matches_path("/admin/users")
        assert not path_cookie.matches_path("/")
        assert not path_cookie.matches_path("/user")

    def test_cookie_to_dict(self):
        """Test converting cookie to dictionary."""
        cookie = Cookie("example.com", "/", False, None, "session_id", "abc123")
        result = cookie.to_dict()
        assert result == {"session_id": "abc123"}

    def test_cookie_to_header_string(self):
        """Test converting cookie to header string."""
        cookie = Cookie("example.com", "/", False, None, "session_id", "abc123")
        result = cookie.to_header_string()
        assert result == "session_id=abc123"


class TestCookieFileParsing:
    """Test cases for cookie file parsing."""

    def create_temp_cookies_file(self, content: str) -> str:
        """Create a temporary cookies.txt file with given content."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(content)
            return f.name

    def teardown_method(self):
        """Clean up temporary files."""
        # This would be called after each test method
        pass

    def test_parse_valid_cookies_file(self):
        """Test parsing a valid cookies.txt file."""
        content = """# Netscape HTTP Cookie File
.example.com	TRUE	/	FALSE	1234567890	session_id	abc123
example.com	FALSE	/admin	TRUE	0	admin_token	def456
"""
        file_path = self.create_temp_cookies_file(content)

        try:
            cookies = parse_cookies_txt(file_path)

            assert len(cookies) == 2

            # First cookie
            assert cookies[0].domain == ".example.com"
            assert cookies[0].include_subdomains is True
            assert cookies[0].path == "/"
            assert cookies[0].secure is False
            assert cookies[0].expires == 1234567890
            assert cookies[0].name == "session_id"
            assert cookies[0].value == "abc123"

            # Second cookie
            assert cookies[1].domain == "example.com"
            assert cookies[1].include_subdomains is False
            assert cookies[1].path == "/admin"
            assert cookies[1].secure is True
            assert cookies[1].expires is None  # 0 means no expiration
            assert cookies[1].name == "admin_token"
            assert cookies[1].value == "def456"

        finally:
            os.unlink(file_path)

    def test_parse_file_with_comments_and_empty_lines(self):
        """Test parsing file with comments and empty lines."""
        content = """# This is a comment

# Another comment
.example.com	TRUE	/	FALSE	1234567890	test	value

"""
        file_path = self.create_temp_cookies_file(content)

        try:
            cookies = parse_cookies_txt(file_path)
            assert len(cookies) == 1
            assert cookies[0].name == "test"
        finally:
            os.unlink(file_path)

    def test_parse_nonexistent_file(self):
        """Test parsing a non-existent file."""
        with pytest.raises(FileNotFoundError):
            parse_cookies_txt("/nonexistent/path/cookies.txt")

    def test_parse_invalid_format(self):
        """Test parsing file with invalid format lines."""
        content = """invalid line
.example.com	TRUE	/	FALSE	1234567890	valid	cookie
incomplete	line
"""
        file_path = self.create_temp_cookies_file(content)

        try:
            cookies = parse_cookies_txt(file_path)
            # Should only parse the valid line
            assert len(cookies) == 1
            assert cookies[0].name == "valid"
        finally:
            os.unlink(file_path)


class TestCookieExtraction:
    """Test cases for URL-specific cookie extraction."""

    def create_test_cookies_file(self) -> str:
        """Create a test cookies file."""
        content = """# Test cookies file
.example.com	TRUE	/	FALSE	1234567890	global_session	abc123
example.com	FALSE	/	FALSE	0	exact_match	def456
.example.com	TRUE	/admin	TRUE	0	admin_secure	ghi789
other.com	FALSE	/	FALSE	0	other_cookie	jkl012
sub.example.com	FALSE	/	FALSE	0	subdomain_only	mno345
"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(content)
            return f.name

    def test_extract_cookies_for_domain(self):
        """Test extracting cookies for a specific domain."""
        file_path = self.create_test_cookies_file()

        try:
            # Test exact domain match
            cookies = extract_cookies_for_url(file_path, "https://example.com/")
            cookie_names = [c.name for c in cookies]

            # Should match: global_session (.example.com), exact_match (example.com)
            assert "global_session" in cookie_names
            assert "exact_match" in cookie_names
            assert "other_cookie" not in cookie_names

            # Test subdomain
            cookies = extract_cookies_for_url(file_path, "https://sub.example.com/")
            cookie_names = [c.name for c in cookies]

            # Should match: global_session (.example.com), subdomain_only (sub.example.com)
            assert "global_session" in cookie_names
            assert "subdomain_only" in cookie_names
            assert "exact_match" not in cookie_names

        finally:
            os.unlink(file_path)

    def test_extract_cookies_with_path_matching(self):
        """Test extracting cookies with path-specific matching."""
        file_path = self.create_test_cookies_file()

        try:
            # Test root path
            cookies = extract_cookies_for_url(file_path, "https://example.com/")
            cookie_names = [c.name for c in cookies]

            # admin_secure should not match root path
            assert "admin_secure" not in cookie_names

            # Test admin path
            cookies = extract_cookies_for_url(file_path, "https://example.com/admin/users")
            cookie_names = [c.name for c in cookies]

            # admin_secure should match admin path
            assert "admin_secure" in cookie_names

        finally:
            os.unlink(file_path)

    def test_extract_cookies_https_vs_http(self):
        """Test extracting cookies with secure flag consideration."""
        file_path = self.create_test_cookies_file()

        try:
            # HTTPS should include secure cookies
            https_cookies = extract_cookies_for_url(file_path, "https://example.com/admin")
            https_names = [c.name for c in https_cookies]
            assert "admin_secure" in https_names

            # HTTP should exclude secure cookies
            http_cookies = extract_cookies_for_url(file_path, "http://example.com/admin")
            http_names = [c.name for c in http_cookies]
            assert "admin_secure" not in http_names

        finally:
            os.unlink(file_path)

    def test_extract_cookies_as_dict(self):
        """Test extracting cookies as dictionary."""
        file_path = self.create_test_cookies_file()

        try:
            result = extract_cookies_as_dict(file_path, "https://example.com/")

            assert isinstance(result, dict)
            assert "global_session" in result
            assert "exact_match" in result
            assert result["global_session"] == "abc123"
            assert result["exact_match"] == "def456"

        finally:
            os.unlink(file_path)

    def test_extract_cookies_as_header(self):
        """Test extracting cookies as header string."""
        file_path = self.create_test_cookies_file()

        try:
            result = extract_cookies_as_header(file_path, "https://example.com/")

            assert isinstance(result, str)
            assert "global_session=abc123" in result
            assert "exact_match=def456" in result
            assert "; " in result  # Should be properly formatted

        finally:
            os.unlink(file_path)

    def test_extract_invalid_url(self):
        """Test extracting cookies with invalid URL."""
        file_path = self.create_test_cookies_file()

        try:
            with pytest.raises(ValueError):
                extract_cookies_for_url(file_path, "not-a-valid-url")

        finally:
            os.unlink(file_path)


class TestCookieUtilities:
    """Test cases for cookie utility functions."""

    def test_cookies_to_dict(self):
        """Test converting list of cookies to dictionary."""
        cookies = [
            Cookie("example.com", "/", False, None, "cookie1", "value1"),
            Cookie("example.com", "/", False, None, "cookie2", "value2")
        ]

        result = cookies_to_dict(cookies)

        assert result == {"cookie1": "value1", "cookie2": "value2"}

    def test_cookies_to_header(self):
        """Test converting list of cookies to header string."""
        cookies = [
            Cookie("example.com", "/", False, None, "cookie1", "value1"),
            Cookie("example.com", "/", False, None, "cookie2", "value2")
        ]

        result = cookies_to_header(cookies)

        assert result == "cookie1=value1; cookie2=value2"

    def test_empty_cookies_to_header(self):
        """Test converting empty list of cookies to header string."""
        result = cookies_to_header([])
        assert result == ""


if __name__ == "__main__":
    pytest.main([__file__])