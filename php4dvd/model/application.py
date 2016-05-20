from selenium.common.exceptions import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from php4dvd.pages.page import Page
from php4dvd.pages.login_page import  LoginPage
from php4dvd.pages.internal_page import  InternalPage
from php4dvd.pages.user_management_page import  UserManagementPage
from php4dvd.pages.user_profile_page import  UserProfilePage
from model.user import  User

class Application(object):

    def __init__(self, driver, base_url):
        self.driver = driver
        driver.get(base_url)
        self.wait = WebDriverWait(driver, 10)
        self.login_page = LoginPage(driver, base_url)
        self.internal_page = InternalPage(driver, base_url)
        self.user_management_page = UserManagementPage(driver, base_url)
        self.user_profile_page = UserProfilePage(driver, base_url)



    def login(self, user):
        lp = self.login_page
        lp.username_field.clear()
        lp.username_field.send_keys(user.username)
        lp.password_field.clear()
        lp.password_field.send_keys(user.password)
        lp.submit_button.click()

    def logout(self):
        self.internal_page.logout_button.click()
        self.wait.until(EC.alert_is_present()).accept()

    def is_logged_in(self):
        return self.internal_page.is_this_page

    def is_logged_in_as(self,user):
        return self.is_logged_in()\
                and self.get_logged_user().username == user.username

    def get_logged_user(self):
        self.internal_page.user_profile_link.click()
        upp = self.user_profile_page
        upp.is_this_page
        return  User(username=upp.username_field.get_attribute("value"),
                     email=upp.email_field.get_attribute("value"))

    def is_not_logged_in(self):
        return self.login_page.is_this_page

    def add_user(self,user):
        self.internal_page.user_management_link.click()
        ump = self.user_management_page
        ump.is_this_page
        ump.user_form.username_field.send_keys(user.username)
        ump.user_form.email_field.send_keys(user.email)
        ump.user_form.password_field.send_keys(user.password)
        ump.user_form.password1_field.send_keys(user.password)
        #ump.user_form.role_select.select_by_visible_text(user.role)
        ump.user_form.submit_button.click()

    def ensure_logout(self):
        element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "nav, #loginform")))
        if element.tag_name == "nav":
            self.logout()

    def ensure_login_as(self,user):
        element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "nav, #loginform")))
        if element.tag_name == "nav":
            #we are on internal page
            if self.is_logged_in_as(user):
                return
            else:
                self.logout()
        self.login(user)
