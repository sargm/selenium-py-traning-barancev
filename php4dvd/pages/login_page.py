from php4dvd.pages import Page
from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage(Page):

    @property
    def username_field(self):
        return self.driver.find_element_by_id("username")

    @property
    def password_field(self):
        return self.driver.find_element_by_id("password")

    @property
    def submit_button(self):
        return self.driver.find_element_by_id("submit")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CSS_SELECTOR,"nav"))