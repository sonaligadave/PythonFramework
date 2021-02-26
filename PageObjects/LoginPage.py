from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    login_link="/html//div[@class='master-wrapper-page']/div[@class='header-menu']/ul[1]//a[@href='/electronics']"
    textbox_username_id="Email"
    textbox_password_id="Password"
    button_login_css=".button-1.login-button"
    link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver

    def clickOnLoginLink(self):
        # self.driver.find_element_by_css_selector(".ico - login").click()
        # self.driver.find_element_by_xpath(self.login_link).click()
        print("first test")

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickOnLogin(self):
        self.driver.find_element_by_css_selector(self.button_login_css).click()
