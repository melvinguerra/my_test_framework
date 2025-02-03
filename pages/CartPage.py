from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import time

class CartPage(BasePage):

    # By locators
    # Identify page elements/objects(input fields, buttons, links)
    shopping_cart_link = (By.CLASS_NAME, "shopping_cart_link")
    checkout_button = (By.ID, "checkout")
    remove_backpack = (By.ID, "remove-sauce-labs-backpack")
    remove_bike_light = (By.ID, "remove-sauce-labs-bike-light")
    remove_bolt_t_shirt = (By.ID, "remove-sauce-labs-bolt-t-shirt")
    remove_fleece_jacket = (By.ID, "remove-sauce-labs-fleece-jacket")
    remove_onesie = (By.ID, "remove-sauce-labs-onesie")
    remove_t_shirt_red = (By.ID, "remove-test.allthethings()-t-shirt-(red)")


    # Actions
    # What interactions you can do in the page

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_cart(self):
        self.press_button(self.shopping_cart_link)
        print("Went to shopping cart")

    def go_to_checkout(self):
        self.press_button(self.checkout_button)
        print("Went to checkout")

    def remove_all_items_from_cart(self):
        self.press_button(self.remove_backpack)
        self.press_button(self.remove_bike_light)
        self.press_button(self.remove_bolt_t_shirt)
        self.press_button(self.remove_fleece_jacket)
        self.press_button(self.remove_onesie)
        self.press_button(self.remove_t_shirt_red)
        print("Removed all items from cart")


