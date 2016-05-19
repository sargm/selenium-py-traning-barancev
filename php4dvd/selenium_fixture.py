from selenium import webdriver
from model.application import Application
import pytest

@pytest.fixture(scope="module")
def app(request):
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    request.addfinalizer(driver.quit)   #close brawser
    return Application(driver)
