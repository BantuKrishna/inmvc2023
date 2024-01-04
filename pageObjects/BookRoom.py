import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class BookRoom:

    button_BookRoom_xpath = "//button[normalize-space()='Book room']"
    button_Room_xpath = "//body/div[@id='root']/div[@id='light']/div[contains(@class,'flexCol scheduleBg height')]/div[contains(@class,'flexRow blockCntr')]/div[contains(@class,'mainContainer')]/div[contains(@class,'innerMainBG')]/div[contains(@class,'flexRow height')]/div[contains(@class,'flexCol mainLeft')]/div[contains(@class,'flexCol height alignCntr resPdngXS')]/div[contains(@class,'flexMinHeightCol pdngHSM')]/div[contains(@class,'flexMinHeightCol')]/div[contains(@class,'respcardwidth scrollY')]/div[1]/div[1]/div[2]"
    button_Dat_xpath = "//button[@title='Next month']"
    button_Day_xpath = "//button[normalize-space()='13']"
    button_time_xpath = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[29]/td[2]"
    button_times_xpath = "/html/body/div/div/div[1]/div[2]/div[3]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td/div/div/div/div[1]/table/tbody/tr[3]/td[2]/div"
    button_timens_xpath = "//tbody/tr[30]/td[2]/div[1]"
    button_timeens_xpath = "/html/body/div/div/div[1]/div[2]/div[3]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td/div/div/div/div[1]/table/tbody/tr[23]/td[2]"
    textbox_title_name = "meetName"
    textbox_desc_name = "meetDescription"
    button_Vcall_id = "public"
    button_Apps_xpath = "/html/body/div/div/div[1]/div[2]/div[3]/div/div/div/div/div/div[2]/div[6]/div[1]/div"
    textbox_meetlink_xpth = "//input[@name='videoUrl']"
    textbox_add_xpath = "/html/body/div/div/div[1]/div[2]/div[3]/div/div/div/div/div/div[2]/div[7]/div/div[1]/div/div/div/div/div/input"
    button_Broom_xpath = "//button[normalize-space()='Book room']"


    def __init__(self,driver):
        self.driver=driver

    def clickBookRoom(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.button_BookRoom_xpath).click()
    def clickRoom(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.button_Room_xpath).click()

    def clickDat(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.button_Dat_xpath).click()

    def clickDay(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.button_Day_xpath).click()

    def clicktime(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.button_time_xpath).click()

    def clicktimes(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_times_xpath).click()

    def clicktimens(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_timens_xpath).click()

    def clicktimeens(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.button_timeens_xpath).click()

    def setTitle(self,title):
        time.sleep(3)
        self.driver.find_element(By.NAME,self.textbox_title_name).send_keys(title)

    def setDesc(self,desc):
        time.sleep(3)
        self.driver.find_element(By.NAME,self.textbox_desc_name).send_keys(desc)

    def clickApps(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.button_Apps_xpath).click()

    def clickVcall(self):
        time.sleep(3)
        self.driver.find_element(By.ID,self.button_Vcall_id).click()

    def setMeetlink(self,meetlink):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.textbox_meetlink_xpth).send_keys(meetlink)

    def setAdd(self,add):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.textbox_add_xpath).send_keys(add)

    def clickBroom(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.button_Broom_xpath).click()












