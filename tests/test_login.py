import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage


def test_valid_login(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )


@pytest.mark.parametrize(
    "username, password",
    [
        ("standard_user", "wrong123"),
        ("wrong_user", "secret_sauce"),
        ("wrong_user", "wrong123")
    ]
)
def test_invalid_login(page, username, password):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(username, password)

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(
        "Username and password do not match"
    )
