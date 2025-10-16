"""Request comparison utility for debugging SDK vs direct requests."""

import httpx
import sys
from urllib.parse import urlparse, parse_qs
from typing import Dict, Any, Optional, TextIO
from collections import defaultdict
from http.cookies import SimpleCookie


class RequestComparator:
    """Captures and compares HTTP requests."""

    def __init__(self, output_file: Optional[TextIO] = None):
        """
        Initialize the request comparator.

        Args:
            output_file: Optional file object to write captured requests to
        """
        self.captured_requests = []
        self.original_send = None
        self.original_async_send = None
        self.output_file = output_file

    def start_capture(self):
        """Start capturing httpx requests."""
        self.original_send = httpx.Client.send
        self.original_async_send = httpx.AsyncClient.send

        def intercepting_send(client_self, request, **kwargs):
            self._capture_request(request, "sync")
            return self.original_send(client_self, request, **kwargs)

        async def intercepting_async_send(client_self, request, **kwargs):
            self._capture_request(request, "async")
            return await self.original_async_send(client_self, request, **kwargs)

        httpx.Client.send = intercepting_send
        httpx.AsyncClient.send = intercepting_async_send

    def stop_capture(self):
        """Stop capturing httpx requests."""
        if self.original_send:
            httpx.Client.send = self.original_send
        if self.original_async_send:
            httpx.AsyncClient.send = self.original_async_send

    def _capture_request(self, request: httpx.Request, request_type: str):
        """Internal method to capture request details."""
        parsed_url = urlparse(str(request.url))

        captured = {
            'type': request_type,
            'method': request.method,
            'url': str(request.url),
            'scheme': parsed_url.scheme,
            'host': parsed_url.netloc,
            'path': parsed_url.path,
            'query_params': parse_qs(parsed_url.query),
            'headers': dict(request.headers),
            'content': request.content if hasattr(request, 'content') else None,
        }

        self.captured_requests.append(captured)

        # Print to console
        self._print_request_details(captured)

        # Also print to file if specified
        if self.output_file:
            self._print_request_details(captured, file=self.output_file)

    def _print_request_details(self, req_info: Dict[str, Any], file: Optional[TextIO] = None):
        """Print captured request details."""
        output = file or sys.stdout

        print("\n" + "="*80, file=output)
        print(f"CAPTURED SDK REQUEST ({req_info['type'].upper()})", file=output)
        print("="*80, file=output)
        print(f"Method: {req_info['method']}", file=output)
        print(f"URL: {req_info['url']}", file=output)
        print(f"\nURL Components:", file=output)
        print(f"  Scheme: {req_info['scheme']}", file=output)
        print(f"  Host: {req_info['host']}", file=output)
        print(f"  Path: {req_info['path']}", file=output)

        if req_info['query_params']:
            print(f"\nQuery Parameters:", file=output)
            for key, values in sorted(req_info['query_params'].items()):
                for value in values:
                    print(f"  {key} = {value}", file=output)

        print(f"\nHeaders:", file=output)
        for key, value in sorted(req_info['headers'].items()):
            # Truncate sensitive headers
            if key.lower() in ['authorization', 'cookie']:
                display_value = f"{value[:30]}..." if len(value) > 30 else value
            else:
                display_value = value
            print(f"  {key}: {display_value}", file=output)

        print("="*80 + "\n", file=output)

    def get_last_request(self) -> Optional[Dict[str, Any]]:
        """Get the most recently captured request."""
        return self.captured_requests[-1] if self.captured_requests else None

    def clear(self):
        """Clear all captured requests."""
        self.captured_requests = []


def parse_cookies(headers: Dict[str, str]) -> Dict[str, str]:
    """
    Parse cookies from headers dictionary.

    Args:
        headers: Dictionary of HTTP headers

    Returns:
        Dictionary of cookie name -> value pairs
    """
    cookies = {}

    # Look for 'cookie' header (case-insensitive)
    cookie_header = None
    for key, value in headers.items():
        if key.lower() == 'cookie':
            cookie_header = value
            break

    if cookie_header:
        # Parse cookie string
        # Cookie header format: "name1=value1; name2=value2; ..."
        cookie = SimpleCookie()
        # SimpleCookie expects Set-Cookie format, but we have Cookie format
        # So we'll parse manually
        for part in cookie_header.split(';'):
            part = part.strip()
            if '=' in part:
                name, value = part.split('=', 1)
                cookies[name.strip()] = value.strip()

    return cookies


def print_direct_request_details(request_info: Dict[str, Any], file: Optional[TextIO] = None):
    """
    Print direct request details in the same format as SDK requests.

    Args:
        request_info: Dict with 'url', 'headers', 'method' from direct call
        file: Optional file object to write to (defaults to stdout)
    """
    output = file or sys.stdout

    # Parse the URL
    parsed_url = urlparse(request_info['url'])
    query_params = parse_qs(parsed_url.query)

    print("\n" + "="*80, file=output)
    print("DIRECT REQUEST (requests library)", file=output)
    print("="*80, file=output)
    print(f"Method: {request_info.get('method', 'GET')}", file=output)
    print(f"URL: {request_info['url']}", file=output)
    print(f"\nURL Components:", file=output)
    print(f"  Scheme: {parsed_url.scheme}", file=output)
    print(f"  Host: {parsed_url.netloc}", file=output)
    print(f"  Path: {parsed_url.path}", file=output)

    if query_params:
        print(f"\nQuery Parameters:", file=output)
        for key, values in sorted(query_params.items()):
            for value in values:
                print(f"  {key} = {value}", file=output)

    headers = request_info.get('headers', {})
    if headers:
        print(f"\nHeaders:", file=output)
        for key, value in sorted(headers.items()):
            # Truncate sensitive headers
            if key.lower() in ['authorization', 'cookie']:
                display_value = f"{value[:30]}..." if len(value) > 30 else value
            else:
                display_value = value
            print(f"  {key}: {display_value}", file=output)

    print("="*80 + "\n", file=output)


def compare_requests(direct_info: Dict[str, Any], sdk_info: Dict[str, Any], file: Optional[TextIO] = None):
    """
    Compare a direct request with an SDK request.

    Args:
        direct_info: Dict with 'url', 'headers', 'method', 'params' from direct call
        sdk_info: Captured SDK request info from RequestComparator
        file: Optional file object to write to (defaults to stdout)
    """
    output = file or sys.stdout
    print("\n" + "="*100, file=output)
    print("REQUEST COMPARISON", file=output)
    print("="*100, file=output)

    # Parse direct request URL
    direct_parsed = urlparse(direct_info['url'])
    direct_params = parse_qs(direct_parsed.query)

    # Parse cookies from both requests
    direct_cookies = parse_cookies(direct_info.get('headers', {}))
    sdk_cookies = parse_cookies(sdk_info['headers'])

    # Compare URLs
    print(f"\n{'URL COMPONENTS':-^100}", file=output)
    print(f"{'Component':<15} {'Direct Request':<40} {'SDK Request':<40} {'Match'}", file=output)
    print("-"*100, file=output)

    components = [
        ('Scheme', direct_parsed.scheme, sdk_info['scheme']),
        ('Host', direct_parsed.netloc, sdk_info['host']),
        ('Path', direct_parsed.path, sdk_info['path']),
        ('Method', direct_info.get('method', 'GET'), sdk_info['method']),
    ]

    for name, direct_val, sdk_val in components:
        match = "✓" if direct_val == sdk_val else "✗"
        print(f"{name:<15} {direct_val:<40} {sdk_val:<40} {match}", file=output)

    # Compare Query Parameters
    print(f"\n{'QUERY PARAMETERS':-^100}", file=output)
    print(f"{'Parameter':<20} {'Direct Request':<35} {'SDK Request':<35} {'Match'}", file=output)
    print("-"*100, file=output)

    all_params = set(direct_params.keys()) | set(sdk_info['query_params'].keys())

    if not all_params:
        print("  No query parameters", file=output)
    else:
        for param in sorted(all_params):
            direct_val = direct_params.get(param, ['MISSING'])[0]
            sdk_val = sdk_info['query_params'].get(param, ['MISSING'])[0]
            match = "✓" if direct_val == sdk_val else "✗"

            # Truncate long values
            direct_display = (direct_val[:30] + "...") if len(direct_val) > 30 else direct_val
            sdk_display = (sdk_val[:30] + "...") if len(sdk_val) > 30 else sdk_val

            print(f"{param:<20} {direct_display:<35} {sdk_display:<35} {match}", file=output)

    # Compare Headers
    print(f"\n{'HEADERS':-^100}", file=output)
    print(f"{'Header':<25} {'Direct Request':<32} {'SDK Request':<32} {'Match'}", file=output)
    print("-"*100, file=output)

    direct_headers = {k.lower(): v for k, v in direct_info.get('headers', {}).items()}
    sdk_headers = {k.lower(): v for k, v in sdk_info['headers'].items()}

    all_headers = set(direct_headers.keys()) | set(sdk_headers.keys())

    # Group headers
    important_headers = {'host', 'authorization', 'user-agent', 'accept', 'content-type', 'cookie'}
    important = [h for h in all_headers if h in important_headers]
    other = [h for h in all_headers if h not in important_headers]

    raw_auth_values = {}
    for header in sorted(important) + sorted(other):
        direct_val = direct_headers.get(header, 'MISSING')
        sdk_val = sdk_headers.get(header, 'MISSING')
        if header == "authorization":
            raw_auth_values["direct"] = direct_val
            raw_auth_values["sdk_val"] = sdk_val

        # Truncate long values
        direct_display = str(direct_val)[:30] + "..." if len(str(direct_val)) > 30 else str(direct_val)
        sdk_display = str(sdk_val)[:30] + "..." if len(str(sdk_val)) > 30 else str(sdk_val)

        match = "✓" if direct_val == sdk_val else "✗"

        # Highlight important headers
        prefix = ">>> " if header in important_headers else "    "
        print(f"{prefix}{header:<21} {direct_display:<32} {sdk_display:<32} {match}", file=output)

    # Compare Cookies
    print(f"\n{'COOKIES':-^100}", file=output)
    print(f"{'Cookie Name':<25} {'Direct Request':<32} {'SDK Request':<32} {'Match'}", file=output)
    print("-"*100, file=output)
    print("\n\n\nRaw authentication values\n\n\n", file=output)
    import json
    print(json.dumps(raw_auth_values, indent=4), file=output    )
    all_cookies = set(direct_cookies.keys()) | set(sdk_cookies.keys())

    if not all_cookies:
        print("  No cookies", file=output)
    else:
        for cookie_name in sorted(all_cookies):
            direct_val = direct_cookies.get(cookie_name, 'MISSING')
            sdk_val = sdk_cookies.get(cookie_name, 'MISSING')

            # Truncate long values
            direct_display = str(direct_val)[:30] + "..." if len(str(direct_val)) > 30 else str(direct_val)
            sdk_display = str(sdk_val)[:30] + "..." if len(str(sdk_val)) > 30 else str(sdk_val)

            match = "✓" if direct_val == sdk_val else "✗"
            print(f"{cookie_name:<25} {direct_display:<32} {sdk_display:<32} {match}", file=output)

    # Summary
    print(f"\n{'SUMMARY':-^100}", file=output)

    param_matches = sum(1 for p in all_params
                       if direct_params.get(p, [''])[0] == sdk_info['query_params'].get(p, [''])[0])
    header_matches = sum(1 for h in all_headers
                        if direct_headers.get(h) == sdk_headers.get(h))
    cookie_matches = sum(1 for c in all_cookies
                        if direct_cookies.get(c) == sdk_cookies.get(c))

    print(f"Query Parameters: {param_matches}/{len(all_params)} match", file=output)
    print(f"Headers: {header_matches}/{len(all_headers)} match", file=output)
    print(f"Cookies: {cookie_matches}/{len(all_cookies)} match", file=output)

    # Show mismatches
    param_mismatches = [p for p in all_params
                       if direct_params.get(p, [''])[0] != sdk_info['query_params'].get(p, [''])[0]]
    header_mismatches = [h for h in all_headers
                        if direct_headers.get(h) != sdk_headers.get(h)]
    cookie_mismatches = [c for c in all_cookies
                        if direct_cookies.get(c) != sdk_cookies.get(c)]

    if param_mismatches:
        print(f"\nQuery parameter mismatches: {', '.join(param_mismatches)}", file=output)

    if header_mismatches:
        print(f"Header mismatches: {', '.join(header_mismatches)}", file=output)

    if cookie_mismatches:
        print(f"Cookie mismatches: {', '.join(cookie_mismatches)}", file=output)

    print("="*100 + "\n", file=output)


if __name__ == "__main__":
    print("Request Comparator utility loaded.")
    print("\nUsage:")
    print("  from request_comparator import RequestComparator, compare_requests, print_direct_request_details")
    print()
    print("  # Display direct request details")
    print("  direct_info = {'url': '...', 'method': 'GET', 'headers': {...}}")
    print("  print_direct_request_details(direct_info)")
    print()
    print("  # Capture and compare SDK requests")
    print("  comparator = RequestComparator()")
    print("  comparator.start_capture()")
    print("  # ... make SDK calls ...")
    print("  comparator.stop_capture()")
    print("  compare_requests(direct_info, comparator.get_last_request())")
    print()
    print("  # Save to file:")
    print("  with open('comparison.log', 'w') as f:")
    print("      print_direct_request_details(direct_info, file=f)")
    print("      compare_requests(direct_info, comparator.get_last_request(), file=f)")
