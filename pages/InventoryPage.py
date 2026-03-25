class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.inventory_container = '.inventory_container'
        self.inventory_items = '.inventory_item'
        self.add_to_cart_buttons = '.btn_inventory'
        self.remove_from_cart_buttons = '.btn_secondary'
        self.cart_badge = '.shopping_cart_badge'
        self.sort_dropdown = '.product_sort_container'
        self.cart_link = '.shopping_cart_link'

    def goto(self):
        self.page.goto('https://www.saucedemo.com/inventory.html')

    def add_item_to_cart(self, index=0):
        self.page.locator(self.add_to_cart_buttons).nth(index).click()

    def remove_item_from_cart(self, index=0):
        self.page.locator(self.remove_from_cart_buttons).nth(index).click()

    def get_cart_badge_count(self):
        badge = self.page.locator(self.cart_badge)
        if badge.is_visible():
            return badge.text_content()
        return '0'

    def sort_products(self, option):
        self.page.select_option(self.sort_dropdown, option)

    def get_product_names(self):
        return self.page.locator('.inventory_item_name').all_text_contents()

    def get_product_prices(self):
        return self.page.locator('.inventory_item_price').all_text_contents()

    def go_to_cart(self):
        self.page.click(self.cart_link)
