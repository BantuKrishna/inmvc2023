import time
from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.BookRoom import BookRoom
from pageObjects.CalendarPage import CalendarPage
from pageObjects.LoginPage import LoginPage
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen

class Test_003_Calendar:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    add = ReadConfig.getadd()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
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
        self.cp.clickEdit()
        time.sleep(3)
        self.cp.setadd(self.add)
        self.cp.setadd(Keys.ENTER)
        time.sleep(3)
        self.cp.clickUpdate()
        time.sleep(3)
        self.cp.clickUpda()


        # def clickTim(self):
        #     wait = WebDriverWait(self.driver, 10)  # Adjust the timeout as needed
            # time_slot_element = wait.until(
            #     EC.element_to_be_clickable((By.XPATH, self.button_tim_xpath))
            # )
        #     time.sleep(5)
        # self.cp.button_tim_xpath.click()


        time.sleep(5)
        self.driver.close()