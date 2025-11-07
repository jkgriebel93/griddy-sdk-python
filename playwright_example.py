import time

from playwright.sync_api import sync_playwright

from griddy.settings import NFL

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://id.nfl.com/account/sign-in")

    page.get_by_test_id("email-input").fill(NFL["login_email"])
    time.sleep(3)
    page.get_by_role("button", name="Continue").click()
    time.sleep(3)
    page.get_by_role("button", name="Sign in with password").click()
    time.sleep(3)
    page.get_by_test_id("password-input").fill(NFL["login_password"])
    time.sleep(1)
    with page.expect_response("**/token") as response_info:
        page.get_by_role("button", name="Sign in").click()

    response = response_info.value
    from pprint import pprint

    try:
        pprint(response.json())
        time.sleep(3)
    except AttributeError as e:
        pprint(vars(response_info), indent=4)
        pprint(dir(response_info), indent=4)
        raise e

    browser.close()
