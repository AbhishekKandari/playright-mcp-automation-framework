import pytest
from playwright.sync_api import expect
import re
from pages.InventoryPage import InventoryPage
from utils.helpers import login_as
import allure

@pytest.fixture(autouse=True)
def setup(page):
    login_as(page, 'standard')

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Inventory Functionality")
@allure.story("Add to Cart")
@allure.description("Verify that a single item can be successfully added to the cart. This test checks the cart badge count updates to 1 after adding an item.")
def test_add_single_item_to_cart(page):
    inventory_page = InventoryPage(page)
    inventory_page.add_item_to_cart(0)
    badge = inventory_page.get_cart_badge_count()
    assert badge == '1'
    screenshot = page.screenshot()
    allure.attach(screenshot, name="Item Added to Cart", attachment_type=allure.attachment_type.PNG)

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Inventory Functionality")
@allure.story("Add to Cart")
@allure.description("Verify that multiple items can be added to the cart. This test checks the cart badge count updates correctly to reflect multiple items.")
def test_add_multiple_items_to_cart(page):
    inventory_page = InventoryPage(page)
    inventory_page.add_item_to_cart(0)
    inventory_page.add_item_to_cart(1)
    badge = inventory_page.get_cart_badge_count()
    assert badge == '2'

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Inventory Functionality")
@allure.story("Remove from Cart")
@allure.description("Verify that an item can be removed directly from the inventory page. This test ensures the cart badge count decreases to 0 after removal.")
def test_remove_item_from_cart_on_inventory_page(page):
    inventory_page = InventoryPage(page)
    inventory_page.add_item_to_cart(0)
    assert inventory_page.get_cart_badge_count() == '1'
    inventory_page.remove_item_from_cart(0)
    assert inventory_page.get_cart_badge_count() == '0'

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Inventory Functionality")
@allure.story("Sorting")
@allure.description("Verify that products can be sorted alphabetically from A to Z. This test ensures products are displayed in ascending alphabetical order.")
def test_sort_products_by_name_a_to_z(page):
    inventory_page = InventoryPage(page)
    inventory_page.sort_products('az')
    names = inventory_page.get_product_names()
    assert names == sorted(names)

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Inventory Functionality")
@allure.story("Sorting")
@allure.description("Verify that products can be sorted alphabetically from Z to A. This test ensures products are displayed in descending alphabetical order.")
def test_sort_products_by_name_z_to_a(page):
    inventory_page = InventoryPage(page)
    inventory_page.sort_products('za')
    names = inventory_page.get_product_names()
    assert names == sorted(names, reverse=True)

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Inventory Functionality")
@allure.story("Sorting")
@allure.description("Verify that products can be sorted by price from low to high. This test ensures products are displayed in ascending price order.")
def test_sort_products_by_price_low_to_high(page):
    inventory_page = InventoryPage(page)
    inventory_page.sort_products('lohi')
    prices = inventory_page.get_product_prices()
    numeric_prices = [float(p.replace('$', '')) for p in prices]
    assert numeric_prices == sorted(numeric_prices)

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Inventory Functionality")
@allure.story("Sorting")
@allure.description("Verify that products can be sorted by price from high to low. This test ensures products are displayed in descending price order.")
def test_sort_products_by_price_high_to_low(page):
    inventory_page = InventoryPage(page)
    inventory_page.sort_products('hilo')
    prices = inventory_page.get_product_prices()
    numeric_prices = [float(p.replace('$', '')) for p in prices]
    assert numeric_prices == sorted(numeric_prices, reverse=True)

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Inventory Functionality")
@allure.story("Navigation")
@allure.description("Verify that the cart can be navigated to from the inventory page. This test ensures the cart icon correctly navigates to the cart URL.")
def test_navigate_to_cart_from_inventory(page):
    inventory_page = InventoryPage(page)
    inventory_page.add_item_to_cart(0)
    inventory_page.go_to_cart()
    expect(page).to_have_url(re.compile(r'/cart'))

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Inventory Functionality")
@allure.story("Product Details")
@allure.description("Verify that product details can be viewed by clicking on a product name. This test ensures navigation to the product details page.")
def test_view_product_details(page):
    page.click('.inventory_item_name')
    expect(page).to_have_url(re.compile(r'/inventory-item'))

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Inventory Functionality")
@allure.story("Product Details")
@allure.description("Verify that an item can be added to cart from the product details page. This test ensures the cart badge updates correctly after adding from details page.")
def test_add_item_from_product_details_page(page):
    page.click('.inventory_item_name')
    page.click('#add-to-cart')
    page.go_back()
    inventory_page = InventoryPage(page)
    assert inventory_page.get_cart_badge_count() == '1'

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Inventory Functionality")
@allure.story("UI Consistency")
@allure.description("Verify UI state consistency when adding and removing items. This test ensures the cart badge count remains consistent during repeated add/remove operations.")
def test_ui_state_consistency(page):
    inventory_page = InventoryPage(page)
    for i in range(3):
        inventory_page.add_item_to_cart(0)
        badge = inventory_page.get_cart_badge_count()
        assert badge == '1'
        inventory_page.remove_item_from_cart(0)
        badge = inventory_page.get_cart_badge_count()
        assert badge == '0'

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Inventory Functionality")
@allure.story("Multi-tab Behavior")
@allure.description("Verify that a new browser tab can be opened and navigated to the inventory page. This test ensures multi-tab functionality works correctly.")
def test_multi_tab_behavior(page):
    inventory_page = InventoryPage(page)
    inventory_page.add_item_to_cart(0)
    new_page = page.context.new_page()
    new_page.goto('https://www.saucedemo.com/inventory')
    assert new_page.url == 'https://www.saucedemo.com/inventory'
