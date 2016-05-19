from php4dvd.pages import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import Select



class UserManagementPage(Page):

    @property
    def username_field(self):
        return self.driver.find_element_by_name("username")

    @property
    def password_field(self):
        return self.driver.find_element_by_name("password")

    @property
    def password1_field(self):
        return self.driver.find_element_by_name("password2")

    @property
    def email_field(self):
        return self.driver.find_element_by_name("email")

    @property
    def submit_button(self):
        return self.driver.find_element_by_id("submit")

    @property
    def role_select(self):
        return Select(self.driver.find_element_by_name("role"))