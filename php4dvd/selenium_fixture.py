from selenium import webdriver
from model.application import Application
import pytest

@pytest.fixture(scope="module")
def app(request, browser_type, base_url):
    if browser_type == "firefox":
        driver = webdriver.Firefox()
    elif browser_type == "chrome":
        driver = webdriver.Chrome()
    elif browser_type == "ie":
        driver = webdriver.Ie()
    #driver.implicitly_wait(30)
    request.addfinalizer(driver.quit)   #close brawser
    return Application(driver, base_url)
