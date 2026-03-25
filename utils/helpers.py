import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
test_data_path = os.path.join(script_dir, 'test-data.json')

with open(test_data_path) as f:
    test_data = json.load(f)

def login_as(page, user_type):
    from pages.LoginPage import LoginPage
    login_page = LoginPage(page)
    user = test_data['users'][user_type]
    login_page.goto()
    login_page.login(user['username'], user['password'])