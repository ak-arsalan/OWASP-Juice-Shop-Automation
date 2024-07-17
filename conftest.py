import os
import pytest
from playwright.sync_api import sync_playwright, Page, expect

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def api_context(playwright):
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()

@pytest.fixture(scope="session")
def base_url():
    return "http://localhost:3000"

@pytest.fixture(scope="function", params=["chromium", "firefox", "webkit", "edge"])
def page(request, playwright):
    browser_type = request.param
    if browser_type == "edge":
        browser = playwright.chromium.launch(headless=True, channel="msedge")
    else:
        browser = getattr(playwright, browser_type).launch(headless=True)
    page = browser.new_page()
    yield page
    browser.close()

@pytest.fixture(scope="function")
def setup(page: Page, base_url: str):
    page.goto(base_url)
    dismiss_buttons = page.locator("text='Dismiss'")
    if dismiss_buttons.count():
        dismiss_buttons.click()
    yield page

@pytest.fixture(scope="session")
def invalid_email():
    return os.getenv("INVALID_EMAIL")

@pytest.fixture(scope="session")
def invalid_password():
    return os.getenv("INVALID_PASSWORD")

@pytest.fixture(scope="session")
def email():
    return os.getenv("EMAIL")

@pytest.fixture(scope="session")
def password():
    return os.getenv("PASSWORD")

@pytest.fixture(scope="session")
def sql_email():
    return os.getenv("SQL_EMAIL")

@pytest.fixture(scope="session")
def xss_script():
    return os.getenv("XSS_SCRIPT")
