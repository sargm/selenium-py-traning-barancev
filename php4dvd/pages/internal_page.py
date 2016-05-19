from php4dvd.pages import Page
from selenium.webdriver.common.by import By
from selenium import webdriver


class InternalPage(Page):

    @property
    def logout_button(self):
        return self.driver.find_element_by_text_link("Log out")

    @property
    def user_management_link(self):
        return self.driver.find_element_by_css_selector("nav a[href $= '?go=users']")

    @property
    def user_profile_link(self):
        return self.driver.find_element_by_css_selector("nav a[href $= '?go=users']") #!!!!!!


    @property
    def is_this_page(self):
        return self.is_element_visible((By.CSS_SELECTOR, "nav"))

