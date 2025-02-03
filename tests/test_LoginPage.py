from pages.LoginPage import LoginPage
from tests.test_BasePage import BasePageTest
from utils.testdata import TestData
import time

# Remember to name the test classes starting with "Test"
# And any function in the test class must start with "test_" for it to be collected by pytest
class TestLoginPage(BasePageTest):

    def test_empty_credentials_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.BLANK_TEXT, TestData.BLANK_TEXT)
        assert self.login_page.get_error_message() == "Epic sadface: Username is required", "Error message for blank username did not appear or changed"
        print(self.login_page.get_error_message())

    def test_with_username_no_password_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.VALID_USERNAME, TestData.BLANK_TEXT)
        assert self.login_page.get_error_message() == "Epic sadface: Password is required"
        print(self.login_page.get_error_message())

    def test_invalid_credentials_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.INVALID_USERNAME, TestData.INVALID_PASSWORD)
        assert self.login_page.get_error_message() == "Epic sadface: Username and password do " \
                                                     "not match any user in this service"
        print(self.login_page.get_error_message())

    def test_valid_credentials_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        assert "/inventory.html" in self.driver.current_url , "Did not reach SauceDemo homepage or homepage URL changed"

    def test_successful_login_and_logout(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        self.login_page.do_logout()
        assert "https://www.saucedemo.com/" == self.driver.current_url








