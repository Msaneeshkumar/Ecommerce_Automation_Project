class CheckoutPage:
    def __init__(self, page):
        self.page = page

        self.checkout_button = page.locator('[data-test="checkout"]')

        self.first_name = page.locator('[data-test="firstName"]')

        self.last_name = page.locator('[data-test="lastName"]')

        self.postal_code = page.locator('[data-test="postalCode"]')

        self.continue_button = page.locator('[data-test="continue"]')

        self.finish_button = page.locator('[data-test="finish"]')

        self.confirmation_message = page.locator('[data-test="complete-header"]')

        self.back_home_button = page.locator('[data-test="back-to-products"]')

        self.error_message = page.locator('[data-test="error"]')

    def start_checkout(self):
        self.checkout_button.click()

    def enter_customer_details(self, first, last, postal):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postal)

    def continue_checkout(self):
        self.continue_button.click()

    def finish_checkout(self):
        self.finish_button.click()

    def back_to_products(self):
        self.back_home_button.click()