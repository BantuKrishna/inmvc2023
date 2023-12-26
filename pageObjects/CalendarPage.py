import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class CalendarPage:

    button_calendar_xpath = "/html/body/div/div/div[1]/div[2]/div[2]/div[1]/ul/li[2]/div/div"
    button_mrooms_xpath = "/html/body/div/div/div[1]/div[2]/div[3]/div/div/div/div/div[1]/div/div[2]/span/button/span[1]"
    button_all_xpath = "/html/body/div[2]/div[3]/ul/div[1]/div[2]/span/input"
    button_room_xpath = "(//input[@class='PrivateSwitchBase-input css-1m9pwf3'])[2]"
    button_appl_xpath = "//span[text()='Apply']"
    button_arr_xpath = "/html/body/div/div/div[1]/div[2]/div[3]/div/div/div/div/div[1]/div/div[1]/div/span[1]"
    button_nex_xpath = "//button[@title='Next month']"
    button_dat_xpath = "/html/body/div[2]/div[3]/ul/div/div[2]/div/div/div[2]/div/div[3]/button[4]"
    button_tim_xpath = "(//div[@class='rbc-timeslot-group'])[35]"

    def __init__(self, driver):
        self.driver = driver

    def clickCalendar(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_calendar_xpath).click()

    def clickMrooms(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.button_mrooms_xpath).click()

    def clickAll(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.button_all_xpath).click()

    def clickRoom(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.button_room_xpath).click()

    def clickAppl(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.button_appl_xpath).click()

    def clickArr(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.button_arr_xpath).click()

    def clickNex(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.button_nex_xpath).click()

    def clickDat(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.button_dat_xpath).click()

    def clickTim(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.button_tim_xpath)
        time.sleep(2)