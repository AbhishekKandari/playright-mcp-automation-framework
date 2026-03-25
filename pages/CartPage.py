class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_items = '.cart_item'
        self.checkout_button = '#checkout'
        self.continue_shopping_button = '#continue-shopping'
        self.remove_buttons = '.btn_secondary'

    def goto(self):
        self.page.goto('https://www.saucedemo.com/cart.html')

    def checkout(self):
        self.page.click(self.checkout_button)

    def continue_shopping(self):
        self.page.click(self.continue_shopping_button)

    def remove_item(self, index=0):
        self.page.locator(self.remove_buttons).nth(index).click()

    def get_cart_item_names(self):
        return self.page.locator('.inventory_item_name').all_text_contents()

    def get_cart_item_count(self):
        return self.page.locator(self.cart_items).count()