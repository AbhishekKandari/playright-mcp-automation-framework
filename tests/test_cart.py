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
def test_view_cart_with_items(page):
    cart_page = CartPage(page)
    assert cart_page.get_cart_item_count() == 1
    screenshot = page.screenshot()
    allure.attach(screenshot, name="Cart with Items", attachment_type=allure.attachment_type.PNG)

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Cart Functionality")
@allure.story("Remove Items")
def test_remove_item_from_cart(page):
    cart_page = CartPage(page)
    cart_page.remove_item(0)
    assert cart_page.get_cart_item_count() == 0

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Cart Functionality")
@allure.story("Navigation")
def test_continue_shopping_from_cart(page):
    cart_page = CartPage(page)
    cart_page.continue_shopping()
    expect(page).to_have_url(re.compile(r'/inventory'))

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Cart Functionality")
@allure.story("Checkout")
def test_checkout_from_cart(page):
    cart_page = CartPage(page)
    cart_page.checkout()
    expect(page).to_have_url(re.compile(r'/checkout'))

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Cart Functionality")
@allure.story("Persistence")
def test_cart_persists_after_page_refresh(page):
    cart_page = CartPage(page)
    assert cart_page.get_cart_item_count() == 1
    page.reload()
    assert cart_page.get_cart_item_count() == 1
