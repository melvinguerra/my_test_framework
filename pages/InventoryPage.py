from faulthandler import is_enabled

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import time

class InventoryPage(BasePage):

    # By locators
    # Identify page elements/objects(input fields, buttons, links)
    backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    bike_light = (By.ID, "add-to-cart-sauce-labs-bike-light")
    bolt_t_shirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    fleece_jacket = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
    t_shirt_red = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    shopping_cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    # Actions
    # What interactions you can do in the page

    def __init__(self, driver):
        super().__init__(driver)

    def add_items_to_cart(self):
        self.press_button(self.backpack)
        print("Clicked on", self.backpack)
        self.press_button(self.bike_light)
        print("Clicked on", self.bike_light)
        self.press_button(self.bolt_t_shirt)
        print("Clicked on", self.bolt_t_shirt)
        self.press_button(self.fleece_jacket)
        print("Clicked on", self.fleece_jacket)
        self.press_button(self.onesie)
        print("Clicked on", self.onesie)
        self.press_button(self.t_shirt_red)
        print("Clicked on", self.t_shirt_red)

    def get_shopping_cart_count(self):
        cart_count = self.get_element_text(self.shopping_cart_badge)
        print("Cart Badge Count/Items in shopping cart: ", cart_count)
        return cart_count

    def is_cart_empty(self):
        return self.is_element_enabled(self.shopping_cart_badge)
    # For refactoring because cart is available in other pages

