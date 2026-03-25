class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = '#user-name'
        self.password_input = '#password'
        self.login_button = '#login-button'
        self.error_message = '.error-message-container'

    def goto(self):
        self.page.goto('https://www.saucedemo.com/')

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_error_message(self):
        return self.page.text_content(self.error_message)

    def logout(self):
        self.page.click('#react-burger-menu-btn')
        self.page.click('#logout_sidebar_link')
