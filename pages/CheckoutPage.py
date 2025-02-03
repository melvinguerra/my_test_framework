from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import time

class CheckoutPage(BasePage):

    # By locators
    # Identify page elements/objects(input fields, buttons, links)
    first_name_field = (By.ID, "first-name")
    last_name_field = (By.ID, "last-name")
    postal_code_field = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    finish_button = (By.ID, "finish")
    order_complete_message = (By.CLASS_NAME, "complete-header")
    error_message = (By.CSS_SELECTOR, "[data-test='error']")


    # Actions
    # What interactions you can do in the page

    def __init__(self, driver):
        super().__init__(driver)

    def do_fillup_information(self, first_name, last_name, postal_code):
        self.send_keys(self.first_name_field, first_name)
        self.send_keys(self.last_name_field, last_name)
        self.send_keys(self.postal_code_field, postal_code)

    def do_continue_checkout(self):
        self.press_button(self.continue_button)
        print("Continue checkout")


    def do_finish_checkout(self):
        self.press_button(self.finish_button)
        print("Finish checkout")

    def get_order_complete_msg(self):
        element = self.get_element_text(self.order_complete_message)
        return element


    def get_error_message(self):
        error = self.get_element_text(self.error_message)
        return error



