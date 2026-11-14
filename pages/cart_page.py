class CartPage:
    def __init__(self,page):
        self.page = page

        self.add_backpack_button = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')

        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')

        self.remove_backpack_button = page.locator('[data-test="remove-sauce-labs-backpack"]')

        self.add_bike_light_button = page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]')

        self.cart_icon = page.locator('[data-test="shopping-cart-link"]')

        self.cart_items = page.locator('[data-test="inventory-item"]')

        self.cart_item_names = page.locator('[data-test="inventory-item-name"]')

    def add_backpack(self):
        self.add_backpack_button.click()

    def remove_backpack(self):
        self.remove_backpack_button.click()

    def add_bike_light(self):
        self.add_bike_light_button.click()

    def open_cart(self):
        self.cart_icon.click()