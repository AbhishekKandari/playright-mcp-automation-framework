import pytest
from playwright.sync_api import expect
import re
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage
from utils.helpers import login_as
import allure

@pytest.fixture(autouse=True)
def setup(page):
    login_as(page, 'standard')
    inventory_page = InventoryPage(page)
    inventory_page.add_item_to_cart(0)
    inventory_page.go_to_cart()

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Cart Functionality")
@allure.story("View Cart")
@allure.description("Verify that the cart displays items correctly after adding an item from the inventory. This test ensures the cart item count is accurate and visual verification is captured.")
def test_view_cart_with_items(page):
    cart_page = CartPage(page)
    assert cart_page.get_cart_item_count() == 1
    screenshot = page.screenshot()
    allure.attach(screenshot, name="Cart with Items", attachment_type=allure.attachment_type.PNG)

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Cart Functionality")
@allure.story("Remove Items")
@allure.description("Verify that a user can successfully remove an item from the cart. This test ensures the cart updates correctly after removal and the item count becomes zero.")
def test_remove_item_from_cart(page):
    cart_page = CartPage(page)
    cart_page.remove_item(0)
    assert cart_page.get_cart_item_count() == 0

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Cart Functionality")
@allure.story("Navigation")
@allure.description("Verify that the Continue Shopping button navigates the user back to the inventory page. This test ensures proper navigation flow from cart to inventory.")
def test_continue_shopping_from_cart(page):
    cart_page = CartPage(page)
    cart_page.continue_shopping()
    expect(page).to_have_url(re.compile(r'/inventory'))

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Cart Functionality")
@allure.story("Checkout")
@allure.description("Verify that the checkout button correctly navigates the user to the checkout page. This test ensures the checkout flow is accessible from the cart.")
def test_checkout_from_cart(page):
    cart_page = CartPage(page)
    cart_page.checkout()
    expect(page).to_have_url(re.compile(r'/checkout'))

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Cart Functionality")
@allure.story("Persistence")
@allure.description("Verify that cart items persist after page refresh. This test ensures data is maintained in the session and cart state remains consistent.")
def test_cart_persists_after_page_refresh(page):
    cart_page = CartPage(page)
    assert cart_page.get_cart_item_count() == 1
    page.reload()
    assert cart_page.get_cart_item_count() == 1
