import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.testdata import TestData


# import pages that will need the webdriver
from pages.LoginPage import LoginPage
# from pages.InventoryPage import InventoryPage


@pytest.fixture()
def get_driver(request):

    global driver
    driver = None

    PATH = "./driver/chromedriver.exe"
    service = Service(PATH)
    driver = webdriver.Chrome(service=service) # downloads the chrome webdriver if you pass no arguments in .Chrome()
    request.cls.driver = driver

    yield
    driver.quit()
    #driver.quit()  quit calls dispose() where dispose() closes all browser windows and safely ends the session
