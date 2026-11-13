from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_products_displayed_after_login(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)

    expect(inventory_page.product_items).to_have_count(6)

def test_sort_products_price_low_to_high(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)

    inventory_page.sort_by_price_low_to_high()

    prices = inventory_page.get_product_prices()

    assert prices == sorted(prices)
