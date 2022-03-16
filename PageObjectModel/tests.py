import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from src.part_2_automation.PageObjectModel.pages.autocomplete_page import Autocomplete
from src.part_2_automation.PageObjectModel.pages.home_page import HomePage


class Test1(unittest.TestCase):
    def setUp(self) -> None:
        self._driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_1(self):
        main_page = HomePage(self._driver)
        main_page.go_to_autocomplete()

    def test_2(self):
        self._driver.get('https://formy-project.herokuapp.com/autocomplete')
        autocomplete = Autocomplete(self._driver)
        autocomplete.enter_address_name('Bujorilor')
        autocomplete.enter_street_address_name('132A')

    def tearDown(self) -> None:
        time.sleep(2)
        self._driver.quit()
