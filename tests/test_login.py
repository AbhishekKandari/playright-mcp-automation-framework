import pytest
from playwright.sync_api import expect
import re
import allure
from pages.LoginPage import LoginPage
from utils.helpers import test_data

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Login Functionality")
@allure.story("Valid Login")
@allure.step("Navigate to login page")
def test_valid_login_standard_user(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(test_data['users']['standard']['username'], test_data['users']['standard']['password'])
    expect(page).to_have_url(re.compile(r'/inventory'))
    screenshot = page.screenshot()
    allure.attach(screenshot, name="Login Successful", attachment_type=allure.attachment_type.PNG)

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Login Functionality")
@allure.story("Invalid Login")
@allure.step("Test invalid username login")
def test_invalid_username(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login('invalid_user', 'secret_sauce')
    error = login_page.get_error_message()
    assert 'Username and password do not match' in error
    screenshot = page.screenshot()
    allure.attach(screenshot, name="Invalid Username Error", attachment_type=allure.attachment_type.PNG)

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Login Functionality")
@allure.story("Invalid Login")
@allure.step("Test invalid password login")
def test_invalid_password(page):
    with allure.step("Initialize login page"):
        login_page = LoginPage(page)
    with allure.step("Navigate to login page"):
        login_page.goto()
    with allure.step("Attempt login with invalid password"):
        login_page.login('standard_user', 'invalid_pass')
    with allure.step("Verify error message"):
        error = login_page.get_error_message()
        assert 'Username and password do not match' in error
    screenshot = page.screenshot()
    allure.attach(screenshot, name="Invalid Password Error", attachment_type=allure.attachment_type.PNG)

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Login Functionality")
@allure.story("Locked User")
@allure.step("Test locked out user login")
def test_locked_out_user(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(test_data['users']['locked']['username'], test_data['users']['locked']['password'])
    error = login_page.get_error_message()
    assert 'Sorry, this user has been locked out' in error
    screenshot = page.screenshot()
    allure.attach(screenshot, name="Locked Out User Error", attachment_type=allure.attachment_type.PNG)

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Login Functionality")
@allure.story("Empty Credentials")
@allure.step("Test empty credentials login")
def test_empty_username_and_password(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login('', '')
    error = login_page.get_error_message()
    assert 'Username is required' in error
    screenshot = page.screenshot()
    allure.attach(screenshot, name="Empty Credentials Error", attachment_type=allure.attachment_type.PNG)

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Login Functionality")
@allure.story("Logout")
@allure.step("Test logout flow")
def test_logout_flow(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(test_data['users']['standard']['username'], test_data['users']['standard']['password'])
    login_page.logout()
    expect(page).to_have_url(re.compile(r'/'))
    screenshot = page.screenshot()
    allure.attach(screenshot, name="Logout Successful", attachment_type=allure.attachment_type.PNG)

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Login Functionality")
@allure.story("Direct URL Access")
@allure.step("Test direct URL access")
def test_direct_url_access(page):
    page.goto('https://www.saucedemo.com/inventory')
    expect(page).to_have_url(re.compile(r'/'))

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Login Functionality")
@allure.story("Session Handling")
@allure.step("Test session handling")
def test_session_handling(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(test_data['users']['standard']['username'], test_data['users']['standard']['password'])
    page.context.clear_cookies()
    page.reload()
    expect(page).to_have_url(re.compile(r'/'))

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Login Functionality")
@allure.story("Performance User")
@allure.step("Test performance user")
def test_performance_user(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(test_data['users']['performance']['username'], test_data['users']['performance']['password'])
    expect(page).to_have_url(re.compile(r'/inventory'))
