import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    usernames = "krishna.tinstavc.com"
    passwords = "inmvC@123"

    logger=LogGen.loggen()


    def test_loginTitle(self,setup):
        self.logger.info("************** Test_oo1_Login ************")
        self.logger.info("************* Verifying Login Title **********")
        self.driver = setup
        time.sleep(3)
        self.driver.get(self.baseURL)
        time.sleep(3)
        act_title=self.driver.title
        if act_title=="InMvc":
            assert True
            self.driver.close()
            self.logger.info("************ Login page title is passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_loginTitle.png")
            self.driver.close()
            self.logger.error("************* Login page title is failed *********")
            assert False


    def test_login(self,setup):
        self.logger.info("************ Verifying Login Test *************")
        self.driver = setup
        time.sleep(3)
        self.driver.get(self.baseURL)
        time.sleep(3)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.passwords)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="InMvc":
            assert True
            self.logger.info("********** Login test is passed *********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("************** Login test is failed **********")
            assert False

    def test_login1(self, setup):
        self.logger.info("************ Verifying Login1 Test *************")
        self.driver = setup
        time.sleep(3)
        self.driver.get(self.baseURL)
        time.sleep(3)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.usernames)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        if "Invalid Email ID" in self.driver.page_source:
            self.logger.info("********** Login test is passed *********")
            self.driver.close()
        else:
            # Log and take a screenshot
            self.logger.error("************** Login test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login1.png")
            assert False


    def test_login2(self, setup):
        self.logger.info("************ Verifying Login2 Test *************")
        self.driver = setup
        time.sleep(3)
        self.driver.get(self.baseURL)
        time.sleep(3)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.passwords)
        self.lp.clickLogin()
        if "Incorrect username or password" in self.driver.page_source:
            self.logger.info("********** Login test is passed *********")
            self.driver.close()
        else:
            # Log and take a screenshot
            self.logger.error("************** Login test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login2.png")
            assert False

