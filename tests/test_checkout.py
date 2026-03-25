import pytest
from playwright.sync_api import expect
import re
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from utils.helpers import login_as, test_data
import allure

@pytest.fixture(autouse=True)
def setup(page):
    login_as(page, 'standard')
    inventory_page = InventoryPage(page)
    inventory_page.add_item_to_cart(0)
    inventory_page.go_to_cart()
    cart_page = CartPage(page)
    cart_page.checkout()

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Checkout Functionality")
@allure.story("Valid Checkout")
@allure.description("Verify the complete checkout flow with valid user information. This test ensures that a user can successfully complete a purchase and receive a confirmation message.")
def test_valid_checkout(page):
    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_info(test_data['checkout']['firstName'], test_data['checkout']['lastName'], test_data['checkout']['postalCode'])
    checkout_page.finish_checkout()
    message = checkout_page.get_complete_message()
    assert message == 'Thank you for your order!'
    screenshot = page.screenshot()
    allure.attach(screenshot, name="Checkout Complete", attachment_type=allure.attachment_type.PNG)

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Checkout Functionality")
@allure.story("Validation")
@allure.description("Verify validation error when first name is missing. This test ensures proper form validation and displays appropriate error message.")
def test_missing_first_name(page):
    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_info('', test_data['checkout']['lastName'], test_data['checkout']['postalCode'])
    error = checkout_page.get_error_message()
    assert 'First Name is required' in error

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Checkout Functionality")
@allure.story("Validation")
@allure.description("Verify validation error when last name is missing. This test ensures proper form validation and displays appropriate error message for last name field.")
def test_missing_last_name(page):
    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_info(test_data['checkout']['firstName'], '', test_data['checkout']['postalCode'])
    error = checkout_page.get_error_message()
    assert 'Last Name is required' in error

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Checkout Functionality")
@allure.story("Validation")
@allure.description("Verify validation error when postal code is missing. This test ensures proper form validation and displays appropriate error message for postal code field.")
def test_missing_postal_code(page):
    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_info(test_data['checkout']['firstName'], test_data['checkout']['lastName'], '')
    error = checkout_page.get_error_message()
    assert 'Postal Code is required' in error

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Checkout Functionality")
@allure.story("Cancel Checkout")
@allure.description("Verify that a user can cancel the checkout process and return to the cart page. This test ensures the cancel functionality works correctly.")
def test_cancel_checkout(page):
    checkout_page = CheckoutPage(page)
    checkout_page.cancel_checkout()
    expect(page).to_have_url(re.compile(r'/cart'))

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Checkout Functionality")
@allure.story("Multiple Items")
@allure.description("Verify checkout process with multiple items in the cart. This test ensures all items are processed correctly during checkout.")
def test_checkout_with_multiple_items(page):
    page.go_back()
    cart_page = CartPage(page)
    cart_page.continue_shopping()
    inventory_page = InventoryPage(page)
    inventory_page.add_item_to_cart(1)
    inventory_page.go_to_cart()
    cart_page = CartPage(page)
    cart_page.checkout()
    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_info(test_data['checkout']['firstName'], test_data['checkout']['lastName'], test_data['checkout']['postalCode'])
    checkout_page.finish_checkout()
    message = checkout_page.get_complete_message()
    assert message == 'Thank you for your order!'

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Checkout Functionality")
@allure.story("Overview")
@allure.description("Verify that the checkout overview page displays all cart items correctly. This test ensures item count and details are shown on the overview page.")
def test_checkout_overview_page(page):
    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_info(test_data['checkout']['firstName'], test_data['checkout']['lastName'], test_data['checkout']['postalCode'])
    expect(page).to_have_url(re.compile(r'/checkout-step-two'))
    item_count = page.locator('.cart_item').count()
    assert item_count == 1

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Checkout Functionality")
@allure.story("Cancel from Overview")
@allure.description("Verify that a user can cancel from the checkout overview page and return to inventory. This test ensures proper navigation after cancellation.")
def test_cancel_from_checkout_overview(page):
    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_info(test_data['checkout']['firstName'], test_data['checkout']['lastName'], test_data['checkout']['postalCode'])
    checkout_page.cancel_checkout()
    expect(page).to_have_url(re.compile(r'/inventory'))

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Checkout Functionality")
@allure.story("Complete Order")
@allure.description("Verify that after completing an order, the user can return to the inventory page. This test ensures proper navigation after successful checkout.")
def test_complete_order_and_return_to_inventory(page):
    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_info(test_data['checkout']['firstName'], test_data['checkout']['lastName'], test_data['checkout']['postalCode'])
    checkout_page.finish_checkout()
    page.click('#back-to-products')
    expect(page).to_have_url(re.compile(r'/inventory'))

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Checkout Functionality")
@allure.story("Empty Cart Checkout")
@allure.description("Verify checkout button behavior with an empty cart. This test ensures the checkout flow handles empty cart scenarios correctly.")
def test_checkout_with_empty_cart(page):
    page.go_back()
    cart_page = CartPage(page)
    cart_page.remove_item(0)
    # In SauceDemo, checkout button remains enabled even with empty cart
    expect(page.locator('#checkout')).to_be_enabled()

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Checkout Functionality")
@allure.story("Price Validation")
@allure.description("Verify that the total price calculation is correct (item total + tax = grand total). This test ensures accurate price computation in the checkout process.")
def test_price_validation(page):
    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_info(test_data['checkout']['firstName'], test_data['checkout']['lastName'], test_data['checkout']['postalCode'])
    item_total_text = checkout_page.get_item_total()
    tax_text = checkout_page.get_tax()
    total_text = checkout_page.get_total()
    item_total = float(item_total_text.replace('Item total: $', ''))
    tax = float(tax_text.replace('Tax: $', ''))
    total = float(total_text.replace('Total: $', ''))
    assert abs((item_total + tax) - total) < 0.01

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Checkout Functionality")
@allure.story("Tax Validation")
@allure.description("Verify that tax is correctly calculated and displayed in the checkout. This test ensures tax is greater than zero and properly formatted.")
def test_tax_validation(page):
    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_info(test_data['checkout']['firstName'], test_data['checkout']['lastName'], test_data['checkout']['postalCode'])
    tax_text = checkout_page.get_tax()
    tax = float(tax_text.replace('Tax: $', ''))
    assert tax > 0

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Checkout Functionality")
@allure.story("Remove from Overview")
@allure.description("Verify that items can be removed from the checkout overview page. This test ensures the item count decreases after removal.")
def test_remove_item_from_overview(page):
    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_info(test_data['checkout']['firstName'], test_data['checkout']['lastName'], test_data['checkout']['postalCode'])
    initial_count = page.locator('.cart_item').count()
    checkout_page.remove_item_from_overview(0)
    new_count = page.locator('.cart_item').count()
    assert new_count == initial_count - 1
