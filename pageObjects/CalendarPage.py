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
    button_dat_xpath = "//button[normalize-space()='13']"
    button_tim_xpath = "//div[@title='10:00 AM – 10:15 AM: Testing Team Meeting']"
    button_Edit_xpath = "//button[normalize-space()='Edit meeting']"
    textbox_add_xpath = "/html/body/div/div/div[1]/div[2]/div[3]/div/div/div/div/div/div[2]/div[7]/div/div[1]/div/div/div/div/div/input"
    button_Update_xpath = "//button[normalize-space()='Update Meeting']"
    button_Upda_xpath = "//button[normalize-space()='Update']"



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

    # def clickTim(self):
    #     time.sleep(5)
    #     self.driver.find_element(By.CSS_SELECTOR,self.button_tim_xpath).click()

    def clickTim(self):
            time.sleep(5)  # It's better to replace this sleep with JavaScript Executor
            element = self.driver.find_element(By.XPATH, self.button_tim_xpath)

            # Use JavaScript Executor to scroll into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

            # Optionally, you can add a small pause to allow the scroll to take effect
            time.sleep(1)

            # Click the element using JavaScript Executor
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(2)

    def clickEdit(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.button_Edit_xpath).click()

    def setadd(self,add):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.textbox_add_xpath).send_keys(add)

    def clickUpdate(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.button_Update_xpath).click()

    def clickUpda(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.button_Upda_xpath).click()