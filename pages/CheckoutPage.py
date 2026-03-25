class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name_input = '#first-name'
        self.last_name_input = '#last-name'
        self.postal_code_input = '#postal-code'
        self.continue_button = '#continue'
        self.cancel_button = '#cancel'
        self.finish_button = '#finish'
        self.complete_message = '.complete-header'
        self.error_message = '.error-message-container'

    def goto(self):
        self.page.goto('https://www.saucedemo.com/checkout-step-one.html')

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.page.fill(self.first_name_input, first_name)
        self.page.fill(self.last_name_input, last_name)
        self.page.fill(self.postal_code_input, postal_code)
        self.page.click(self.continue_button)

    def finish_checkout(self):
        self.page.click(self.finish_button)

    def cancel_checkout(self):
        self.page.click(self.cancel_button)

    def get_complete_message(self):
        return self.page.text_content(self.complete_message)

    def get_error_message(self):
        return self.page.text_content(self.error_message)

    def get_item_total(self):
        return self.page.text_content('.summary_subtotal_label')

    def get_tax(self):
        return self.page.text_content('.summary_tax_label')

    def get_total(self):
        return self.page.text_content('.summary_total_label')

    def remove_item_from_overview(self, index=0):
        self.page.click('.cart_button')
