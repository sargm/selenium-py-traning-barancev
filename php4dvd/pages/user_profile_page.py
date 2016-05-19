from php4dvd.pages import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import Select



class UserMProfilePage(Page):

    @property
    def username_field(self):
        return self.driver.find_element_by_name("username")

    @property
    def email_field(self):
        return self.driver.find_element_by_name("email")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.ID, "loginform"))


