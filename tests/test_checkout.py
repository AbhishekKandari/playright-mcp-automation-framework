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
def test_missing_first_name(page):
    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_info('', test_data['checkout']['lastName'], test_data['checkout']['postalCode'])
    error = checkout_page.get_error_message()
    assert 'First Name is required' in error

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Checkout Functionality")
@allure.story("Validation")
def test_missing_last_name(page):
    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_info(test_data['checkout']['firstName'], '', test_data['checkout']['postalCode'])
    error = checkout_page.get_error_message()
    assert 'Last Name is required' in error

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Checkout Functionality")
@allure.story("Validation")
def test_missing_postal_code(page):
    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_info(test_data['checkout']['firstName'], test_data['checkout']['lastName'], '')
    error = checkout_page.get_error_message()
    assert 'Postal Code is required' in error

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Checkout Functionality")
@allure.story("Cancel Checkout")
def test_cancel_checkout(page):
    checkout_page = CheckoutPage(page)
    checkout_page.cancel_checkout()
    expect(page).to_have_url(re.compile(r'/cart'))

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Checkout Functionality")
@allure.story("Multiple Items")
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
def test_checkout_overview_page(page):
    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_info(test_data['checkout']['firstName'], test_data['checkout']['lastName'], test_data['checkout']['postalCode'])
    expect(page).to_have_url(re.compile(r'/checkout-step-two'))
    item_count = page.locator('.cart_item').count()
    assert item_count == 1

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Checkout Functionality")
@allure.story("Cancel from Overview")
def test_cancel_from_checkout_overview(page):
    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_info(test_data['checkout']['firstName'], test_data['checkout']['lastName'], test_data['checkout']['postalCode'])
    checkout_page.cancel_checkout()
    expect(page).to_have_url(re.compile(r'/inventory'))

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Checkout Functionality")
@allure.story("Complete Order")
def test_complete_order_and_return_to_inventory(page):
    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_info(test_data['checkout']['firstName'], test_data['checkout']['lastName'], test_data['checkout']['postalCode'])
    checkout_page.finish_checkout()
    page.click('#back-to-products')
    expect(page).to_have_url(re.compile(r'/inventory'))

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Checkout Functionality")
@allure.story("Empty Cart Checkout")
def test_checkout_with_empty_cart(page):
    page.go_back()
    cart_page = CartPage(page)
    cart_page.remove_item(0)
    # In SauceDemo, checkout button remains enabled even with empty cart
    expect(page.locator('#checkout')).to_be_enabled()

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Checkout Functionality")
@allure.story("Price Validation")
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
def test_tax_validation(page):
    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_info(test_data['checkout']['firstName'], test_data['checkout']['lastName'], test_data['checkout']['postalCode'])
    tax_text = checkout_page.get_tax()
    tax = float(tax_text.replace('Tax: $', ''))
    assert tax > 0

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Checkout Functionality")
@allure.story("Remove from Overview")
def test_remove_item_from_overview(page):
    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_info(test_data['checkout']['firstName'], test_data['checkout']['lastName'], test_data['checkout']['postalCode'])
    initial_count = page.locator('.cart_item').count()
    checkout_page.remove_item_from_overview(0)
    new_count = page.locator('.cart_item').count()
    assert new_count == initial_count - 1
