from php4dvd.pages import Page
from selenium.webdriver.common.by import By
from selenium import webdriver


class InternalPage(Page):

    @property
    def logout_button(self):
        return self.driver.find_element_by_text_link("Log out")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.ID, "loginform"))

'''
    @property
    def username_field(self):
        return self.driver.find_element_by_id("username")

    @property
    def password_field(self):
        return self.driver.find_element_by_id("password")


        '''