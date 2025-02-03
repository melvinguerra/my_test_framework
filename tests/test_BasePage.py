import pytest
from pages.LoginPage import LoginPage
from utils.testdata import TestData

# Gets the WebDriver from conftest.py
@pytest.mark.usefixtures("get_driver")
class BasePageTest:

    pass

    # def setUp(self):
    #     self.login_page = LoginPage(self.driver)
    #     self.driver.get(TestData.URL)
    # def tearDown(self):
    #     pass