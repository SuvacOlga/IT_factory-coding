from selenium.webdriver.common.by import By
from src.part_2_automation.PageObjectModel.pages.base_page import BasePage


class Autocomplete(BasePage):
    ADDRESS_ID = 'autocomplete'
    STREET_ADDRESS_ID = 'street_number'

    def enter_address_name(self, address):
        self._driver.find_element(By.ID, self.ADDRESS_ID).send_keys(address)

    def enter_street_address_name(self, street_number):
        self._driver.find_element(By.ID, self.STREET_ADDRESS_ID).send_keys(street_number)
