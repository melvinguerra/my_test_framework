from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.testdata import TestData

# Generic actions for all pages
# Inherit from this class to interact with the DOM elements

class BasePage:

    def __init__(self, driver): #Receive WebDriver
        self.driver = driver


    def open_url(self):
        self.driver.get(TestData.URL) # Opens our application under test
        print("Accessed page:", self.driver.title)

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()
        # Works better for element that is not visible on page load

    def press_button(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).click()

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_element_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located(by_locator))
        # Will return True if element is not located
        return bool(element)
