import os
from pathlib import Path

from pages.login_page import LoginPage
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=os.getenv("CI") == "true",slow_mo=0 if os.getenv("CI") == "true" else 400)

        page = browser.new_page()

        yield page

        browser.close()

@pytest.fixture
def logged_in_page(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    return page

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)

            safe_name = "".join(
                char if char.isalnum() or char in "-_" else "_"
                for char in item.nodeid
            )

            screenshot_path = screenshots_dir / f"{safe_name}.png"

            page.screenshot(
                path=str(screenshot_path),
                full_page=True
            )

            print(f"\nFailure screenshot: {screenshot_path}")
