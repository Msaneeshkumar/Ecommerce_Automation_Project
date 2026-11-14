from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.cart_page import CartPage


def test_add_product_to_cart(logged_in_page):
    cart_page = CartPage(logged_in_page)

    cart_page.add_backpack()

    expect(cart_page.cart_badge).to_have_text("1")

def test_remove_product_from_cart(logged_in_page):
    cart_page = CartPage(logged_in_page)

    cart_page.add_backpack()
    expect(cart_page.cart_badge).to_have_text("1")

    cart_page.remove_backpack()
    expect(cart_page.cart_badge).to_have_count(0)


def test_add_multiple_products_to_cart(logged_in_page):
    cart_page = CartPage(logged_in_page)

    cart_page.add_backpack()
    cart_page.add_bike_light()

    expect(cart_page.cart_badge).to_have_text("2")


def test_cart_product_details(logged_in_page):
    cart_page = CartPage(logged_in_page)

    cart_page.add_backpack()
    cart_page.add_bike_light()
    cart_page.open_cart()

    expect(logged_in_page).to_have_url(
        "https://www.saucedemo.com/cart.html"
    )

    expect(cart_page.cart_items).to_have_count(2)

    expect(cart_page.cart_item_names).to_contain_text([
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light"
    ])