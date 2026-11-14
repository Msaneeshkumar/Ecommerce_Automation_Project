from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_customer_information(page):
    login_page = LoginPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    cart_page.add_backpack()
    cart_page.open_cart()

    checkout_page.start_checkout()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    checkout_page.enter_customer_details("Aneesh", "Kumar", "638002")

    checkout_page.continue_checkout()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

def test_complete_order(page):
    login_page = LoginPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    cart_page.add_backpack()
    cart_page.open_cart()

    checkout_page.start_checkout()

    checkout_page.enter_customer_details("Aneesh", "Kumar", "638001")

    checkout_page.continue_checkout()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    checkout_page.finish_checkout()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")

    expect(checkout_page.confirmation_message).to_have_text("Thank you for your order!")

def test_checkout_without_first_name(page):
    login_page = LoginPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    cart_page.add_backpack()
    cart_page.open_cart()

    checkout_page.start_checkout()

    checkout_page.enter_customer_details("", "Kumar", "638001")

    checkout_page.continue_checkout()

    expect(checkout_page.error_message).to_be_visible()

    expect(checkout_page.error_message).to_have_text("Error: First Name is required")