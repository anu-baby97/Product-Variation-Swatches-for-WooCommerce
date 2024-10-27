import time
import pytest

from pages.LoginPage import LoginPage
from tests.BaseClass import BaseClass
from config import TestData
from utilities.helper import get_case

@pytest.mark.order(1)
class TestLoginPage(BaseClass):
    def test_login(self):
        print('Logging into the website')
        # log = BaseClass().getLogger()
        loginPage = LoginPage(self.driver)
        time.sleep(3)
        loginPage.enter_username(TestData.USER_NAME)
        loginPage.enter_password(TestData.PASSWORD)
        loginPage.click_login_button()
        # log.info("User is logged in")
        # get_case('1010983')

