from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import unittest
from pages.login import logintest
from pages.task import tasktest
from utils.config import chromedriver

class TestAll(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        s = Service(chromedriver)
        cls.driver = webdriver.Chrome(service=s)
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(120)

    def testcase(self):
        login = logintest(self.driver)
        login.open_web()
        login.login()
        login.click_submit()
        task = tasktest(self.driver)
        task.select_task()
        task.create_new_task()
        task.write_task()
        task.click_save_button()
        task.task_created()
        task.task_completed()
        task.verify_task_completed_text()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
