from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import unittest


class ContextMenu(unittest.TestCase):
    CONTEXT = (By.CSS_SELECTOR, '#content > ul > li:nth-child(7) > a')
    BOX = (By.ID, 'hot-spot')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get('https://the-internet.herokuapp.com/')

    def test(self):
        self.driver.find_element(*self.CONTEXT).click()
        action = ActionChains(self.driver)
        action.context_click(self.driver.find_element(*self.BOX)).perform()
        time.sleep(3)
        self.driver.switch_to.alert.accept()

    def tearDown(self) -> None:
        self.driver.quit()
