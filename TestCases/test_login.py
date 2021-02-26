import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage

class Test_100_Login:
    baseUrl = "https://frontend.nopcommerce.com/";
    username = "admin@yourstore.com";
    password = "admin1"


    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "nopCommerce demo store":
            assert True
        else:
            assert False
        self.driver.close()

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.clickOnLoginLink()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickOnLogin()
        self.driver.close()


