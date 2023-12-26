import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys

from pageObjects.BookRoom import BookRoom
from pageObjects.CalendarPage import CalendarPage
from pageObjects.LoginPage import LoginPage
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen

class Test_003_Calendar:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_calendar(self,setup):
        self.logger.info("*************** Test_002_Calendar **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***************** Login successful ********")

        self.logger.info("************ Starting Calendar Test **********")

        self.cp = CalendarPage(self.driver)
        self.cp.clickCalendar()
        self.cp.clickMrooms()
        self.cp.clickAll()
        self.cp.clickRoom()
        self.cp.clickAppl()
        self.cp.clickArr()
        self.cp.clickNex()
        self.cp.clickDat()
        time.sleep(3)
        self.cp.clickTim()
        time.sleep(3)
        self.driver.close()