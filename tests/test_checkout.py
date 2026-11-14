import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_customer_information(logged_in_page):
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)

    cart_page.add_backpack()
    cart_page.open_cart()

    checkout_page.start_checkout()

    expect(logged_in_page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    checkout_page.enter_customer_details("Aneesh", "Kumar", "638002")

    checkout_page.continue_checkout()

    expect(logged_in_page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

def test_complete_order(logged_in_page):
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)

    cart_page.add_backpack()
    cart_page.open_cart()

    checkout_page.start_checkout()

    checkout_page.enter_customer_details("Aneesh", "Kumar", "638001")

    checkout_page.continue_checkout()

    expect(logged_in_page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    checkout_page.finish_checkout()

    expect(logged_in_page).to_have_url("https://www.saucedemo.com/checkout-complete.html")

    expect(checkout_page.confirmation_message).to_have_text("Thank you for your order!")

@pytest.mark.parametrize("first,last,postal,expected_error",
    [
        ("", "Kumar", "638001", "First Name is required"),
        ("Aneesh", "", "638001", "Last Name is required"),
        ("Aneesh", "Kumar", "", "Postal Code is required"),
    ]
)
def test_checkout_required_fields(logged_in_page, first, last, postal, expected_error):
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)

    cart_page.add_backpack()
    cart_page.open_cart()

    checkout_page.start_checkout()

    checkout_page.enter_customer_details(first, last, postal)

    checkout_page.continue_checkout()

    expect(checkout_page.error_message).to_be_visible()

    expect(checkout_page.error_message).to_contain_text(expected_error)