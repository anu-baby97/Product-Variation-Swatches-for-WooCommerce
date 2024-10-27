from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from config import TestData


class LoginPage(BasePage):
    username = (By.ID, "user_login")
    password = (By.ID, "user_pass")
    loginButton = (By.ID, "wp-submit")

# constructor
    def __init__(self, driver):
        super().__init__(driver)
        self.launch_page(TestData.GLOBAL_SETTINGS_URL)

    # page actions
    def enter_username(self, uname):
        self.text_clear(self.username)
        self.do_sendkeys(self.username, uname)

    def enter_password(self, pwd):
        self.text_clear(self.password)
        self.do_sendkeys(self.password, pwd)

    def click_login_button(self):
        self.do_click(self.loginButton)

    def validLogin(self, uname, pwd):
        self.text_clear(self.username)
        self.text_clear(self.password)
        self.enter_username(uname)
        self.enter_password(pwd)
        self.click_login_button()

    def checkLogin(self):
        self.sleep(1)
        self.text_clear(self.username)
        self.text_clear(self.password)
        self.enter_username(TestData.USER_NAME)
        #self.sleep(1)
        self.enter_password(TestData.PASSWORD)
        #self.sleep(1)
        self.click_login_button()
        # self.sleep(2)
