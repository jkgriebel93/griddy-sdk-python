"""Utility functions for Griddy SDK."""

import json
import time

from collections import defaultdict
from functools import wraps
from datetime import datetime, timezone
from typing import TypeVar, Callable, Dict, List
from urllib.parse import urlparse
from pathlib import Path
import re

T = TypeVar("T")


def retry_on_rate_limit(max_retries: int = 3, backoff_factor: float = 1.0) -> Callable:
    """
    Decorator to retry function calls on rate limit errors.

    Args:
        max_retries: Maximum number of retry attempts
        backoff_factor: Factor for exponential backoff
    """

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> T:
            from .exceptions import RateLimitError

            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except RateLimitError as e:
                    if attempt == max_retries:
                        raise

                    # Calculate backoff time
                    backoff_time = backoff_factor * (2**attempt)
                    if e.retry_after:
                        backoff_time = max(backoff_time, e.retry_after)

                    time.sleep(backoff_time)

            return func(*args, **kwargs)  # This should never be reached

        return wrapper

    return decorator


def parse_date(date_str: str | None) -> datetime | None:
    """
    Parse date string into datetime object.

    Args:
        date_str: Date string in various formats

    Returns:
        Parsed datetime object or None
    """
    if not date_str:
        return None

    # Common date formats to try
    formats = [
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S.%f",
        "%Y-%m-%dT%H:%M:%S.%fZ",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d",
        "%m/%d/%Y",
        "%m/%d/%Y %H:%M:%S",
    ]

    for fmt in formats:
        try:
            dt = datetime.strptime(date_str, fmt)
            # Add timezone info if not present
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except ValueError:
            continue

    # If no format matches, return None
    return None


def clean_text(text: str | None) -> str | None:
    """
    Clean and normalize text data.

    Args:
        text: Text to clean

    Returns:
        Cleaned text or None
    """
    if not text:
        return None

    # Strip whitespace and normalize
    cleaned = text.strip()
    if not cleaned:
        return None

    return cleaned


def safe_int(value: any) -> int | None:
    """
    Safely convert value to integer.

    Args:
        value: Value to convert

    Returns:
        Integer value or None
    """
    if value is None:
        return None

    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def safe_float(value: any) -> float | None:
    """
    Safely convert value to float.

    Args:
        value: Value to convert

    Returns:
        Float value or None
    """
    if value is None:
        return None

    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def build_url(base_url: str, path: str, params: dict[str, any] | None = None) -> str:
    """
    Build URL from base URL, path, and parameters.

    Args:
        base_url: Base URL
        path: URL path
        params: Query parameters

    Returns:
        Complete URL
    """
    # Ensure base_url doesn't end with slash and path starts without slash
    base_url = base_url.rstrip("/")
    path = path.lstrip("/")

    url = f"{base_url}/{path}" if path else base_url

    if params:
        # Filter out None values
        filtered_params = {k: v for k, v in params.items() if v is not None}
        if filtered_params:
            from urllib.parse import urlencode

            url += f"?{urlencode(filtered_params)}"

    return url


class Cookie:
    """Represents a single HTTP cookie."""

    def __init__(
        self,
        domain: str,
        path: str,
        secure: bool,
        expires: int | None,
        name: str,
        value: str,
        http_only: bool = True,
        include_subdomains: bool = False,
    ):
        self.domain = domain
        self.path = path
        self.secure = secure
        self.expires = expires
        self.name = name
        self.value = value
        self.http_only = http_only
        self.include_subdomains = include_subdomains

    @property
    def is_expired(self) -> bool:
        """Check if the cookie is expired."""
        if self.expires is None:
            return False
        return datetime.now().timestamp() > self.expires

    def matches_domain(self, domain: str) -> bool:
        """Check if this cookie matches the given domain."""
        # Remove leading dot from cookie domain for comparison
        cookie_domain = self.domain.lstrip(".")
        target_domain = domain.lower()

        # Exact match
        if cookie_domain.lower() == target_domain:
            return True

        # Subdomain match (if cookie domain starts with .)
        if self.domain.startswith(".") or self.include_subdomains:
            return target_domain.endswith("." + cookie_domain.lower())

        return False

    def matches_path(self, path: str) -> bool:
        """Check if this cookie matches the given path."""
        if self.path == "/":
            return True
        return path.startswith(self.path)

    def to_dict(self) -> dict[str, str]:
        """Convert cookie to dictionary format."""
        return {self.name: self.value}

    def to_header_string(self) -> str:
        """Convert cookie to HTTP header format."""
        return f"{self.name}={self.value}"


def parse_cookies_txt(file_path: str | Path) -> list[Cookie]:
    """
    Parse a cookies.txt file and return a list of Cookie objects.

    Args:
        file_path: Path to the cookies.txt file

    Returns:
        List of Cookie objects

    Raises:
        FileNotFoundError: If the cookies file doesn't exist
        ValueError: If the file format is invalid
    """
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Cookies file not found: {file_path}")

    cookies = []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()

                # Skip empty lines and comments
                if not line or line.startswith("#"):
                    continue

                # Parse tab-separated values
                parts = line.split("\t")

                # Netscape cookie format should have 7 fields
                if len(parts) != 7:
                    continue

                try:
                    domain = parts[0]
                    include_subdomains = parts[1].upper() == "TRUE"
                    path = parts[2]
                    secure = parts[3].upper() == "TRUE"
                    expires_str = parts[4]
                    name = parts[5]
                    value = parts[6]

                    # Parse expiration time
                    expires = None
                    if expires_str and expires_str != "0":
                        try:
                            expires = int(expires_str)
                        except ValueError:
                            expires = None

                    cookie = Cookie(
                        domain=domain,
                        path=path,
                        secure=secure,
                        expires=expires,
                        name=name,
                        value=value,
                        include_subdomains=include_subdomains,
                    )

                    cookies.append(cookie)

                except (IndexError, ValueError) as e:
                    # Log the error but continue parsing
                    continue

    except UnicodeDecodeError:
        raise ValueError(f"Invalid file encoding in {file_path}")

    return cookies


def extract_cookies_for_url(
    cookies_file: str | Path, target_url: str, include_expired: bool = False
) -> list[Cookie]:
    """
    Extract cookies that match a specific URL from a cookies.txt file.

    Args:
        cookies_file: Path to the cookies.txt file
        target_url: URL to match cookies against
        include_expired: Whether to include expired cookies

    Returns:
        List of matching Cookie objects

    Raises:
        FileNotFoundError: If the cookies file doesn't exist
        ValueError: If the URL or file format is invalid
    """
    # Parse the target URL
    try:
        parsed_url = urlparse(target_url)
        domain = parsed_url.netloc.lower()
        path = parsed_url.path or "/"
        is_https = parsed_url.scheme.lower() == "https"
    except Exception:
        raise ValueError(f"Invalid URL: {target_url}")

    # Parse all cookies from file
    all_cookies = parse_cookies_txt(cookies_file)

    # Filter cookies that match the URL
    matching_cookies = []

    for cookie in all_cookies:
        # Skip expired cookies unless requested
        if not include_expired and cookie.is_expired:
            continue

        # Skip secure cookies on non-HTTPS URLs
        if cookie.secure and not is_https:
            continue

        # Check domain match
        if not cookie.matches_domain(domain):
            continue

        # Check path match
        if not cookie.matches_path(path):
            continue

        matching_cookies.append(cookie)

    return matching_cookies


def cookies_to_dict(cookies: list[Cookie]) -> dict[str, str]:
    """
    Convert a list of cookies to a dictionary format.

    Args:
        cookies: List of Cookie objects

    Returns:
        Dictionary with cookie names as keys and values as values
    """
    result = {}
    for cookie in cookies:
        result[cookie.name] = cookie.value
    return result


def cookies_to_header(cookies: list[Cookie]) -> str:
    """
    Convert a list of cookies to a Cookie header string.

    Args:
        cookies: List of Cookie objects

    Returns:
        Cookie header string (e.g., "name1=value1; name2=value2")
    """
    if not cookies:
        return ""

    return "; ".join(cookie.to_header_string() for cookie in cookies)


def extract_cookies_as_dict(
    cookies_file: str | Path, target_url: str, include_expired: bool = False
) -> dict[str, str]:
    """
    Extract cookies for a URL and return as a dictionary.

    Args:
        cookies_file: Path to the cookies.txt file
        target_url: URL to match cookies against
        include_expired: Whether to include expired cookies

    Returns:
        Dictionary with cookie names as keys and values as values
    """
    cookies = extract_cookies_for_url(cookies_file, target_url, include_expired)
    return cookies_to_dict(cookies)


def extract_cookies_as_header(
    cookies_file: str | Path, target_url: str, include_expired: bool = False
) -> str:
    """
    Extract cookies for a URL and return as a Cookie header string.

    Args:
        cookies_file: Path to the cookies.txt file
        target_url: URL to match cookies against
        include_expired: Whether to include expired cookies

    Returns:
        Cookie header string suitable for HTTP requests
    """
    cookies = extract_cookies_for_url(cookies_file, target_url, include_expired)
    return cookies_to_header(cookies)


def extract_minified_har_entry(har_entry: Dict):
    response_json = json.loads(har_entry["response"]["content"]["text"])
    request_info = {key: value for key, value in har_entry["request"].items()
                    if key in ["url", "headers", "queryString", "method", "path"]}

    url = request_info.pop("url")
    path_with_params = url.split(".com")[-1]
    path_only = path_with_params.split("?")[0]

    request_info["path"] = path_only

    return {
        "request": request_info,
        "response": response_json
    }

class HarEntryPathManager:
    def __init__(self, path: str, filename_prefix: str):
        self.path = path
        self.headers = {}
        self.query_params = defaultdict(set)
        # Not sure if we'll use this
        self.cookies = {}

        # Can we get away with just one?
        # if not, do we need to map params to the response?
        self.response_example = None
        self.filename_prefix = filename_prefix

    @property
    def filename(self):
        sub_name = ""
        for node in self.path.split("/"):
            if node == "api":
                continue
            sub_name += "_" + node.title()

        name = f"{self.filename_prefix}{sub_name}.json"
        return name.replace("-", "").replace("__", "_")

    def as_dict(self, exclude: List[str]) -> Dict:
        obj_dict = {}

        for attr in ["path", "headers", "query_params", "response_example"]:
            if attr in exclude:
                continue
            value = getattr(self, attr)
            if attr == "query_params":
                value = {
                    name: list(param_values)
                    for name, param_values
                    in value.items()
                }

            obj_dict[attr] = value

        return obj_dict

    def add_entry(self, entry: Dict):
        if entry["request"]["path"] != self.path:
            raise ValueError(f"Entry path {entry['request']['path']} "
                             f"does not match the class path {self.path}")

        for req_header in entry["request"]["headers"]:
            header = req_header["name"]
            value = req_header["value"]
            self.headers[header] = value

        for qp in entry["request"]["queryString"]:
            name = qp["name"]
            val = qp["value"]
            self.query_params[name].add(val)

        if entry["response"]:
            self.response_example = entry["response"]

def consolidate_minified_entries(entries: List[Dict]) -> Dict[str, HarEntryPathManager]:
    consolidated = {}

    for entry in entries:
        api_path = entry["request"]["path"]
        if api_path not in consolidated:
            consolidated[api_path] = HarEntryPathManager(path=api_path, filename_prefix="FiddlerSnapshots/ProNFL")

        consolidated[api_path].add_entry(entry=entry)

    return consolidated


def write_consolidated_to_files(consolidated: Dict[str, HarEntryPathManager], exclude: List[str]):
    for path, entries in consolidated.items():
        with open(entries.filename, "w") as outfile:
            jsonified = entries.as_dict(exclude=exclude)
            json.dump(jsonified, outfile, indent=4)


def minify_har(har_file: str):
    with open(har_file, mode="r", encoding="utf-8-sig") as infile:
        har_entries = json.load(infile)["log"]["entries"]

    minified_entries = []
    for entry in har_entries:
        minified_entries.append(extract_minified_har_entry(entry))

    return minified_entries
