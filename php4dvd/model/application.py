from selenium.common.exceptions import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from php4dvd.pages.page import Page
from php4dvd.pages.login_page import  LoginPage
from php4dvd.pages.internal_page import  InternalPage

class Application(object):

    def __init__(self, driver, base_url):
        driver.get(base_url)
        self.wait = WebDriverWait(driver, 10)
        self.login_page = LoginPage(driver, base_url)
        self.internal_page = InternalPage(driver, base_url)


    #def go_to_home_page(self):
    #    self.driver.get(self.base_url)

    def login(self, user):
        lp = self.login_page
        lp.username_field.clear()
        lp.username_field.send_keys(user.username)
        lp.username_field.clear()
        lp.username_field.send_keys(user.password)
        lp.submit_button.click()


    def logout(self):
        self.internal_page.logout_button.click()
        self.wait.until(EC.alert_is_present()).accept()


    def is_logged_in(self):
        return self.login_page.is_this_page

    def is_not_logged_in(self):
        return self.internal_page.is_this_page
