from selenium.webdriver.common.by import By
from utils.config import user_email_object, user_password_object, submitBtn, url, email, pwd


class logintest(object):
    def __init__(self, driver):
        self.driver = driver
    
    def open_web(self):
        driver = self.driver
        driver.get(url)

    def login(self):
        # Verify email object in the screen
        email_input = self.driver.find_element(By.ID, user_email_object)
        email_input.click()
        email_input.clear()
        # Write email
        email_input.send_keys(email)
        # Verify password object in the screen
        password = self.driver.find_element(By.ID, user_password_object)
        password.click()
        password.clear()
        # Write password 
        password.send_keys(pwd)

    def click_submit(self):
        Sign_in = self.driver.find_element(By.ID, submitBtn)
        Sign_in.click()
