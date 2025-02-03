from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage
from pages.CartPage import CartPage
from tests.test_BasePage import BasePageTest
from utils.testdata import TestData
import time

# Remember to name the test classes starting with "Test"
# And any function in the test class must start with "test_" for it to be collected by pytest
class TestCartPage(BasePageTest):

    def test_remove_items_from_cart(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        self.inventory_page = InventoryPage(self.driver)
        self.inventory_page.add_items_to_cart()
        self.cart_page = CartPage(self.driver)
        self.cart_page.go_to_cart()
        self.cart_page.remove_all_items_from_cart()
        assert self.inventory_page.is_cart_empty() is True