from selenium.webdriver.common.by import By
from utils.config import task_menu, new_task, title, save_button, task_completed_button, task_completed_object_message, task_completed_message

class tasktest(object):
    def __init__(self, driver):
              self.driver = driver
    
    def select_task(self):
        task = self.driver.find_element(By.ID, task_menu)
        task.click()
    
    def create_new_task(self):
        create_new_task = self.driver.find_element(By.XPATH, new_task)
        create_new_task.click()

    def write_task(self):
        write_task = self.driver.find_element(By.ID, title)
        write_task.click()
        write_task.clear()
        write_task.send_keys("Hi")
    
    def click_save_button(self):
        save = self.driver.find_element(By.CSS_SELECTOR, save_button)
        save.click()
    
    def task_created(self):
       created_task = self.driver.find_element(By.CLASS_NAME, task_completed_button)
       assert created_task , "Task was not created"
       
    def task_completed(self): 
        task_1 = self.driver.find_element(By.CLASS_NAME, task_completed_button)
        task_1.click()
    
    def verify_task_completed_text(self):
        task_completed = self.driver.find_element(By.CLASS_NAME, task_completed_object_message)
        message = task_completed.get_attribute("innerText")
        if message == task_completed_message:
            print(f"verify that it was successfully marked as completed: \n The following message was displayed on the screen:{message}")