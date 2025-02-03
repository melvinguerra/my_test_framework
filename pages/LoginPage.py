from pages.BasePage import BasePage
from utils.testdata import TestData
from selenium.webdriver.common.by import By
import time


class LoginPage(BasePage):

    # By locators
    # Identify page elements/objects(input fields, buttons, links)
    user_name = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.CSS_SELECTOR, "[data-test='error']")
    burger_menu_button = (By.ID, "react-burger-menu-btn")
    logout_button = (By.ID, "logout_sidebar_link")

    # Actions
    # What interactions you can do in the page

    def __init__(self, driver):
        super().__init__(driver)
        self.open_url()

    def do_login(self, username, password):
        self.send_keys(self.user_name, username), print("Entered username: ", username)
        self.send_keys(self.password, password), print("Entered password: ", password)
        self.press_button(self.login_button), print("Clicked on login button")

    def do_logout(self):
        self.press_button(self.burger_menu_button), print("Clicked on burger menu button")
        self.do_click(self.logout_button), print("Clicked on logout link")

    def get_error_message(self):
        error = self.get_element_text(self.error_message)
        return error