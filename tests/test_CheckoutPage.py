from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from tests.test_BasePage import BasePageTest
from utils.testdata import TestData
import time

# Remember to name the test classes starting with "Test"
# And any function in the test class must start with "test_" for it to be collected by pytest
class TestCheckoutPage(BasePageTest):

    def test_empty_checkout_information(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        self.inventory_page = InventoryPage(self.driver)
        self.inventory_page.add_items_to_cart()
        self.cart_page = CartPage(self.driver)
        self.cart_page.go_to_cart()
        self.cart_page.go_to_checkout()
        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_page.do_fillup_information(TestData.BLANK_TEXT, TestData.BLANK_TEXT, TestData.BLANK_TEXT)
        self.checkout_page.do_continue_checkout()
        assert self.checkout_page.get_error_message() == "Error: First Name is required"
        print(self.checkout_page.get_error_message())

    def test_first_name_required_checkout(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        self.inventory_page = InventoryPage(self.driver)
        self.inventory_page.add_items_to_cart()
        self.cart_page = CartPage(self.driver)
        self.cart_page.go_to_cart()
        self.cart_page.go_to_checkout()
        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_page.do_fillup_information(TestData.BLANK_TEXT, TestData.BLANK_TEXT, TestData.BLANK_TEXT)
        self.checkout_page.do_continue_checkout()
        assert self.checkout_page.get_error_message() == "Error: First Name is required"
        print(self.checkout_page.get_error_message())

    def test_last_name_required_checkout(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        self.inventory_page = InventoryPage(self.driver)
        self.inventory_page.add_items_to_cart()
        self.cart_page = CartPage(self.driver)
        self.cart_page.go_to_cart()
        self.cart_page.go_to_checkout()
        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_page.do_fillup_information(TestData.FIRST_NAME, TestData.BLANK_TEXT, TestData.BLANK_TEXT)
        self.checkout_page.do_continue_checkout()
        assert self.checkout_page.get_error_message() == "Error: Last Name is required"
        print(self.checkout_page.get_error_message())

    def test_postal_code_required_checkout(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        self.inventory_page = InventoryPage(self.driver)
        self.inventory_page.add_items_to_cart()
        self.cart_page = CartPage(self.driver)
        self.cart_page.go_to_cart()
        self.cart_page.go_to_checkout()
        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_page.do_fillup_information(TestData.FIRST_NAME, TestData.LAST_NAME, TestData.BLANK_TEXT)
        self.checkout_page.do_continue_checkout()
        assert self.checkout_page.get_error_message() == "Error: Postal Code is required"
        print(self.checkout_page.get_error_message())

    def test_valid_checkout_information(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        self.inventory_page = InventoryPage(self.driver)
        self.inventory_page.add_items_to_cart()
        self.cart_page = CartPage(self.driver)
        self.cart_page.go_to_cart()
        self.cart_page.go_to_checkout()
        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_page.do_fillup_information(TestData.FIRST_NAME, TestData.LAST_NAME, TestData.POSTAL_CODE)
        self.checkout_page.do_continue_checkout()
        self.checkout_page.do_finish_checkout()
        assert self.checkout_page.get_order_complete_msg() == "Thank you for your order!"
        print(self.checkout_page.get_order_complete_msg())