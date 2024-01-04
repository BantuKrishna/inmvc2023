import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys

from pageObjects.BookRoom import BookRoom
from pageObjects.LoginPage import LoginPage
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen

class Test_002_BookRoom:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    title = ReadConfig.gettitle()
    desc = ReadConfig.getdesc()
    meetlink = ReadConfig.getmeetlink()
    add = ReadConfig.getadd()
    logger=LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_bookroom(self,setup):
        self.logger.info("*************** Test_002_BookRoom **********************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***************** Login successful ********")

        self.logger.info("************ Starting Book Room Test **********")

        self.br = BookRoom(self.driver)
        self.br.clickBookRoom()
        self.br.clickRoom()
        self.br.clickDat()
        self.br.clickDay()
        self.br.clicktime()
        self.br.setTitle(self.title)
        self.br.setDesc(self.desc)
        self.br.clickVcall()
        self.br.clickBroom()
        time.sleep(3)
        if "Successfully booked a meeting room" in self.driver.page_source:
            self.logger.info("********** Book Room test is passed *********")
            self.driver.close()

        else:
            # Log and take a screenshot
            self.logger.error("************** Book Room test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_bookroom.png")
            assert False

    @pytest.mark.regression
    def test_bookroom1(self, setup):
        self.logger.info("*************** Test_002_BookRoom **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***************** Login successful ********")

        self.logger.info("************ Starting Book Room1 Test **********")

        self.br = BookRoom(self.driver)
        self.br.clickBookRoom()
        self.br.clickRoom()
        self.br.clickDat()
        self.br.clickDay()
        self.br.clicktimes()
        self.br.setTitle(self.title)
        self.br.setDesc(self.desc)
        self.br.clickApps()
        self.br.clickBroom()
        time.sleep(3)
        if "Invalid Params" in self.driver.page_source:
            self.logger.info("********** Book Room test1 is passed *********")
            self.driver.close()

        else:
            # Log and take a screenshot
            self.logger.error("************** Book Room test1 is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_bookroom.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_bookroom2(self, setup):
        self.logger.info("*************** Test_002_BookRoom **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***************** Login successful ********")

        self.logger.info("************ Starting Book Room2 Test **********")

        self.br = BookRoom(self.driver)
        self.br.clickBookRoom()
        self.br.clickRoom()
        self.br.clickDat()
        self.br.clickDay()
        self.br.clicktimens()
        self.br.setTitle(self.title)
        self.br.setDesc(self.desc)
        self.br.setMeetlink(self.meetlink)
        self.br.clickBroom()
        time.sleep(5)
        if "Successfully booked a meeting room" in self.driver.page_source:
            self.logger.info("********** Book Room test2 is passed *********")
            self.driver.close()

        else:
            # Log and take a screenshot
            self.logger.error("************** Book Room test2 is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_bookroom.png")
            assert False


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_bookroom3(self, setup):
        self.logger.info("*************** Test_002_BookRoom **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***************** Login successful ********")

        self.logger.info("************ Starting Book Room3 Test **********")

        self.br = BookRoom(self.driver)
        self.br.clickBookRoom()
        self.br.clickRoom()
        self.br.clickDat()
        self.br.clickDay()
        self.br.clicktimeens()
        self.br.setTitle(self.title)
        self.br.setDesc(self.desc)
        self.br.clickVcall()
        self.br.setAdd(self.add)
        self.br.setAdd(Keys.ENTER)
        self.br.clickBroom()
        time.sleep(5)
        if "Successfully booked a meeting room" in self.driver.page_source:
            self.logger.info("********** Book Room test3 is passed *********")
            self.driver.close()

        else:
            # Log and take a screenshot
            self.logger.error("************** Book Room test3 is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_bookroom.png")
            assert False



