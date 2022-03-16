from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import unittest


class Multitab(unittest.TestCase):
    CONTEXT = (By.CSS_SELECTOR, '#content > ul > li:nth-child(33) > a')
    NEW_TAB = (By.CSS_SELECTOR, '#content > div > a')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get('https://the-internet.herokuapp.com/')

    def test(self):
        self.driver.find_element(*self.CONTEXT).click()
        self.driver.find_element(*self.NEW_TAB).click()
        tab1 = self.driver.window_handles[0]
        tab2 = self.driver.window_handles[1]
        time.sleep(2)
        i = 0
        while i <= 15:
            self.driver.switch_to.window(tab1)
            self.driver.switch_to.window(tab2)
            i += 1

    def tearDown(self) -> None:
        self.driver.quit()
