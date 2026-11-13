class InventoryPage:

    def __init__(self, page):
        self.page = page

        self.product_items = page.locator(
            '[data-test="inventory-item"]'
        )

        self.sort_dropdown = page.locator(
            '[data-test="product-sort-container"]'
        )

        self.product_prices = page.locator(
            '[data-test="inventory-item-price"]'
        )

    def get_product_count(self):
        return self.product_items.count()

    def sort_by_price_low_to_high(self):
        self.sort_dropdown.select_option("lohi")

    def get_product_prices(self):
        prices = self.product_prices.all_text_contents()

        return [
            float(price.replace("$", ""))
            for price in prices
        ]