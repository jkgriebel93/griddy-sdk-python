"""
Example usage of cookie extraction utilities in Griddy SDK.

This script demonstrates how to extract cookies from a cookies.txt file
for specific URLs and use them in HTTP requests.
"""

from pathlib import Path
import tempfile
import requests

from griddy.core.utils import (
    extract_cookies_for_url,
    extract_cookies_as_dict,
    extract_cookies_as_header,
    parse_cookies_txt,
    Cookie
)


def create_sample_cookies_file() -> str:
    """Create a sample cookies.txt file for demonstration."""
    sample_content = """# Netscape HTTP Cookie File
# This is a sample cookies file for demonstration

# Session cookies for example.com
.example.com	TRUE	/	FALSE	1735689600	session_id	abc123def456
example.com	FALSE	/	FALSE	0	csrf_token	xyz789
.example.com	TRUE	/api	TRUE	1735689600	api_key	secret123

# Cookies for other sites
.github.com	TRUE	/	TRUE	1735689600	logged_in	yes
github.com	FALSE	/	TRUE	1735689600	user_session	github_session_123

# Expired cookie (timestamp from 2020)
.old-site.com	TRUE	/	FALSE	1577836800	old_cookie	expired_value

# Social media cookies
.facebook.com	TRUE	/	TRUE	1735689600	c_user	123456789
.facebook.com	TRUE	/	FALSE	0	locale	en_US
"""

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='_cookies.txt') as f:
        f.write(sample_content)
        return f.name


def main():
    """Main demonstration function."""
    print("=== Griddy SDK - Cookie Extraction Example ===\n")

    # Create a sample cookies file
    cookies_file = create_sample_cookies_file()
    print(f"Created sample cookies file: {cookies_file}")

    try:
        # Example 1: Parse all cookies from file
        print("\n1. Parsing all cookies from file:")
        all_cookies = parse_cookies_txt(cookies_file)
        print(f"   Found {len(all_cookies)} total cookies")

        for cookie in all_cookies[:3]:  # Show first 3
            print(f"   - {cookie.name}: {cookie.value} (domain: {cookie.domain})")
            print(f"     Path: {cookie.path}, Secure: {cookie.secure}")
            if cookie.expires:
                import datetime
                expiry = datetime.datetime.fromtimestamp(cookie.expires)
                print(f"     Expires: {expiry}")
            print()

        # Example 2: Extract cookies for specific URL
        print("\n2. Extracting cookies for 'https://example.com/':")
        target_url = "https://example.com/"
        matching_cookies = extract_cookies_for_url(cookies_file, target_url)

        print(f"   Found {len(matching_cookies)} matching cookies:")
        for cookie in matching_cookies:
            print(f"   - {cookie.name}: {cookie.value}")
            print(f"     Domain: {cookie.domain}, Path: {cookie.path}")
            if cookie.is_expired:
                print("     ⚠️  This cookie is expired")

        # Example 3: Extract cookies as dictionary
        print("\n3. Extracting cookies as dictionary:")
        cookies_dict = extract_cookies_as_dict(cookies_file, target_url)
        print(f"   Cookies dict: {cookies_dict}")

        # Example 4: Extract cookies as HTTP header string
        print("\n4. Extracting cookies as HTTP header:")
        cookie_header = extract_cookies_as_header(cookies_file, target_url)
        print(f"   Cookie header: {cookie_header}")

        # Example 5: Using cookies in HTTP requests
        print("\n5. Using cookies in HTTP requests:")

        # Method 1: Using dictionary with requests
        print("   Method 1 - Using cookies dictionary:")
        try:
            response = requests.get(
                "https://httpbin.org/cookies",
                cookies=cookies_dict,
                timeout=5
            )
            print(f"   Response: {response.json()}")
        except Exception as e:
            print(f"   Request failed: {e}")

        # Method 2: Using header string
        print("\n   Method 2 - Using Cookie header:")
        try:
            headers = {"Cookie": cookie_header}
            response = requests.get(
                "https://httpbin.org/headers",
                headers=headers,
                timeout=5
            )
            cookie_header_received = response.json().get("headers", {}).get("Cookie", "")
            print(f"   Cookie header sent: {cookie_header_received}")
        except Exception as e:
            print(f"   Request failed: {e}")

        # Example 6: Subdomain cookie matching
        print("\n6. Testing subdomain cookie matching:")
        subdomain_url = "https://api.example.com/v1/data"
        subdomain_cookies = extract_cookies_for_url(cookies_file, subdomain_url)

        print(f"   URL: {subdomain_url}")
        print(f"   Matching cookies: {len(subdomain_cookies)}")
        for cookie in subdomain_cookies:
            print(f"   - {cookie.name}: {cookie.value} (from {cookie.domain})")

        # Example 7: Path-specific cookie matching
        print("\n7. Testing path-specific cookie matching:")
        api_url = "https://example.com/api/users"
        api_cookies = extract_cookies_for_url(cookies_file, api_url)

        print(f"   URL: {api_url}")
        print(f"   Matching cookies: {len(api_cookies)}")
        for cookie in api_cookies:
            print(f"   - {cookie.name}: {cookie.value} (path: {cookie.path})")

        # Example 8: HTTPS vs HTTP secure cookie handling
        print("\n8. Testing secure cookie handling:")

        https_url = "https://example.com/api"
        http_url = "http://example.com/api"

        https_cookies = extract_cookies_for_url(cookies_file, https_url)
        http_cookies = extract_cookies_for_url(cookies_file, http_url)

        print(f"   HTTPS cookies ({https_url}): {len(https_cookies)}")
        for cookie in https_cookies:
            secure_flag = "🔒" if cookie.secure else "🔓"
            print(f"   - {secure_flag} {cookie.name}: {cookie.value}")

        print(f"\n   HTTP cookies ({http_url}): {len(http_cookies)}")
        for cookie in http_cookies:
            secure_flag = "🔒" if cookie.secure else "🔓"
            print(f"   - {secure_flag} {cookie.name}: {cookie.value}")

        # Example 9: Handling expired cookies
        print("\n9. Testing expired cookie handling:")

        # Include expired cookies
        old_site_url = "https://old-site.com/"
        with_expired = extract_cookies_for_url(cookies_file, old_site_url, include_expired=True)
        without_expired = extract_cookies_for_url(cookies_file, old_site_url, include_expired=False)

        print(f"   URL: {old_site_url}")
        print(f"   With expired cookies: {len(with_expired)}")
        print(f"   Without expired cookies: {len(without_expired)}")

        for cookie in with_expired:
            status = "⚠️ EXPIRED" if cookie.is_expired else "✅ VALID"
            print(f"   - {cookie.name}: {cookie.value} ({status})")

        # Example 10: Integration with Griddy SDK clients
        print("\n10. Integration with Griddy SDK:")
        print("    You can use these cookies with any of the SDK clients:")
        print("    ")
        print("    ```python")
        print("    from griddy import nfl")
        print("    from griddy.core.utils import extract_cookies_as_dict")
        print("    ")
        print("    # Extract cookies for NFL.com")
        print("    cookies = extract_cookies_as_dict('cookies.txt', 'https://nfl.com')")
        print("    ")
        print("    # Create client with custom headers including cookies")
        print("    client = nfl.Client(headers={'Cookie': extract_cookies_as_header('cookies.txt', 'https://nfl.com')})")
        print("    ```")

    except Exception as e:
        print(f"Error during demonstration: {e}")

    finally:
        # Clean up the temporary file
        Path(cookies_file).unlink(missing_ok=True)
        print(f"\n=== Cleaned up temporary file: {cookies_file} ===")


if __name__ == "__main__":
    main()