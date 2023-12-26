import time

from selenium.webdriver.common.by import By

class LoginPage:

    textbox_username_name="email"
    textbox_password_id="password"
    button_login_xpath="//button[normalize-space()='Login']"


    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        time.sleep(3)
        self.driver.find_element(By.NAME,self.textbox_username_name).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()
        time.sleep(3)