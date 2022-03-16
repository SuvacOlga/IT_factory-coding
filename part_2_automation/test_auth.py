from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class Authentication(unittest.TestCase):
    AUTH = (By.CSS_SELECTOR, '#content > ul > li:nth-child(3) > a')
    LINK = 'https://the-internet.herokuapp.com/'
    USERNAME = 'admin'
    PASSWORD = 'admin'

    def setUp(self) -> None:
        # driver = webdriver.Firefox(executable_path='geckodriver.exe')
        self.driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        # driver.get(LINK)
        # driver.find_element(*AUTH).click()
        # time.sleep(3)

    def test_1(self):
        self.driver.get('https://' + self.USERNAME + ':' + self.PASSWORD + '@the-internet.herokuapp.com/basic_auth')

    def tearDown(self) -> None:
        self.driver.quit()
