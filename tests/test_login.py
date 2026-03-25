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
@allure.description("Verify that a standard user can successfully log in with valid credentials. This test ensures the user is redirected to the inventory page after login.")
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
@allure.description("Verify that login fails with an invalid username. This test ensures an appropriate error message is displayed when the username doesn't exist.")
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
@allure.description("Verify that login fails with an invalid password. This test ensures an appropriate error message is displayed when the password is incorrect.")
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
@allure.description("Verify that a locked out user cannot log in. This test ensures the appropriate error message is displayed for locked accounts.")
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
@allure.description("Verify that login fails when both username and password are empty. This test ensures validation requires both fields to be filled.")
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
@allure.description("Verify that a logged-in user can successfully log out. This test ensures the user is redirected to the login page after logout.")
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
@allure.description("Verify that accessing the inventory page directly without login redirects to the login page. This test ensures proper authentication protection.")
def test_direct_url_access(page):
    page.goto('https://www.saucedemo.com/inventory')
    expect(page).to_have_url(re.compile(r'/'))

@allure.epic("SauceDemo E2E Testing")
@allure.feature("Login Functionality")
@allure.story("Session Handling")
@allure.step("Test session handling")
@allure.description("Verify that clearing cookies invalidates the session. This test ensures the user is redirected to login after clearing session cookies.")
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
@allure.description("Verify that the performance glitch user can log in successfully. This test ensures different user types can access the system.")
def test_performance_user(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(test_data['users']['performance']['username'], test_data['users']['performance']['password'])
    expect(page).to_have_url(re.compile(r'/inventory'))
